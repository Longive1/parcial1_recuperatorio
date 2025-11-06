class BaseService:

    def __init__(self, repository):
        self.repository = repository

    def crear(self, entity):
        return self.repository.crear(entity)

    def buscar_por_id(self, id: int):
        return self.repository.buscar_por_id(id)

    def buscar_todos(self):
        return self.repository.buscar_todos()

    def borrar_por_id(self, id: int) -> bool:
        return self.repository.borrar_por_id(id)

    def actualizar(self, id: int, data: any) -> any:
        existente = self.repository.buscar_por_id(id)
        if not existente:
            return None
        data.id = id
        return self.repository.actualizar(data)