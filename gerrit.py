import requests
import json
import sys
from datetime import datetime

def MergedPatches(username, before, after):
    link = "https://gerrit.wikimedia.org/r/changes/?q=owner:"
    try:
        url = link+username+'+before:'+before+'+after:'+after+'+status:merged'
        response = requests.get(url)
        response_text = response.text
        json_response = response_text.replace(")]}'", '', 1)
        merged_patches = json.loads(json_response)
        return merged_patches
    except:
        print('Make sure you entered a valid username')
        sys.exit(-1)

if __name__ == "__main__":
    username = input('Enter Gerrit username: ')
    after_date = input('Enter the lower limit date in DD/MM/YYYY format: ')
    try:
        day, month, year = map(int, after_date.split('/'))
        after = datetime(year,month,day)
        after = after.strftime('%Y-%m-%d')
    except:
        print('Invalid Date')
        sys.exit(-1)

    before_date = input('Enter the upper limit date in DD/MM/YYYY format: ')   
    try:
        day, month, year = map(int, before_date.split('/'))
        before = datetime(year,month,day)
        before = before.strftime('%Y-%m-%d')
    except:
        print('Invalid Date')
        sys.exit(-1)

    print("-----------------------------------------------------------------")
    print('Number of merged patches between {} and {} are {}'.format(
        after, before, len(MergedPatches(username, before, after))
    ))    
