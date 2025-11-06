from marshmallow import fields, Schema, post_load, validate
from app.models import Autoridad
from .base_mapping import BaseMapping


class AutoridadMapping(BaseMapping):
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    telefono = fields.String(validate=validate.Length(max=20), allow_none=True)
    email = fields.String(validate=validate.Length(max=100), allow_none=True)

    cargo_id = fields.Integer(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(model_class=Autoridad,*args, **kwargs)