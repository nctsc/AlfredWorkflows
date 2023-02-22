# coding: utf-8

from workflow import Workflow3, web
import time
import re
import sys
import hashlib
import uuid
reload(sys)
sys.setdefaultencoding('utf8')


def generate_wf_results(data=''):
    wf = Workflow3()
    results = []
    if isinstance(data, list):
        for k in data:
            results.append({
                'title': str(k),
                'subtitle': '',
                "valid": True,
                'arg': str(k)
            })
    else:
        results.append({
            'title': data,
            'subtitle': '',
            "valid": False,
            'arg': ''
        })
    for r in results:
        wf.add_item(**r)
    wf.send_feedback()


if __name__ == "__main__":
    lower_uuid = str(uuid.uuid4())
    upper_uuid = lower_uuid.upper()
    generate_wf_results([lower_uuid, upper_uuid])
