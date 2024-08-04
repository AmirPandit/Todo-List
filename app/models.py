from django.db import models

class formdataset(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.Title