# Overzicht
- Maak een directory voor je project op de RPi
- Maak **in die directory** een python3 virtual environment
- Fork je repo m.b.v. GitHub Classroom
- Clone het repo via PyCharm in een nieuw project
- Voeg een remote *upstream* toe die jouw fork linkt met het master-repo
- Stel een Deployment Configuration in om je code te uploaden naar de Pi
- Stel een Remote Interpreter in om je code op de Pi te draaien
- Schakel voor het gemak Automatic Uploads in 

---

# 0. Prerequisites
Een unieke hostname:
```console
pi@raspberrypi:~$ sudo raspi-config nonint do_hostname my-rpi
pi@raspberrypi:~$ sudo reboot
```
Een eigen user: 
- maak een variabele met de gewenste gebruikersnaam
  ```console
  pi@my-rpi:~$ user=me 	
  ```
- copy & paste magic:
  ```bash
  groups=$(id pi -Gn | sed 's/^pi //g' | sed 's/ /,/g')
  sudo useradd ${user} -s /bin/bash -m -G ${groups}
  sudo sed "s/^pi/${user}/" /etc/sudoers.d/010_pi-nopasswd | sudo tee "/etc/sudoers.d/011_${user}-nopasswd"
  sudo passwd ${user}
  ```
- log in:
  ```console
  pi@my-rpi:~$ su - me
  Password:
  me@my-rpi:~$ 
  ```
Verbonden met WiFi:
```console
me@my-rpi:~$ wpa_passphrase 'NMCT-rPI' '--zie LEHO--' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf
me@my-rpi:~$ wpa_cli -i wlan0 reconfigure
```
Internet werkt:
```console
me@my-rpi:~$ wget google.com
--2018-02-22 21:46:20--  http://google.com/
Resolving google.com (google.com)... 172.217.17.110, 2a00:1450:400e:808::200e
Connecting to google.com (google.com)|172.217.17.110|:80... connected.
HTTP request sent, awaiting response... 302 Found
Location: http://www.google.be/?gfe_rd=cr&dcr=0&ei=rCyPWq-uOK3c8Ae-wqyoBw [following]
--2018-02-22 21:46:20--  http://www.google.be/?gfe_rd=cr&dcr=0&ei=rCyPWq-uOK3c8Ae-wqyoBw
Resolving www.google.be (www.google.be)... 216.58.212.227, 2a00:1450:400e:803::2003
Connecting to www.google.be (www.google.be)|216.58.212.227|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: 'index.html'

index.html                        [ <=>                                              ]  12.89K  --.-KB/s    in 0s

2018-02-22 21:46:20 (28.2 MB/s) - 'index.html' saved [13200]
me@my-rpi:~$ 
```
Up-to-date:
```console
me@my-rpi:~$ sudo apt update
me@my-rpi:~$ sudo apt full-upgrade -y
me@my-rpi:~$ sudo reboot
```
# 1. Raspberry Pi
- maak een directory `datacom` in je homefolder en ga erheen:
```console
me@my-rpi:~$ mkdir datacom
me@my-rpi:~$ cd datacom
me@my-rpi:~/datacom$
```
- maak een python*3* virtual environment aan
```console
me@my-rpi:~/datacom$ sudo apt update && sudo apt install -y python3-venv
me@my-rpi:~/datacom$ python3 -m pip install --upgrade pip setuptools wheel 
me@my-rpi:~/datacom$ python3 -m venv --system-site-packages env
me@my-rpi:~/datacom$ ls env/
bin  include  lib  lib64  pyvenv.cfg  share
me@my-rpi:~/datacom$
```

# 2. GitHub
Maak een eigen fork van <https://github.com/NMCT-S2-DataCom1/DataCommunication-I-student.git> om in te werken:
- volg de instructies via GitHub Classroom (link: zie LEHO)
- **kies je e-mailadres uit de lijst!**
- er wordt een private fork in https://github.com/NMCT-S2-DataCom1 gemaakt die enkel jij kan zien

*NB: enkel commits in dit repository kunnen mee geëvalueerd worden!*

# 3. PyCharm:
## a) git 
Is normaalgezien al geïnstalleerd van bij Basic Programming, maar als PyCharm klaagt over git.exe:
- download & install: <https://git-scm.com/downloads> 
- ga naar `File > Settings > Version Control > Git` **(Git != GitHub!)**
- Vul het pad naar git.exe in (standaard `C:\Program Files\Git\bin\git.exe`, 
of gebruik de `...`-knop om te bladeren) + OK

## b) clone repo -> PyCharm project
- ga naar `VCS > Checkout from Version Control > GitHub`
- als je **nog geen** token hebt, klik dan op `Generate API token` en geef je user/pass van GitHub in + OK
- kies uit de lijst: *https://github.com/NMCT-S2-DataCom1/datacommunication-1-*<username>*.git*
- kies een geschikte plaats voor het project op je harde schijf ("Parent directory")

## c) git remotes
Om elke week nieuw materiaal te kunnen binnentrekken moet je in de lokale git-config jouw repo nog aan het master-repo linken:
- ga naar `VCS > Git > Remotes... `
- voeg een remote toe met `+` en **neem letterlijk over**:
	- Name: **upstream**
	- URL: **https://github.com/NMCT-S2-DataCom1/DataCommunication-I-student.git**
- test of het werkt: `VCS > Git > Rebase my GitHub fork` (als je net pas je fork gemaakt hebt, zal er niets wijzigen, maar je zou alleszins geen fout mogen krijgen)

## d) deployment config
Als je een goede deployment config hebt van week 1, kan je die recycleren. Check wel de settings, vooral tabblad `Mappings`

- Ga naar `File > Settings` en dan `Build Execution, Deployment > Deployment`
- Voeg een toe met `+`, geef een naam (bv. RPi-APIPA) en kies type `SFTP`
- Vink `Visible only for this project` **af**
- Type: `SFTP` 
- Geef hostname of IP, user+password in en vink 'Save password' aan
- Klik `Test SFTP Connection`
- Klik `Autodetect` er net onder

*Belangrijk om te checken vooral ook **als je een werkende config recycleert:***
- Ga naar tabblad `Mappings`
- Deployment path on server: `/datacom`
- Zet deze config als default: bladje met groen vinkje --> naam wordt vetgedrukt
- Klik `Apply` voor je naar de volgende stap gaat

## e) Remote interpreter
- Ga naar Project: ... > Project Interpreter

*NB: De "Deployment Config" waarop je "Remote Interpreter" gebaseerd is **moet** dezelfde 
zijn als diegene die voor het project is geconfigureerd, anders werkt het niet!
Hou dus geen hoop nutteloze kopieën van je Deployment Config bij!*

### Om een nieuwe toe te voegen:
- *Tandwieltje* --> `Add Remote...`
- Kies **dezelfde** deployment config als diegene die je daarnet hebt ingesteld
- Pas `Remote Interpreter Path` aan naar de python executable **in je Virtual Environment**: `<env-dir>/bin/python`

  bv. `/home/me/datacom/env/bin/python` 
 
  *NB: omdat dit venv met Python3 is aangemaakt, verwijst `python` in die directory ook gewoon naar Python3 - dit in tegenstelling tot `/usr/bin/python`*

### Zeker als je die van week 1 recycleert:
**Check dubbel dat alles zeker juist is:**
- versie: 3.5.x
- remote: user@host
- pad naar python moet verwijzen naar virtual environment in `/home/...` en dus **NIET** `/usr/bin/python`

Bv.: `Remote Python 3.5.3 (sftp://tom@169.254.10.1:22/home/me/datacom/env/bin/python)`

### Check dat het veld `Path Mappings` aanwezig en ingevuld is!** 
- goed: `<project root> --> /home/me/datacom`
- slecht: `(Empty)` of gewoon helemaal niet te zien

### Om een te verwijderen of aan te passen:
- Klik *`tandwieltje`* > `More...` (of Show All in nieuwste versie)
- Klik `+`, `-` of *`potloodje`*, al naargelang

**Check AGAIN dat het veld `Path Mappings` nu aanwezig en ingevuld is!!!** 

## f) Automatic upload naar de RPi
- Ga naar (menu) `Tools > Deployment > Options`
- Kies ongeveer in het midden 'Always' i.p.v. 'Never' uit het drop-downmenu
- Nieuwe bestanden moet de je de eerste keer wel nog steeds manueel uploaden, daarom: 
- Rechterklik op project root directory > 'Upload to RPi-APIPA' (of whatever de naam van je deployment config is)
*Als je hier porblemen mee hebt is je deployment config ofwel niet juist, ofwel misschien gewoon **niet als default ingesteld***!
