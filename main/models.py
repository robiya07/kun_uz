from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


class ZoneModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'
        db_table = 'main_zones'

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'main_categories'

    def __str__(self):
        return self.name


class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()
    video_url = models.URLField(max_length=255, null=True, blank=True)
    zone = models.ForeignKey(ZoneModel, on_delete=models.RESTRICT)
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=True)
    is_chosen = models.BooleanField(default=False)
    is_interview = models.BooleanField(default=False)
    is_breaking_new = models.BooleanField(default=False)
    is_inquiry = models.BooleanField(default=False)
    is_article = models.BooleanField(default=False)
    is_ad = models.BooleanField(default=False)
    is_video_news = models.BooleanField(default=False)
    is_photo_news = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_p',
                                        related_query_name='hit_count_generic_relation')

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ["-created_at"]
        db_table = 'main_news'

    def __str__(self):
        return self.title


class TagModel(models.Model):
    name = models.CharField(max_length=50)
    news = models.ManyToManyField(NewsModel)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'main_tags'

    def __str__(self):
        return self.name
