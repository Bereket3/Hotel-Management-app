# Generated by Django 4.1.1 on 2022-10-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everything', '0004_alter_roomregestration_photo_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomregestration',
            name='Photo_Room',
            field=models.ImageField(blank=True, null=True, upload_to='statics/Photos/1/%Y/%m/%d'),
        ),
    ]
