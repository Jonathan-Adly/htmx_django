# Generated by Django 3.2.8 on 2021-10-10 01:21

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('pages', '0001_initial'), ('pages', '0002_blog_views'), ('pages', '0003_auto_20211004_0104'), ('pages', '0004_remove_blog_category'), ('pages', '0005_rename_views_blog_blog_views'), ('pages', '0006_alter_blog_tag'), ('pages', '0007_auto_20211010_0119'), ('pages', '0008_auto_20211010_0120')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribe', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('notes', ckeditor.fields.RichTextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('main_img', models.ImageField(blank=True, upload_to='blogimages/')),
                ('blog_views', models.IntegerField(default=0)),
                ('tag', models.CharField(default='django/htmx', max_length=50)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
