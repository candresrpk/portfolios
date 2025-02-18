from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Transaction(models.Model):
    # Transaction Type
    options = (
        ('Income', 'Income'),
        ('Expense', 'Expense')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()
    transaction_type = models.CharField(max_length=10, choices=options)

    def __str__(self):
        return f"{self.owner.username} - {self.amount} - {self.transaction_type}"

# Create your models here.
