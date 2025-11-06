from flask import jsonify, Blueprint, request
from app.mapping.universidad_mapping import UniversidadMapping
from app.services.universidad_service import UniversidadService
from .base_resource import BaseResource
from .utils import register_crud_resource

universidad_bp = Blueprint('universidad', __name__)
universidad_service = UniversidadService()
universidad_schema = UniversidadMapping()

class UniversidadResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=universidad_service,
            schema=universidad_schema,
            nombre_entidad="Universidad"
        )

register_crud_resource(
    blueprint=universidad_bp,
    resource_class=UniversidadResource,
    view_name='universidad_api', 
    url_prefix='universidad'     
)

