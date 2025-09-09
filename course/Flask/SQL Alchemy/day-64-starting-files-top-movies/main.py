from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FloatField
from wtforms.validators import DataRequired,Length
import requests

TMDB_API_KEY="092e806b55e1eb16f386eb9198326436"
TMDB_BEARER_TOKEN="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwOTJlODA2YjU1ZTFlYjE2ZjM4NmViOTE5ODMyNjQzNiIsIm5iZiI6MTcyNDgxMDM1OC41MzYsInN1YiI6IjY2Y2U4NDc2NGM5MjU1MTc3ZGM2MTJmNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.c1d2ah9uzpDcv8OFIuxF1NlWnlqdhiSeStP-oyIGr8o"
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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///movies-collection.db"
db.init_app(app)
# CREATE TABLE

class Movie(db.Model):
    id:Mapped[int]=mapped_column(primary_key=True)
    title : Mapped[str] = mapped_column(String(250),nullable=False,unique=True)
    year : Mapped[int] = mapped_column(nullable=False)
    description : Mapped[str] = mapped_column(String(250),nullable=False)
    rating : Mapped[float] = mapped_column(nullable=True)
    ranking : Mapped[int] = mapped_column(nullable=True)
    review : Mapped[str] = mapped_column(String(250),nullable=True)
    img_url : Mapped[str] = mapped_column(String(250),nullable=False)

with app.app_context():
    # db.create_all()

    second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )
    # db.session.add(second_movie)
    # db.session.commit()

class RateMovieForm(FlaskForm):
    rating = FloatField(label='Your rating out of 10')
    review = StringField(label='Your review')
    submit = SubmitField(label='Done')


@app.route("/")
def home():
    result=db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies=result.scalars().all()  
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html",movies=all_movies)

@app.route("/edit",methods=['GET','POST'])
def edit():
    form=RateMovieForm()
    id=request.args.get('id')
    movie = db.get_or_404(Movie, id)
    if form.validate_on_submit():
        movie_to_update=db.session.execute(db.select(Movie).where(Movie.id==id)).scalar()
        movie_to_update.rating=form.rating.data
        movie_to_update.review=form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html',movie=movie,form=form)

@app.route("/delete")
def delete():
    id=request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, id)
    
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

class AddMovieForm(FlaskForm):
    title = StringField(label='Movie Title')
    submit = SubmitField(label='Add Movie')

url = "https://api.themoviedb.org/3/search/movie"
headers = {
"accept": "application/json",
"Authorization": f"Bearer {TMDB_BEARER_TOKEN}"
}

@app.route("/add",methods=['GET','POST'])
def add():
    form=AddMovieForm()
    if form.validate_on_submit():
        movie_title=form.title.data
        response = requests.get(url=url, params={"api_key": TMDB_API_KEY, "query": movie_title},timeout=10)
        response.raise_for_status()
        data=response.json()["results"]
        return render_template('select.html',result=data)
    return render_template('add.html',form=form)

@app.route('/find')
def find_movie():
    movie_id=request.args.get('id')
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}",params={"api_key": TMDB_API_KEY})
    data=response.json()
    add_movie = Movie(
    title=data["original_title"],
    year=data["release_date"][0:4],
    description=data["overview"],
    img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    )
    db.session.add(add_movie)
    db.session.commit()
    return redirect(url_for('edit'))


if __name__ == '__main__':
    app.run(debug=True)
