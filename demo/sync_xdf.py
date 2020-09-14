# !/usr/bin/env python
import requests

url = 'http://openapi.ifchange.com/api/xdf/staff'
body = {
    "staff_number": "000040",
    "position_id": "10077777",
    "management_experience": "1",
    "department": "1410000000",
    "rank_id": "6",
    "work_city": "北京市",
    "work_address": "北京市海淀区丹棱街3号B座315室",
    "source": "社会招聘—其他",
    "departure_date": "",
    "departure_reasons": "",
    "immediate_leader": "000003",
    "subject": "",
    "depend_subject": "",
    "position_sequence": "IN0101",
    "management_level": "战略决策者",
    "teacher_level": "T1",
    "staff_level": "6",
    "first_basic_manager_date": "",
    "first_middle_manager_date": "",
    "first_high_manager_date": "2003-12-01",
    "work_type": 2,
    "status": 2,
    "entry_date": "2003-12-01",
    "formal_date": "",
    "name": "李旭之",
    "gender": "M",
    "nation": "汉族",
    "political_status": 3,
    "phone": "15000050523",
    "email": "shike@xdf.cn",
    "marital": "1",
    "birth": "1985-10-05",
    "religion": "佛教",
    "first_work_date": "2010-01-01",
    "account_type": 1,
    "native_place": "上海",
    "live_city": "黄浦区",
    "birth_city": "上海市",
    "position_change_record": [
        {
            "change_before_position": "",
            "change_after_position": "10001154",
            "change_before_department": "1031900000",
            "change_after_department": "2200000359",
            "change_before_rank": "6",
            "change_after_rank": "6",
            "change_reason": "薪资更改",
            "change_date": "2011-05-26"
        },
        {
            "change_before_position": "10001154",
            "changeafter_position": "",
            "change_before_department": "2200000359",
            "change_after_department": "2200000359",
            "change_before_rank": "6",
            "change_after_rank": "6",
            "change_reason": "数据更改",
            "change_date": "2014-04-16"
        },
        {
            "change_before_position": "",
            "changeafter_position": "10077777",
            "change_before_department": "2200000359",
            "change_after_department": "1410000000",
            "change_before_rank": "6",
            "change_after_rank": "6",
            "change_reason": "调动",
            "change_date": "2014-05-05"
        }
    ],
    "family_members": [

    ],
    "work": [

    ],
    "education": [
        {
            "school_name": "第二军医大学",
            "discipline_name": "遗传学",
            "start_time": "2007-09-01",
            "end_time": "2010-07-01",
            "degree": 3
        }
    ],
    "part_time_job": [
        {
            "position_id": "10077777",
            "department": "1140700000",
            "position_sequence": "",
            "subject": "",
            "depend_subject": "",
            "status": 2,
            "start_time": "2010-08-26",
            "end_time": "2010-08-31"
        },
        {
            "position_id": "10077777",
            "department": "2200002640",
            "position_sequence": "",
            "subject": "",
            "depend_subject": "",
            "status": 2,
            "start_time": "2014-06-03",
            "end_time": "2017-02-14"
        }
    ],
    "certificate": [

    ]
}

# X-signature 替换为对应的token
headers = {'content-type': "application/json", 'X-signature': ""}


def send_post():
    for n in range(1, 51):
        body["staff_number"] = "0000" + str(n).zfill(2)
        body["name"] = "李旭之" + str(n).zfill(2)
        body["phone"] = "100000000" + str(n).zfill(2)
        body["email"] = str(n).zfill(2) + "@xdf.cn"
        print(body)
        response = requests.post(url, json=body, headers=headers)
        print(response.text)


if __name__ == "__main__":
    send_post()
