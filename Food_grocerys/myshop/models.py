from django.db import models


class RegistrationModel(models.Model):
    rno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    contact=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)
    otp=models.IntegerField()
    doj=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default="pending")

class CategoryModel(models.Model):
    cno=models.AutoField(primary_key=True)
    type= models.CharField(max_length=100)


class ProductModel(models.Model):
    pno=models.AutoField(primary_key=True)
    customer=models.OneToOneField(RegistrationModel,on_delete=models.CASCADE)
    pname=models.CharField(max_length=50)
    price=models.FloatField()
    quantity=models.IntegerField()
    photo=models.ImageField(upload_to='prod_img/')
    ctype=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)




# Create your models here.
