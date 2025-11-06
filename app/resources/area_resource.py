from flask import Blueprint

from app.mapping.area_mapping import AreaMapping
from app.services.area_service import AreaService
from .base_resource import BaseResource
from .utils import register_crud_resource

area_bp = Blueprint('area', __name__)
area_service = AreaService()
area_schema = AreaMapping()

class AreaResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=area_service,
            schema=area_schema,
            nombre_entidad="Area"
        )

register_crud_resource(
    blueprint=area_bp,
    resource_class=AreaResource,
    view_name='area_api',
    url_prefix='area'
)
