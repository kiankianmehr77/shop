from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering = ("name",)
        verbose_name_plural = "categories"


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)  # موجودی انبار
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        if self.stock <= 0:
            self.available = False
            self.stock = 0
        else:
            self.available = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name