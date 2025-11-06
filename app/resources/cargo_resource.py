from flask import Blueprint

from app.mapping.cargo_mapping import CargoMapping
from app.services.cargo_service import CargoService
from .base_resource import BaseResource
from .utils import register_crud_resource

cargo_bp = Blueprint('cargo', __name__)
cargo_service = CargoService()
cargo_schema = CargoMapping()

class CargoResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=cargo_service,
            schema=cargo_schema,
            nombre_entidad="Cargo"
        )

register_crud_resource(
    blueprint=cargo_bp,
    resource_class=CargoResource,
    view_name='cargo_api',
    url_prefix='cargo'
)
