# Generated by Django 5.1.1 on 2024-09-09 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_rename_services_service'),
        ('rooms', '0002_roomsobject_created_roomsobject_updated'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]
