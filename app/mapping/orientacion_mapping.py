from marshmallow import fields, Schema, post_load, validate
from app.models import Orientacion
from .base_mapping import BaseMapping


class OrientacionMapping(BaseMapping):
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=50))

    especialidad_id = fields.Integer(required=True)

    plan_id = fields.Integer(required=True)

    materia_id = fields.Integer(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(model_class=Orientacion,*args, **kwargs)