from django.db import models
    
class Surfboard(models.Model):
    TYPES = (
        ('shortboard', 'Shortboard'),
        ('longboard', 'Longboard'),
        ('fish', 'Fish'),
        ('funboard', 'Funboard'),
    )
    UNITS = (
        ('cm', 'cm'),
        ('inches', 'inches'),
        ('feet', 'feet'),
        ('liters', 'liters'),
    )

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPES)  
    brand = models.CharField(max_length=50) 
    length = models.FloatField()
    length_units = models.CharField(max_length=10, choices=UNITS, default='feet')
    width = models.FloatField()
    width_units = models.CharField(max_length=10, choices=UNITS, default='inches')
    thickness = models.FloatField()
    thickness_units = models.CharField(max_length=10, choices=UNITS, default='inches')
    volume = models.DecimalField(max_digits=4, decimal_places=2)
    volume_units = models.CharField(max_length=10, choices=UNITS, default='liters')

    def __str__(self):
        return f"{self.brand} {self.name} ({self.type})"



