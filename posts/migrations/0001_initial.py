# Generated by Django 4.0.5 on 2022-06-28 05:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_author_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('dd1b5e16-ff37-4d5f-9520-1d5cdb5f0aa9'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='posts/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='users.author')),
            ],
        ),
    ]