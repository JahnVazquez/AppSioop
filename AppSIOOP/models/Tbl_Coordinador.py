from django.db import models 



class Tbl_Coordinador (models.Model):
    Coor_Cedula= models.IntegerField(primary_key= True, max_length=10)
    Coor_Nombre= models.CharField('Nombre', max_length=30)
    Coor_Apellido= models.CharField('Apellido', max_length=30)
    Coor_Correo=models.EmailField('Correo Electrónico',max_length=30)
    Coor_Telefono=models.models.IntegerField('Telefono'max_length=10)
    
