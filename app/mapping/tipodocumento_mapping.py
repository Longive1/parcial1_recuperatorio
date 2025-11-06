from marshmallow import fields, Schema, post_load, validate
from app.models import TipoDocumento
from .base_mapping import BaseMapping

class TipoDocumentoMapping(BaseMapping):
    dni = fields.Integer(required=True, validate=validate.Range(min=1000000, max=99999999))
    libreta_civica = fields.String(required=True, validate=validate.Length(min=1, max=20))
    libreta_enrolamiento = fields.String(required=True, validate=validate.Length(min=1, max=20))
    pasaporte = fields.String(required=True, validate=validate.Length(min=1, max=20))


    def __init__(self, *args, **kwargs):
        super().__init__(model_class=TipoDocumento,*args, **kwargs)
