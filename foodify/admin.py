from django.contrib import admin
from django.urls import reverse
from .forms import RecipeeCategoryForm
from foodify.models import RecipeeCategory,Ingredients,ExtraIngredients,RecipeeVarients
from django.utils.html import format_html
# Register your models here.

@admin.register(RecipeeCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['name','cal_product','cal_order','status','edit','delete']
    list_editable =['status',]
    change_list_template ='admin/category_display.html'
    search_fields =['name']
    sortable_by =['name',]
    list_filter =['status']
    list_per_page = 3
    
    
    form = RecipeeCategoryForm

    

    @admin.display(description="Products")
    def cal_product(self,obj):
        return 1
    


    @admin.display(description="Order")
    def cal_order(self,obj):
        return 1
    
    @admin.display()
    def edit(self,obj):
        return format_html('<a href="#">  edit</a>')
    
    @admin.display()
    def delete(self,obj):
        address = reverse('delete-category-list')
        return format_html(f'<a class="deleteBtn"> <i class="fa-regular fa-trash-can"></i> </a>')
    

@admin.register(Ingredients)
class IngredientAdmin(admin.ModelAdmin):
  pass

@admin.register(ExtraIngredients)
class ExtraIngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(RecipeeVarients)
class VarientsAdmin(admin.ModelAdmin):
    pass

# Recipee Varients Inline
class RecipeeVarientInline(admin.TabularInline):
    model = RecipeeVarients
    extra = 0
