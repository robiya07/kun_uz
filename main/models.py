from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class ZoneModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=300, blank=True)

    class Meta:
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'
        db_table = 'main_zones'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

            while NewsModel.objects.filter(slug=self.slug).exists():
                slug = NewsModel.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

            super().save(*args, **kwargs)


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=300, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'main_categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

            while NewsModel.objects.filter(slug=self.slug).exists():
                slug = NewsModel.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

            super().save(*args, **kwargs)


class NewsModel(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=310, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()
    video_url = models.URLField(max_length=255, null=True, blank=True)
    zone = models.ForeignKey(ZoneModel, on_delete=models.RESTRICT, null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=True)
    is_chosen = models.BooleanField(default=False)
    is_interview = models.BooleanField(default=False)
    is_breaking_new = models.BooleanField(default=False)
    is_inquiry = models.BooleanField(default=False)
    is_article = models.BooleanField(default=False)
    is_ad = models.BooleanField(default=False)
    is_video_news = models.BooleanField(default=False)
    is_photo_news = models.BooleanField(default=False)
    slug = models.SlugField(max_length=300, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

            while NewsModel.objects.filter(slug=self.slug).exists():
                slug = NewsModel.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.title:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

            super().save(*args, **kwargs)

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
    slug = models.SlugField(max_length=300, blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'main_tags'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

            while NewsModel.objects.filter(slug=self.slug).exists():
                slug = NewsModel.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

            super().save(*args, **kwargs)
