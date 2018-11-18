import os
import requests as re

def rnc_grabber():
    """
    downloads all rnc available from the fixed links
    :return:path
    """
    rnc_response = re.get("https://www.dgii.gov.do/app/WebApps/Consultas/RNC/DGII_RNC.zip", stream=True, timeout=int(1e6))
    if rnc_response.status_code != 200:
        print("THERE WAS AN ERROR WITH THE REQUEST", rnc_response.status_code)
        return None
    writable = rnc_response.iter_content()
    with open("zipper.zip",'wb') as zipper:
        for chunk in writable:
            zipper.write(chunk)
        else:
            print("DONE WITHOUTH ERRORS")
            return zipper.name
