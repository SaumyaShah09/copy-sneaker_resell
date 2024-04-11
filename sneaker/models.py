from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATE_CHOICES=(

        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Ladakh', 'Ladakh'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal')


)






CATEGORY_CHOICES=(
    ('F','Fashion'),
    ('DE','Daily Essentials'),
    ('Home','Homedecor'),
    ('El','Electronics'),
    ('Books','Books'),
    ('Outdoor','Outdoor'),

)


class Product(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=250,default='xyz@gmail.com')
    prodapp = models.TextField(default='')
    category =models.CharField(choices=CATEGORY_CHOICES,max_length=10)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name


from django.contrib.auth.models import User

from django.contrib.auth.models import User

from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.db import models

class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , default=None, null=True, blank=True)  # Use CASCADE instead of SET_NULL
    name = models.CharField(max_length=200)
    requirement = models.CharField(max_length=100)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
