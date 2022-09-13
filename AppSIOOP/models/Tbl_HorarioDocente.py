from django.db import models
from .Tbl_Horario import Tbl_Horario
from .Tbl_Docente import Tbl_Docente



class Tbl_HorarioDocente (models.Model):
    Hor_Codigo= models.BigAutoField(primary_key= True)
    Tbl_Horario=models.ForeignKey(Tbl_Horario,related_name='Horario',on_delete=models.CASCADE)
    Tbl_Docente=models.ForeignKey(Tbl_Docente,related_name='Docente',on_delete=models.CASCADE)