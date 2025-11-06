from flask import jsonify, Blueprint, request

from app.mapping.orientacion_mapping import OrientacionMapping
from app.services.orientacion_service import OrientacionService 
from .base_resource import BaseResource
from .utils import register_crud_resource

orientacion_bp = Blueprint('orientacion', __name__)
orientacion_service = OrientacionService()
orientacion_schema = OrientacionMapping()

class OrientacionResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=orientacion_service,
            schema=orientacion_schema,
            nombre_entidad="Orientacion"
        )

register_crud_resource(
    blueprint=orientacion_bp,
    resource_class=OrientacionResource,
    view_name='orientacion_api',
    url_prefix='orientacion'
)