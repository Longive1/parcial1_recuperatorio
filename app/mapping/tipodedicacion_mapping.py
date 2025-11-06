from marshmallow import fields, Schema, post_load, validate
from app.models import TipoDedicacion
from .base_mapping import BaseMapping

class TipoDedicacionMapping(BaseMapping):
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    observacion = fields.String(required=True, validate=validate.Length(min=1, max=200))

    def __init__(self, *args, **kwargs):
        super().__init__(model_class=TipoDedicacion,*args, **kwargs)
