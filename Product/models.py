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
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=50, null = True, blank = True)
    overview = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="product_category", null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
class Product_version(models.Model):
    cover_image = models.ImageField(upload_to="product_images", null = True, blank = True)
    price = models.FloatField()
    quantity = models.IntegerField()
    details = models.TextField(null = True, blank = True)
    color = models.CharField(max_length=50, null = True, blank = True)
    discount = models.BooleanField(default=False)
    new_price = models.FloatField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_version")
    
    def __str__(self):
        return f"{self.product.name}"

    class Meta:
        verbose_name = "Product Version"
        verbose_name_plural = "Product Versions"

class Size_of_product(models.Model):
    sign = models.CharField(max_length=4)
    version = models.ForeignKey(Product_version, on_delete=models.CASCADE, related_name="product_size")

    def __str__(self):
        return f"{self.version}'s {self.sign} size"

    class Meta:
        verbose_name = "Product Size"
        verbose_name_plural = "Product Size"

class Images_of_product(models.Model):
    image = models.ImageField(upload_to="product_images")
    version = models.ForeignKey(Product_version, on_delete=models.CASCADE, related_name="product_images")

    def __str__(self):
        return f"{self.version}'s images"

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

class Tags(models.Model):
    name = models.CharField(max_length=20)
    version = models.ForeignKey(Product_version, on_delete=models.CASCADE, related_name="product_tag")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Tag"
        verbose_name_plural = "Product Tags"  

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
    version = models.ForeignKey(Product_version, on_delete=models.CASCADE, related_name="product_review")

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