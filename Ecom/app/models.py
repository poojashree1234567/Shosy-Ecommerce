from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinLengthValidator

STATE_CHOICES = {
    ('Adaman & Nicobar Island' , 'Adaman & Nicobar Island'),
    ('Andhra Pradesh' , 'Andhra Pradesh'),
    ('Madhya Pradesh' , 'Madhya Pradesh'),
    ('Uttar Pradesh' , 'Uttar Pradesh'),
    ('Arunachal Pradesh' , 'Arunachal Pradesh'),
    ('Assam' , 'Assam'),
    ('Bihar' , 'Bihar'),
    ('Chandigarh' , 'Chandigarh'),
    ('chattisgarh' , 'chattisgarh'),
    ('Maharashtra' , 'Maharashtra'),
    ('Gujrat' , 'Gujrat'),
    ('Punjab' , 'Punjab'),
    ('Nagaland' , 'Nagaland'),
    ('Odisha' , 'Odisha'),
    ('Tamil Nadu' , 'Tamil Nadu'),
    ('Telangana' , 'Telangana'),
    ('Tripura' , 'Tripura'),
    ('Uttarakhand' , 'Uttarakhand'),
    ('Sikkim' , 'Sikkim'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Puducherry', 'Puducherry'),
    ('Rajasthan', 'Rajasthan'),
    ('West Bengal', 'West Bengal'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
}
class Customer(models.Model):
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES = {
    ('mobile', 'Mobile'),
    ('electronics', 'Electronics'),
    ('top wear', 'Top Wear'),
    ('bottom wear', 'Bottom Wear'),
    ('glasses','Glasses'),
}
class Product(models.Model):
    is_active = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length= 20)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price

STATUS_CHOICES = {
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way', 'On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
}
class OrderPlaced(models.Model):
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price
    
    class Meta:
        verbose_name = "Order Placed"
        verbose_name_plural = "Orders Placed"
        ordering = ['-ordered_date']  # Newest orders first

    def __str__(self):
        return f"{self.product.title} - {self.status}"
    
class Banner(models.Model):
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='app/images/banner/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.alt_text or f"Banner {self.id}"
    
class LiveSale(models.Model):
    is_active = models.BooleanField(default=False)
    discount_details = models.CharField(max_length=255, default="5% Instant Discount on Axis Bank Credit and Debit Card")
    term_and_condition = models.CharField(max_length=255, default="Term and Condition Applied (For details visit Bank's official Website)")
    
    def __str__(self):
        return "Live Sale" if self.is_active else "No Sale"
    