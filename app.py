from flask import Flask, render_template, request, redirect, url_for

from dao.db import PostgresDb
from sqlalchemy.sql.expression import func
from dao.credentials import *
from dao.db import *
from dao.orm.model import ormAlbum, ormStudent, ormGenre
from forms.genre_form import GenreForm
from forms.student_form import StudentForm
from forms.album_form import AlbumForm

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "LKM-VSNEJ91-VM:LMVE")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL",
                                                  f"postgresql://{username}:{password}@{host}:{port}/{database}")
db = PostgresDb()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/genre.html', methods=['GET'])
def show_genre():
    result = db.sqlalchemy_session.query(ormGenre).all()
    return render_template('genre.html', genres=result)


@app.route('/album.html', methods=['GET'])
def show_album():
    result = db.sqlalchemy_session.query(ormAlbum).all()
    return render_template('album.html', albums=result)


@app.route('/student.html', methods=['GET'])
def show_student():
    result = db.sqlalchemy_session.query(ormStudent).all()
    return render_template('student.html', students=result)



@app.route('/new_student', methods=['GET', 'POST'])
def new_student():
    db = PostgresDb()
    form = StudentForm()

    if request.method == 'POST':
        if not form.validate():
            return render_template('form_for_student.html', form=form, form_name="New student", action="new_student")
        else:
            student_id = list(db.sqlalchemy_session.query(func.max(ormStudent.student_id)))[0][0]
            student_obj = ormStudent(
                student_id=student_id+1,
                faculty=form.faculty.data,
                group=form.group.data,
                name=form.name.data,
                surname=form.surname.data,
                username=form.username.data)

            db.sqlalchemy_session.add(student_obj)
            db.sqlalchemy_session.commit()

            return redirect(url_for('show_student'))

    return render_template('form_for_student.html', form=form, form_name="New student", action="new_student")


@app.route('/edit_student', methods=['GET', 'POST'])
def edit_student():
    form = StudentForm()

    if request.method == 'GET':

        id = request.args.get('id')

        db = PostgresDb()
        student_obj = db.sqlalchemy_session.query(ormStudent).filter(ormStudent.student_id == id).one()

        # fill form and send to user
        form.id.data = student_obj.student_id
        form.faculty.data = student_obj.faculty
        form.group.data = student_obj.group
        form.name.data = student_obj.name
        form.surname.data = student_obj.surname
        form.username.data = student_obj.username

        return render_template('form_for_student.html', form=form, form_name="Edit student", action="edit_student")

    else:
        if not form.validate():
            return render_template('form_for_student.html', form=form, form_name="Edit student",
                                   action="edit_student")
        else:
            db = PostgresDb()
            # find professor
            student_obj = db.sqlalchemy_session.query(ormStudent).filter(ormStudent.student_id == form.id.data).one()

            # update fields from form data
            student_obj.student_id = form.id.data
            student_obj.faculty = form.faculty.data
            student_obj.group = form.group.data
            student_obj.name = form.name.data
            student_obj.surname = form.surname.data
            student_obj.username = form.username.data

            db.sqlalchemy_session.commit()

            return redirect(url_for('show_student'))

@app.route('/delete_student')
def delete_student():
    student_id = request.args.get('id')

    db = PostgresDb()

    result = db.sqlalchemy_session.query(ormStudent).filter(ormStudent.student_id == student_id).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()

    return redirect(url_for('show_student'))

@app.route('/new_album', methods=['GET', 'POST'])
def new_album():
    db = PostgresDb()
    form = AlbumForm()

    if request.method == 'POST':
        if not form.validate():
            return render_template('form_for_album.html', form=form, form_name="New album", action="new_album")
        else:
            album_id = list(db.sqlalchemy_session.query(func.max(ormAlbum.album_id)))[0][0]
            album_obj = ormAlbum(
                album_id=album_id+1,
                album_title=form.album_name.data,
                performer=form.album_performer.data)

            db.sqlalchemy_session.add(album_obj)
            db.sqlalchemy_session.commit()

            return redirect(url_for('show_album'))

    return render_template('form_for_album.html', form=form, form_name="New album", action="new_album")

@app.route('/edit_album', methods=['GET', 'POST'])
def edit_album():
    form = AlbumForm()

    if request.method == 'GET':

        id = request.args.get('id')

        db = PostgresDb()
        album_obj = db.sqlalchemy_session.query(ormAlbum).filter(ormAlbum.album_id == id).one()

        # fill form and send to user
        form.id.data = album_obj.album_id
        form.album_name.data = album_obj.album_title
        form.album_performer.data = album_obj.performer


        return render_template('form_for_album.html', form=form, form_name="Edit album", action="edit_album")

    else:
        if not form.validate():
            return render_template('form_for_album.html', form=form, form_name="Edit album",
                                   action="edit_album")
        else:
            db = PostgresDb()
            # find professor
            album_obj = db.sqlalchemy_session.query(ormAlbum).filter(ormAlbum.album_id == form.id.data).one()

            # update fields from form data
            album_obj.album_id = form.id.data
            album_obj.album_title = form.album_name.data
            album_obj.performer = form.album_performer.data


            db.sqlalchemy_session.commit()

            return redirect(url_for('show_album'))

@app.route('/delete_album')
def delete_album():
    album_id = request.args.get('id')

    db = PostgresDb()

    result = db.sqlalchemy_session.query(ormAlbum).filter(ormAlbum.album_id == album_id).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()

    return redirect(url_for('show_album'))

@app.route('/new_genre', methods=['GET', 'POST'])
def new_genre():
    db = PostgresDb()
    form = GenreForm()

    if request.method == 'POST':
        if not form.validate():
            return render_template('form_for_genre.html', form=form, form_name="New genre", action="new_genre")
        else:
            genre_id = list(db.sqlalchemy_session.query(func.max(ormGenre.genre_id)))[0][0]
            genre_obj = ormGenre(
                genre_id=genre_id+1,
                genre_name=form.genre_name.data,
                psychotype=form.psychotype.data)

            db.sqlalchemy_session.add(genre_obj)
            db.sqlalchemy_session.commit()

            return redirect(url_for('show_genre'))

    return render_template('form_for_genre.html', form=form, form_name="New genre", action="new_genre")

@app.route('/edit_genre', methods=['GET', 'POST'])
def edit_genre():
    form = GenreForm()

    if request.method == 'GET':

        id = request.args.get('id')

        db = PostgresDb()
        genre_obj = db.sqlalchemy_session.query(ormGenre).filter(ormGenre.genre_id == id).one()

        # fill form and send to user
        form.id.data = genre_obj.genre_id
        form.genre_name.data = genre_obj.genre_name
        form.psychotype.data = genre_obj.psychotype


        return render_template('form_for_genre.html', form=form, form_name="Edit genre", action="edit_genre")

    else:
        if not form.validate():
            return render_template('form_for_genre.html', form=form, form_name="Edit genre",
                                   action="edit_genre")
        else:
            db = PostgresDb()
            # find professor
            genre_obj = db.sqlalchemy_session.query(ormGenre).filter(ormGenre.genre_id == form.id.data).one()

            # update fields from form data
            genre_obj.genre_id = form.id.data
            genre_obj.genre_name = form.genre_name.data
            genre_obj.psychotype = form.psychotype.data


            db.sqlalchemy_session.commit()

            return redirect(url_for('show_genre'))

@app.route('/delete_genre')
def delete_genre():
    genre_id = request.args.get('id')

    db = PostgresDb()

    result = db.sqlalchemy_session.query(ormGenre).filter(ormGenre.genre_id == genre_id).one()

    db.sqlalchemy_session.delete(result)
    db.sqlalchemy_session.commit()

    return redirect(url_for('show_genre'))

if __name__ == '__main__':
    app.run()
