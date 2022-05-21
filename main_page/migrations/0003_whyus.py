# Generated by Django 4.0.3 on 2022-03-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(unique=True)),
                ('name', models.CharField(db_index=True, max_length=30, unique=True)),
                ('about', models.TextField(max_length=200)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]