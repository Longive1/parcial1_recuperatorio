from app.models import Alumno
from .base_repositorios import BaseRepository

class AlumnoRepository(BaseRepository):

    def __init__(self):
        super().__init__(Alumno)
