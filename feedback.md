# Feedback
Bij het uitvoeren van de eerste laag ontstaan er problemen. 
De configuratie moet per omgeving ingesteld worden, dat is anzich niet het probleem.
Maar de dependencies zijn niet bekend en de verlading is te traag.
Onderstaande zijn alle feedback puntjes die niet verder gaan dan de eerste verlading.
We gaan een sessie doen om hier doorheen te lopen waarna we een tweede iteratie doen voor opdracht 2.

Momenteel is de opdracht een ___4,5___. 
Als je onderstaande punten op lost, zal dit al een ___7,5___ zijn. 
Lagen 2 en 3 heb je goed gedaan en daar heb ik minimale feedback op.
De visualisatie is prima.

## Verbeterpunten:

- [ ] [1_load_raw.py](1_load_raw.py)    -> download is uitgecommentarieerd -> elke stap moet [idempotent](https://en.wikipedia.org/wiki/Idempotence) zijn zodat je het per stap kan herdraaien
- [ ] loader/[upload.py](loader%2Fupload.py) -> Code smell: `DB_PARAMS` en `schema_name` globals worden direct geinjecteerd -> hierdoor kun je de `PostgresLoader` nooit geïsoleerd gebruiken -> gebruik constructor voor configuratie van object
- [ ] [requirements.txt](requirements.txt) -> Setup: Er is geen requirements.txt -> je moet linksom rechtom laten weten via de readme of conventie hoe iemand de requirements kan installeren!
- [ ] [constants.py](constants.py) -> Setup: `directory` gebruikt een harde waarde naar `/Users/olivier/PycharmProjects/opdracht-2/raw` dit zou ook een relatief pad kunnen zijn zoals `./raw`
- [ ] loader/[download.py](loader%2Fdownload.py) -> Code smell: wat als je een invalide url gebruikt -> dan moet de routine stoppen met een nette foutmelding
- [ ] loader/[download.py](loader%2Fdownload.py) -> Code smell: constants worden direct in de Download class geïnjecteerd -> hierdoor kun je de `Download` nooit geïsoleerd gebruiken
- [ ] loader/[download.py](loader%2Fdownload.py) -> Anti pattern: Bestaande files worden niet opgeruimd -> hierdoor kun je verladen met oude data die niet gedownload is tijdens een fout in de download na een succesvolle verlading -> Als je een laag opnieuw verlaad moet je met een schone lij beginnen in principe wil je dat je acties [idempotent](https://en.wikipedia.org/wiki/Idempotence) zijn 
- [ ] loader/[download.py](loader%2Fdownload.py) -> Anti pattern: regel 31 -> Als een bestand niet gedownload kan worden dan moet de routine stoppen met een foutmelding, anders zou de database verlading gewoon doorgaan terwijl een bronbestand er niet is
- [ ] [1_load_raw.py](1_load_raw.py) -> verladen is traag -> implementeer bulk inserts -> laden duurt nu al langer dan een uur
- [ ] [1_load_raw.py](1_load_raw.py) -> Anti pattern: regel 9 -> `dlf.download_files()` download de bestanden en zou logischer wijze ook de lijst van gedownloade bestanden terug geven, nu worden de gedownloade bestanden weer opnieuw uitgelezen uit alles wat in raw staat -> als je dus handmatig iets toevoegt wordt, wordt dat ook verladen terwijl het niet in de download list staat
