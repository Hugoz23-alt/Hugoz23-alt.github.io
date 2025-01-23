from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        message = f"Gracias, {nombre}! Tu mensaje ha sido enviado."
        # Aquí podrías procesar el mensaje, por ejemplo, enviarlo a un correo electrónico.

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)