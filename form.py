
# importing Flask and other modules
from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def formulario():
    if request.method == "POST":
       first_name = request.form.get("fname")
       last_name = request.form.get("lname")
       fnacimiento = request.form.get("nacimiento")
       ocupa = request.form.get("ocupacion")
       celu = request.form.get("contacto1")
       correo = request.form.get("contacto2")
       fnaci = request.form.get("nacionalidad")
       ingles = request.form.get("Inglés")
       progra = request.form.get("programacion")
       aptitud = request.form.get("Aptitudes")
       habilidad = request.form.get("habili")
       return render_template("Curriculum.html", nombre = first_name, apellido=last_name, nacimiento = fnacimiento, pocupado=ocupa, celular = celu, email = correo, nati = fnaci, nivel=ingles, lenguajes = progra, apt = aptitud, habilid = habilidad)
    return render_template("form.html")

 
if __name__=='__main__':
   app.run()