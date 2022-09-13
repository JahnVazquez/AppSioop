from django.db import models 



class Tbl_Aula (models.Model):
    
    Aul_Codigo= models.BigAutoField(primary_key= True,)
    Aul_Nombre= models.CharField('Nombre', max_length=30)
    Aul_Cupo=models.IntegerField('Cupo',max_length=2)
