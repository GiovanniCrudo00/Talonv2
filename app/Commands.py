import dns.resolver
import whois
from app.CustomExceptions import *
import datetime
import requests
import json

def DNS_lookup(target_domain):
    results = {}
    dns_types = ["A","AAAA","ALIAS","CNAME","MX","NS","PTR","SOA","SRV","TXT"]
    for record in dns_types:
        try:
            result = dns.resolver.query(target_domain,record)
            for i in result:
                r=str(i)
                results[record] = r
        except Exception:
            pass
    return results

def whois_lookup(target_domain):
    results = {}
    try:
        w=results = whois.whois(target_domain)
        for i in w:
            if w[i] is None:
                results[i]=str("N/A")
            # Conversion from datetime.datetime object to string
            if i == "creation_date" or i == "updated_date" or i == "expiration_date":
                data_datetime = w[i]
                data_stri = data_datetime.strftime("%Y-%m-%d")
                results[i]=str(data_stri) # Cast to string
            else:
                results[i]=str(w[i])
    except Exception:
        print("Something went wrong...")
    
    return results
    
def ip_geolocation(target):
    results={}
    try:
        request_url = 'https://geolocation-db.com/jsonp/' + target
        response = requests.get(request_url)
        result = response.content.decode()
        result = result.split("(")[1].strip(")")
        res  = json.loads(result)
        for i in res:
            results[i]=str(res[i])
    except Exception:
        print("Something went wrong...")
    return results
