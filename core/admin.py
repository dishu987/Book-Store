from django.contrib import admin
from .models import (
    Favbooks,RecentSearch
)

@admin.register(Favbooks)
class FavbooksModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','selling_price','discounted','description','brand','product_image',)

@admin.register(RecentSearch)

class RecentSearchAdmin(admin.ModelAdmin):
    list_display = ('id','name','time')