from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name  


#class Product(models.Model):
 # title = models.CharField(max_length=200)
  # price = models.FloatField()
   # description = models.TextField()
    #category = ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    #image = models.CharField(max_length=5000)
    #date_added = models.DateTimeField(auto_now=True)  
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='categorie/')  # Utilisation de ImageField pour les images
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now_add=True)  # Utilisation de auto_now_add=True pour la date de création
    

    class Meta:
        ordering = ['-date_added']     
    def __str__(self):
        return self.title 
    
class Commande(models.Model):
    items = models.CharField(max_length=300) 
    total = models.CharField(max_length=150) 
    nom = models.CharField(max_length=150) 
    email = models.EmailField(max_length=200) 
    adress = models.CharField(max_length=300) 
    ville = models.CharField(max_length=300) 
    pays = models.CharField(max_length=300) 
    zipcode = models.CharField(max_length=300) 
    date_commande = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-date_commande']


    def __str__(self):
        return self.nom     