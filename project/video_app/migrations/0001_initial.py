# Generated by Django 5.1.3 on 2024-11-09 14:31

import django.db.models.deletion
import pgvector.django.vector
from pgvector.django import VectorExtension
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    def insert_data(apps, schema_editor):
        p_types = [chr(ord('a') + i) for i in range(16)]
        g_types = ['g' + chr(ord('a') + i) for i in range(4)]
        Personality = apps.get_model('video_app', 'Personality')
        PersonalityGroup = apps.get_model('video_app', 'PersonalityGroup')
        for i in range(len(g_types)):
            g = PersonalityGroup.objects.create(name=g_types[i])
            for j in range(4 * i, 4 * i + 4):
                Personality.objects.create(name=p_types[j], group=g)

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        VectorExtension(),
        migrations.CreateModel(
            name='PersonalityGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Personality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_app.personalitygroup')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('vector', pgvector.django.vector.VectorField(dimensions=6)),
                ('cluster', models.SmallIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(insert_data)
    ]
