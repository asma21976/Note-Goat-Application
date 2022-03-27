import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notegoat.settings")

"""
YOU ONLY NEED ONE OF THESE.
Choose middleware to serve static files. 
WhiteNoise seems to be the go-to but I've used dj-static 
successfully in many production applications.
"""

# If using WhiteNoise:
from whitenoise import WhiteNoise
application = WhiteNoise(get_wsgi_application())
