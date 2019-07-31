# altpapierBot

Kleines Python 3.6 Script um einen Telegram Reminder für Karton- und Papierabfuhr Daten der Stadt Zürich zu erstellen

## Datengrundlage
Die Abfuhrdaten werden von der [OpenERZ Api](https://www.stadt-zuerich.ch/portal/de/index/ogd/anwendungen/2019/open_erz_api.html)
 bezogen 

## Requirements

Requirements mit [pip](https://pip.pypa.io/en/stable/) installieren

```bash
pip3 install -r requirements.txt
```
[Telegram Bot erstellen und Token erhalten](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token)

[Telegram Chat Id finden](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)


## Konfiguration

Der Bot benutzt Umgebungsvariablen für die Konfiguration.
Diese können entweder via [`.env`-Datei](https://github.com/theskumar/python-dotenv) gesetzt werden oder direkt als Umgebungsvariablen gesetzt werden.

Am besten die Datei `.env.dist` kopieren und anpassen:

```
cp .env.dist .env
# .env editieren für die eigenen Werte
```

Inhalt von `.env.dist`:

```
TELEGRAM_BOT_TOKEN=mein_geheimer_token
TELEGRAM_CHAT_ID=meine_chat_id
ZIP_CODE=8000 # Postleitzahl
```

## Hosting
Bspw. mit
[PythonAnywhere](https://www.pythonanywhere.com)
