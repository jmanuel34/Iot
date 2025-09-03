from bs4 import BeautifulSoup

# Ruta al archivo HTML en tu ordenador
archivo_html = '/Users/josemanuelmendez/Documents/Iot/Qwen.html'  # Cambia esto por la ruta real

# Abrir y leer el archivo
with open(archivo_html, 'r', encoding='utf-8') as file:
    contenido = file.read()

# Crear el objeto BeautifulSoup
soup = BeautifulSoup(contenido, 'html.parser')

# Extraer solo el texto
texto = soup.get_text()

# Opcional: limpiar el texto (eliminar espacios extra, saltos de línea, etc.)
texto_limpio = ' '.join(texto.split())

# Mostrar o guardar el texto
print(texto_limpio)
