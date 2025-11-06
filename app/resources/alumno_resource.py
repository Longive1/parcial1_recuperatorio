from flask import jsonify, Blueprint, request

from app.mapping.alumno_mapping import AlumnoMapping
from app.services.alumno_service import AlumnoService 
from .base_resource import BaseResource
from .utils import register_crud_resource

alumno_bp = Blueprint('alumno', __name__)
alumno_service = AlumnoService()
alumno_schema = AlumnoMapping()

class AlumnoResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=alumno_service,
            schema=alumno_schema,
            nombre_entidad="Alumno"
        )

register_crud_resource(
    blueprint=alumno_bp,
    resource_class=AlumnoResource,
    view_name='alumno_api',
    url_prefix='alumno'
)