from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation

from hitcount.models import HitCountMixin
from hitcount.models import HitCount
from taggit.managers import TaggableManager

from media.models import Photo
from profiles.models import Profile


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Story(models.Model, HitCountMixin):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    author = models.ManyToManyField(Profile)
    # author = models.ForeignKey(
     #   Profile, related_name='stories_of', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    published_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=50, unique_for_date='published_date')
    featured_photo = models.ForeignKey(
        Photo, related_name='article_cover', null=True, blank=True, on_delete=models.SET_NULL)
    tags = TaggableManager()
    visits_count = GenericRelation(
        HitCount, object_id_field='object_pk', related_query_name='visits_count_generic_relation')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-published_date',)
