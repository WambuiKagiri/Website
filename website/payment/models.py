from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=191)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{}".format(self.id, self.email)

    def total_cost(self):
        return sum([ li.cost() for li in self.lineitem_set.all() ] )