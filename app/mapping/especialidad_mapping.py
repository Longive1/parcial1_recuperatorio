from marshmallow import fields, Schema, post_load, validate
from app.models import Especialidad
from .base_mapping import BaseMapping


class EspecialidadMapping(BaseMapping):
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=100))
    letra = fields.String(required=True, validate=validate.Length(equal=1))
    observacion = fields.String(
        validate=validate.Length(max=255), allow_none=True)

    tipoespecialidad_id = fields.Integer(required=True)

    facultad_id = fields.Integer(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(model_class=Especialidad,*args, **kwargs)
