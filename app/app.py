import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, request, session, redirect
# from firebase_admin import storage
from firebase_admin import storage
from werkzeug.utils import secure_filename


# Obtén la ruta completa al archivo JSON de las credenciales de servicio

# Inicializa la aplicación de Firebase utilizando las credenciales de servicio
cred = credentials.Certificate('clave.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'ecomarket-a1832.appspot.com'
})


db = firestore.client()

app = Flask(__name__)

app.secret_key = '987654321'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/shop')
def tienda():
    return render_template("shop.html")

@app.route('/producto')
def producto():
    return render_template("producto.html")

@app.route('/adminindex')
def admin_Index():
    return render_template("adminindex.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users_ref = db.collection('Usuario')
        query = users_ref.where('username', '==', username).where('password', '==', password)
        result = query.get()
        session['usuario'] = username

        if len(result) > 0:  # Verifica si se encontraron documentos
            if username:
                users_ref = db.collection('Usuario')
                #La función a continuación sirve para hacer consultas con el where
                query = users_ref.where('username', '==', username).where('admin', '==', 1)
                result = query.get()
                if len(result) > 0:
                    return render_template("adminindex.html", usuario=username)
                else:
                    return render_template('index.html', usuario = username)
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')
    else:
            return render_template('login.html')

    
@app.route('/dashboard')
def perfil():
    username = session.get('usuario')
    if username:
        return render_template("dashboard.html", usuario=username)
    else:
        return redirect('/login')


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
    
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/')

@app.route('/adminpage')
def admin_Page():
    username = session.get('usuario')
    if username:
        users_ref = db.collection('Usuario')
        #La función a continuación sirve para hacer consultas con el where
        query = users_ref.where('username', '==', username).where('admin', '==', 1)
        result = query.get()
        if len(result) > 0:
            return render_template("adminpage.html", usuario=username)
    return redirect('/login')

@app.route('/productos_Admin', methods=['GET', 'POST'])
def crear_Producto():
    if request.method == 'POST':
        producto = request.form.get('product_name')
        precio = request.form.get('product_price')
        imagen = request.files.get('product_image')
        print(imagen)
        nombre_imagen = secure_filename(imagen.filename) if imagen else None

        if nombre_imagen:
            # Cargar imagen en Firebase Storage
            bucket = storage.bucket()
            blob = bucket.blob(nombre_imagen)
            blob.upload_from_file(imagen)

            imagen_url = blob.public_url

            nuevo_Producto = {"producto": producto, "precio": precio, "imagen": imagen_url}
            doc_ref = db.collection("Producto").add(nuevo_Producto)
        
        return render_template("productos_Admin.html")

    return render_template("productos_Admin.html")


if __name__ == '__main__':
    app.run(debug=True)

