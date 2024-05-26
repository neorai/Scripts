
import http.client
import api

conn = http.client.HTTPSConnection("opendata.aemet.es")

headers = {
    'cache-control': "no-cache"
    }

conn.request("GET", f"/opendata/api/maestro/municipios/?api_key={api.api_key}", headers=headers)

res = conn.getresponse()
data = res.read()



# Abre un archivo en modo binario y guarda los datos sin decodificar
with open('e:\\github\\Scripts\\python\\aemet\\municipios.txt', 'wb') as archivo_salida:
    archivo_salida.write(data)
    print("Los datos se han guardado en 'municipios.txt'")