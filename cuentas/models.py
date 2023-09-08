from django.db import models

# Create your models here.

# Models for counts
class Counts(models.Model):
    grade = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    mount = models.DecimalField(max_digits=10, decimal_places=2)
    payed = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Grade: {self.grade} Teacher: {self.teacher}"