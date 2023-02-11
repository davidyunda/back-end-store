from django.db import models

# Create your models here.

class PhotoModel(models.Model):
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     old_photo = PhotoModel.objects.filter(pk=self.pk).first()
    #     if old_photo and old_photo.photo:
    #         if old_photo.photo != self.photo:
    #             self.delete_photo(old_photo.photo)
    #     super().save(*args, ** kwargs)

    # def __self__(self):
    #     return f'{self.name} {self.price}'

