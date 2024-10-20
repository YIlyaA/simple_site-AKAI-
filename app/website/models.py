from django.db import models
class DataCris(models.Model):
    typ = models.CharField(max_length=100)
    masa = models.CharField(max_length=100)
    czystosc = models.CharField(max_length=100)
    barwa = models.CharField(max_length=100)
    pochodzenie = models.CharField(max_length=100)
    wlasciciel = models.CharField(max_length=100)
    objects = models.Manager()  # The default manager.

    def __str__(self):
        return f"{self.typ} {self.czystosc} {self.wlasciciel}"

    def clean_masa(self):
        return self.masa.replace(",", ".").strip().lower()

    def get_masa_in_grams(self):
        masa_cleaned: str = self.masa.replace(
            ",", "."
        ).strip()

        if "ct" in masa_cleaned:
            return float(masa_cleaned.replace("ct", "")) * 0.2  # 1 ct = 0.2 g
        elif "g" in masa_cleaned:
            return float(masa_cleaned.replace("g", ""))
        else:
            return 0
