from django.db import models
from uuid import uuid4
from os import path
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.validators import RegexValidator
import datetime
from datetime import datetime
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        ordering = ('position', )


class Dish(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes', filename)

    name = models.CharField(max_length=50, unique=True, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField(max_length=500, blank=True)
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}: {self.price}'


class WhyUs(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)
    number = models.PositiveSmallIntegerField(unique=True)
    about = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}: {self.number}'

    class Meta:
        ordering = ('number', )


class Events(models.Model):
    def get_file_name_events(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/events', filename)

    name = models.CharField(max_length=40, unique=True, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    desc = models.TextField(max_length=200)
    first_check = models.TextField(max_length=100, unique=True)
    second_check = models.TextField(max_length=100, unique=True, blank=True)
    third_check = models.TextField(max_length=100, unique=True, blank=True)
    last_word = models.TextField(max_length=200)
    photo = models.ImageField(upload_to=get_file_name_events)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name}: {self.price}'


class Chefs(models.Model):
    def get_file_name_chefs(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/chefs', filename)

    name = models.CharField(max_length=30, unique=True, db_index=True)
    spec = models.CharField(max_length=40, unique=True)
    photo = models.ImageField(upload_to=get_file_name_chefs)
    twitter = models.CharField(max_length=50, unique=True)
    facebook = models.CharField(max_length=50, unique=True)
    insta = models.CharField(max_length=50, unique=True)
    linkedin = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name}: {self.spec}: {self.is_visible}'


class Testimonials(models.Model):
    def get_file_name_testimonials(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/testimonials', filename)

    name = models.CharField(max_length=40, unique=True, db_index=True)
    speciality = models.CharField(max_length=50, unique=True)
    whatsaid = models.TextField(max_length=500)
    photo = models.ImageField(upload_to=get_file_name_testimonials)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name} : {self.speciality} : {self.is_visible}'


class Gallery(models.Model):
    def get_file_name_gallery(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/gallery', filename)

    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=40, unique=True, db_index=True)
    photo = models.ImageField(upload_to=get_file_name_gallery)
    photo_thumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(800, 600)], format='JPEG',
                                     options={'quality': 60})
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}: {self.number}: {self.is_visible}'


class BookATable(models.Model):
    def validate_date(self):
        pass

    def validate_email(self):
        if "@" in self:
            return self
        else:
            raise ValidationError('Incorrect email')

    mobile_regex = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')
    # date_regex = RegexValidator(regex=r'^(3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9])/(?:[0-9]{2})?[0-9]{2}$',
    #                            message="dd/mm/yyyy")
    # time_regex = RegexValidator(regex=r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/', message='HH:MM of 24-hour format')
    name = models.CharField(max_length=40, db_index=True)
    phone = models.CharField(max_length=15, validators=[mobile_regex])
    persons = models.PositiveSmallIntegerField()
    email = models.CharField(max_length=50, validators=[validate_email])
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=5)
    message = models.TextField(max_length=500, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'{self.name}: {self.phone}: {self.message[:30]}'


class ContactUs(models.Model):
    def validate_email(self):
        if "@" in self:
            return self
        else:
            raise ValidationError('Incorrect email')

    name = models.CharField(max_length=50, db_index=True)
    email = models.CharField(max_length=50, validators=[validate_email])
    subject = models.CharField(max_length=60)
    message = models.TextField(max_length=500, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'{self.name}: {self.subject}'
