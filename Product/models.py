from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_navbar = models.BooleanField(default=True)
    p_category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="parent_category", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Product(models.Model):
    discounts = (
        (5, '5'),
        (10, '10'),
        (15, '15'),
        (20, '20'),
        (25, '25'),
        (30, '30'),
        (35, '35'),
        (40, '40'),
        (45, '45'),
        (50, '50'),
        (55, '55'),
        (60, '60'),
        (65, '65'),
        (70, '70'),
    )
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to="product_images")
    price = models.FloatField()
    in_sale = models.BooleanField(default=False)
    discount = models.IntegerField(choices=discounts, null=True, blank=True)
    new_price = models.FloatField(null=True, blank=True)
    overview = models.TextField()
    details = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="product_category", null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.in_sale:
            self.new_price = self.price - self.price*(self.discount/100)
        return super().save()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
class Product_version(models.Model):
    quantity = models.IntegerField()
    color = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_version")
    
    def __str__(self):
        return f"{self.product.name}'s {self.color} version"

    class Meta:
        verbose_name = "Product Version"
        verbose_name_plural = "Product Versions"

class Images_of_product(models.Model):
    image = models.ImageField(upload_to="product_images")
    version = models.ForeignKey(Product_version, on_delete=models.CASCADE, related_name="product_images")

    def __str__(self):
        return f"{self.version}'s images"

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

class Review(models.Model):
    Rates = {
        (1, "20"),
        (2, "40"),
        (3, "60"),
        (4, "80"),
        (5, "100")
    }
    price_review = models.IntegerField(choices=Rates)
    value_review = models.IntegerField(choices=Rates)
    quality_review = models.IntegerField(choices=Rates)
    nickname = models.CharField(max_length=75)
    summary = models.CharField(max_length=50)
    product_review = models.TextField()
    review_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_review")

    def __str__(self):
        return f"{self.nickname}'s reviews"

    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"

class ProductStatistic(models.Model):
    product = models.ForeignKey(Product_version, on_delete=models.CASCADE, related_name="product_statistic")
    reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product}'s stats"

    class Meta:
        verbose_name = "Product Statistic"
        verbose_name_plural = "Product Statistics"