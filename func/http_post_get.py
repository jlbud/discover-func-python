# !/usr/bin/env python
import requests
from requests import Response

url = 'http://localhost:8036/activity-report/view'
body = {
    "header": {
        "company_id": 2500884
    },
    "request": {
        "w": "",
        "c": "",
        "m": "",
        "p": {
            "company_id": 8186,
            "activity_id": 130,
            "be_tester_id": 2207908467749273603,
            "reports": ""
        }
    }
}
headers = {'content-type': "application/json"}


def send_post() -> Response:
    response = requests.post(url, json=body, headers=headers)
    return response


if __name__ == "__main__":
    resp = send_post()
    print(resp.status_code)
    print(resp.text)
