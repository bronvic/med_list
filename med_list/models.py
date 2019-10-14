from django.db import models


class Description(models.Model):
    description = models.TextField(unique=True)

    def __str__(self):
        short_desc = self.description[:20]
        return f'{short_desc}...'


class Drug(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.ForeignKey('Description', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}'
