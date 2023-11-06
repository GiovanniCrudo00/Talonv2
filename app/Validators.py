from app.CustomExceptions import *
import re

#COSTANTS
DOMAIN_PATTERN=r'^((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$'
IP_PATTERN=r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
def ValidateChoice(chc:int):
    if(0 <= chc <=3):
        return chc
    else:
        raise ValueError() # Raise an exception on error

def ValidateTargetDomain(tgt:str):
    if(tgt is None):
        raise DomainNotValid
    if(len(tgt)>100): # Check for the len of the string given
        raise DomainNotValid
    if(not (re.match(DOMAIN_PATTERN,tgt))): # Verify regex for a valid domain
        raise DomainNotValid
    else:
        return tgt

def ValidateTargetIP(tgt:str):
    if(tgt is None):
        raise IPNotValid
    if(len(tgt)>30) or (len(tgt)<6):
        raise IPNotValid
    if(not (re.match(IP_PATTERN,tgt))):
        raise IPNotValid
    else:
        return tgt