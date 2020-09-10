import json


def to_json(content):
    return json.dumps(content, ensure_ascii=False)
