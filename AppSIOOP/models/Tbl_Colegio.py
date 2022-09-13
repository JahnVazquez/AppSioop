from django.db import models 



class Tbl_Colegio (models.Model):
    
    Col_Codigo= models.BigAutoField(primary_key= True,)
    Col_Nombre= models.CharField('Nombre', max_length=30)
    Col_Direccion=models.CharField('Dirección',max_length=100)
