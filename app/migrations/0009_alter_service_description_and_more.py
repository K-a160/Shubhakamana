# Generated by Django 5.0.3 on 2024-04-05 18:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_service_subservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='subservice',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
