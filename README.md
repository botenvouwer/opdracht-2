# Opdracht 2
In deze opdracht gaan we door op de python en SQL kennis die opgebouwd is.
Alleen er is wel een verschil.
We gaan gebruikmaken van een oefen dataset.
In deze opdracht gaan we weer net als in opdracht 1 terug in het diepe.
Wij verwachten dat je komende twee weken investeert in de uitvoering.
Je python niveau is goed genoeg om deze opdracht uit te voeren, maar je zal enkele nieuwe dingen moeten bijleren.
Wij gaan er in eerste instantie vanuit dat je dit zelfstandig en autonoom kan uitvoeren.
William is beschikbaar voor vragen en als je er niet uitkomt kunnen we iets mer zijwieltjes plaatsen.

# Waarom
Als data-analist kom je terecht in verschillende domeinen met hun eigen entiteiten. 
Hierin zal je zelfstandig je weg moeten kunnen vinden door alle basis competenties toe te passen.

# Wat
We hebben een test dataset van [Adventure Works](https://github.com/sfrechette/adventureworks-neo4j/tree/master/data).
Deze gaan we gebruiken in een fictief scenario.
Jij bent ingehuurd om de data van Adventure Works (AW) in kaart te brengen.
AW heeft de volgende business questions waar zij graag antwoord op willen:

1. Wat zijn de top 3 producten die wij per maand verkopen;
2. Welke medewerker verkoopt per jaar de meeste producten;
3. Een top 10 van welke klanten de meeste bestellingen gedaan hebben;
4. Een top 10 van welke klanten overall de meeste producten gekocht hebben;
5. Een top 10 van welke klanten overall de hoogste opbrengsten gegenereerd hebben.

## Uitgangspunten
Tijdens deze opdracht zijn de volgende uitgangspunten van toepassing:

* Er wordt gewerkt vanuit deze repo (we zetten een nieuw project op);
* Er wordt gewerkt vanuit vooraf aangegeven volgorde in de daarbij behorende files;
* Code mag hergebruikt worden op gekopieerd uit andere bronnen;
* Python code is OOP;
* Python code is CLEAN CODE;
* Python code is SOLID;
* Eerste verlading wordt gedaan vanuit python _**zonder gebruik te maken van kant en klare frameworks zoals panda's**_;
* Tweede verlading wordt gedaan via SQL;
* Analyse wordt gedaan door zowel SQL als panda's;
* Visualisatie wordt gedaan in een jupiter notebook door gebruik te maken van een zelf gekozen framework.

## Tijdsduur
We gaan ervan uit dat deze opdracht in twee weken afgerond is.
Wij zetten een opleverdatum in je agenda.

# Hoe
Wij gaan ervan uit dat we python maatwerk nodig hebben om de data te verladen.
We gaan de ETL-cyclus in combinatie met Crisp-DM een paar keer itereren.
William speelt fictief als vertegenwoordiger van AW.

_Zijwieltjes (we gaan je niet helemaal in het diepe gooien):_

1. Maak een postgres database met drie lagen (lees schema's);
   1. `raw`
   2. `domain`
   3. `models`
2. Eerst moet de [data](https://github.com/sfrechette/adventureworks-neo4j/tree/master/data) van AW verladen worden naar de `raw`;
   1. Gebruik eerder verworven python kennis om de raw laag op te bouwen vanuit python;
   2. De bestanden moeten worden gedownload uit github door gebruik te maken van de raw file url.
      1. In github ga naar het bestand en klik op RAW rechtsbovenin!;
      2. Je kan zelf uitzoeken hoe je in python bestanden kan download van internet;
      3. Je plaatst de bestanden in een lokale cache om er mee te werken, deze noemen we `raw` directory;
3. Daarna moet de ruwe data geanalyseerd worden en verladen naar een coherent datamodel;
   1. Gebruik het template ([2_analyse_domain_model.xlsx](2_analyse_domain_model.xlsx)) om elke entiteit te analyseren;
   2. Haal alle entiteiten die je nodig hebt uit de `raw` laag en verlaad ze naar de `domain` laag;
   3. In het `domain` hebben alle velden het datatype wat bij hun eigenschappen hoort (dus een datum is ook echt een DATETIME of TIMESTAMP);
   4. In het `domain` bestaan alleen de entiteiten die we nodig hebben;
   5. In het `domain` is de data genormaliseerd en coherent.
      1. bijvoorbeeld alle primary keys zijn van hetzelfde type;
      2. bijvoorbeeld alle datums hanteren hetzelfde formaat;
      3. bijvoorbeeld alle financiële getallen zijn van het type FLOAT;
      4. etc.
4. Als we een coherent datamodel in `domain` hebben kunnen we onze business questions gaan modelleren in de `models` laag;
   1. In deze laag kun je tussenresultaten opslaan op basis van de data uit `domain`, maar het mogen ook views zijn.
5. Als laatste stap maken we visualisaties op onze modellen.
   1. Voor nu maken we deze in een jupiter notebook;
   2. Kies voor elke business question een geschikte visualisatie die past bij het informatie type;
   3. Gebruik een zelfgekozen framework zoals `Matplotlib` of `Seaborn`.
