# Generated by Django 4.0.4 on 2022-05-31 11:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True)),
                ('content', models.TextField()),
                ('publishAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
