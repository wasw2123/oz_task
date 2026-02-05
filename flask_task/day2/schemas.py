from marshmallow import Schema, fields, post_dump

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)