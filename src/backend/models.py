'''
Models of the backend app. They should save data persistently that
represents important information about the project
'''
from django.db import models

class Config(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Config, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class SiteConfig(Config):

    def __str__(self):
        return "Singleton de configurare"

    aproveNewsletterMessage = models.TextField(default='Sunt de acord.')
    