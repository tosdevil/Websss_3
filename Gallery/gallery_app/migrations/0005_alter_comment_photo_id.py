# Generated by Django 4.2.1 on 2023-05-31 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0004_alter_comment_photo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo_id',
            field=models.IntegerField(null=True, verbose_name='ID фоточки'),
        ),
    ]
