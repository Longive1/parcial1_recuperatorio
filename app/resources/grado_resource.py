from flask import jsonify, Blueprint, request

from app.mapping.grado_mapping import GradoMapping
from app.services.grado_service import GradoService 
from .base_resource import BaseResource
from .utils import register_crud_resource

grado_bp = Blueprint('grado', __name__)
grado_service = GradoService()
grado_schema = GradoMapping()

class GradoResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=grado_service,
            schema=grado_schema,
            nombre_entidad="Grado"
        )

register_crud_resource(
    blueprint=grado_bp,
    resource_class=GradoResource,
    view_name='grado_api',
    url_prefix='grado'
)
