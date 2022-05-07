from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):

    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'))
    PETS=(('petsareallowed','I have a pet or I am not against keeping pets at home.'),('petsarenotallowed',"I do not have a pet and I don't want any pets in my house."))
    SMOKE=(("smokingisallowed","I smoke or I am not against smoking in the home."),("smokingisnotallowed" , "I do not smoke and I don't want smoking in my home."))
    ALCHOOL=(("alchoolisallowed","I drink alcohol or I am not against alcohol consumption at home."),("alchoolisnotallowed","I do not drink alcohol and I do not want alcohol consumed in my home."))
    HOME=(("hashome","I have a house and I am looking for a roommate for my house."),("nohome","I do not have a house, I am looking for a house and roommate."))
        
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect()),
    pets = forms.ChoiceField(choices=PETS, widget=forms.RadioSelect()),
    smoke = forms.ChoiceField(choices=SMOKE, widget=forms.RadioSelect()),
    alchool = forms.ChoiceField(choices=ALCHOOL, widget=forms.RadioSelect()),
    home = forms.ChoiceField(choices=HOME,widget=forms.RadioSelect()),
    class Meta:
        model = Profile 
        fields = ['image','name','surname','gender','age','city','cityofarival','school','department','pets','smoke','alchool','home']
        

      

# class InformationForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['name','surname','gender','age','city','cityofarival','school','department','pets','smoke','alchool','home']
#         GENDER_CHOICES = (('M', 'Male'),('F', 'Female'))
#         PETS=(('petsareallowed','I have a pet or I am not against keeping pets at home.'),('petsarenotallowed',"I don't have a pet and I don't want any pets in my house."))
#         SMOKE=(("smokingisallowed","I smoke or I am not against smoking in the home."),("smokingisnotallowed" , "I don't smoke and I don't want smoking in my home."))
#         ALCHOOL=(("alchoolisallowed","I drink alcohol or I am not against alcohol consumption at home."),("alchoolisnotallowed","I do not drink alcohol and I do not want alcohol consumed in my home."))
#         HOME=(("hashome","I have a house and I am looking for a roommate for my house."),("nohome","I do not have a house, I am looking for a house and roommate."))
#         widgets = {
#             'gender': forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect()),
#             'pets': forms.ChoiceField(choices=PETS, widget=forms.RadioSelect()),
#             'smoke': forms.ChoiceField(choices=SMOKE, widget=forms.RadioSelect()),
#             'alchool': forms.ChoiceField(choices=ALCHOOL, widget=forms.RadioSelect()),
#             'home':forms.ChoiceField(choices=HOME,widget=forms.RadioSelect()),
        
#         }