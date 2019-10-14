Resamplear<-function(hasta, desde){
  #Verificar la proyección
  if(proj4string(desde)!=proj4string(hasta)){
    # print("las proyecciones son diferentes")
    hasta_proj<-projectRaster(hasta,crs=CRS(proj4string(desde)))
    # print(proj4string(hasta_proj))
  }else{
    # print("Tienen la misma proyeccion")
    hasta_proj<-hasta
  }
  #Verificando Extensión
  if(extent(desde)!=extent(hasta_proj)){
    # print("las resoluciones son diferentes")
    hasta_resam<-resample(hasta_proj,desde)
  }else{
    # print("las resoluciones son las mismas")
    hasta_resam<-hasta_proj
  }
  return(hasta_resam)
}

reproyectar = function(hasta, desde){
  if(proj4string(desde)!=proj4string(hasta)){
    print("las proyecciones son diferentes")
    hasta_proj<-projectRaster(hasta,crs=CRS(proj4string(desde)))
    print(proj4string(hasta_proj))
  }else{
    print("Tienen la misma proyeccion")
    hasta_proj<-hasta
  }
}


orderDatosHidro <- function(ruta) {
  #require(gdata)
  #require(openxlsx)
  estacion = read.xlsx(ruta)
  data = unmatrix(as.matrix(estacion[,2:13]), byrow=T)
  desde = paste0(as.character(min(estacion[,1])),"/1/1")
  hasta = paste0(as.character(max(estacion[,1])),"/12/31")
  ts = seq(as.Date(desde), as.Date(hasta), "month")
  return(data.frame(ts, data))
}

coneccion <- function(tabla){
  require(sf)
  require(RPostgreSQL)
  pw <- {
    "72916096"
  }
  drv <- dbDriver("PostgreSQL")
  con <- dbConnect(drv, 
                   dbname = "TESIS", 
                   host = "localhost", 
                   user = "postgres", 
                   port = 8888, 
                   password = pw)
  queryTb = paste0('SELECT * FROM public."', tabla, '"')
  GEOM = st_read_db(con, query = queryTb)
  dbDisconnect(con)
  dbUnloadDriver(drv)
  return(GEOM)
}





extractValue <- function(){
  
}

data <- data.frame(coordinates(germany.places.mrc.sample),
                   germany.places.mrc.sample$name, 
                   extract(germany.mrc, germany.places.mrc.sample))





#--------------------------------------------------------------------------
# Hallar estadisticas zonales
myZonal <- function (x, z, stat, digits = 0, na.rm = TRUE, 
                     ...) { 
  library(data.table)
  fun <- match.fun(stat) 
  vals <- getValues(x) 
  zones <- round(getValues(z), digits = digits) 
  rDT <- data.table(vals, z=zones) 
  setkey(rDT, z) 
  rDT[, lapply(.SD, fun, na.rm = TRUE), by=z] 
} 

ZonalPipe<- function (zone.in, raster.in, shp.out=NULL, stat){
  require(raster)
  require(rgdal)
  require(plyr)
  
  r <- stack(raster.in)
  shp <- readOGR(zone.in)
  shp <- spTransform(shp, crs(r))
  
  shp@data$ID<-c(1:length(shp@data[,1]))
  
  r <- crop(r, extent(shp))	
  zone <- rasterize(shp, r, field="ID", dataType = "INT1U") # Change dataType if nrow(shp) > 255 to INT2U or INT4U
  
  Zstat<-data.frame(myZonal(r, zone, stat))
  colnames(Zstat)<-c("ID", paste0(names(r), "_", c(1:(length(Zstat)-1)), "_",stat))
  
  shp@data <- plyr::join(shp@data, Zstat, by="ID")
  
  if (is.null(shp.out)){
    return(shp)
  }else{
    writeOGR(shp, shp.out, layer= sub("^([^.]*).*", "\\1", basename(zone.in)), driver="ESRI Shapefile")
  }
}

# zone.in <- "E:/TESIS/datos/shp/tmp/microcuencasWS.shp"
# raster.in <- "E:/TESIS/process/sdr/sdr4.tif"
# shp.out <- "E:/TESIS/datos/shp/tmp/tmp.shp"

# ZonalPipe(zone.in, raster.in, shp.out, stat="mean")
# shp <- ZonalPipe(zone.in, raster.in, stat="mean")

#--------------------------------------------------------------------------