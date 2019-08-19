from __future__ import print_function
import cx_Oracle as oracle
import os

__author__ = 'Roy Yali Samaniego'
__copyright__ = 'INGEMMET 2019'
__credits__ = ['Roy Yali S.']
__version__ = '1.0'
__maintainer__ = 'Roy Yali S.'
__mail__ = 'autonomoosi02@ingemmet.gob.pe'
__status__ = 'Production'

BASE_DIR = os.path.dirname(__file__)
CONN = os.path.join(os.path.dirname(BASE_DIR), "config\\bdgeocat_huawei_dataedit.sde")