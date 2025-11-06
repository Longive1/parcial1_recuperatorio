from flask import jsonify, Blueprint, request

from app.mapping.grupo_mapping import GrupoMapping
from app.services.grupo_service import GrupoService 
from .base_resource import BaseResource
from .utils import register_crud_resource

grupo_bp = Blueprint('grupo', __name__)
grupo_service = GrupoService()
grupo_schema = GrupoMapping()

class GrupoResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=grupo_service,
            schema=grupo_schema,
            nombre_entidad="Grupo"
        )

register_crud_resource(
    blueprint=grupo_bp,
    resource_class=GrupoResource,
    view_name='grupo_api',
    url_prefix='grupo'
)
