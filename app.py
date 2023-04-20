from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
import product
from product import Producto

db = dbase.dbConnection()

#instancia de flask
app = Flask(__name__)

#Rutas de aplicacion
@app.route('/')
def home():
    #se crea la coleccion en la base de datos
    productosDB = db['productos']
    productosRecibidos = productosDB.find()
    #esta linea de codigo refresca la pagina y devuelve los datos contenidos en la base
    return render_template('index.html', productosDB = productosRecibidos, product = product.Producto)

#Metodo POST
@app.route('/productos', methods=['POST'])
def agregarProducto():
    #El request form es para pedir los datos de los inputs del html
    productosDB = db['productos']
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']

    #se validan los 3 datos recibidos y envia una respuesta al servidor
    if nombre and precio and cantidad:
       producto = Producto(nombre, precio, cantidad)
       productosDB.insert_one(producto.toDBCollection())
       response = jsonify({
           'nombre': nombre,
           'precio': precio,
           'cantidad': cantidad
       })
       return redirect(url_for('home'))
    else:
        #si falla la validacion se llama a la funcion de error
        return notFound()

#Metodo Delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    productosDB = db['productos']
    productosDB.delete_one({'nombre' : product_name})
    return redirect(url_for('home'))


#Metodo POST EDIT
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    productosDB = db['productos']
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']

    if nombre and precio and cantidad:
        productosDB.update_one({'nombre': product_name}, {'$set': {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}})
        response = jsonify({'mensaje' : 'Producto '+ product_name + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

# funcion de error
@app.errorhandler(404)
def notFound(error=None):
    mensaje={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(mensaje)
    response.status_code = 404
    return response

#validacion para que la app se ejecute en modo debug y use el puerto 4000
if __name__== '__main__':
    app.run(debug=True, port=4000)


