import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, request, session, redirect

cred = credentials.Certificate('clave.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

app.secret_key = '987654321'

def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        nuevo_usuario = {"username": username, "password": password, "email": email}
        doc_ref = db.collection("Usuario").add(nuevo_usuario)
        
        return render_template('dashboard.html')
    else:
        return render_template('index.html')

def leer():
    documents = db.collection('Usuario').order_by('username').get()
    for document in documents:
        data = document.to_dict()
        username = data.get('username')
        password = data.get('password')

def eliminar(document_id):
    doc_ref = db.collection('Usuario').document(document_id)
    doc_ref.delete()
    print(f"Documento con ID {document_id} eliminado correctamente.")

def actualizar(document_id, nuevos_datos):
    doc_ref = db.collection('Usuario').document(document_id)
    doc_ref.update(nuevos_datos)
    print(f"Documento con ID {document_id} actualizado correctamente.")

# Llamada a la función actualizar() con el ID del documento y los nuevos datos
nuevos_datos = {"username": "Juan Carlos", "password": "manolo78"}
