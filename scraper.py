import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# URL de la página de Wikipedia
url = 'https://es.wikipedia.org/wiki/Anexo:Estad%C3%ADsticas_de_la_Copa_Mundial_de_F%C3%BAtbol'

# Hacer la solicitud a la página
response = requests.get(url)
if response.status_code == 200:
    # Parsear el contenido HTML con BeautifulSoup
    soup = bs(response.content, 'html.parser')

    # Buscar todas las tablas en la página
    tables = soup.find_all('table', {'class': 'wikitable'})

    # Si se encuentra al menos una tabla
    if tables:
        # Procesar la primera tabla como ejemplo
        table = tables[0]

        # Extraer los datos de la tabla
        rows = []
        for row in table.find_all('tr'):  # Iterar por cada fila
            cells = [cell.text.strip() for cell in row.find_all(['th', 'td'])]
            if cells:
                rows.append(cells)

        # Convertir a DataFrame
        df = pd.DataFrame(rows[1:], columns=rows[0])  # La primera fila es el encabezado
        print(df)

        # Guardar en un archivo CSV
        df.to_csv('statsWorldCup.csv', index=False)
        print("Datos guardados en 'statsWorldCup.csv'")
    else:
        print("No se encontraron tablas en la página.")
else:
    print(f"Error al acceder a la página. Código de estado: {response.status_code}")
