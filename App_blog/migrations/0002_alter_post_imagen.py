# Generated by Django 5.0.4 on 2024-06-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/blog'),
        ),
    ]
