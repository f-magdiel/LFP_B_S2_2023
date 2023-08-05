
# ? Modo w+: Lectura y escritura
# * Abrir el archivo
Archivo = open('ejemplo.txt', 'w+')
# ! Crea el archivo si no existe o sobrescribe su contenido.

# * Escribir en el archivo
Archivo.write('\nEscribiendo con W+\n')

# * Cerrar el archivo
Archivo.close()