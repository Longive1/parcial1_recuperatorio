import datetime
from io import BytesIO
from app.models import Alumno
from app.repositories import AlumnoRepository, TipoDocumentoRepository, EspecialidadRepository
from app.services.documentos_office_service import obtener_tipo_documento
from .base_service import BaseService

class AlumnoService(BaseService):

    def __init__(self):
        super().__init__(AlumnoRepository())
    
    def actualizar(self, id: int, data: Alumno) -> Alumno:
        alumno_existente = self.repository.buscar_por_id(id)
        if not alumno_existente:
            return None
        alumno_existente.nombre = data.nombre
        alumno_existente.apellido = data.apellido
        alumno_existente.nrodocumento = data.nrodocumento
        alumno_existente.tipo_documento_id = data.tipo_documento_id
        alumno_existente.fecha_nacimiento = data.fecha_nacimiento
        alumno_existente.sexo = data.sexo
        alumno_existente.nro_legajo = data.nro_legajo
        alumno_existente.fecha_ingreso = data.fecha_ingreso
        alumno_existente.especialidad_id = data.especialidad_id
        return self.repository.actualizar(alumno_existente)
        
    def generar_certificado_alumno_regular(self, id: int, tipo: str) -> BytesIO:

        alumno = self.alumno_repository.buscar_por_id(id)
        if not alumno:
            return None
        
        context = self.__obteneralumno(alumno)
        documento = obtener_tipo_documento(tipo)
        if not documento:
            return None
        plantillas = {
            'pdf': 'certificado_pdf',       # Usa la plantilla HTML
            'odt': 'certificado_plantilla',  # Usa la plantilla ODT
            'docx': 'certificado_plantilla' # Usa la plantilla DOCX
        }
        plantilla_seleccionada = plantillas.get(tipo)
        if not plantilla_seleccionada:
            return None
        return documento.generar(
            carpeta='template/certificado', 
            plantilla=plantilla_seleccionada, 
            context=context
        )
    
    def __obtener_fechaactual(self):
        fecha_actual = datetime.datetime.now()
        fecha_str = fecha_actual.strftime('%d de %M de %Y')
        return fecha_str
    
    def __obteneralumno(self, alumno: Alumno) -> dict:
        especialidad = alumno.especialidad
        facultad = especialidad.facultad
        universidad = facultad.universidad
        return{
            "alumno": alumno,
            "especialidad": especialidad,
            "facultad": facultad,
            "universidad": universidad,
            "fecha":self.__obtener_fechaactual()
            }
