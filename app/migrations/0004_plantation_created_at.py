# Generated by Django 3.1.3 on 2020-11-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_donation_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantation',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
