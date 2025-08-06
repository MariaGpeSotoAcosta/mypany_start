from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
import re

def busquedaOCA(QUERY_OCA):
  # Empezamos el scraping
  
  #OTRA FORMA ES:
  #req = requests.get(URL_BASE)
  #html_obtenido = req.text
  BUSQUEDA= QUERY_OCA
  pagina = 1
  url_imagenes = []
  URL_BASE = 'https://openclipart.org/search/?p='+ str(pagina) + '&query='+ BUSQUEDA 
  html = urllib.request.urlopen(URL_BASE)
  soup = BeautifulSoup(html, "html.parser")
  smalls = soup.find_all('small')

  for s in smalls:
    pages = s.contents[0]
    pagess=pages.strip()
    print(pagess,len(pagess))
    act_page = re.findall('[0-9]+',str(pagess))
    print(act_page)

  while len(url_imagenes) < 20 and pagina <= int(act_page[1]):
    src_todos = soup.find_all(src=True)
    
    for i, imagen in enumerate(src_todos):

      if imagen['src'].startswith('/image'):
      
        print(imagen['src'])
        x="https://openclipart.org"+ imagen['src']
        print(x)
        url_imagenes.append(x)
    
    pagina = pagina+1
    URL_BASE = 'https://openclipart.org/search/?p='+ str(pagina) + '&query='+ BUSQUEDA 
    print(URL_BASE)
    html = urllib.request.urlopen(URL_BASE)
    soup = BeautifulSoup(html, "html.parser")

  return url_imagenes,act_page


  


  #X es mi link a ingresar en el array

#GUARDAR EN COMPU:
  #r = urllib.request.urlopen(f"https://openclipart.org{imagen['src']}").read()

  # with open(f'imagen_{i}.png', 'wb') as f:
  #  f.write(r)
