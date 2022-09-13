from django.db import models 
from .Tbl_Coordinador import Tbl_Coordinador
from .Tbl_Docente import Tbl_Docente


class Tbl_Horario (models.Model):
    Hor_Codigo= models.BigAutoField(primary_key= True)
    Tbl_Coordinador=models.ForeignKey(Tbl_Coordinador,related_name='Coordinador',on_delete=models.CASCADE)
    Tbl_Docente=models.ForeignKey(Tbl_Docente,related_name='Docente',on_delete=models.CASCADE)
    Hor_Fecha_Inicio=models.DateField('Fecha de Inicio')
    Hor_Fecha_Fin=models.DateField('Fecha de Finalización')
    Hor_Hora_Inicio=models.TimeField('Hora de Inicio')
    Hor_Hora_Fin=models.TimeField('Hora de Finalización')
    
    