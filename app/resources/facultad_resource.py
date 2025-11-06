from flask import jsonify, Blueprint, request

from app.mapping.facultad_mapping import FacultadMapping
from app.services.facultad_service import FacultadService 
from .base_resource import BaseResource
from .utils import register_crud_resource

facultad_bp = Blueprint('facultad', __name__)
facultad_service = FacultadService()
facultad_schema = FacultadMapping()

class FacultadResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=facultad_service,
            schema=facultad_schema,
            nombre_entidad="Facultad"
        )

register_crud_resource(
    blueprint=facultad_bp,
    resource_class=FacultadResource,
    view_name='facultad_api',
    url_prefix='facultad'
)