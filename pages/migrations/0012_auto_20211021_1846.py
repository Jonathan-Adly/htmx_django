# Generated by Django 3.2.8 on 2021-10-21 18:46

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20211021_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='content',
        ),
        migrations.AddField(
            model_name='project',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='test'),
            preserve_default=False,
        ),
    ]
