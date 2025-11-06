from marshmallow import fields, Schema, post_load, validate
from app.models import Materia
from .base_mapping import BaseMapping


class MateriaMapping(BaseMapping):
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=255))
    codigo = fields.String(required=True, validate=validate.Length(min=1, max=20))
    observacion = fields.String(validate=validate.Length(max=255), allow_none=True)

    def __init__(self, *args, **kwargs):
        super().__init__(model_class=Materia,*args, **kwargs)