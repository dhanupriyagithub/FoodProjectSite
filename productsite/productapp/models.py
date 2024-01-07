from django.db import models

class DemoModel(models.Model):
    Title = models.CharField(max_length=120)
    Image = models.ImageField(upload_to="demo",null=False,blank=False,help_text="Image size must be 1080px")
    Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Price in USD")
    Description = models.TextField(null=True, blank=True, help_text="Product description")
    Availability = models.BooleanField(default=True, help_text="Is the product available?")

    def __str__(self):
        return self.Title
