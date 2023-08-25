# Welkom bij mijn API over auto's en hun eigenaars

## Inhoudsopgave
1. [Inleiding](#inleiding)
2. [frontend](#frontend)
3. [Postman](#postman)
4. [Swagger](#swagger)

## Inleiding
Ik heb gebruikt gemaakt van FastAPI om een API te maken over auto's en hun eigenaars. De API is gemaakt met Python en de data wordt opgeslagen in een SQLite database. De API is te benaderen via de browser, Postman en Swagger. De bedoeling hiervan is dat mensen die een garage delen kunnen zien welke eigenaar bij welke auto hoort.

## Frontend
De bedoeling was om een volledige frontend te bouwen rond alle endpoints voor mijn api ik heb enkel een login endpoint kunnen realiseren in de frontend. Ik heb wel mijn best gedaan om deze er zo goed mogelijk uit te laten zien.

Dit is de login pagina van de frontend:
![login](images/frontendlogin1.png)

Hier zie je het ingelogde scherm en hier zie je ook dat er na het inloggen een get endpoint tevoorschijn komt:
![login](images/frontendlogin2.png)

Deze Get endpoint zorgt ervoor dat je alle auto's en hun eigenaars te zien krijgt:
![login](images/frontendlogin3.png)

## Postman
Ik heb ook gebruik gemaakt van Postman om mijn API te testen. Ik heb hier een collectie gemaakt met alle endpoints die ik heb gemaakt.

### Post token
![postman](images/postman1.png)
### Get owners and cars authenticated
![postman](images/postman2.png)
### Create owner
![postman](images/postman3.png)

