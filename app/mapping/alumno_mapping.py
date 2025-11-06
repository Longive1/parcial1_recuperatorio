from marshmallow import Schema, fields, post_load, validate
from app.models import Alumno
from .base_mapping import BaseMapping

class AlumnoMapping(BaseMapping):
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=50))
    apellido = fields.String(required=True, validate=validate.Length(min=1, max=50))
    nrodocumento = fields.String(required=True, validate=validate.Length(min=1, max=50))
    tipo_documento_id = fields.Integer(required=True)
    fecha_nacimiento = fields.Date(required=True)
    sexo = fields.String(required=True, validate=validate.Length(equal=1))
    nro_legajo = fields.Integer(required=True)
    fecha_ingreso = fields.Date(required=True)
    
    especialidad_id = fields.Integer(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(model_class=Alumno,*args, **kwargs)