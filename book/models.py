from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return self.title
