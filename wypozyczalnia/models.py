from django.db import models

class Autor(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    def __str__(self):
        return self.imie+" "+self.nazwisko

class Ksiazka(models.Model):
    tytul = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    rok_wydania = models.IntegerField()
    dostepnosc = models.BooleanField()
    def __str__(self):
        return self.tytul

