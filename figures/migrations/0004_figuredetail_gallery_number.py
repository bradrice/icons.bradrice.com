# Generated by Django 4.2.13 on 2024-07-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figures', '0003_figuredetail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='figuredetail',
            name='gallery_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
