from marshmallow import Schema, fields


class VolcanoUpdateSchema(Schema):
    name = fields.Str()
    height = fields.Str()
    last_eruption = fields.Str()
    state = fields.Str()


class VolcanoSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    height = fields.Str(required=True)
    last_eruption = fields.Str(required=True)
    state = fields.Str(required=True)
