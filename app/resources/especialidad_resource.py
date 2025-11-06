from flask import jsonify, Blueprint, request
from app.mapping.especialidad_mapping import EspecialidadAlumnosFacultadMapping
from app.mapping.especialidad_mapping import EspecialidadMapping
from app.services.especialidad_service import EspecialidadService 
from .base_resource import BaseResource
from .utils import register_crud_resource

especialidad_bp = Blueprint('especialidad', __name__)
especialidad_service = EspecialidadService()
especialidad_schema = EspecialidadMapping()
especialidad_alumnos_facultad_schema = EspecialidadAlumnosFacultadMapping()

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
@especialidad_bp.route('/especialidad/<hashid:id>/alumnos', methods=['GET'])
def get_alumnos_por_especialidad(id):
    resultado = especialidad_service.obtener_alumnos_y_facultad(id)
    if not resultado:
        return jsonify({"message": "Especialidad no encontrada"}), 404
    return especialidad_alumnos_facultad_schema.dump(resultado), 200