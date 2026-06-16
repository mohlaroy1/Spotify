from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField( blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='albums/%Y/%m', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Song(models.Model):

    genre_choices = (
        ('pop', 'pop'),
        ('rock', 'rock'),
        ('classic', 'classic'),
    )

    name = models.CharField(max_length=100)
    genre = models.CharField(choices=genre_choices,max_length=100)
    duration = models.DurationField()
    file = models.FileField(upload_to='songs/%Y/%m', blank=True, null=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.singer}"



