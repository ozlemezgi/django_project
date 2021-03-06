# Generated by Django 3.2.7 on 2022-06-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='alchool',
            field=models.CharField(choices=[('I drink alcohol or I am not against alcohol consumption at home.', 'I drink alcohol or I am not against alcohol consumption at home.'), ('I do not drink alcohol and I do not want alcohol consumed in my home.', 'I do not drink alcohol and I do not want alcohol consumed in my home.')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='home',
            field=models.CharField(choices=[('I have a house and I am looking for a roommate for my house.', 'I have a house and I am looking for a roommate for my house.'), ('I do not have a house, I am looking for a house and roommate.', 'I do not have a house, I am looking for a house and roommate.')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pets',
            field=models.CharField(choices=[('I have a pet or I am not against keeping pets at home.', 'I have a pet or I am not against keeping pets at home.'), ("I don't have a pet and I don't want any pets in my house.", "I don't have a pet and I don't want any pets in my house.")], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='smoke',
            field=models.CharField(choices=[('I smoke or I am not against smoking in the home.', 'I smoke or I am not against smoking in the home.'), ("I don't smoke and I don't want smoking in my home.", "I don't smoke and I don't want smoking in my home.")], max_length=100, null=True),
        ),
    ]
