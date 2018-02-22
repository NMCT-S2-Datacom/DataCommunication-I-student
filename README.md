# DataCommunication I

## Inhoud
- [syllabus](datacom): uitleg & schema's die je nodig hebt voor de practica
- [datacom](datacom): jouw werkmap. Tegen het eind van het semester is dit een library met componenten 
die je kan importeren in jouw projecten. 
- [oefeningen](oefeningen): kleine oefeningen op binair rekenen, etc - voor thuis, of als je klaar 
bent met het practicum. 
- [test](test): unit tests die je kan gebruiken om jouw oplossingen te testen. **In deze directory niets wijzigen!**

## Configuratie (enkel 1e keer)

*Zie ook [setup](syllabus/setup.md) voor een meer uitgebreide versie!*

Maak eerst jouw eigen "fork" in GitHub classroom (zie link op LEHO)

Via console (git bash):
```console
git clone https://github.com/NMCT-S2-DataCom1/datacommunication-1-<user> DataCommunication-1
cd DataCommunication-1
git remote add upstream https://github.com/NMCT-S2-DataCom1/DataCommunication-I-student.git
```
*vervang <user> door jouw GitHub-username*

Of via PyCharm:
- `VCS > Checkout from Version Control > GitHub...`
- Kies jouw repository uit de lijst en pas eventueel de lokale directory (Parent directory) aan.
- Ga naar `VCS > Git > Remotes...`
- Voeg een remote toe (+) (let op: de beide **letterlijk** over te nemen, anders werkt het niet!)
  - naam: **upstream**
  - URL: **https://github.com/NMCT-S2-DataCom1/DataCommunication-I-student.git**
- Bevestig met OK

**Daarna moet je nog Deployment Config & Remote Interpreter instellen voor het nieuwe project!**
(zie document week01 op LEHO)

## Updaten (elke week)
Via console (git bash):
```console
cd DataCommunication-1
git fetch upstream
git rebase upstream/master
git push origin/master
```

Of via PyCharm:
- `VCS > Git > Rebase my GitHub fork`
- `VCS > Git > Push...`

