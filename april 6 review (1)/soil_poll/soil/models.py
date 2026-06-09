from django.db import models

class Crop(models.Model):
    """Model to store crop recommendations with optimal soil conditions"""
    name = models.CharField(max_length=100, unique=True)
    emoji = models.CharField(max_length=10)
    scientific_name = models.CharField(max_length=150, blank=True, null=True)
    
    # Optimal pH range
    min_ph = models.FloatField()
    max_ph = models.FloatField()
    
    # Optimal moisture range (%)
    min_moisture = models.FloatField()
    max_moisture = models.FloatField()
    
    # Optimal temperature range (°C)
    min_temperature = models.FloatField()
    max_temperature = models.FloatField()
    
    # Description
    description = models.CharField(max_length=255)
    
    # Priority (higher = better match)
    priority = models.IntegerField(default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-priority']
    
    def __str__(self):
        return f"{self.emoji} {self.name}"
