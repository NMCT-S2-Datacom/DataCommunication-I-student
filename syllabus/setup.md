# 1) Overzicht
- Maak een directory voor je project op de RPi
- Maak **in die directory** een python3 virtual environment
- Fork je repo m.b.v. GitHub Classroom
- Clone het repo via PyCharm in een nieuw project
- Voeg een remote *upstream* toe die jouw fork linkt met het master-repo
- Stel een Deployment Configuration in om je code te uploaden naar de Pi
- Stel een Remote Interpreter in om je code op de Pi te draaien
- Schakel voor het gemak Automatic Uploads in 

# 1) Raspberry Pi
- maak verbinding via SSH (PuTTY)
- maak een directory `datacom` in je homefolder en ga erin:
```console
tom@rpi-tom:~$ mkdir datacom
tom@rpi-tom:~$ cd datacom
tom@rpi-tom:~/datacom$
```
- maak een python*3* virtual environment aan
```console
tom@rpi-tom:~/datacom$ sudo apt update && sudo apt install -y python3-venv
tom@rpi-tom:~/datacom$ python3 -m pip install --upgrade pip setuptools wheel 
tom@rpi-tom:~/datacom$ python3 -m venv --system-site-packages env
tom@rpi-tom:~/datacom$ ls env/
bin  include  lib  lib64  pyvenv.cfg  share
tom@rpi-tom:~/datacom$
```

# 2) GitHub
- volg de instructies via GitHub Classroom (link: zie LEHO)
- **kies je e-mailadres uit de lijst!**

# 3) PyCharm:
## a) git 
*Is normaalgezien al geïnstalleerd van bij Basic Programming, maar als PyCharm klaagt over git.exe:* 
- download & install: <https://git-scm.com/downloads> 
- ga naar `File > Settings > Version Control > Git` **(Git != GitHub!)**
- Vul het pad naar git.exe in (standaard `C:\Program Files\Git\bin\git.exe`, 
of gebruik de `...`-knop om te bladeren) + OK

## b) clone repo -> PyCharm project
- ga naar `VCS > Checkout from Version Control > GitHub`
- als je **nog geen** token hebt, klik dan op `Generate API token` en geef je user/pass van GitHub in + OK
- kies uit de lijst: *datacommunication-1-*\<username>*.git*
- kies een geschikte plaats voor het project op je harde schijf ("Parent directory")

## c) remotes
Om elke week nieuw materiaal te kunnen binnentrekken moet je jouw repo 
linken aan het "master" repo:
- ga naar `VCS > Git > Remotes... `
- voeg een remote toe met `+` en **neem letterlijk over**:
	- Name: **upstream**
	- URL: **https://github.com/NMCT-S2-DataCom1/DataCommunication-I-student.git**
- test of het werkt: `VCS > Git > Rebase my GitHub fork` (als je net pas je fork gemaakt hebt, zal er niets wijzigen, maar je zou alleszins geen fout mogen krijgen)

## d) deployment config
*Als je een goede deployment config hebt van week 1, kan je die recycleren. Check wel de settings, tabblad Mappings* 
- Ga naar `File > Settings` en dan `Build Execution, Deployment > Deployment`
- Voeg een toe met `+`, geef een naam (bv. RPi-APIPA) en kies type `SFTP`
- Vink 'Visible only for this project' **af**
- Type: moet `SFTP` zijn
- Geef hostname of IP, user+password in en vink 'Save password' aan
- Klik 'Test SFTP Connection'
- Klik 'Autodetect' er net onder

**Belangrijk om te checken ook als je een werkende config recycleert:**
- Ga naar tabblad *Mappings*
- Deployment path on server: `/datacom`
- Zet deze config als default: bladje met groen vinkje --> naam wordt vetgedrukt
- Klik *Apply* voor je naar de volgende stap gaat

## Remote interpreter
- Ga naar Project: datacommunication-1-... > Project Interpreter

### Als je die van week 1 recycleert:

**Check dubbel dat alles zeker juist is!**
- Versie (3.5.x)
- remote: user@host
- pad naar python moet verwijzen naar virtual environment

Bv.: `Remote Python 3.5.3 (sftp://tom@169.254.10.1:22/home/tom/datacom/env/bin/python)`

**Check dat het veld 'Path Mappings' aanwezig en ingevuld is!!!** 
- GOED (bv.): `<project root> --> /home/tom/datacom`
- NIET GOED: `(Empty)`


NB: De "Deployment Config" waarop je "Remote Interpreter" gebaseerd is **moet** dezelfde 
zijn als diegene die voor het project is geconfigureerd, anders werkt het niet!
Hou dus geen hoop nutteloze kopieën van je Deployment Config bij!

In geval van twijfel: verwijderen en opnieuw beginnen

### Om een te verwijderen of aan te passen:
- Klik tandwieltje > More... (of Show All in nieuwste versie)
- Klik +, - of potloodje al naargelang

### Om een nieuwe toe te voegen:
- Tandwieltje --> 'Add Remote...'
- Kies **dezelfde deployment config** als diegene die je daarnet hebt ingesteld
- Pas Remote Interpreter Path aan naar je Virtual Environment!
*dus bv. /home/tome/datacom/env en **NIET** /usr/bin/python*!!

Bevestig tenslotte alles met OK

### Automatic upload naar de RPi
*Als je hier porblemen mee hebt is je deployment config ofwel niet juist, ofwel **niet als default ingesteld***!
- Ga naar (menu) `Tools > Deployment > Options`
- Kies ongeveer in het midden 'Always' i.p.v. 'Never' uit het drop-downmenu
- Nieuwe bestanden moet de je de eerste keer wel nog steeds manueel uploaden, daarom: 
- Rechterklik op project root directory > 'Upload to RPi-APIPA' (of whatever de naam van je deployment config is)

