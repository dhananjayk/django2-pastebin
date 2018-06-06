from django.db import models
from django.contrib.auth.models import User
import datetime
from random import randrange


charset = tuple("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
def generate_url_key(length=8):
    password = ""
    lc = ""
    while len(password) < length:
        password += charset[randrange(0,62)]
    return password

def expiration_date_default():
    return datetime.date.today() + datetime.timedelta(days=7)


# Create your models here.
class PasteObject(models.Model):
    """Contains all the Pastes submitted"""
    url_key = models.CharField(unique=True, null=True, max_length=8)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(default=expiration_date_default)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        url_key = generate_url_key()
        while UsedUrlKeys.objects.filter(url_key=url_key).exists():
           url_key = generate_url_key()
           
        UsedUrlKeys.objects.create(url_key=url_key)
        self.url_key = url_key
        super(PasteObject, self).save(*args, **kwargs) # Call the real save() method

    class Meta:
        """Meta definition for PasteObject."""

        verbose_name = 'PasteObject'
        verbose_name_plural = 'PasteObjects'

class UsedUrlKeys(models.Model):
    """Model to store all the used url keys"""
    url_key = models.CharField(unique=True, null=True, max_length=8,)

