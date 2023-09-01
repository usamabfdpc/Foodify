from django import forms
from foodify.models import RecipeeCategory

# Order Recipee Form
class RecipeeCategoryForm(forms.ModelForm):
    class Meta:
        model = RecipeeCategory
        fields = ('name','packing_fee','status')
      
        widgets = {
            'name' : forms.TextInput(attrs={'class':'category-name'}),
            'packing_fee' : forms.TextInput(attrs={'class':'packing_fee'}),
            'status':forms.CheckboxInput(attrs={'class':'category-status'})
        }