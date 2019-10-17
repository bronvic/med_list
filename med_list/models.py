from django.db import models


class Description(models.Model):
    description = models.TextField()

    def __str__(self):
        return f'{self.pk}'

    def short_description(self):
        short_desc = self.description[:100]
        return f'{short_desc}...' if len(self.description) > 100 else f'{short_desc}'


class Drug(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.ForeignKey('Description', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}'
