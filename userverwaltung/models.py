from django.db import models
from django.urls import reverse

# Create your models here.
class Dozent(models.Model):
    name = models.CharField("Name", max_length=50)
    beschreibung = models.TextField("Beschreibung", blank=True)

    class Meta:
        verbose_name = "Dozent"
        verbose_name_plural = "Dozenten"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Dozent_detail", kwargs={"pk": self.pk})


class Benutzer(models.Model):
    email = models.CharField("E-Mail", max_length=50, primary_key=True)
    password = models.CharField("Passwort", max_length=250, pass)
    dozent = models.ManyToManyField(Dozent, verbose_name="Dozent")
    class Meta:
        verbose_name = "Benutzer"
        verbose_name_plural = "Benutzer"

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("Benutzer_detail", kwargs={"pk": self.pk})
