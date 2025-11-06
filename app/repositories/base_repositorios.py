from app import db

class BaseRepository:   #Base generica para todos los repositorios
    def __init__(self,model):
        self.model=model

    def crear(self,entity):
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def buscar_por_id(self, id: int):
        return db.session.query(self.model).filter_by(id=id).first()
    
    def buscar_todos(self):
        return db.session.query(self.model).all()
    
    def actualizar(self,entity)->any:
        db.session.merge(entity)
        db.session.commit()
        return entity
    
    def borrar_por_id(self,id:int)->bool:
        entity=self.buscar_por_id(id)
        if not entity:
            return False
        db.session.delete(entity)
        db.session.commit()
        return True
