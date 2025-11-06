def register_crud_resource(blueprint, resource_class, view_name, url_prefix):
    """
    Registra las rutas CRUD estándar para un BaseResource (MethodView).
    
    Esto crea las 5 rutas necesarias:
    - GET /url_prefix
    - POST /url_prefix
    - GET /url_prefix/<id>
    - PUT /url_prefix/<id>
    - DELETE /url_prefix/<id>
    """
    view_func = resource_class.as_view(view_name)
    
    # Rutas sin ID: GET (todos) y POST (crear)
    blueprint.add_url_rule(
        f"/{url_prefix}",
        view_func=view_func,
        methods=['GET', 'POST']
    )
    
    # Rutas con ID: GET (uno), PUT (actualizar) y DELETE (borrar)
    blueprint.add_url_rule(
        f"/{url_prefix}/<hashid:id>",
        view_func=view_func,
        methods=['GET', 'PUT', 'DELETE']
    )