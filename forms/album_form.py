from flask_wtf import Form, FlaskForm
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators

class AlbumForm(FlaskForm):

    id = HiddenField()

    album_name = StringField("Title: ", [
        validators.DataRequired("Please enter album title."),
        validators.Length(3, 20, "Value should be from 3 to 20 symbols")
    ])

    album_performer = StringField("Performer: ", [
        validators.DataRequired("Please enter performer."),
        validators.Length(3, 20, "Value should be from 3 to 20 symbols")
    ])

    submit = SubmitField("Save")