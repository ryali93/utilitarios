library(dplyr)
library(ncdf4)
library(raster)

## VERSION TRADICIONAL
# Funciones de estadisticas zonales
##-------------------------------------------------------------------------
myZonal <- function (x, z, stat, digits = 0, na.rm = TRUE, ...) {
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
  zone <- rasterize(shp, r, field="ID", dataType = "INT1U") # Cambiar dataType si nrow(shp) > 255 a INT2U o INT4U
  
  Zstat<-data.frame(myZonal(r, zone, stat))
  colnames(Zstat)<-c("ID", paste0(names(r), "_", c(1:(length(Zstat)-1)), "_",stat))
  
  shp@data <- plyr::join(shp@data, Zstat, by="ID")
  
  if (is.null(shp.out)){
    return(shp)
  }else{
    writeOGR(shp, shp.out, layer= sub("^([^.]*).*", "\\1", basename(zone.in)), driver="ESRI Shapefile")
  }
}
##-------------------------------------------------------------------------

ppbrick = brick("E:/TESIS/datos/nc/PISCO_19812015.nc")
shp     = shapefile("E:/TESIS/datos/shp/tmp/microcuencasWS.shp")
shpRp   = spTransform(shp, proj4string(ppbrick))

ppcrop  = crop(ppbrick, shpRp) # Cortando el area de estudio
ppmask  = mask(ppcrop, shpRp)
writeRaster(ppmask, "E:/2018/MAGALY/ppMask.tif")


# Hallar las estadísticas zonales
zone.in   = "E:/TESIS/datos/shp/tmp/microcuencasWS.shp"
raster.in = "E:/2018/MAGALY/ppMask.tif"
shp.out   = "E:/2018/MAGALY/ppZonal.shp"

shp = ZonalPipe(zone.in, raster.in, stat="mean")
tbpp = read.csv("E:/2018/MAGALY/tablaPP.csv", header = T, sep = ",")



# Media para cada subcuenca
# len = nlayers(ppmask)
# 
# lista = c()
# for(i in c(1:len)){
#   a = mean(getValues(ppmask[[i]]), na.rm=T)
#   lista = c(lista,a)
# }
# 
# serie = seq(as.Date(""), as.Date(""),by = "monthly") #
# df  = data.frame(serie,lista)


## VERSION VELOX
install.packages("velox")
library(velox)

ppbrick = brick("E:/TESIS/datos/nc/PISCO_19812015.nc")
shp     = shapefile("E:/TESIS/datos/shp/tmp/microcuencasWS.shp")
Area   = spTransform(shp, proj4string(ppbrick))

vx = velox("C:/Users/PERSONAL/Desktop/WW/ppMask.tif") # Cambiar ruta
vxe = vx$extract(Area, fun=function(x){mean(x, na.rm=T)})

write.csv(t(vxe), "C:/Users/PERSONAL/Desktop/WW/vxe.csv")
