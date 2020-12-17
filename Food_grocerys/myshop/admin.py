from django.contrib import admin
from django.contrib.auth.admin import Group,User

from myshop.models import CategoryModel,ProductModel,ProfileModel


admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(ProfileModel)


admin.site.unregister(Group)
admin.site.unregister(User)
# Register your models here.
