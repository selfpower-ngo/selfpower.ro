'''
post_save: trigger a function to run at creation of an instance
'''
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.db.models.signals import post_delete
from django.dispatch import receiver

from SelfpowerProject.settings.utils import prepare_you_tube_url

class ProjectQuerySet(models.QuerySet):
    '''
    A query set model.
    '''
    def published(self):
        '''
        Return project posts that are published
        '''
        return self.filter(publish=True)


class Proiect(models.Model):
    '''
    Proiect
    '''
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)
    publish = models.BooleanField(default=True)
    objects = ProjectQuerySet.as_manager()
    # profile = models.FileField(upload_to = 'hubImages/',blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        '''
        Get absolute url of object proiect
        '''
        return reverse("proiecte_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = "Proiecte"
        verbose_name = "Proiect"
        ordering = ["id"]


class Image(models.Model):
    '''
    Object that references an image for different other models
    '''
    image = models.FileField(upload_to='hubImages/', blank=False)
    proiect = models.ForeignKey(Proiect, on_delete=models.CASCADE, related_name='images')


@receiver(post_delete, sender=Image)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 


class Resursa(models.Model):
    '''
    Resursa model. No longer used in the project
    It was deactivated on client's wish.
    It's similar to a blog structure but contains in addition
    on video url and a different image field.
    '''
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)
    videoUrl = models.CharField(max_length=300, blank=True)
    profile = models.FileField(upload_to='hubImages/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "resurse"

    def save(self, *args, **kwargs):
        '''
        Overwriting save()
        '''
        self.videoUrl = prepare_you_tube_url(self.videoUrl)
        super(Resursa, self).save(*args, **kwargs)


class BookUrl(models.Model):
    '''
    Ideally this should represet a book.
    Contains a title, the a reference to a resursa model and
    the url to the pdf/file.
    '''
    url = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    resursa = models.ForeignKey(Resursa, on_delete=models.DO_NOTHING)

    class Meta:
        '''
        Verbose names; contain translations in romanian
        '''
        verbose_name = "carte"
        verbose_name_plural = "carti"
