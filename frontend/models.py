from django.db import models
from account.models import CustomUser
from medicines.models import Medicine


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="User", on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, verbose_name="Medicine", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")

    def __str__(self):
        return str(self.user)

    # Creating Model Property to calculate Quantity x Price
    @property
    def total_price(self):
        return self.quantity * self.medicine.price


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    ordered_date = models.DateTimeField(auto_now_add=True)
