# -*- coding: utf-8 -*-
"""
    nome
    ~~~~~~~~~~~~~~

    Here goes the description of this file.

    :copyright: (c) 2012 by arruda.
"""
import sys
import os


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT =os.path.dirname(PROJECT_ROOT)
sys.path.append(SITE_ROOT)

sys.path.append(os.path.join(PROJECT_ROOT,'apps'))
sys.path.append(os.path.join(PROJECT_ROOT,PROJECT_ROOT, 'libs'))

SECRET_KEY = ''

CURRENT_ENV = os.environ.get('CURRENT_ENV', 'DEV')

from config import *
from installed_apps import *
from logging import *

NO_DEPRECATION_WARNINGS=False
if CURRENT_ENV == 'PROD':
    NO_DEPRECATION_WARNINGS=True
    from env_prod import *
else:
    from env_dev import *

if NO_DEPRECATION_WARNINGS:
    import warnings
    warnings.simplefilter('ignore', DeprecationWarning)


