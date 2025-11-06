from marshmallow import fields, Schema, post_load, validate
from app.models import Grupo
from .base_mapping import BaseMapping


class GrupoMapping(BaseMapping):
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=50))

    def __init__(self, *args, **kwargs):
        super().__init__(model_class=Grupo,*args, **kwargs)
