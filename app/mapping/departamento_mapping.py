from marshmallow import fields, Schema, post_load, validate
from app.models import Departamento
from .base_mapping import BaseMapping


class DepartamentoMapping(BaseMapping):
    nombre = fields.String(
        required=True, validate=validate.Length(min=1, max=50))

    def __init__(self, *args, **kwargs):
        super().__init__(model_class=Departamento,*args, **kwargs)
