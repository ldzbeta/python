from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
# localhost:5000 == 127.0.0.1:5000

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    result=db.session.execute(db.select(Book))
    all_books=result.scalars().all()  #scalar represents a complex data type represents basic dataypes like int str float etc.
    return render_template('index.html',books=all_books)


@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        data = request.form
        # new_book = {
        #     "title": data["title"],
        #     "author": data["author"],
        #     "rating": data["rating"]
        # }
        # # If you want to use +=, uncomment the next two lines:
        # global all_books
        # all_books += [new_book]
        # # curly  brackets imp
        # # Otherwise, using append() is preferred and does not require global:
        # # all_books.append(new_book)

        new_book = Book(title=data["title"], author=data["author"], rating=data["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit',methods=["GET","POST"])
def edit():
    id=request.args.get('id') #to get the value of id from url
    # id is not passed as parameter , so it will ad as args in url /edit?id=value
    if request.method=="POST": 
        book_to_update=db.session.execute(db.select(Book).where(Book.id==id)).scalar()
        book_to_update.rating=request.form["new_rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book = db.session.execute(db.select(Book).where(Book.id==id)).scalar()
    return render_template('edit.html',item=book)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

