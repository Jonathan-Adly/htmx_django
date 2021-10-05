# Generated by Django 3.2.7 on 2021-10-04 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_blog_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.CharField(default='blogging', max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('sd', 'Software Development'), ('hc', 'Healthcare'), ('o', 'Other')], max_length=2),
        ),
    ]