from flask import Blueprint

from app.mapping.categoriacargo_mapping import CategoriaCargoMapping
from app.services.categoriacargo_service import CategoriaCargoService
from .base_resource import BaseResource
from .utils import register_crud_resource

categoriacargo_bp = Blueprint('categoriacargo', __name__)
categoriacargo_service = CategoriaCargoService()
categoriacargo_schema = CategoriaCargoMapping()

class CategoriaCargoResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=categoriacargo_service,
            schema=categoriacargo_schema,
            nombre_entidad="Categoria Cargo"
        )

register_crud_resource(
    blueprint=categoriacargo_bp,
    resource_class=CategoriaCargoResource,
    view_name='categoriacargo_api',
    url_prefix='categoriacargo'
)
