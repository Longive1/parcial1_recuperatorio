from flask import Blueprint

from app.mapping.autoridad_mapping import AutoridadMapping
from app.services.autoridad_service import AutoridadService
from .base_resource import BaseResource
from .utils import register_crud_resource

autoridad_bp = Blueprint('autoridad', __name__)
autoridad_service = AutoridadService()
autoridad_schema = AutoridadMapping()

class AutoridadResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=autoridad_service,
            schema=autoridad_schema,
            nombre_entidad="Autoridad"
        )

register_crud_resource(
    blueprint=autoridad_bp,
    resource_class=AutoridadResource,
    view_name='autoridad_api',
    url_prefix='autoridad'
)