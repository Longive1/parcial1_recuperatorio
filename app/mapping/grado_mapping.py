from marshmallow import fields, Schema, post_load, validate
from app.models import Grado
from .base_mapping import BaseMapping

class GradoMapping(BaseMapping):
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=50))
    descripcion = fields.String(required=True, validate=validate.Length(min=1, max=200))
    
    def __init__(self, *args, **kwargs):
        super().__init__(model_class=Grado,*args, **kwargs)
