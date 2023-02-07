# coding: utf-8

from workflow import Workflow3, web
import time
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def generate_wf_results(data=''):
    wf = Workflow3()
    results = []
    if isinstance(data, dict):
        for k in data:
            results.append({
                'title': str(k) + ': ' + str(data[k]),
                'subtitle': '',
                "valid": True,
                'arg': str(data[k])
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
    input = "{query}"
    if re.match(r'^(\d{4})\-(\d{1,2})\-(\d{1,2})\s(\d{1,2})\:(\d{1,2})\:(\d{1,2})$', input):
        seconds = int(time.mktime(time.strptime(input, '%Y-%m-%d %H:%M:%S')))
        timestamp = int(time.mktime(time.strptime(input, '%Y-%m-%d %H:%M:%S')) * 1000)
        generate_wf_results({'Timestamp': timestamp, 'Seconds': seconds})
    elif re.match(r'^(\d{4})\-(\d{1,2})\-(\d{1,2})$', input):
        seconds = int(time.mktime(time.strptime(input, '%Y-%m-%d')))
        timestamp = int(time.mktime(time.strptime(input, '%Y-%m-%d')) * 1000)
        generate_wf_results({'Timestamp': timestamp, 'Seconds': seconds})
    elif re.match(r'^(\d{13})$', input):
        datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(input) / 1000))
        date = time.strftime('%Y-%m-%d', time.localtime(float(input) / 1000))
        generate_wf_results({'DateTime': datetime, 'Date': date})
    elif re.match(r'^(\d{10})$', input):
        datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(input)))
        date = time.strftime('%Y-%m-%d', time.localtime(float(input)))
        generate_wf_results({'DateTime': datetime, 'Date': date})
    else:
        generate_wf_results('invalid input...')
