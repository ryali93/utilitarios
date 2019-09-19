var AREA = ; // insertar area que quieres cortar
var dataset = ee.ImageCollection('LANDSAT/LC08/C01/T1_32DAY_NDVI')
                  .filterDate('2000-01-01', '2017-12-31').select('NDVI');

var datasetview = dataset.map(function(image){return image.clip(AREA)});
var empty = ee.Image();

var colorizedVis = {
  min: 0.0,
  max: 1.0,
  palette: [
    'FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901',
    '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01',
    '012E01', '011D01', '011301'
  ],
};
var vizparams = {color: 'FF0000'}
//add to map
print("dataset");
var listOfImages = dataset.toList(dataset.size());
print(listOfImages);

var img1 =ee.Image(listOfImages.get(0));
var img2 = img1.clip(AREA)
print(img1);


// Map.addLayer(AREA, vizparams,'socota');
Map.addLayer(datasetview, colorizedVis, 'Colorized');
Map.centerObject(AREA);

var ndvi = ee.Image(dataset.iterate(function(image,previous){
  var name = ee.String('NDVI_').cat(image.id());
  var ndvi = image.rename(name);
  return ee.Image(previous).addBands(ndvi);
},empty));

ndvi = ndvi.select(ndvi.bandNames().remove('constant'));

//exportar imagen
Export.image.toDrive({
  image: ndvi,
  description: 'imageToDriveExample',
  scale: 250,
  region: AREA
});




// Map.setCenter(-78.8, -7.12, 10);
// Map.addLayer(dataset, colorizedVis, 'Colorized');

// // Map.addLayer(AREA);

// Export.image.toDrive({
//   image: dataset,
//   description: 'Landsat8',
//   scale: 30,
//   region: AREA
// });
