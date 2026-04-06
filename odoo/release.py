# Part of Odoo. See LICENSE file for full copyright and licensing details.

RELEASE_LEVELS = [ALPHA, BETA, RELEASE_CANDIDATE, FINAL] = ['alpha', 'beta', 'candidate', 'final']
RELEASE_LEVELS_DISPLAY = {ALPHA: 'a',
                          BETA: 'b',
                          RELEASE_CANDIDATE: 'rc',
                          FINAL: ''}

# version_info format: (MAJOR, MINOR, MICRO, RELEASE_LEVEL, SERIAL)
# inspired by Python's own sys.version_info, in order to be
# properly comparable using normal operators, for example:
#  (6,1,0,'beta',0) < (6,1,0,'candidate',1) < (6,1,0,'candidate',2)
#  (6,1,0,'candidate',2) < (6,1,0,'final',0) < (6,1,2,'final',0)
# NOTE: during release, the MAJOR version can become an arbitrary string ('saas~xx')
version_info = (19, 0, 0, FINAL, 0, '')
series = serie = major_version = '.'.join(str(s) for s in version_info[:2])
version = series + RELEASE_LEVELS_DISPLAY[version_info[3]] + str(version_info[4] or '') + version_info[5]

product_name = 'Odoo'
description = 'Odoo Server'
long_desc = '''Odoo is a complete ERP and CRM. The main features are accounting (analytic
and financial), stock management, sales and purchases management, tasks
automation, marketing campaigns, help desk, POS, etc. Technical features include
a distributed server, an object database, a dynamic GUI,
customizable reports, and XML-RPC interfaces.
'''
classifiers = """Development Status :: 5 - Production/Stable
License :: OSI Approved :: GNU Lesser General Public License v3

Programming Language :: Python
"""
url = 'https://www.odoo.com'
author = 'OpenERP S.A.'
author_email = 'info@odoo.com'
license = 'LGPL-3'

nt_service_name = "odoo-server-" + series.replace('~','-')

MIN_PY_VERSION = (3, 10)
MAX_PY_VERSION = (3, 13)
MIN_PG_VERSION = 13

version += '-20260402'

repos_heads = {'odoo': '06fb412d240cda87de5bb9b835fca1e725b1add8', 'enterprise': '96fb0cceecb3e80543d353e11a3c4951df0d246e', 'design-themes': '26e16256e831b74a305688220b92f7e19c38963e'}
