from dao.orm.model import *
from dao.db import PostgresDb

db = PostgresDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session

# clear all tables in right order
session.query(ormAlbum).delete()
session.query(ormGenre).delete()
session.query(ormStudent).delete()

Zemlya = ormAlbum(album_id=1, album_title='Zemlya', performer='Okean Elzy')
Closer = ormAlbum(album_id=2, album_title='Closer', performer='The Hardkiss')
Sontse = ormAlbum(album_id=3, album_title='Sontse', performer = 'Antytila')

rock = ormGenre(genre_id=1, genre_name='rock', psychotype='giperteam')
indie_pop = ormGenre(genre_id=2, genre_name='indie-pop', psychotype='emotive')
pop = ormGenre(genre_id=3, genre_name='pop', psychotype='giperteam')

Atamanchuk = ormStudent(student_id=1, faculty = 'FICT', group = 'IT-93', name = 'Lena', surname = 'Atamanchuk', username = '@lenech')
Popova = ormStudent(student_id=2, faculty = 'IASA', group = 'KA-61', name = 'Dasha', surname = 'Popova', username = '@popovaaa')
Petukhova = ormStudent(student_id=3, faculty = 'IASA', group = 'KA-63', name = 'Katya', surname = 'Petukhova', username = '@KatePetukhova')

session.add_all([Zemlya, Closer, Sontse, rock, indie_pop, pop, Atamanchuk, Popova, Petukhova])
res = session.query(ormAlbum)
result = session.execute(res)
for row in res:
    print(row)
session.commit()