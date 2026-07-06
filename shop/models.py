from django.db import models



class Category(models.Model):

    name = models.CharField(
        max_length=100
    )
    slug = models.SlugField(unique=True) #url رو به اسم تغییر میده بجای id 
    def __str__(self):
        return self.name
     


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(max_length=100)

    slug = models.SlugField(unique=True)

    description = models.TextField()

    price = models.PositiveIntegerField()

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    download_link = models.URLField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name