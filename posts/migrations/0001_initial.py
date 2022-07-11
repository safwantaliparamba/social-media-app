# Generated by Django 4.0.6 on 2022-07-11 06:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('0e8adeb9-7075-48dc-8024-f873218afe77'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='posts/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='users.author')),
                ('likes', models.ManyToManyField(related_name='likes', to='users.author')),
            ],
        ),
    ]
