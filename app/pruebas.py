# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import storage

# # Inicializa la aplicación de Firebase
# cred = credentials.Certificate('clave.json')
# firebase_admin.initialize_app(cred, {
#     'storageBucket': 'ecomarket-a1832.appspot.com'
# })

# ruta_imagen_local = 'app/static/img/logo.png'
# ruta_destino_firebase = 'imagen.png'

# # Sube la imagen a Firebase Storage
# bucket = storage.bucket()
# blob = bucket.blob(ruta_destino_firebase)
# blob.upload_from_filename(ruta_imagen_local)

# print('Imagen subida con éxito a Firebase Storage.')

# import firebase_admin
# from firebase_admin import credentials, firestore
# from flask import Flask, render_template, request, session, redirect
# from firebase_admin import storage
# from werkzeug.utils import secure_filename
# import datetime


# # Obtén la ruta completa al archivo JSON de las credenciales de servicio

# # Inicializa la aplicación de Firebase utilizando las credenciales de servicio
# cred = credentials.Certificate('clave.json')
# firebase_admin.initialize_app(cred, {"universe_domain": "googleapis.com",
#   "apiKey": "AIzaSyDTFaBDaOIzIdpbCzQopxpuKPJQxQXrQR4",
#   "authDomain": "ecomarket-a1832.firebaseapp.com",
#   "projectId": "ecomarket-a1832",
#   "storageBucket": "ecomarket-a1832.appspot.com",
#   "messagingSenderId": "736616157400",
#   "appId": "1:736616157400:web:86659058a4f8f2a05987ad"})

# bucket = storage.bucket()
# blob = bucket.blob('banner2.jpg')  # Reemplaza "ruta/a/tu/imagen.jpg" con la ruta de tu imagen en Firebase Storage
# token = blob.generate_signed_url(expiration=datetime.timedelta(minutes=15), method='GET')
# print(token)
# @app.route('/buscar_producto', methods=['GET', 'POST'])
# def buscar_producto():
#     producto = None

#     if request.method == 'POST':
#         nombre_producto = request.form.get('nombre_producto')

#         # Obtener una referencia a la colección "Producto"
#         productos_ref = db.collection("Producto")

#         # Realizar una consulta para buscar el producto por su nombre
#         query = productos_ref.where("producto", "==", nombre_producto)
#         resultados = query.get()

#         # Verificar si se encontraron resultados
#         if resultados:
#             for producto_doc in resultados:
#                 # Obtener el producto encontrado junto con su ID
#                 producto = producto_doc.to_dict()
#                 producto['id'] = producto_doc.id
#                 break
#             bucket = storage.bucket()
#             blob = bucket.blob(producto['imagen'])  # Reemplaza "ruta/a/tu/imagen.jpg" con la ruta de tu imagen en Firebase Storage
#             token = blob.generate_signed_url(expiration=datetime.timedelta(minutes=15), method='GET')
        

#     return render_template('buscar_producto.html', producto=producto, imagen=token)




# <!DOCTYPE html>
# <html>
# <head>
#     <title>Buscar y Actualizar Producto</title>
# </head>
# <body>
#     <h1>Buscar Producto</h1>
#     <form method="POST" action="/buscar_producto">
#         <label for="nombre_producto">Nombre del Producto:</label>
#         <input type="text" id="nombre_producto" name="nombre_producto">
#         <button type="submit">Buscar</button>
#     </form>
#     {% if producto %}
#         <h2>Detalles del Producto:</h2>
#         <p>ID: {{ producto.id }}</p>
#         <p>Nombre: {{ producto.producto }}</p>
#         <p>Precio: {{ producto.precio }}</p>
#         {% if imagen %}
#             <img src="{{ imagen }}" alt="Imagen del Producto">
#         {% endif %}
#         <h2>Actualizar Producto:</h2>
#         <form method="POST" action="/actualizar_producto">
#             <input type="hidden" name="nombre_producto" value="{{ producto.producto }}">
#             <label for="nuevo_nombre">Nuevo Nombre:</label>
#             <input type="text" id="nuevo_nombre" name="nuevo_nombre">
#             <label for="nuevo_precio">Nuevo Precio:</label>
#             <input type="text" id="nuevo_precio" name="nuevo_precio">
#             <button type="submit">Actualizar</button>
#         </form>
#     {% else %}
#         <p>No se encontró ningún producto con el nombre especificado.</p>
#     {% endif %}
# </body>
# </html>

