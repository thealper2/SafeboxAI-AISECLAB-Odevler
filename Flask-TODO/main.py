from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	completed = db.Column(db.Boolean)

	def __init__(self, title):
		self.title = title
		self.completed = False

@app.route("/")
def index():
	todos = Todo.query.all()
	return render_template("index.html", todos=todos)

@app.route("/create", methods=["POST"])
def create():
	title = request.form["title"]
	todo = Todo(title)
	db.session.add(todo)
	db.session.commit()
	return redirect("/")

@app.route("/complete/<int:id>")
def complete(id):
	todo = Todo.query.get(id)
	todo.completed = True
	db.session.commit()
	return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
	todo = Todo.query.get(id)
	db.session.delete(todo)
	db.session.commit()
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)
