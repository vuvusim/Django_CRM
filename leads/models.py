from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# custom user model
class User(AbstractUser):
    pass

class Lead(models.Model):

    # SOURCE_CHOICES = (
    #     ('Youtube', 'Youtube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter'),
        
    # )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # if on_delete=SET_NULL must be null=True
    # if on_delete=SET_DEFAULT must be default=(default value)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)


class Agent(models.Model):
    # one agent can have one user (OneToOneField)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # we don't need firstname and lastname since agen will login to CRM, and User model asks for first name and lastname
    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)