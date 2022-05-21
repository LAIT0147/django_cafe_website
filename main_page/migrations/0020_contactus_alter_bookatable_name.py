# Generated by Django 4.0.3 on 2022-03-14 10:51

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0019_alter_bookatable_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('email', models.CharField(max_length=50, validators=[main_page.models.ContactUs.validate_email])),
                ('subject', models.CharField(max_length=60)),
                ('message', models.TextField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.AlterField(
            model_name='bookatable',
            name='name',
            field=models.CharField(db_index=True, max_length=40),
        ),
    ]
