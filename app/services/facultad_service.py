from app.models import Facultad
from app.repositories import FacultadRepository, AutoridadRepository
from .base_service import BaseService

class FacultadService(BaseService):
    
    def __init__(self):
        super().__init__(FacultadRepository())
        
        self.autoridad_repository = AutoridadRepository()
        self.facultad_repository = self.repository

    def actualizar(self, id: int, data: Facultad) -> Facultad:
        facultad_existente = self.repository.buscar_por_id(id)
        if not facultad_existente:
            return None
        facultad_existente.nombre = data.nombre
        facultad_existente.abreviatura = data.abreviatura
        facultad_existente.directorio = data.directorio
        facultad_existente.sigla = data.sigla
        facultad_existente.codigopostal = data.codigopostal
        facultad_existente.ciudad = data.ciudad
        facultad_existente.domicilio = data.domicilio
        facultad_existente.telefono = data.telefono
        facultad_existente.contacto = data.contacto
        facultad_existente.email = data.email
        facultad_existente.universidad_id = data.universidad_id
        return self.repository.actualizar(facultad_existente)

    def asociar_autoridad(self, facultad_id: int, autoridad_id: int):
        facultad = self.repository.buscar_por_id(facultad_id)
        autoridad = self.autoridad_repository.buscar_por_id(autoridad_id)
        if not facultad or not autoridad:
            raise ValueError("Facultad o autoridad no encontrada")
        FacultadRepository.asociar_autoridad(facultad, autoridad)

    def desasociar_autoridad(self, facultad_id: int, autoridad_id: int):
        facultad = self.repository.buscar_por_id(facultad_id)
        autoridad = self.autoridad_repository.buscar_por_id(autoridad_id)
        if not facultad or not autoridad:
            raise ValueError("Facultad o autoridad no encontrada")
        FacultadRepository.desasociar_autoridad(facultad, autoridad)
