from django.db import models


class Video(models.Model):
    link = models.CharField(max_length=200)
    title = models.CharField(max_length=10000)
    first = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(
        null=True,
        blank=True,
        max_length=200
    )
    description = models.CharField(
        null=True,
        blank=True,
        max_length=200
    )
    date = models.DateField(auto_now_add=True)
    photo = models.CharField(
        null=True,
        blank=True,
        max_length=200
    )


class Contact(models.Model):
    mail = models.EmailField(max_length=200)
    sujet = models.CharField(max_length=500, default='')
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    pseudo = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(max_length=2000)
