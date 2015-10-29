"""WSGI Module.

Version: 1.0
Author: Pablo Trinidad
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialauthentication.settings")

application = get_wsgi_application()
