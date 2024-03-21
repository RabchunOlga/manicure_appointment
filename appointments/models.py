from django.db import models
from users.models import User


class AppointmentCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Категория: ' + self.name


class AppointmentsListModel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='manicure_images')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(to=AppointmentCategory, on_delete=models.CASCADE)


class Records(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(to=AppointmentsListModel, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
