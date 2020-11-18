from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=5)

    #This method is an overide save in the model field of ticker.
    #It will CAPITALIZE whatever is submitted in the ticker field.
    def save(self, force_insert=False, force_update=False):
        self.ticker = self.ticker.upper()
        super(Stock, self).save(force_insert, force_update)

    def __str__(self):
        return self.ticker
