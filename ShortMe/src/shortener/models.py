from __future__ import unicode_literals
from django.db import models

# Create your models here.
from .utils import code_generator, create_shortcode

class ShortMeManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(ShortMeManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs
    def refresh_shortcodes(self):
        qs = ShortMeURL.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i = new_codes)

class ShortMeURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank= True)
    active = models.BooleanField(default=True)

    objects = ShortMeManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)

        super(ShortMeURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
