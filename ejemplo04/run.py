import requests
import json

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    # pasar los datos a estructuras de Python
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    if d['nombre'][0] in ["A", "B", "L"]:
        lista_datos.append(d)

base_datos = "personas004"
# Configurar el acceso a la base de datos
url = f"http://127.0.0.1:5985/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar datos

for doc in lista_datos:
    response = requests.post(
        url,
        json=doc
    )
    print(f"Insertando {doc['nombre']} | {response.status_code}")




"""
Las pricipales diferencias que podemos ver es que en el ejemplo 3 se enviavan los datos 
utilizamos para hacer la inserción de los datos utilizamos el bulk_docs enviamos todos los documentos
fitrandolos por el HTTPS post a chouchDB  en el ejemplo 4 podemos ver que cada insercion es una por 
una con peticiones post individuales imprimiendo cada estatusde cada insercion.
"""
