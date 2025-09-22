# detectamos la extensión 
nombre = "trabajo_de investigacion.PDF"
extension = nombre.lower().split(".")[-1]
#diccionario con extensiones
tipos = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "aplication/pdf",
    "zip": "aplication/zip"
}
#buscamos la extension en el diccionario 
tipo_mime = tipos.get(extension, "aplication/octet-stream")
print("tipo mime:",tipo_mime)


