# Generated by Django 3.0.7 on 2020-12-11 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('cno', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('rno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('otp', models.IntegerField()),
                ('doj', models.DateField(auto_now_add=True)),
                ('status', models.CharField(default='pending', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('pno', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('photo', models.ImageField(upload_to='prod_img/')),
                ('ctype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.CategoryModel')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myshop.RegistrationModel')),
            ],
        ),
    ]
