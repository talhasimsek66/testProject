from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name + " at " + self.url

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Book(models.Model):
    title = models.CharField(max_length=50)
    numpages = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title + " published by " + str(self.publisher)