# -*- coding: utf-8 -*-
import cx_Oracle

def testOracle():
    inst = "bdgeocat"
    user_sde = "bdtecnica"
    password_sde = "bdtecnica"

    connection = cx_Oracle.connect(user_sde, password_sde, inst)
    cursor = connection.cursor()
    expresion_sql = 'PKG_SISTEMA_MORFOPEDOLOGIA.P_MS_UPDATEPOG'
    listaCodcal = [u'GR36B-CA001', u'GR36B-CA150', u'GR36B-CA151', u'GR36B-CA152', u'GR36B-CA153', u'GR36B-CA154', u'GR36B-CA219', u'GR36B-CA218', u'GR36B-CA217', u'GR36B-CA216', u'GR36B-CA215', u'GR36B-CA214', u'GR36B-CA213', u'GR36B-CA211', u'GR36B-CA212', u'GR36B-CA160', u'GR36B-CA158', u'GR36B-CA157', u'GR36B-CA156', u'GR36B-CA155', u'GR36B-CA227', u'GR36B-CA226', u'GR36B-CA225', u'GR36B-CA224', u'GR36B-CA223', u'GR36B-CA222', u'GR36B-CA221', u'GR36B-CA220', u'GR36B-CA228', u'GR36B-CA171', u'GR36B-CA170', u'GR36B-CA169', u'GR36B-CA168', u'GR36B-CA167', u'GR36B-CA166', u'GR36B-CA165', u'GR36B-CA164', u'GR36B-CA163', u'GR36B-CA162', u'GR36B-CA161', u'GR36B-CA172', u'GR36B-CA229', u'GR36B-CA173', u'GR36B-CA230', u'GR36B-CA174', u'GR36B-CA175', u'GR36B-CA231', u'GR36B-CA176', u'GR36B-CA177', u'GR36B-CA178', u'GR36B-CA159', u'GR36B-CA179', u'GR36B-CA181', u'GR36B-CA180', u'GR36B-CA183', u'GR36B-CA182', u'GR36B-CA184', u'GR36B-CA185', u'GR36B-CA186', u'GR36B-CA187', u'GR36B-CA150', u'GR36B-CA188', u'GR36B-CA189', u'GR36B-CA190', u'GR36B-CA191', u'GR36B-CA192', u'GR36B-CA193', u'GR36B-CA194', u'GR36B-CA195', u'GR36B-CA196', u'GR36B-CA197', u'GR36B-CA198', u'GR36B-CA199', u'GR36B-CA200', u'GR36B-CA201']
    for codcal in listaCodcal:
        try:
            lCursor = cursor.callproc(expresion_sql, [codcal])
            print "Calicata {} actualizada con exito".format(codcal)
        except Exception as e:
            print "El código de calicata {} tiene un error".format(codcal)
    cursor.close()

testOracle()