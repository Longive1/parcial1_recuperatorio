from app.models import Plan
from app.repositories import PlanRepository
from .base_service import BaseService

class PlanService(BaseService):

    def __init__(self):
        repository = PlanRepository()

        super().__init__(repository)
