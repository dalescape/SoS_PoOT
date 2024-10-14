from django.db import models
from django.contrib.auth.models import AbstractUser   # I added this

# Create your models here.

# For User I only want a username, character name and password, not email. 
# This module defines a custom User model for our application, extending Django's AbstractUser.
# The model is tailored specifically to store usernames and character names only, as emails are not required.
# Passwords are required by default with AbstractUser and is built in. 
# The 'username' is unique across the model ensuring each user can be uniquely identified.
# The 'char_name' is for game-related character identification and is not required to be unique.
# Future feature: Ability to select a favorite animal from a predefined list of game animals. This feature is 
# commented out for initial deployment and will be implemented later once basic functionalities are stable.

class User(AbstractUser):
    username = models.CharField(
        verbose_name='unique username',
        max_length=30,
        unique=True,
    )
    char_name = models.CharField(
        verbose_name='character name',
        max_length=30,
        unique=False,
    )
    # favorite_animal = models.CharField(
        # max_length=50,
        # choices=ANIMAL_CHOICES, # I need to refrence a list of all animals in the game, where should that data go?
        # default='dog',  # Optional: set a default value
        # blank=False,  # Optional: allows the field to be blank
        # help_text="Choose your favorite animal from the list."
    # )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['char_name'] #'favorite_animal'


