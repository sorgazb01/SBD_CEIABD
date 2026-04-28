# ==========================================================
# SELENIUM CON BOOKS TO SCRAPE
# ==========================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import os


# def iniciar_navegador():
#     options = Options()

#     # Ejecutar Chrome sin abrir ventana
#     options.add_argument("--headless=new")

#     # Tamaño de ventana virtual para que la web cargue en modo escritorio
#     options.add_argument("--window-size=1920,1080")

#     # En Windows puede ayudar cuando usamos headless
#     options.add_argument("--disable-gpu")

#     # Reduce ruido en consola
#     options.add_argument("--log-level=3")

#     # Indicamos que el chromedriver.exe está en la misma carpeta que el script
#     servicio = Service(executable_path="chromedriver.exe")

#     # Crear y devolver el navegador con esas opciones
#     driver = webdriver.Chrome(service=servicio, options=options)
#     return driver

# ----------------------------------------------------------
# 1. CREAR CARPETA PARA GUARDAR LAS CAPTURAS
# ----------------------------------------------------------

# carpeta_capturas = "capturas_libros"

# if not os.path.exists(carpeta_capturas):
#     os.makedirs(carpeta_capturas)

# ----------------------------------------------------------
# 2. CREAR EL NAVEGADOR
# ----------------------------------------------------------

# driver = iniciar_navegador()

# ----------------------------------------------------------
# 3. ABRIR LA WEB
# ----------------------------------------------------------

# driver.get("https://books.toscrape.com/")

# # # Captura inicial
# driver.save_screenshot(f"{carpeta_capturas}/01_inicio.png")

# print("TÍTULO DE LA PÁGINA:")
# print(driver.title)
# print("-------------------------------------")

# ----------------------------------------------------------
# 4. COMPROBAR EL ENCABEZADO PRINCIPAL
# ----------------------------------------------------------

# titulo_principal = driver.find_element(By.TAG_NAME, "h1")

# print("ENCABEZADO PRINCIPAL:")
# print(titulo_principal.text)
# print("-------------------------------------")

# ----------------------------------------------------------
# 5. SACAR LOS LIBROS DE LA PRIMERA PÁGINA
# ----------------------------------------------------------

# libros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

# print("NÚMERO DE LIBROS EN LA PRIMERA PÁGINA:")
# print(len(libros))
# print("-------------------------------------")

# print("DATOS DE LOS LIBROS DE LA PRIMERA PÁGINA:")

# for libro in libros:
#     titulo = libro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
#     precio = libro.find_element(By.CLASS_NAME, "price_color").text
#     disponibilidad = libro.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()

#     print("Título:", titulo)
#     print("Precio:", precio)
#     print("Disponibilidad:", disponibilidad)
#     print("-----------------------")

# ----------------------------------------------------------
# 6. ENTRAR EN EL PRIMER LIBRO
# ----------------------------------------------------------

# primer_libro = driver.find_element(By.CSS_SELECTOR, "article.product_pod h3 a")
# titulo_antes = primer_libro.get_attribute("title")

# print("VAMOS A ENTRAR EN ESTE LIBRO:")
# print(titulo_antes)
# print("-------------------------------------")

# primer_libro.click()

# # # Captura dentro del detalle del libro
# driver.save_screenshot(f"{carpeta_capturas}/02_detalle_libro.png")

# titulo_detalle = driver.find_element(By.TAG_NAME, "h1").text
# precio_detalle = driver.find_element(By.CLASS_NAME, "price_color").text
# disponibilidad_detalle = driver.find_element(By.CLASS_NAME, "instock").text.strip()

# print("DATOS DEL LIBRO EN SU FICHA:")
# print("Título:", titulo_detalle)
# print("Precio:", precio_detalle)
# print("Disponibilidad:", disponibilidad_detalle)
# print("-------------------------------------")

# ----------------------------------------------------------
# 7. VOLVER ATRÁS
# ----------------------------------------------------------

# driver.back()

# # # Captura tras volver a la portada
# driver.save_screenshot(f"{carpeta_capturas}/03_vuelta_portada.png")

# print("HEMOS VUELTO A LA PÁGINA PRINCIPAL")
# print(driver.title)
# print("-------------------------------------")

# ----------------------------------------------------------
# 8. SACAR TODAS LAS CATEGORÍAS
# ----------------------------------------------------------

# categorias = driver.find_elements(By.CSS_SELECTOR, "div.side_categories ul li ul li a")

# print("CATEGORÍAS DISPONIBLES:")

# for categoria in categorias:
#     print(categoria.text.strip())

# print("-------------------------------------")

# ----------------------------------------------------------
# 9. ENTRAR EN LA CATEGORÍA TRAVEL
# ----------------------------------------------------------

# for categoria in categorias:
#     if categoria.text.strip() == "Travel":
#         categoria.click()
#         break

# # # Captura dentro de la categoría Travel
# driver.save_screenshot(f"{carpeta_capturas}/04_categoria_travel.png")

# titulo_categoria = driver.find_element(By.TAG_NAME, "h1").text

# print("HEMOS ENTRADO EN LA CATEGORÍA:")
# print(titulo_categoria)
# print("-------------------------------------")

# print("LIBROS DE LA CATEGORÍA TRAVEL:")

# libros_travel = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

# for libro in libros_travel:
#     titulo = libro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
#     precio = libro.find_element(By.CLASS_NAME, "price_color").text
#     print("Título:", titulo)
#     print("Precio:", precio)
#     print("-----------------------")

# ----------------------------------------------------------
# 10. VOLVER A LA PORTADA
# ----------------------------------------------------------

# driver.back()

# # Captura al volver a la portada
# driver.save_screenshot(f"{carpeta_capturas}/05_portada_otra_vez.png")

# ----------------------------------------------------------
# 11. PASAR A LA SIGUIENTE PÁGINA
# ----------------------------------------------------------

# siguiente = driver.find_element(By.CSS_SELECTOR, "li.next a")
# siguiente.click()

# # Captura de la segunda página
# driver.save_screenshot(f"{carpeta_capturas}/06_segunda_pagina.png")

# print("HEMOS PASADO A LA SIGUIENTE PÁGINA")
# print("URL actual:", driver.current_url)
# print("-------------------------------------")

# print("LIBROS DE LA SEGUNDA PÁGINA:")

# libros_pagina_2 = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

# for libro in libros_pagina_2:
#     titulo = libro.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
#     precio = libro.find_element(By.CLASS_NAME, "price_color").text
    
#     print("Título:", titulo)
#     print("Precio:", precio)
#     print("-----------------------")

# ----------------------------------------------------------
# 12. CERRAR NAVEGADOR
# ----------------------------------------------------------

# driver.quit()

# print("NAVEGADOR CERRADO")
# print("LAS CAPTURAS SE HAN GUARDADO EN LA CARPETA:", carpeta_capturas)


# ==========================================================
# EJERCICIOS DE SELENIUM SOBRE BOOKS TO SCRAPE
# ==========================================================
#
# WEB DE TRABAJO:
# https://books.toscrape.com/
#
# IDEAS GENERALES:
# - Usa como base la práctica guiada que ya hemos visto.
# - Intenta reutilizar la función iniciar_navegador().
# - Si lo necesitas, guarda capturas para verificar en qué parte de la web estás.
#
# Estos ejercicios no son solo para “sacar datos”, sino para aprender a:
# - recorrer elementos
# - tomar decisiones
# - navegar por la web
# - comparar resultados
# - guardar información
# ==========================================================

def iniciar_navegador():
    options = Options()

    # Ejecutar Chrome sin abrir ventana
    options.add_argument("--headless=new")

    # Tamaño de ventana virtual para que la web cargue en modo escritorio
    options.add_argument("--window-size=1920,1080")

    # En Windows puede ayudar cuando usamos headless
    options.add_argument("--disable-gpu")

    # Reduce ruido en consola
    options.add_argument("--log-level=3")

    # Indicamos que el chromedriver.exe está en la misma carpeta que el script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    servicio = Service(executable_path=os.path.join(script_dir, "chromedriver.exe"))

    # Crear y devolver el navegador con esas opciones
    driver = webdriver.Chrome(service=servicio, options=options)
    return driver

carpeta_capturas = "capturas_libros_tarea"

if not os.path.exists(carpeta_capturas):
    os.makedirs(carpeta_capturas)
    
driver = iniciar_navegador()

driver.get("https://books.toscrape.com/")

# ==========================================================
# EJERCICIO 1
# MOSTRAR TODAS LAS CATEGORÍAS DISPONIBLES
# ==========================================================
#
# Mostrar todas las categorías que aparecen en la barra lateral.
# ==========================================================

categoriasLibros = driver.find_elements(By.CSS_SELECTOR, 'div.side_categories ul li ul li a')

print('-- EJERCICIO 1 --')
print('Categorías: ')
print('---------------------------')
for categoria in categoriasLibros:
    print(categoria.text.strip())
print('---------------------------')

# ==========================================================
# EJERCICIO 2
# COMPROBAR QUE EL TÍTULO COINCIDE AL ENTRAR EN UN LIBRO
# ==========================================================
#
# Entrar en un libro de la portada y comprobar si el título visible en la
# portada coincide con el título de la ficha del libro.
# ==========================================================

print('-- EJERCICIO 2 --')

# Obtenemos el titulo del primer libro de la portada
tituloPortada = driver.find_element(By.CSS_SELECTOR, 'article.product_pod h3 a').get_attribute('title')
# Accedemos a la ficha del libro
driver.find_element(By.CSS_SELECTOR, 'article.product_pod h3 a').click()
# Obtenemos el título de la página del libro
tituloFicha = driver.find_element(By.TAG_NAME, 'h1').text
# Mostramos los dos titulos
print('Título en la portada: ', tituloPortada)
print('Título en la ficha: ', tituloFicha)
print(f'Coinciden? {tituloPortada == tituloFicha}')

# Volvemos a la pagina de inicio
driver.back()

print('-----------------------------------------------------')

# ==========================================================
# EJERCICIO 3
# LIBRO MÁS CARO DE LA PRIMERA PÁGINA
# ==========================================================
#
# Recorre todos los libros de la primera página y muestra:
# - el título del libro más caro
# - su precio
# ==========================================================

print('-- EJERCICIO 3 --')

librosPortada = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
tituloLibroMasCaro = ''
precioLibroMasCaro = 0
for libro in librosPortada:
    # Obtenemos el titulo y el precio de cada libro
    tituloLibro = libro.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
    precioLibro = libro.find_element(By.CSS_SELECTOR, 'p.price_color').text
    # Quitamos la moneda y lo convertimos a float para poder comparar
    precioLibro = precioLibro.replace('£', '')
    precioLibro = float(precioLibro)
    # Comparamos los datos del libro actual del bucle y lo comparamos con el libro mas caro
    if precioLibro > precioLibroMasCaro:
        tituloLibroMasCaro = tituloLibro
        precioLibroMasCaro = precioLibro
print(f'El titulo del libro mas caro es: {tituloLibroMasCaro}')
print(f'El precio del libro mas caro es:  £{precioLibroMasCaro}')

print('-----------------------------------------------------')

# ==========================================================
# EJERCICIO 4
# CONTAR CUÁNTOS LIBROS CUESTAN MÁS DE 50 LIBRAS
# ==========================================================
#
# Es recomendable crear una lista para el ejercicio 5.
#
# Mostrar:
# - cuántos libros de la primera página cuestan más de 50 libras
# - qué títulos son
# ==========================================================

print('-- EJERCICIO 4 --')

librosMas50Libras = []
for libro in librosPortada:
    # Obtenemos el titulo y el precio de cada libro
    tituloLibro = libro.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
    precioLibro = libro.find_element(By.CSS_SELECTOR, 'p.price_color').text
    # Quitamos la moneda y lo convertimos a float para poder comparar
    precioLibro = precioLibro.replace('£', '')
    precioLibro = float(precioLibro)
    if precioLibro > 50:
        librosMas50Libras.append(libro)

print(f'Hay {len(librosMas50Libras)} libros que cuestan mas de 50 libras')
print('Los libros son: ')
for libro in librosMas50Libras:
    tituloLibro = libro.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
    print(tituloLibro)

print('-----------------------------------------------------')

# ==========================================================
# EJERCICIO 5
# ENTRAR EN EL PRIMER LIBRO QUE CUESTA MÁS DE 50 LIBRAS Y SACAR DATOS
# ==========================================================
#
# Obtener del primer libro que cuesta más de 50 libras:
# - título
# - precio
# - disponibilidad
# - categoría
# ==========================================================

print('-- EJERCICIO 5 --')

# Obtenemos el primer elemento de la lista de libros de mas de 50 libras
primerLibroMas50Libras = librosMas50Libras[0]
# Obtenemos el titulo
tituloLibroMas50Libras = primerLibroMas50Libras.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
# Obtenemos el precio
precioLibroMas50Libras = primerLibroMas50Libras.find_element(By.CSS_SELECTOR, 'p.price_color').text
# Obtenemos la disponibilidad
disponibilidadLibroMas50Libras = primerLibroMas50Libras.find_element(By.CSS_SELECTOR, 'p.instock.availability').text
# Accedemos a la pagina del libro (el selector es relativo al propio article, por eso usamos 'h3 a')
primerLibroMas50Libras.find_element(By.CSS_SELECTOR, 'h3 a').click()
# Obtenemos la categoria
categoriaLibro = driver.find_element(By.CSS_SELECTOR, 'ul.breadcrumb li:nth-child(3)').text
print(f'Título: {tituloLibroMas50Libras}')
print(f'Precio: {precioLibroMas50Libras}') 
print(f'Disponibilidad: {disponibilidadLibroMas50Libras}')
print(f'Categoría: {categoriaLibro}')

driver.back()

print('-----------------------------------------------------')

# ==========================================================
# EJERCICIO 6
# ENTRAR EN LA CATEGORÍA Humor Y ANALIZARLA
# ==========================================================
#
# Entrar en la categoría Humor y mostrar:
# - el nombre de la categoría
# - cuántos libros aparecen en esa página
# - cuál es el libro más caro de esa categoría
# ==========================================================

print('-- EJERCICIO 6 --')

categorias = driver.find_elements(By.CSS_SELECTOR, "div.side_categories ul li ul li a")

for categoria in categorias:
    if categoria.text.strip() == "Humor":
        categoria.click()
        break
    
categoriaHumor = driver.find_element(By.CSS_SELECTOR, 'div.page-header.action h1').text
print(f'Nombre categoría: {categoriaHumor}')
    
librosHumor = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
print(f'Hay {len(librosHumor)} libros de Humor.')

tituloLibroMasCaro = ''
precioLibroMasCaro = 0
for libro in librosHumor:
    # Obtenemos el titulo y el precio de cada libro
    tituloLibro = libro.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
    precioLibro = libro.find_element(By.CSS_SELECTOR, 'p.price_color').text
    # Quitamos la moneda y lo convertimos a float para poder comparar
    precioLibro = precioLibro.replace('£', '')
    precioLibro = float(precioLibro)
    # Comparamos los datos del libro actual del bucle y lo comparamos con el libro mas caro
    if precioLibro > precioLibroMasCaro:
        tituloLibroMasCaro = tituloLibro
        precioLibroMasCaro = precioLibro
print(f'El titulo del libro de humor mas caro es: {tituloLibroMasCaro}')
print(f'El precio del libro de humor mas caro es:  £{precioLibroMasCaro}')

driver.back()

print('-----------------------------------------------------')

# ==========================================================
# EJERCICIO 7
# AVERIGUAR EL PRECIO MEDIO DE UNA CATEGORÍA
# ==========================================================
#
# Entra en una categoría, por ejemplo Childrens, y calcula:
# - cuántos libros tiene esa categoría
# - el precio medio de esos libros
# ==========================================================

print('-- EJERCICIO 7 --')

categorias = driver.find_elements(By.CSS_SELECTOR, "div.side_categories ul li ul li a")
for categoria in categorias:
    if categoria.text.strip() == "Childrens":
        categoria.click()
        break

librosChildrens = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
numeroLibrosChildrens = len(librosChildrens)
print(f'Hay {numeroLibrosChildrens} libros de Childrens.')

precioTotal = 0
for libro in librosChildrens:
    # Obtenemos el precio de cada libro y lo convertimos a float
    precioLibro = libro.find_element(By.CSS_SELECTOR, 'p.price_color').text
    precioLibro = precioLibro.replace('£', '')
    precioLibro = float(precioLibro)
    # Acumulamos el precio para calcular la media después
    precioTotal += precioLibro

precioMedio = round((precioTotal / numeroLibrosChildrens) ,2)
print(f'El precio medio de los libros de Childrens es: £{precioMedio}')

driver.back()

print('-----------------------------------------------------')

# ==========================================================
# EJERCICIO 8
# RECORRER 3 PÁGINAS Y ENCONTRAR EL LIBRO MÁS CARO
# ==========================================================
#
# Recorrer las 3 primeras páginas y averiguar:
# - cuál es el libro más caro
# - cuánto cuesta
# - en qué página estaba
# ==========================================================

print('-- EJERCICIO 8 --')

tituloLibroMasCaro = ''
precioLibroMasCaro = 0
numeroPaginas = 3

for pagina in range(1, numeroPaginas + 1):
    # Obtenemos los libros de la página actual
    librosPagina = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    for libro in librosPagina:
        # Obtenemos el titulo y el precio de cada libro
        tituloLibro = libro.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
        precioLibro = libro.find_element(By.CSS_SELECTOR, 'p.price_color').text
        # Quitamos la moneda y convertimos a float para poder comparar
        precioLibro = precioLibro.replace('£', '')
        precioLibro = float(precioLibro)
        # Si el precio actual supera al máximo, actualizamos y guardamos la página
        if precioLibro > precioLibroMasCaro:
            tituloLibroMasCaro = tituloLibro
            precioLibroMasCaro = precioLibro
            paginaLibroMasCaro = pagina
    # Si no hemos llegado a la última página, avanzamos a la siguiente
    if pagina < numeroPaginas:
        driver.find_element(By.CSS_SELECTOR, 'li.next a').click()

print(f'El libro más caro es: {tituloLibroMasCaro}')
print(f'Cuesta: £{precioLibroMasCaro}')
print(f'Estaba en la página: {paginaLibroMasCaro}')

print('-----------------------------------------------------')


# ==========================================================
# EJERCICIO 9
# BUSCAR EL LIBRO MÁS BARATO Y EL MÁS CARO Y COMPARAR SUS ESTRELLAS
# ==========================================================
#
# Recorre las siete primeras páginas y guarda en una lista:
# - título
# - precio
# - estrellas
#
# Después muestra:
# - cuál es el libro más barato y cuántas estrellas tiene
# - cuál es el libro más caro y cuántas estrellas tiene
# - cuál de los dos tiene mejor valoración
# ==========================================================

print('-- EJERCICIO 9 --')

estrellasTextoANumero = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

tituloLibroMasCaro = ''
precioLibroMasCaro = 0
estrellasLibroMasCaro = 0

tituloLibroMasBarato = ''
precioLibroMasBarato = float('inf')
estrellasLibroMasBarato = 0

numeroPaginas = 7

driver.get("https://books.toscrape.com/")

for pagina in range(1, numeroPaginas + 1):
    # Obtenemos los libros de la página actual
    librosPagina = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    for libro in librosPagina:
        # Obtenemos el titulo del libro
        tituloLibro = libro.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
        # Obtenemos el precio y lo convertimos a float para poder comparar
        precioLibro = libro.find_element(By.CSS_SELECTOR, 'p.price_color').text
        precioLibro = float(precioLibro.replace('£', ''))
        # Obtenemos la clase CSS del elemento de estrellas y extraemos el número de estrellas
        claseEstrellas = libro.find_element(By.CSS_SELECTOR, 'p.star-rating').get_attribute('class')
        palabraEstrellas = claseEstrellas.split()[1]
        estrellasLibro = estrellasTextoANumero.get(palabraEstrellas, 0)
        # Actualizamos el libro más caro si el precio actual es mayor
        if precioLibro > precioLibroMasCaro:
            tituloLibroMasCaro = tituloLibro
            precioLibroMasCaro = precioLibro
            estrellasLibroMasCaro = estrellasLibro
        # Actualizamos el libro más barato si el precio actual es menor
        if precioLibro < precioLibroMasBarato:
            tituloLibroMasBarato = tituloLibro
            precioLibroMasBarato = precioLibro
            estrellasLibroMasBarato = estrellasLibro
    # Si no hemos llegado a la última página, avanzamos a la siguiente
    if pagina < numeroPaginas:
        driver.find_element(By.CSS_SELECTOR, 'li.next a').click()

print(f'El libro más caro es: {tituloLibroMasCaro}')
print(f'Cuesta: £{precioLibroMasCaro}')
print(f'Estrellas: {estrellasLibroMasCaro}')


print(f'El libro más barato es: {tituloLibroMasBarato}')
print(f'Cuesta: £{precioLibroMasBarato}')
print(f'Estrellas: {estrellasLibroMasBarato}')


if estrellasLibroMasCaro > estrellasLibroMasBarato:
    print(f'Mejor valorado: {tituloLibroMasCaro} (el más caro)')
elif estrellasLibroMasBarato > estrellasLibroMasCaro:
    print(f'Mejor valorado: {tituloLibroMasBarato} (el más barato)')
else:
    print('Ambos tienen la misma valoración')


print('-----------------------------------------------------')

# ==========================================================
# EJERCICIO 10
# COMPARAR DOS CATEGORÍAS
# ==========================================================
#
# Elige dos categorías, por ejemplo:
# - Humor
# - Mystery
#
# En cada una de ellas guarda en una lista:
# - título
# - precio
#
# Después compara:
# - cuántos libros aparecen en cada una
# - cuál tiene el libro más caro
# - cuál tiene el precio medio más alto
#
# IMPORTANTE:
# Si una categoría tiene varias páginas, debes tener en cuenta todos los libros
# de todas sus páginas, no solo los de la primera.
# ==========================================================


print('-- EJERCICIO 10 --')


driver.get("https://books.toscrape.com/")

categorias = driver.find_elements(By.CSS_SELECTOR, "div.side_categories ul li ul li a")
for categoria in categorias:
    if categoria.text.strip() == "Humor":
        categoria.click()
        break

datosLibrosHumor = []
while True:
    librosHumor = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    for libro in librosHumor:
        # Obtenemos el titulo y el precio de cada libro y los guardamos como tupla
        tituloLibro = libro.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
        precioLibro = float(libro.find_element(By.CSS_SELECTOR, 'p.price_color').text.replace('£', ''))
        datosLibrosHumor.append((tituloLibro, precioLibro))
    # Comprobamos si hay más páginas y avanzamos
    siguientes = driver.find_elements(By.CSS_SELECTOR, 'li.next a')
    if siguientes:
        siguientes[0].click()
    else:
        break

driver.get("https://books.toscrape.com/")
categorias = driver.find_elements(By.CSS_SELECTOR, "div.side_categories ul li ul li a")
for categoria in categorias:
    if categoria.text.strip() == "Mystery":
        categoria.click()
        break

datosLibrosMystery = []
while True:
    librosMystery = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    for libro in librosMystery:
        # Obtenemos el titulo y el precio de cada libro y los guardamos como tupla
        tituloLibro = libro.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
        precioLibro = float(libro.find_element(By.CSS_SELECTOR, 'p.price_color').text.replace('£', ''))
        datosLibrosMystery.append((tituloLibro, precioLibro))
    # Comprobamos si hay más páginas y avanzamos
    siguientes = driver.find_elements(By.CSS_SELECTOR, 'li.next a')
    if siguientes:
        siguientes[0].click()
    else:
        break

print(f'Número de libros en Humor: {len(datosLibrosHumor)}')
print(f'Número de libros en Mystery: {len(datosLibrosMystery)}')

libroMasCaroHumor = max(datosLibrosHumor, key=lambda x: x[1])
libroMasCaroMystery = max(datosLibrosMystery, key=lambda x: x[1])

print(f'Libro más caro de Humor: {libroMasCaroHumor[0]} (£{libroMasCaroHumor[1]})')
print(f'Libro más caro de Mystery: {libroMasCaroMystery[0]} (£{libroMasCaroMystery[1]})')

if libroMasCaroHumor[1] > libroMasCaroMystery[1]:
    print('Humor tiene el libro más caro')
elif libroMasCaroMystery[1] > libroMasCaroHumor[1]:
    print('Mystery tiene el libro más caro')
else:
    print('Ambas categorías tienen el mismo precio máximo')

precioMedioHumor = round(sum(p for _, p in datosLibrosHumor) / len(datosLibrosHumor), 2)
precioMedioMystery = round(sum(p for _, p in datosLibrosMystery) / len(datosLibrosMystery), 2)

print(f'Precio medio de Humor: £{precioMedioHumor}')
print(f'Precio medio de Mystery: £{precioMedioMystery}')

if precioMedioHumor > precioMedioMystery:
    print('Humor tiene el precio medio más alto')
elif precioMedioMystery > precioMedioHumor:
    print('Mystery tiene el precio medio más alto')
else:
    print('Ambas categorías tienen el mismo precio medio')


print('-----------------------------------------------------')


# ==========================================================
# EJERCICIO 11
# CONTAR CUÁNTOS LIBROS HAY EN CADA CATEGORÍA
# ==========================================================
#
# Recorre todas las categorías de la web y guarda en una lista:
# - nombre de la categoría
# - número de libros que contiene
#
# Después muestra:
# - cuántos libros tiene cada categoría
# - qué categoría es la que más libros tiene
#
# IMPORTANTE:
# Si una categoría tiene varias páginas, debes contar todos los libros
# de todas sus páginas, no solo los de la primera.
# ==========================================================

print('-- EJERCICIO 11 --')


driver.get("https://books.toscrape.com/")


categorias = driver.find_elements(By.CSS_SELECTOR, "div.side_categories ul li ul li a")
nombresCategorias = []
enlacesCategorias = []
for categoria in categorias:
    nombresCategorias.append(categoria.text.strip())
    enlacesCategorias.append(categoria.get_attribute('href'))


datosCategorias = []


for i in range(len(nombresCategorias)):
    driver.get(enlacesCategorias[i])
    totalLibros = 0
    while True:
        libros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
        totalLibros += len(libros)
        siguientes = driver.find_elements(By.CSS_SELECTOR, 'li.next a')
        if siguientes:
            siguientes[0].click()
        else:
            break
    datosCategorias.append((nombresCategorias[i], totalLibros))
    print(f'{nombresCategorias[i]}: {totalLibros} libros')


categoriaMasLibros = max(datosCategorias, key=lambda x: x[1])
print(f'La categoría con más libros es: {categoriaMasLibros[0]} ({categoriaMasLibros[1]} libros)')


print('-----------------------------------------------------')


# ==========================================================
# EJERCICIO 12
# ENCONTRAR LOS LIBROS CON 5 ESTRELLAS Y ORDENARLOS POR PRECIO
# ==========================================================
#
# Recorre todas las páginas y guarda en una lista:
# - título
# - precio
# - estrellas
#
# Después quédate solo con los libros que tengan 5 estrellas y ordénalos
# de mayor a menor precio.
#
# Muestra el ranking resultante.
# ==========================================================

print('-- EJERCICIO 12 --')

# Volvemos a la pagina de inicio
driver.get("https://books.toscrape.com/")

# Diccionario que contiene el valor de cada numero de estrellas
diccionarioEstrellas = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

# Lista para guardar todos los libros
totalLibros = []

# Bucle para recorrer todas las paginas de la web para guardar todos sus libros
while True:
    # Obtenemos la lista de libros
    libros = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    for libro in libros:
        # Obtenemos el titulo del libro actual
        tituloLibro = libro.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
        # Obtenemos el precio del libro actual, lo convertimos a float para poder comparar
        precioLibro = libro.find_element(By.CSS_SELECTOR, 'p.price_color').text
        precioLibro = precioLibro.replace('£', '')
        precioLibro = float(precioLibro)
        # Obtenemos la clase del elemento que contiene las estrellas
        estrellas = libro.find_element(By.CSS_SELECTOR, 'p.star-rating').get_attribute('class')
        # Obtenemos el numero de estrellas a partir de la clase que indica el numero de estrellas
        numeroEstrellas = estrellas.split()[1]
        # Asignamos el numero de estrellas correspondiente por el diccionario
        estrellasLibro = diccionarioEstrellas.get(numeroEstrellas, 0)
        totalLibros.append((tituloLibro, precioLibro, estrellasLibro))
    # Comprobamos si hay mas paginas y avanzamos
    siguientes = driver.find_elements(By.CSS_SELECTOR, 'li.next a')
    if siguientes:
        siguientes[0].click()
    else:
        break

# Creamos una lista con los libros que tengan 5 estrellas
libros5Estrellas = []

for libro in totalLibros:
    # Comprobamos que el libro actual tenga 5 estrellas
    if libro[2] == 5:
        libros5Estrellas.append(libro)
# Ordenamos la lista de libros por precio de mayor a menor
libros5Estrellas.sort(key=lambda x: x[1], reverse=True)

# Mostramos los resultados
print(f'Libros con 5 estrellas: {len(libros5Estrellas)}')
print('Ranking de mayor a menor precio:')
for indice, (titulo, precio, estrellas) in enumerate(libros5Estrellas, 1):
    print(f'{indice}. {titulo} - £{precio}')

print('-----------------------------------------------------')

# ==========================================================
# EJERCICIO 13
# EL MEJOR LIBRO
# ==========================================================
#
# Recorre libros y guarda en una lista:
# - título
# - precio
# - estrellas
# - disponibilidad
#
# El objetivo es encontrar el primer libro que cumpla estas condiciones:
# - cuesta menos de 20 libras
# - tiene 5 estrellas
# - está disponible
#
# Después muestra todos sus datos.
# ==========================================================

print('-- EJERCICIO 13 --')

# Volvemos a la pagina de inicio
driver.get("https://books.toscrape.com/")

# Diccionario que contiene el valor de cada numero de estrellas
diccionarioEstrellas = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

# Libro que cumpla las 3 condiciones
mejorLibro = None

# Bucle para recorrer todos los libros en busca del libro que cumpla las 3 condiciones
while not mejorLibro:
    libros = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')
    # Recorremos la lista de libros de la pagina
    for libro in libros:
        # Obtenemos el titulo del libro actual
        tituloLibro = libro.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
        # Obtenemos el precio del libro actual, lo convertimos a float para poder comparar
        precioLibro = libro.find_element(By.CSS_SELECTOR, 'p.price_color').text
        precioLibro = precioLibro.replace('£', '')
        precioLibro = float(precioLibro)
        # Obtenemos la clase del elemento que contiene las estrellas
        estrellas = libro.find_element(By.CSS_SELECTOR, 'p.star-rating').get_attribute('class')
        # Obtenemos el numero de estrellas a partir de la clase que indica el numero de estrellas
        numeroEstrellas = estrellas.split()[1]
        # Asignamos el numero de estrellas correspondiente por el diccionario
        estrellasLibro = diccionarioEstrellas.get(numeroEstrellas, 0)
        # Obtenemos la disponibilidad del libro actual
        disponibilidad = libro.find_element(By.CSS_SELECTOR, 'p.instock.availability').text.strip()
        # Comprobamos si el libro cumple las 3 condiciones, en el caso de cumplirlas lo guardamos y salimos del bucle
        if precioLibro < 20 and estrellasLibro == 5 and 'In stock' in disponibilidad:
            mejorLibro = (tituloLibro, precioLibro, estrellasLibro, disponibilidad)
            break
    # Si la lista de libros no contiene el ningun libro que cumpla las 3 condicones
    # avanzamos a la siguiente pagina
    if not mejorLibro:
        siguientes = driver.find_elements(By.CSS_SELECTOR, 'li.next a')
        if siguientes:
            siguientes[0].click()
        else:
            break

# En el caso de encontrar un libro que cumpla las 3 condiciones lo mostramos
if mejorLibro:
    print(f'Título: {mejorLibro[0]}')
    print(f'Precio: £{mejorLibro[1]}')
    print(f'Estrellas: {mejorLibro[2]}')
    print(f'Disponibilidad: {mejorLibro[3]}')
else:
    print('No se ha encontrado ningún libro que cumpla las condiciones')

print('-----------------------------------------------------')

driver.quit()