from django.db import models

# Create your models here.


class Product(models.Model):
    product_name=models.CharField(max_length=200)
    product_price=models.IntegerField(null=True)
    product_description=models.TextField()
    product_images=models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.product_name
    


