setwd("E:/BASE_DATOS/PISCO")

rm(list = ls())

# Cargar librerias
if(!require(raster)) install.packages("raster"); library(raster)
if(!require(ncdf4)) install.packages("ncdf4"); library(ncdf4)
if(!require(sp)) install.packages("sp"); library(sp)
if(!require(rgeos)) install.packages("rgeos"); library(rgeos)
if(!require(velox)) install.packages("velox"); library(velox)
if(!require(ggplot2)) install.packages("ggplot2"); library(ggplot2)

# Modificar estos archivos
archivo_coords = "pruena.csv"
archivo_nc = "PISCOpm21.nc"
archivo_salida = "salida.csv"
dates = seq(as.Date("1981/01/01"), as.Date("2016-12-31"), by = "month")

# Funcion de extraccion
long_lat <- read.csv(archivo_coords, sep=";", header = T)
vx     = velox(stack(archivo_nc))
spoint = SpatialPoints(coords = long_lat[c("x","y")])
data   = vx$extract_points(sp=spoint)

# Cambiar nombre a los campos
d = as.data.frame(t(data))
colnames(d) = long_lat$NN
resp = cbind(d, dates)


# Ejecutando la funcion
datos = extrae_data_PISCO(archivo_coords, archivo_nc, dates)

# Exportar datos
# write.csv(resp, archivo_salida, quote = F)

# Mostrar graficos
ggplot(datos, aes(x=dates)) +
  geom_line(aes(y = EST1), color = "darkred") +
  geom_line(aes(y = EST2), color = "steelblue")

st = stack(archivo_nc)
plot(st[[1]])
plot(spoint, add=TRUE)
