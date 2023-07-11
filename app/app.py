import firebase_admin 
from firebase_admin import credentials, firestore
from flask import Flask, render_template, request

cred = credentials.Certificate('clave.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/shop')
def tienda():
    return render_template("shop.html")

@app.route('/producto')
def producto():
    return render_template("producto.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users_ref = db.collection('Usuario')
        query = users_ref.where('username', '==', username).where('password', '==', password)
        result = query.get()
        print(result)

        if len(result) > 0:  # Verifica si se encontraron documentos
            return render_template('dashboard.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        nuevo_usuario = {"username": username, "password": password, "email": email}
        doc_ref = db.collection("Usuario").add(nuevo_usuario)
        
        return render_template('login.html')
    else:
        return render_template('register.html')

    
if __name__ == '__main__':
    app.run(debug=True)