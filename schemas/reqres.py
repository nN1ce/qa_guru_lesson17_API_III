from voluptuous import Schema, PREVENT_EXTRA, All, Length, Any

CreateUserSchema = Schema(
    {
        "name": str,
        "job": Any(str, None),
        "id": str,
        "createdAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)


def validate_pantone_value(value):
    part_1, part_2 = value.split('-')
    if len(part_1) == 2 and len(part_2) == 4:
        return True
    else:
        raise ValueError(f'len part_1 "{part_1}" != 2 or len part_2 "{part_2}" != 4 ')


UnknownListDataField = Schema(
    {
        "id": int,
        "name": str,
        "year": int,
        "color": str,
        "pantone_value": All(str, validate_pantone_value)
    },
    required=True,
    extra=PREVENT_EXTRA,
)

UnknownSupport = Schema(
    {
        "url": str,
        "text": str
    },
    required=True,
    extra=PREVENT_EXTRA,
)
UnknownListSchema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": All([UnknownListDataField], Length(min=1)),
        "support": UnknownSupport
    },
    required=True,
    extra=PREVENT_EXTRA,
)
