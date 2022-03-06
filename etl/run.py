import requests
from io import BytesIO
import py7zr
import os

basepath = "opt/ml/processing/output"
dlpath = f"{basepath}/rais"

urls = [
    "ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2020/RAIS_VINC_PUB_CENTRO_OESTE.7z",
    "ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2020/RAIS_VINC_PUB_NORDESTE.7z",
    "ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2020/RAIS_VINC_PUB_NORTE.7z",
    "ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2020/RAIS_VINC_PUB_SUL.7z",
    "ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2020/RAIS_VINC_PUB_MG_ES_RJ.7z",
    "ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2020/RAIS_VINC_PUB_SP.7z",
]

def obter_dados(url):
    filebytes = BytesIO(requests.get(url, stream=True).content)
    archive = py7zr.SevenZipFile(filebytes)
    archive.extractall(path=basepath)
    archive.close()
    return True
    
if __name__ == "__main__":
    os.makedirs(dlpath, exist_ok=True)

    for url in urls:
        print(f"Extracting from {url}")
        res = obter_dados(url)
        print(res)
    
    print("Done!")
