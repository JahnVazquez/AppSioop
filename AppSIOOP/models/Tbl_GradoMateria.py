from django.db import models
from .Tbl_Grado import Tbl_Grado
from .Tbl_Materias import Tbl_Materias



class Tbl_GradoMateria (models.Model):
    Mat_Gra_Codigo= models.BigAutoField(primary_key= True)
    Tbl_Grado=models.ForeignKey(Tbl_Grado,related_name='Grado',on_delete=models.CASCADE)
    Tbl_Materias=models.ForeignKey(Tbl_Materias,related_name='Materias',on_delete=models.CASCADE)


