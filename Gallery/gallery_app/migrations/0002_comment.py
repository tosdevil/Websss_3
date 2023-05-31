# Generated by Django 4.2.1 on 2023-05-31 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=250, verbose_name='Автор комментария')),
                ('comment_text', models.CharField(max_length=250, verbose_name='Текст комментария')),
                ('photo_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery_app.photo')),
            ],
        ),
    ]