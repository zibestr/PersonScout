from django.db import models
from pgvector.django import VectorField


class Video(models.Model):
    file = models.FileField()
    vector = VectorField(dimensions=6)
    cluster = models.SmallIntegerField()
    user = models.ForeignKey('login.CustomUser', on_delete=models.CASCADE)


class Vacancy(models.Model):
    name = models.CharField(max_length=50)
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
