from django.db import models


class DevTool(models.Model):
    objects = models.Manager()
    name_tool = models.CharField(max_length=50, verbose_name="Средство разработки")


class Language(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, verbose_name="Язык программирования")
    year = models.CharField(max_length=50, verbose_name="Год выпуска")
    lang_dev = models.ForeignKey(DevTool, on_delete=models.CASCADE, null=True)
