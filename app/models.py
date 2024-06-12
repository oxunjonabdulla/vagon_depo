from django.core.validators import MaxLengthValidator
from django.db import models


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='banner')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'banners'
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    main_image = models.ImageField(upload_to='about')
    mini_image = models.ImageField(upload_to='about')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'abouts'
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


class Blog(BaseModel):
    image = models.ImageField(upload_to='blog')
    description = models.TextField()
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blogs'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class Service(BaseModel):
    image = models.ImageField(upload_to='service')

    title = models.CharField(max_length=100)
    description = models.TextField()
    mini_image = models.ImageField(upload_to='service', null=True, blank=True)
    mini_image2 = models.ImageField(upload_to='service', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'services'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Contact(BaseModel):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    message = models.TextField(MaxLengthValidator(limit_value=300,
                                                  message="Your message is too long. Please keep it under 300 characters."))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contacts'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class OurResult(BaseModel):
    icon = models.ImageField(upload_to='our_result')
    number = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'our_results'
        verbose_name = 'Our Result'
        verbose_name_plural = 'Our Results'
