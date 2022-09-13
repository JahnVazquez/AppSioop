from django.db import models 



class Tbl_Materias (models.Model):
    
    Mat_Codigo= models.BigAutoField(primary_key= True,)
    Mat_Nombre= models.CharField('Nombre', max_length=30)
    Mat_Horas=models.IntegerField('Horas',max_length=2)
