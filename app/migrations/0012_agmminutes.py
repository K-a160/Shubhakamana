# Generated by Django 5.0.3 on 2024-04-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_quarterlyreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='AGMMinutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='agm_minutes/')),
            ],
        ),
    ]
