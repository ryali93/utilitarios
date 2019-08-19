if (!require("velox")) install.packages("velox")

filesPP = list.files("C:/Users/PERSONAL/Desktop/chirps", full.names = T) # Ruta donde se encuentren los archivos TIF
st    = stack(filesPP)
shp = shapefile("C:/Users/PERSONAL/Desktop/WW/Subcuencas_Piura.shp") # Área como polígono
Area  = spTransform(shp, proj4string(st))

vx = velox(st)
vxe = vx$extract(Area, fun=function(x){mean(x, na.rm=T)})            # Cambiar la funcion (en este caso es mean)
write.csv(t(vxe), "C:/Users/PERSONAL/Desktop/WW/results/vxe.csv")    # Ruta para guardar como csv
