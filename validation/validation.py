def validate_data(data, schema):
    for key, expected_type in data.items():
        if key in schema:
            if not isinstance(expected_type, schema[key]):
                raise ValueError(f"Invalid type for {key}. Expected {schema[key]}, got {type(data[key])}.")
        else:
            raise ValueError(f"Invalid {key}. Not existed {key} in schema")
