# Generated by Django 4.1 on 2022-09-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favbooks',
            name='product_image',
            field=models.CharField(max_length=200),
        ),
    ]
