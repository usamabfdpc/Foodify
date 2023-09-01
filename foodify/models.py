from django.db import models

# Create your models here.

class RecipeeCategory(models.Model):   

    name = models.CharField(max_length=100,verbose_name='Category name')
    packing_fee = models.DecimalField(decimal_places=3,max_digits=10)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str( self.name)


class Ingredients(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self) -> str:
        return str( self.title)
    


class Recipee(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='recipy',blank=True)
    category = models.ManyToManyField(RecipeeCategory)
    ingredients = models.ManyToManyField(Ingredients,related_name='ingredients')
    status = models.BooleanField(default=True)
    featured_recipy = models.BooleanField()
    price_set_by_size = models.BooleanField()
    price= models.DecimalField(max_digits=10,decimal_places=2,blank = True,null=True)
           
    def __str__(self) -> str:
        return str( self.name)    
    
class ExtraIngredients(models.Model):
    ingredient = models.OneToOneField(Ingredients,on_delete=models.CASCADE)        
    price = models.DecimalField(max_digits=10,decimal_places=3)
    recipee = models.ManyToManyField(Recipee)

    def __str__(self) -> str:
        return f'{self.ingredient} ({self.price})'



class RecipeeVarients(models.Model):
    SIZES_CHOICES = [
        ('extra_small','Extra small'),
        ('small','Small'),
        ('normal','Normal'),
        ('large','Large'),
        ('extra_large','Extra Large'),

    ]
    size = models.CharField(max_length=20,choices=SIZES_CHOICES,default=SIZES_CHOICES[1])
    price = models.DecimalField(max_digits=10,decimal_places=3)
    recipee = models.ForeignKey(Recipee,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.size} ({self.price})$'
    