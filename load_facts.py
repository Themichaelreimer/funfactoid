import requests
import re
from database import *

def load_dyk():
    """ Loads all the fun facts from https://www.did-you-knows.com into our nifty database """
    db = Database()
    BASE_URL = "https://www.did-you-knows.com/?page="  # Goes up to 50
    
    for i in range(1,51):
        url = BASE_URL+str(i)
        res = requests.get(url)

        if res.status_code == 200:
            html = res.text

            facts = re.findall(r"<li>(.*)<\/li>",html)
            facts = [proc_insert(fact) for fact in facts]
            facts = [fact for fact in facts if fact] #This is not super efficient for the computer, but it is for me :)

            for fact in facts:
                db.insert(fact)
                
        else:
            print(res.status_code)
            print(res.text)


def proc_insert(fact:str):
    """Processes a list item into something fit for our database"""
    if not "<span" in fact:
        return "" # There are navlinks that are also list items,but are not facts

    res = ""

    ignore_chars = False
    for ch in fact:
        if ch == "<":
            ignore_chars = True
        elif ch == ">":
            ignore_chars = False
        elif not ignore_chars:
            res += ch
    return res

    #print("FACT: {}\n".format(res))


load_dyk()

