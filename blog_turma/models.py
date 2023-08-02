from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tittle = models.CharField(max_length = 200)
    text = RichTextUploadingField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    published_date= models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.tittle   