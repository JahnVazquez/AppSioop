from django.db import models 



class Tbl_Docente (models.Model):
    Doc_Cedula= models.IntegerField(primary_key= True, max_length=10)
    Doc_Nombre= models.CharField('Nombre', max_length=30)
    Doc_Apellido= models.CharField('Apellido', max_length=30)
    Doc_Correo=models.EmailField('Correo Electrónico',max_length=30)
    Doc_Telefono=models.models.IntegerField('Telefono'max_length=10)
    
