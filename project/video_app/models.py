from django.db import models
from pgvector.django import VectorField


class Video(models.Model):
    file = models.FileField()
    vector = VectorField(dimensions=5, null=True)


class Speciality(models.Model):
    name = models.CharField(max_length=50)
    vector = VectorField(dimensions=5, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Personality(models.Model):
    name = models.CharField(max_length=40)
    group = models.ForeignKey('PersonalityGroup', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class PersonalityGroup(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
