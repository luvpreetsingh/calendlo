# third party level imports
from marshmallow import (
    Schema,
    fields,
    validates_schema,
    ValidationError,
)


class SlotSchema(Schema):
    """
    This is base schema to validate for dict consisting of
    start_time and end_time for a slot.
    """
    start_time = fields.Time()
    end_time = fields.Time()

    @validates_schema
    def validate_time(self, data, **kwargs):
        if data["end_time"] <= data["start_time"]:
            raise ValidationError("end_time must be greater than start_time")


class TimingSchema(Schema):
    """
    This schema will validate list of timings for multiple slots
    """
    timings = fields.List(fields.Nested(lambda: SlotSchema()))
