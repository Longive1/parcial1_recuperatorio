from flask import jsonify, Blueprint, request

from app.mapping.departamento_mapping import DepartamentoMapping
from app.services.departamento_service import DepartamentoService 
from .base_resource import BaseResource
from .utils import register_crud_resource

departamento_bp = Blueprint('departamento', __name__)
departamento_service = DepartamentoService()
departamento_schema = DepartamentoMapping()

class DepartamentoResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=departamento_service,
            schema=departamento_schema,
            nombre_entidad="Departamento"
        )

register_crud_resource(
    blueprint=departamento_bp,
    resource_class=DepartamentoResource,
    view_name='departamento_api',
    url_prefix='departamento'
)
