from marshmallow import fields, Schema, post_load, validate
from app.models import Universidad
from .base_mapping import BaseMapping


class UniversidadMapping(BaseMapping):
    nombre = fields.String(required = True, validate = validate.Length(min=1, max=100))
    sigla = fields.String(required = True, validate = validate.Length(min=1, max=10))

    def __init__(self, *args, **kwargs):
        super().__init__(model_class=Universidad,*args, **kwargs)
