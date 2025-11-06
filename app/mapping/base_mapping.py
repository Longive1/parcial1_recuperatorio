from marshmallow import Schema, fields, post_load

class BaseMapping(Schema):
    
    hashid = fields.String(dump_only=True)   # Campo comun para todos los schemas

    def __init__(self, *args, **kwargs):
        
        self.model_class = kwargs.pop('model_class', None)
        super().__init__(*args, **kwargs)

    @post_load
    def make_object(self, data, **kwargs):
        if self.model_class:
            return self.model_class(**data)
        return data