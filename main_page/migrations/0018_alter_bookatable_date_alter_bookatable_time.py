# Generated by Django 4.0.3 on 2022-03-13 18:00

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0017_alter_bookatable_date_alter_bookatable_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookatable',
            name='date',
            field=models.CharField(max_length=10, validators=[main_page.models.BookATable.validate_date]),
        ),
        migrations.AlterField(
            model_name='bookatable',
            name='time',
            field=models.CharField(max_length=5),
        ),
    ]
