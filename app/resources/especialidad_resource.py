from flask import jsonify, Blueprint, request

from app.mapping.especialidad_mapping import EspecialidadMapping
from app.services.especialidad_service import EspecialidadService 
from .base_resource import BaseResource
from .utils import register_crud_resource

especialidad_bp = Blueprint('especialidad', __name__)
especialidad_service = EspecialidadService()
especialidad_schema = EspecialidadMapping()

class EspecialidadResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=especialidad_service,
            schema=especialidad_schema,
            nombre_entidad="Especialidad"
        )

register_crud_resource(
    blueprint=especialidad_bp,
    resource_class=EspecialidadResource,
    view_name='especialidad_api',
    url_prefix='especialidad'
)