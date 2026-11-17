from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = None
    estado = ""

    if request.method == "POST":
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

    return render_template(
        "ejercicio1.html",
        promedio=promedio,
        estado=estado
    )

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombre_mayor = ""
    cantidad = 0

    if request.method == "POST":
        nombres = [
            request.form["nombre1"],
            request.form["nombre2"],
            request.form["nombre3"]
        ]

        nombre_mayor = max(nombres, key=len)
        cantidad = len(nombre_mayor)

    return render_template(
        "ejercicio2.html",
        nombre_mayor=nombre_mayor,
        cantidad=cantidad
    )

if __name__ == "__main__":
    app.run(debug=True)