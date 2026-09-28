from django.db import models


class Country_total_deaths(models.Model):
    """Legacy model retained from the original COVID-19 visualization prototype."""

    country = models.CharField(max_length=255)
    deaths = models.IntegerField()

    def __str__(self):
        return f"{self.country}: {self.deaths}"
