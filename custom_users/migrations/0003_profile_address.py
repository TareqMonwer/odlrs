# Generated by Django 2.2.1 on 2019-06-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0002_profile_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
