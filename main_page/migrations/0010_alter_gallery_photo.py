# Generated by Django 4.0.3 on 2022-03-12 08:16

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0009_alter_gallery_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(upload_to=main_page.models.Gallery.get_file_name_gallery),
        ),
    ]
