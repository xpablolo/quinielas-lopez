# Quinielas López
Simple project of Data Extraction, Web Scraping and Web Application in Python developed by me.


## Brief description
Given an Excel document with the weekly predictions of football matches of a group of people, the project automates the process of comparison with the real results extracted from a webpage. The information is shown in a web-app created with Flask and hosted at  <http://pablolo.pythonanywhere.com>.

The project contains hence:
- A Python script `init.py` which reads the Excel document `datos.xlsx` using _Pandas_ and extracts the information needed from <https://www.quiniela15.com/resultados-quiniela> using _BeautifulSoup_ so the predictions can be validated. The scripts creates lastly an Excel document `Resultados.xlsx` with the results of the predictions.
- A Python script `partidos_quiniela.py` which extracts the relevant matches from the same web. This information was not given in the initial Excel document `datos.xlsx`.
- A Python document `flask_app.py` for the initialization of the web using _Flask_.
- The needed html templates for the web grouped in the repository `/templates`.



