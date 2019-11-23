// Necesitas importar la tabla de tu shapefile de las estaciones.
// Necesitas importar el producto satelital a trabajar.
// Aun falta mejorar el codigo, no me salen los nombres de las estaciones; pero sí las coordenadas, con eso se puede unir. 
// No he verificado la data desde cuándo existe, se tendrían que cambiar las fechas.

var estaciones = ee.FeatureCollection(table)
Map.addLayer(estaciones)

// LST_Day_1km
// LST_Night_1km

var yearly = ee.ImageCollection(MOD11A1).filterDate('2017-01-01', '2017-01-10'); // Cambiar las fechas
var mapfunc = function(feat) {
  var id = ee.String(feat.id())
  var geom = feat.geometry()
  var newfc = ee.List([])
  // var nameEst = ee.FeatureCollection(feat).first()
  
  var addProp = function(img, fc) {
    fc = ee.List(fc)
    var date = img.date().format()
    
    var value1 = img.reduceRegion(ee.Reducer.first(), geom, 30).get('LST_Day_1km')
    var val1 = ee.String(ee.Algorithms.If(value1, ee.String(value1), ee.String('No data')))

    var value2 = img.reduceRegion(ee.Reducer.first(), geom, 30).get('LST_Night_1km')
    var val2 = ee.String(ee.Algorithms.If(value2, ee.String(value2), ee.String('No data')))

    var featname = ee.String("feat_").cat(id).cat(ee.String("-")).cat(date)
    print(id)
    var newfeat = ee.Feature(geom, {name:featname,
                                    "fecha": date,
                                    "LST_Day_1km":val1,
                                    "LST_Night_1km":val2,
    })
    return fc.add(newfeat)
  }
  var newfeat = ee.FeatureCollection(ee.List(yearly.iterate(addProp, newfc)))
  return newfeat
};

var newft = estaciones.map(mapfunc).flatten();

Export.table.toDrive(newft,
"ESTACIONES",
"ESTACIONES",
"ESTACIONES");
