from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify


class PublishedStateOptions(models.TextChoices):
    PUBLISH = 'PU', 'Publish'
    DRAFT = 'DR', 'Draft'


class PlaylistQuerySet(models.QuerySet):
    def published(self):
        return self.filter(
            state=PublishedStateOptions.PUBLISH,
            publish_timestamp__lte=timezone.now())


class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class Playlist(models.Model):
    title = models.CharField(max_length=200)
    decription = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    state = models.CharField(
        max_length=2, choices=PublishedStateOptions.choices, default=PublishedStateOptions.DRAFT)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish_timestamp = models.DateTimeField(
        auto_now_add=False, auto_now=False, blank=True, null=True)

    objects = PlaylistManager()

    @property
    def is_published(self):
        return self.active


def published_satet_pre_save(instance, *args, **kwarg):
    if instance.state == PublishedStateOptions.PUBLISH and instance.publish_timestamp is None:
        instance.publish_timestamp = timezone.now()
    elif instance.state == PublishedStateOptions.DRAFT:
        instance.publish_timestamp = None


pre_save.connect(published_satet_pre_save, sender=Playlist)


def slugify_pre_save(instance, *args, **kwarg):
    title = instance.title
    slug = instance.slug
    if slug is None:
        instance.slug = slugify(title)


pre_save.connect(slugify_pre_save, sender=Playlist)
