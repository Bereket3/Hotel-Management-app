# Generated by Django 4.1.1 on 2022-10-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everything', '0002_alter_roomregestration_photo_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingform',
            name='Customer_Name',
            field=models.CharField(max_length=50),
        ),
    ]
