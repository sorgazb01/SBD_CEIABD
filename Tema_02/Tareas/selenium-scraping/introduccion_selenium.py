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
    servicio = Service(executable_path="chromedriver.exe")

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
# Accedemos a la pagina del libro
primerLibroMas50Libras.find_element(By.CSS_SELECTOR, 'article.product_pod h3 a').click()
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





driver.quit()