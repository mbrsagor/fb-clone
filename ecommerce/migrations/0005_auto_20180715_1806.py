# Generated by Django 2.0.6 on 2018-07-15 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='item',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
