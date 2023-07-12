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
