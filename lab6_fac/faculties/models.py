from django.db import models

class Faculties(models.Model):
    faculty_name = models.CharField(max_length=50, verbose_name="Название факультета")
    passing_score = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Проходной балл")
    is_growing = models.BooleanField(verbose_name="Увеличивается ли проходной балл?")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Когда последний раз обновлялась информация о проходном балле?")