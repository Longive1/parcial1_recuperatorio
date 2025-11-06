from flask import jsonify, Blueprint, request
from app.mapping.tipoespecialidad_mapping import TipoEspecialidadMapping
from app.services.tipoespecialidad_service import TipoEspecialidadService
from .base_resource import BaseResource
from .utils import register_crud_resource

tipo_especialidad_bp = Blueprint('tipoespecialidad', __name__)
tipo_especialidad_service = TipoEspecialidadService()
tipo_especialidad_schema = TipoEspecialidadMapping()

class TipoEspecialidadResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=tipo_especialidad_service,
            schema=tipo_especialidad_schema,
            nombre_entidad="Tipo Especialidad"
        )

register_crud_resource(
    blueprint=tipo_especialidad_bp,
    resource_class=TipoEspecialidadResource,
    view_name='tipoespecialidad_api',
    url_prefix='tipo_especialidad'
)
