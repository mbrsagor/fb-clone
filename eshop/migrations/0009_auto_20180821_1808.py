# Generated by Django 2.0.6 on 2018-08-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0008_category_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
