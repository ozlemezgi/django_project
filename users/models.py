from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female'))
    CITIES=(('nicosia','nicosia'),('famagusta','famagusta'),('kyrenia','kyrenia'),('omorfo','omorfo'),('lefka','lefka'))
    PETS=(('I have a pet or I am not against keeping pets at home.','I have a pet or I am not against keeping pets at home.'),("I don't have a pet and I don't want any pets in my house.","I don't have a pet and I don't want any pets in my house."))
    SMOKE=(("I smoke or I am not against smoking in the home.","I smoke or I am not against smoking in the home."),("I don't smoke and I don't want smoking in my home.", "I don't smoke and I don't want smoking in my home."))
    ALCHOOL=(("I drink alcohol or I am not against alcohol consumption at home.","I drink alcohol or I am not against alcohol consumption at home."),("I do not drink alcohol and I do not want alcohol consumed in my home.","I do not drink alcohol and I do not want alcohol consumed in my home."))
    HOME=(("I have a house and I am looking for a roommate for my house.","I have a house and I am looking for a roommate for my house."),("I do not have a house, I am looking for a house and roommate.","I do not have a house, I am looking for a house and roommate."))

    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    name = models.CharField(max_length=100,null=True)
    surname = models.CharField(max_length=100,null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100,null=True)
    age= models.CharField(max_length=50,null=True)
    city= models.CharField(choices=CITIES, max_length=100,null=True)
    cityofarival= models.CharField(max_length=100,null=True)
    school= models.CharField(max_length=100,null=True)
    department= models.CharField(max_length=100,null=True)
    pets= models.CharField(choices=PETS, max_length=100,null=True)
    smoke= models.CharField(choices=SMOKE, max_length=100,null=True)
    alchool= models.CharField(choices=ALCHOOL, max_length=100,null=True)
    home=models.CharField(choices=HOME, max_length=100,null=True)
    


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img =Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)





