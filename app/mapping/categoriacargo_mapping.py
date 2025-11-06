from marshmallow import fields, Schema, post_load, validate
from app.models import CategoriaCargo
from .base_mapping import BaseMapping

class CategoriaCargoMapping(BaseMapping):
    hashid = fields.String(dump_only = True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=30))
    
    def __init__(self, *args, **kwargs):
        super().__init__(model_class=CategoriaCargo,*args, **kwargs)
