from flask import jsonify, Blueprint, request

from app.mapping.tipodocumento_mapping import TipoDocumentoMapping
from app.services.tipodocumento_service import TipoDocumentoService

from .base_resource import BaseResource
from .utils import register_crud_resource

tipodocumento_bp = Blueprint('tipodocumento', __name__)
tipodocumento_service = TipoDocumentoService()
tipodocumento_schema = TipoDocumentoMapping()

class TipoDocumentoResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=tipodocumento_service,
            schema=tipodocumento_schema,
            nombre_entidad="Tipo Documento"
        )

register_crud_resource(
    blueprint=tipodocumento_bp,
    resource_class=TipoDocumentoResource,
    view_name='tipodocumento_api',
    url_prefix='tipodocumento'
)
