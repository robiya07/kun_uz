# Generated by Django 4.2.2 on 2023-07-01 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Main Category',
                'verbose_name_plural': 'Main Categories',
                'db_table': 'main_categories',
            },
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('video_url', models.URLField(blank=True, max_length=255, null=True)),
                ('is_chosen', models.BooleanField(default=False)),
                ('is_interview', models.BooleanField(default=False)),
                ('is_breaking_new', models.BooleanField(default=False)),
                ('is_inquiry', models.BooleanField(default=False)),
                ('is_article', models.BooleanField(default=False)),
                ('is_ad', models.BooleanField(default=False)),
                ('is_video_news', models.BooleanField(default=False)),
                ('is_photo_news', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.categorymodel')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'db_table': 'main_news',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ZoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Zone',
                'verbose_name_plural': 'Zones',
                'db_table': 'main_zones',
            },
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('posts', models.ManyToManyField(to='main.newsmodel')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'db_table': 'main_tags',
            },
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.zonemodel'),
        ),
    ]
