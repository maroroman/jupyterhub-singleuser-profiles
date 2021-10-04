from multiprocessing import Pool
import requests
import time
import datetime

def test_calls(count):
    JH_URL = 'https://jupyterhub-redhat-ods-applications.apps.mroman.dev.datahub.redhat.com/services/jsp-api/api/'
    api_calls = ['ui/config','sizes?pure_json=true', 'images', 'user/configmap']

    for j in range(0,count):
        for i in range(len(api_calls)):
            output = requests.get('%s%s' % JH_URL, api_calls[i-1])
            if output.status_code != 200:
                warning = 'WARN'
            if output.status_code < 400 and output.status_code > 299:
                warning = 'REDIRECT'

            with open('output.txt', 'w') as f:
                f.writelines('%s: IN: %s  OUT: %s   %s' % datetime.datetime.now(), api_calls[i-1], output, warning)
            
            time.sleep(0.1)
        time.sleep(5)
    

if __name__ == '__main__':
    with Pool(20) as p:
        p.map(test_calls)
