from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    score = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '学生'
        db_table = 'student'
