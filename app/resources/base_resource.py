from flask.views import MethodView
from flask import request, jsonify

class BaseResource(MethodView):

    def __init__(self, service, schema, nombre_entidad):
        self.service = service
        self.schema = schema
        self.nombre_entidad = nombre_entidad # Para mensajes de respuesta (ej. "Universidad")

    def get(self, id=None):
        if id is None:
            # GET /entidad (buscar todos)
            todos = self.service.buscar_todos()
            return self.schema.dump(todos, many=True), 200
        else:
            # GET /entidad/<id> (buscar por id)
            entidad = self.service.buscar_por_id(id)
            if not entidad:
                return jsonify({"message": f"{self.nombre_entidad} no encontrada"}), 404
            return self.schema.dump(entidad), 200

    def post(self):
        try:
            data = self.schema.load(request.get_json())
            entidad_creada = self.service.crear(data)
            return jsonify({"message": f"{self.nombre_entidad} creada exitosamente"}), 201
        except Exception as e:
            return jsonify({"message": "Error en la carga de datos", "errors": str(e)}), 400

    def put(self, id):
        try:
            data = self.schema.load(request.get_json())
            entidad_actualizada = self.service.actualizar(id, data)
            
            if not entidad_actualizada:
                return jsonify({"message": f"{self.nombre_entidad} no encontrada"}), 404
            
            return jsonify({"message": f"{self.nombre_entidad} actualizada exitosamente"}), 200
        except Exception as e:
            return jsonify({"message": "Error en la carga de datos", "errors": str(e)}), 400

    def delete(self, id):
        if not self.service.borrar_por_id(id):
            return jsonify({"message": f"{self.nombre_entidad} no encontrada"}), 404
        
        return jsonify({"message": f"{self.nombre_entidad} borrada exitosamente"}), 200