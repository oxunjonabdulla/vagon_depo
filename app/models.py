from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


# Banner Models
class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'banners'
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'


@receiver(post_delete, sender=Banner)
def delete_banner_image(sender, instance, **kwargs):
    # Delete the image file when the Banner instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=Banner)
def delete_banner_image(sender, instance, **kwargs):
    # Delete the old image file when the Banner instance is updated
    if instance.pk:
        old_image = Banner.objects.get(pk=instance.pk).image
        if old_image != instance.image:
            old_image.delete(save=False)

    else:
        instance.image.delete(save=False)


# -------------------------------------------------------------------------

# About Models
class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    main_image = models.ImageField(upload_to='about/')
    mini_image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'abouts'
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


@receiver(post_delete, sender=About)
def delete_about_image(sender, instance, **kwargs):
    # Delete the image file when the About instance is deleted
    instance.main_image.delete(save=False)
    instance.mini_image.delete(save=False)


@receiver(pre_save, sender=About)
def delete_about_image(sender, instance, **kwargs):
    # Delete the old image file when the About instance is updated
    if instance.pk:
        old_image = About.objects.get(pk=instance.pk).main_image
        if old_image != instance.main_image:
            old_image.delete(save=False)

        old_mini_image = About.objects.get(pk=instance.pk).mini_image
        if old_mini_image != instance.mini_image:
            old_mini_image.delete(save=False)
    else:
        instance.main_image.delete(save=False)
        instance.mini_image.delete(save=False)


# -------------------------------------------------------------------------


# Blog Models
class Blog(BaseModel):
    image = models.ImageField(upload_to='blog/')
    description = models.TextField()
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blogs'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def get_absolute_url(self):
        return reverse("blog_details", args=[self.slug])


@receiver(post_delete, sender=Blog)
def delete_blog_image(sender, instance, **kwargs):
    # Delete the image file when the Blog instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=Blog)
def delete_blog_image(sender, instance, **kwargs):
    # Delete the old image file when the Blog instance is updated
    if instance.pk:
        old_image = Blog.objects.get(pk=instance.pk).image
        if old_image != instance.image:
            old_image.delete(save=False)

    else:
        instance.image.delete(save=False)


class SocialLink(BaseModel):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='social_link/')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'social_links'
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'


@receiver(signal=post_delete, sender=SocialLink)
def delete_social_link_image(sender, instance, **kwargs):
    # Delete the image file when the SocialLink instance is deleted
    instance.icon.delete(save=False)


@receiver(signal=pre_save, sender=SocialLink)
def delete_social_link_image(sender, instance, **kwargs):
    if instance.pk:
        old_image = SocialLink.objects.get(pk=instance.pk).icon
        if instance.icon != old_image:
            old_image.delete(save=False)
    else:
        instance.icon.delete(save=False)


class BlogSocialLink(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,
                             related_name='social_links')
    social_link = models.ForeignKey(SocialLink, on_delete=models.CASCADE,
                                    related_name='social_links')
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.link + " - " + self.blog.title


# -------------------------------------------------------------------------


# Service Models


class Service(BaseModel):
    image = models.ImageField(upload_to='service/')
    icon = models.ImageField(upload_to='service/')

    title = models.CharField(max_length=100)
    description = models.TextField()
    mini_image = models.ImageField(upload_to='service/', null=True, blank=True)
    mini_image2 = models.ImageField(upload_to='service/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'services'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


@receiver(post_delete, sender=Service)
def delete_service_image(sender, instance, **kwargs):
    # Delete the image file when the Service instance is deleted
    instance.image.delete(save=False)
    instance.icon.delete(save=False)

    if instance.mini_image:
        instance.mini_image.delete(save=False)

    if instance.mini_image2:
        instance.mini_image2.delete(save=False)


@receiver(pre_save, sender=Service)
def delete_service_image(sender, instance, **kwargs):
    # Delete the old image file when the Service instance is updated
    if instance.pk:
        old_image = Service.objects.get(pk=instance.pk).image
        if old_image != instance.image:
            old_image.delete(save=False)

        old_icon = Service.objects.get(pk=instance.pk).icon
        if old_icon != instance.icon:
            old_icon.delete(save=False)

        if instance.mini_image:
            old_mini_image = Service.objects.get(pk=instance.pk).mini_image
            if old_mini_image != instance.mini_image:
                old_mini_image.delete(save=False)

        if instance.mini_image2:
            old_mini_image2 = Service.objects.get(pk=instance.pk).mini_image2
            if old_mini_image2 != instance.mini_image2:
                old_mini_image2.delete(save=False)
    else:
        instance.image.delete(save=False)
        instance.icon.delete(save=False)

        if instance.mini_image:
            instance.mini_image.delete(save=False)

        if instance.mini_image2:
            instance.mini_image2.delete(save=False)


# -------------------------------------------------------------------------

# Contact Models

class Contact(BaseModel):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    message = models.TextField(MaxLengthValidator(limit_value=300,
                                                  message="Your message is too long. Please keep it under 300 characters."))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contacts'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


# -------------------------------------------------------------------------

# Our Result Models
class OurResult(BaseModel):
    icon = models.ImageField(upload_to='our_result/')
    number = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'our_results'
        verbose_name = 'Our Result'
        verbose_name_plural = 'Our Results'


@receiver(post_delete, sender=OurResult)
def delete_our_result_image(sender, instance, **kwargs):
    # Delete the image file when the OurResult instance is deleted
    instance.icon.delete(save=False)


@receiver(pre_save, sender=OurResult)
def delete_our_result_image(sender, instance, **kwargs):
    # Delete the old image file when the OurResult instance is updated
    if instance.pk:
        old_icon = OurResult.objects.get(pk=instance.pk).icon
        if old_icon != instance.icon:
            old_icon.delete(save=False)

    else:
        instance.icon.delete(save=False)


# -------------------------------------------------------------------------

# Gallery Models
class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")

    class Meta:
        db_table = 'gallery'
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'


@receiver(post_delete, sender=Gallery)
def delete_gallery_image(sender, instance, **kwargs):
    # Delete the image file when the Gallery instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=Gallery)
def delete_gallery_image(sender, instance, **kwargs):
    # Delete the old image file when the Gallery instance is updated
    if instance.pk:
        old_image = Gallery.objects.get(pk=instance.pk).image
        if old_image != instance.image:
            old_image.delete(save=False)

    else:
        instance.image.delete(save=False)


# -------------------------------------------------------------------------

# History Models

class History(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="history/")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "history"
        verbose_name = "History"
        verbose_name_plural = "History"


@receiver(post_delete, sender=History)
def delete_history_image(sender, instance, **kwargs):
    # Delete the image file when the History instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=History)
def delete_history_image(sender, instance, **kwargs):
    # Delete the old image file when the History instance is updated
    if instance.pk:
        old_image = History.objects.get(pk=instance.pk).image
        if old_image != instance.image:
            old_image.delete(save=False)

    else:
        instance.image.delete(save=False)


# -------------------------------------------------------------------------

# Management Models

class Management(models.Model):
    image = models.ImageField(upload_to="management/")
    fullname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    admission_days = models.TextField()

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = "management"
        verbose_name = "Management"
        verbose_name_plural = "Management"


@receiver(post_delete, sender=Management)
def delete_management_image(sender, instance, **kwargs):
    # Delete the image file when the Management instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=Management)
def delete_management_image(sender, instance, **kwargs):
    # Delete the old image file when the Management instance is updated
    if instance.pk:
        old_image = Management.objects.get(pk=instance.pk).image
        if old_image != instance.image:
            old_image.delete(save=False)

    else:
        instance.image.delete(save=False)

# -------------------------------------------------------------------------
