if __name__ == '__main__':
    message = str()
    arcpy.AddMessage("MENSAJE")
    try:
        import sys
        import os
        import arcpy

        pname = arcpy.GetInstallInfo()['ProductName']
        arcpy.AddMessage(pname)

        if pname == 'Server':
            path = r'D:\\aplicaciones\\geoproceso\\updateCollector'
        else:
            path = os.path.dirname(__file__)

        sys.path.append(path)
        arcpy.AddMessage(path)

        arcpy.AddMessage("Llego aqui0")

        ESQUEMA  = arcpy.GetParameterAsText(0)  # ESQUEMA
        PARENT   = arcpy.GetParameterAsText(1)  # PARENT

        arcpy.AddMessage("Llego aqui1")
        from updateCollector import *
        arcpy.AddMessage("Llego aqui2")
        service_reconcile_versions(ESQUEMA, PARENT)

        message = "Actualizado con exito"
    except Exception as e:
        message = e.message.__str__()

    finally:
        arcpy.SetParameterAsText(2, message)