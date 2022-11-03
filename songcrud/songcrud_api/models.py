from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=50)
    release_date =models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lyrics(models.Model):
    content = models.CharField(max_length=300)
    song_id = models.OneToOneField(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.content