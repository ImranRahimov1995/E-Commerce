from django.db import models
from django.urls import reverse


class Category(models.Model):
    """simple category for group products"""

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('shop:by_category', args=[self.slug, ])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"


class Product(models.Model):
    

    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                            related_name="products")

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    image = models.ImageField(upload_to="products/%Y/%m/%d",
                                         blank=True)
    
    description = models.TextField(blank=True)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    available = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)