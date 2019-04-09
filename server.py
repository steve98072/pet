from flask import Flask, render_template,request,redirect,session
from mysqlco import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('pets')	       
    pets = mysql.query_db('SELECT * FROM pet where id=int(pet_id)')  
    return render_template("index.html", all_pets = pets, id=int(pet_id))

@app.route("/create", methods=["POST"])
def add_pet_to_db():
    # session['count'] += 1

    query = "INSERT INFO pets (pet_id,name,type,created_at,updated_at)VALUES ((%pname)s, (%ptype)s, NOW(),NOW());"
    data = {
        'pn': request.form['pname'],
        'pt': request.form['ptype']
    }
    db = connectToMySQL('pets')
    db.query_db(query, data)
    return redirect('/')
            
if __name__ == "__main__":
    app.run(debug=True)
