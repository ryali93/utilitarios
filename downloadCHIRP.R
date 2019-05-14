# Cargar librerias
if (!require("dplyr")) install.packages("dplyr")
if (!require("raster")) install.packages("raster")
if (!require("RCurl")) install.packages("RCurl")
if (!require("R.utils")) install.packages("R.utils")
if (!require("Hmisc")) install.packages("Hmisc")

# Declarar funcion de descarga
download_CHIRPd<-function(date,
                          set_dir = database_directory,
                          BBlonMin = -86,     # Limite del area a cortar
                          BBlonMax = -66,     # Limite del area a cortar
                          BBlatMin = -19.25,  # Limite del area a cortar
                          BBlatMax = 1.25     # Limite del area a cortar
){
  ftp <- "ftp://ftp.chg.ucsb.edu/pub/org/chg/products/CHIRPS-2.0/global_daily/tifs/p05"  #ftp data
  ftp2 <- sprintf("%s/%s/", ftp, 2018)  # Cambiar si se requiere otro año
  filenames <- getURL(ftp2, ftp.use.epsv = FALSE, ftplistonly = TRUE, 
                      crlf = TRUE)
  filePaths <- paste(ftp2, strsplit(filenames, "\r*\n")[[1]], sep = "")  #obsolete
  filePaths <- grep("\\.gz$", filePaths, value = T)  #obsolete
  fechas <- substr(basename(filePaths), 13, 22) %>% 
    as.Date(., format = "%Y.%m.%d")  #obsolete
  selects <- fechas %in% (date %>% as.Date) %>% which
  selectedfilePaths <- filePaths[selects]
  nameT<-sprintf("%s/%s",set_dir,basename(selectedfilePaths))
  nameT2<-gsub("\\.gz","",nameT)
  #if(file.exists(nameT2)) file.remove(nameT2)
  mapply(function(i){
    download.file(selectedfilePaths[i],nameT[i],mode="wb")
    gunzip(nameT[i])
    chirp_crop <- crop(raster(nameT2[i]),c(BBlonMin, BBlonMax, BBlatMin, BBlatMax) )
    chirp_crop[chirp_crop<0]=0
    writeRaster(chirp_crop, nameT2[i], overwrite = T)  
  }, 2:length(selectedfilePaths))
}


# Ejecucion del codigo
date=as.Date("2018-02-15")  # Cambiar la fecha de inicio
initDay <- sprintf("%s-01",substr(date,1,7)) %>% as.Date
finalDay <- sprintf("%s-01",substr(date,1,7)) %>% as.Date + monthDays(date) - 1
serieDay <- seq.Date(initDay,finalDay,"day")
database_directory<-"C:/Users/PERSONAL/Desktop/chirps" # Cambiar la ruta de salida
download_CHIRPd(date = serieDay)

# Creditos Cesar Aybar (https://github.com/csaybar)
