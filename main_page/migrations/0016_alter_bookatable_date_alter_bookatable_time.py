# Generated by Django 4.0.3 on 2022-03-13 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0015_alter_bookatable_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookatable',
            name='date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='bookatable',
            name='time',
            field=models.CharField(max_length=5),
        ),
    ]