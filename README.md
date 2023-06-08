# Wk4d3_homework

Set up database in Terminal:
dropdb book_manager
createdb book_manager

To link database and database sql file:
psql -d book_manager -f db/book_manager.sql

Another handy command in Terminal:
psql book_manager
which takes you into the database in Terminal, so you can run PSQL commands such as:
SELECT * FROM books;
INSERT INTO albums (title, artist_id, genre) VALUES ('Definitely Maybe', 17, 'Rock');

\q to quit psql



Populate database by adding objects into Console, then run:
python3 console.py  

To run the program:
flask run
then, command click the URL that appears in Terminal
Control C to exit Flask

To debug, use pdb.set_trace() in Console 

Add 
FLASK_DEBUG=true 
to your .flaskenv file to keep Flask updated (means you don't have to keep quitting and restarting Flask)



