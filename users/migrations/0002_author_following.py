# Generated by Django 4.0.6 on 2022-07-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='follows', to='users.author'),
        ),
    ]
