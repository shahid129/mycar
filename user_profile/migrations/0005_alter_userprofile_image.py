# Generated by Django 3.2.15 on 2022-09-26 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='/static/images/audi.jpeg', null=True, upload_to=''),
        ),
    ]
