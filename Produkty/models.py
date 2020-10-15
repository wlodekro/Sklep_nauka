from django.db import models

# Create your models here.

class Kategoria(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Producent(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"


class Produkty(models.Model):
    def __str__(self):
        return self.nazwa

    kategoria = models.ForeignKey(Kategoria, null = True, blank = True, on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=6,decimal_places=2)


    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

