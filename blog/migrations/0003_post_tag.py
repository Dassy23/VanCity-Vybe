# Generated by Django 2.0.4 on 2018-05-12 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(max_length=100, null=True),
        ),
    ]