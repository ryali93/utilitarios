# coding=utf-8
"""
Modulo que sirve para actualizar los registros generados en Collector y actualice el mapa web
Roy Yali.
"""

from config import *
import arcpy

def _get_users_from_edit(parent):
    """
    Extrae los usuarios que han realizado alguna modificacion y sincronizacion
    """
    versions = arcpy.da.ListVersions(CONN)
    verReconcileList = []
    for version in versions:
        if version.parentVersionName == parent:
            verReconcileList.append(version.name)
    return ';'.join(verReconcileList)

def service_reconcile_versions(schema, parent):
    """
    Obtiene todos los petitorios por el numero RUC del titular
    :param ruc: Numero de RUC del titular
    :return: lista de derechos mineros como una cadena
    """
    if schema == "": schema = 'DATA_EDIT'
    if parent == "": parent = 'collector'

    _PARENT = schema + "." + parent

    USERS = _get_users_from_edit(_PARENT)
    arcpy.ReconcileVersions_management(
        input_database=CONN, 
        reconcile_mode="ALL_VERSIONS", 
        target_version=_PARENT, 
        edit_versions=USERS, 
        acquire_locks="LOCK_ACQUIRED", 
        abort_if_conflicts="ABORT_CONFLICTS", 
        conflict_definition="BY_OBJECT", 
        conflict_resolution="FAVOR_TARGET_VERSION", 
        with_post="POST", 
        with_delete="DELETE_VERSION", 
        out_log="")