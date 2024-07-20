from django.db import models


class CitySearch(models.Model):
    city_name = models.CharField(max_length=100)
    search_count = models.IntegerField(default=1)
    last_searched = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('city_name', 'search_count')

    def __str__(self):
        return f"{self.city_name} (searched {self.search_count} times)"
