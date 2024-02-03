from flask import Flask, render_template, request, session

app = Flask(__name__)

# configuracion de clave secreta
app.config['SECRET_KEY'] = '1234'

# Activa el modo depuracion
app.debug = True


# ruta para el home
@app.route('/')
def home():
    session['nombre'] = 'juan'
    return render_template('Home.html')


# ruta para el ejercicio 1
@app.route('/dashboardUser', methods=['GET', 'POST'])
def inventario():
    if request.method == 'POST':
        # tomando los datos desde el formulario

        nombre = request.form['nombre']
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        seccion = request.form['seccion']
        # proceso de los datos
        try:
            # Código que podría lanzar una excepción

            if not isinstance(nombre, str):
                raise TypeError("Error: Solo se permite un nombre valido")
            elif tipo == "verde":

                nombre = "aqui va el nombre"
                tipo = "aqui va el tipo"
                descripcion = "aqui va la descripcion"
                seccion = "aqui va la seccion a la que pertenece"
                return render_template('dashboardUser.html', nombre=nombre, tipo=tipo,
                                       descripcion=descripcion, seccion=seccion)
            elif tipo == "blanco":

                nombre = "aqui va el nombre"
                tipo = "aqui va el tipo"
                descripcion = "aqui va la descripcion"
                seccion = "aqui va la seccion a la que pertenece"
                return render_template('dashboardUser.html', nombre=nombre, tipo=tipo,
                                       descripcion=descripcion, seccion=seccion)

            return render_template('dashboardUser.html')

        except TypeError as e:
            # Manejo de la excepción TypeError
            print(e)


# ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # tomando los datos desde el formulario
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        # opcion administrador
        if nombre == 'juan' and contrasena == 'admin':
            session['nombre'] = nombre
            resultado = f'Bienvenido administrador {nombre}'
            return render_template('dashboardAdmin.html', resultado=resultado)
        # opcion usuario
        elif nombre == 'pepe' and contrasena == 'user':
            session['nombre'] = nombre
            resultado = f'Bienvenido usuario {nombre}'
            return render_template('dashboardUser.html', resultado=resultado)
        else:
            resultado = 'Nombre o contraseña equivocado'
            return render_template('Home.html', resultado=resultado)

    return render_template('Home.html')


# Ejecucion de la app
if __name__ == '__main__':
    app.run()
