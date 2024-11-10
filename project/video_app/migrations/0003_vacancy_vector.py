# Generated by Django 5.1.3 on 2024-11-09 15:21

import pgvector.django.vector
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0002_remove_video_cluster_alter_video_vector'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='vector',
            field=pgvector.django.vector.VectorField(dimensions=5, null=True),
        ),
    ]