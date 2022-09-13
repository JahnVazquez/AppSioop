from django.db import models 



class Tbl_Usuario (models.Model):
    Usu_Codigo= models.BigAutoField(primary_key= True,)
    Usu_id=models.IntegerField(max_length=15)
    Usu_Nombre= models.CharField('Nombre', max_length=30)
    Usu_Apellido= models.CharField('Apellido', max_length=30)
    Usu_Correo=models.EmailField('Correo Electrónico',max_length=30)
    Usu_Telefono=models.models.IntegerField('Telefono'max_length=10)
    Usu_usuario=models.CharField('Usuario',max_length=45)
    Usu_Usuario=models.CharField('Usuario',max_length=45)
    Usu_Contraseña=models.CharField(_'Contraseña', max_length=100)
    Usu_Estado=models.BooleanField(default=True)
    
    
