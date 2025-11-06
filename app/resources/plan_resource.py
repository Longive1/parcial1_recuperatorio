from flask import jsonify, Blueprint, request

from app.mapping.plan_mapping import PlanMapping
from app.services.plan_service import PlanService

from .base_resource import BaseResource
from .utils import register_crud_resource

plan_bp = Blueprint('plan', __name__)
plan_service = PlanService()
plan_schema = PlanMapping()

class PlanResource(BaseResource):
    def __init__(self):
        super().__init__(
            service=plan_service,
            schema=plan_schema,
            nombre_entidad="Plan"
        )

register_crud_resource(
    blueprint=plan_bp,
    resource_class=PlanResource,
    view_name='plan_api',
    url_prefix='plan'
)