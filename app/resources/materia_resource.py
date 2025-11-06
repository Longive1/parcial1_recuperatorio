from flask import jsonify, Blueprint, request

from app.mapping.materia_mapping import MateriaMapping
from app.services.materia_service import MateriaService 
from .base_resource import BaseResource
from .utils import register_crud_resource

materia_bp = Blueprint('materia', __name__)
materia_service = MateriaService()
materia_schema = MateriaMapping()

class MateriaResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=materia_service,
            schema=materia_schema,
            nombre_entidad="Materia"
        )

register_crud_resource(
    blueprint=materia_bp,
    resource_class=MateriaResource,
    view_name='materia_api',
    url_prefix='materia'
)