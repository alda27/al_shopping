# Generated by Django 3.0.7 on 2020-12-15 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='articles/%Y/%m/%d/'),
        ),
    ]
