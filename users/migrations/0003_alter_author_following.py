# Generated by Django 4.0.6 on 2022-07-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_author_following'),
    ]
    
    operations = [
        migrations.AlterField(
            model_name='author',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='users.author'),
        ),
    ]
