import json

with open('siphos/summary3.json', 'r') as handle:
    summary = json.load(handle)
    uids = summary['result']['uids']
    for uid in uids:
        print summary['result'][uid]['organism']
