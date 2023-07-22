import socket
from urllib.parse import urlparse
def get_website_ip_address(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        ip_address = socket.gethostbyname(hostname)
        print("Web sitesinin IP adresi:", ip_address)
    except socket.gaierror as e:
        print("IP adresi alınamadı:", str(e))
website_url = input("Web sitesinin tam URL'sini girin: ")
get_website_ip_address(website_url)