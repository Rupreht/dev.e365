# e365/catalogue/models.py

from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    video_url = models.URLField(default='')


from oscar.apps.catalogue.models import *  # pylint: disable=wildcard-import,unused-wildcard-import
