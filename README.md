# GoogleSearchApp

If Docker file will work you need to do:

~~~~
docker-compose build
docker-compose up
~~~~

If it doesn't what is needed is to set up Postgres database with configuration as in config.py file.

Then you just run:

~~~~
python3 main.py
~~~~

Web form for searching will be available under localhost:5000/search_form
