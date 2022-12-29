from django.db import models
# from django.urls import reverse
# from Personalerfassung import settings
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Mitarbeiter(models.Model):
    Vorname = models.CharField(max_length=200) 
    Nachname = models.CharField(max_length=200) 
    Geburtsdatum= models.DateField(default=None, null=True)
    SZVS = models.IntegerField()
    Kinder = models.IntegerField(default=0) #ändern auf anzahl
    
    def __str__(self): # Neu
         return str(self.id) + " " + self.Vorname # Zeigt in der AdminKonsole die Id und den Vornamen an

    # def get_absolute_url(self): # Neu
    #     return reverse('mitarbeiter_detail', args=[str(self.id)]) # Neu
    

class Kinder(models.Model):
    Vorname = models.CharField(max_length=200) 
    Nachname = models.CharField(max_length=200)
    Geburtsdatum= models.DateField(default=None, null=True) 
    SZVS = models.IntegerField()
    Familienbonus = models.BooleanField()
    Mitarbeiter = models.ForeignKey("Mitarbeiter",on_delete=models.SET_NULL,null=True)
    def __str__(self): # Neu
         return str(self.id) + " " + self.Vorname # Zeigt in der AdminKonsole die Id und den Vornamen an

class Vordienstzeiten(models.Model): # alles was man für berechnung für vordienstz bracuht , wo er gearbeitet, stundenanzahl, was wielange,
    Dienstjahre = models.IntegerField()
    Wo = models.CharField(max_length=200)
    Anstellungsart = models.CharField(max_length=200)
    #MitarbeiterID = models.ForeignKey("Mitarbeiter",on_delete=models.SET_NULL,null=True)
    MitarbeiterNR = models.ForeignKey("Mitarbeiter",on_delete=models.SET_NULL,null=True)

    def __str__(self): # Neu
         return str(self.id) # zeigt in der AdminKonsole die Id an

class Vertragstabelle(models.Model):
    Vertragsart = models.CharField(max_length=200)
    Gehaltstufe = models.IntegerField()
    MitarbeiterID = models.ForeignKey("Mitarbeiter",on_delete=models.SET_NULL,null=True)

    def __str__(self): # Neu
         return str(self.id) # zeigt in der AdminKonsole die Id an

    # def __str__(self): # Neu
    #     return self.nachname # Neu

    # def get_absolute_url(self): # Neu
    #     return reverse('adress_detail', args=[str(self.id)]) # Neu