from marshmallow import fields, Schema, post_load, validate
from app.models import Plan
from .base_mapping import BaseMapping

class PlanMapping(BaseMapping):
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=50))
    fecha_inicio = fields.Date(required=True)
    fecha_fin = fields.Date(required=True)
    observacion = fields.String(validate=validate.Length(max=255), allow_none=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(model_class=Plan,*args, **kwargs)
     
     
     
    
