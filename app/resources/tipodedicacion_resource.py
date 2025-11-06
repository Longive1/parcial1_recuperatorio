from flask import jsonify, Blueprint, request

from app.mapping.tipodedicacion_mapping import TipoDedicacionMapping
from app.services.tipodedicacion_service import TipoDedicacionService 
from .base_resource import BaseResource
from .utils import register_crud_resource

tipodedicacion_bp = Blueprint('tipodedicacion', __name__)
tipodedicacion_service = TipoDedicacionService()
tipodedicacion_schema = TipoDedicacionMapping()

class TipoDedicacionResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=tipodedicacion_service,
            schema=tipodedicacion_schema,
            nombre_entidad="Tipo Dedicación"
        )

register_crud_resource(
    blueprint=tipodedicacion_bp,
    resource_class=TipoDedicacionResource,
    view_name='tipodedicacion_api',
    url_prefix='tipodedicacion'
)