# Generated by Django 4.0.3 on 2022-03-13 11:35

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0011_bookatable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookatable',
            name='email',
            field=models.CharField(max_length=50, validators=[main_page.models.BookATable.validate_email]),
        ),
    ]
