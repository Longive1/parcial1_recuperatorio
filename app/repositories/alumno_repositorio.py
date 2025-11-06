from app.models import Alumno
from .base_repositorios import BaseRepository
from app import db

class AlumnoRepository(BaseRepository):

    def __init__(self):
        super().__init__(Alumno)

    def buscar_por_especialidad(self, especialidad_id: int):
        return db.session.query(Alumno).filter_by(especialidad_id=especialidad_id).all()
