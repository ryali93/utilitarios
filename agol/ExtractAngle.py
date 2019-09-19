## ELIMINAR VERTICES CON ANGULO DE 180


class extractAngle:
    def __init__(self, feature):
        self.feature = feature
        self.distBuff = 100 	# cambiar
        self.path = path

    def getPointGeom(self):
        self.mfl = arcpy.MakeFeatureLayer_management(self.feature, 'polygon')
        self.vertices = arcpy.FeatureVerticesToPoints_management(self.mfl, 'in_memory\\vertices', 'ALL')
        arcpy.DeleteIdentical_management(self.vertices, 'SHAPE', '#', '0')

    def getAngle(self):
        angles = {}
        self.listcoord = []
        polBuffer = arcpy.Buffer_analysis(self.vertices, 'in_memory\\buffer', '{} Centimeters'.format(self.distBuff), 'FULL', 'ROUND', 'NONE', '#', 'PLANAR')
        arcs = arcpy.Clip_analysis(polBuffer, self.mfl, 'in_memory\\clip', '#')

        for x in arcpy.da.SearchCursor(arcs, ["ORIG_FID", "SHAPE@AREA"]):
            angle = self.getAnglewithArea(x[1], self.distBuff)
            print angle
            if angle != 180:
                coord = [(y[1], y[2]) for y in arcpy.da.SearchCursor(self.vertices, ["FID", "SHAPE@X", "SHAPE@Y"], "FID = {}".format(x[0]))]
                self.listcoord.extend(coord)
        self.createPolygon()

    def createPolygon(self):
        array = arcpy.Array([arcpy.Point(x[0], x[1]) for x in self.listcoord])
        polygon = arcpy.Polygon(array)
        
        cursor = arcpy.da.InsertCursor(self.path, ['SHAPE@'])
        cursor.insertRow([polygon])


    def getAnglewithArea(self, area, radio):
        angleDec = (area*2*180*pow(100, 2))/(pow(radio, 2)*math.pi)  #<--- ANGULO
        degrees = round(angleDec)
        return degrees

    def main(self):
        self.getPointGeom()
        self.getAngle()

if __name__ == "__main__":
    poo = extractAngle('poli')
    poo.main()
