from urllib.request import urlretrieve
import py7zr
import os

print("Alteracao para deployment")

basepath = "./opt/ml/processing/output"
dlpath = f"{basepath}/rais"

names = [
     #"RAIS_VINC_PUB_CENTRO_OESTE.7z",
     "RAIS_VINC_PUB_NORDESTE.7z",
     "RAIS_VINC_PUB_NORTE.7z",
     "RAIS_VINC_PUB_SUL.7z",
     "RAIS_VINC_PUB_MG_ES_RJ.7z",
     "RAIS_VINC_PUB_SP.7z",
]
urls = [
    #"ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2020/RAIS_VINC_PUB_CENTRO_OESTE.7z",
    "ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2020/RAIS_VINC_PUB_NORDESTE.7z",
    "ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2020/RAIS_VINC_PUB_NORTE.7z",
    "ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2020/RAIS_VINC_PUB_SUL.7z",
    "ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2020/RAIS_VINC_PUB_MG_ES_RJ.7z",
    "ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2020/RAIS_VINC_PUB_SP.7z",
]

def obter_dados(url, name):
    filename = dlpath + '/' + name
    urlretrieve(url, filename=filename)
    #print(filename)
    #archive = py7zr.SevenZipFile(filename)
    #archive.extractall(path=dlpath)
    #archive.close()
    #os.remove(filename)
    return True
    
if __name__ == "__main__":
    os.makedirs(dlpath, exist_ok=True)

    for i in range(len(urls)):
        print(f"Extracting from {urls[i]}")
        res = obter_dados(urls[i], names[i])
        print(res)
    
    print("Done!")
