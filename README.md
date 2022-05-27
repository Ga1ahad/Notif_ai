# Notif.ai

Zadanie rekrutacyjne notif.ai.

## Użyte technologie
- Django
- Django Rest Framework
- Heroku

## Baza danych:

### Messages
- id
- body (not null, CharField(160))
- views PositiveIntegerField(default=0)


### User
- id
- username
- password


## Widoki
### Rejestracja użytkownika
url: https://notif-ai-app-daftcode.herokuapp.com/register

metoda: POST


pola: username, password

### Uzyskanie tokena
https://notif-ai-app-daftcode.herokuapp.com/token

metoda: POST

pola: username, password

### Podgląd wiadomiści
https://notif-ai-app-daftcode.herokuapp.com/messages/<id>


metoda: GET

argumenty: message.pk
### Dodawanie wiadomiści
https://notif-ai-app-daftcode.herokuapp.com/messages

metoda: POST

pola: username, password


### Edycja wiadomośći
https://notif-ai-app-daftcode.herokuapp.com/messages/<id>

metoda: PUT

argumenty: message.pk

### Usuwanie wiadomośći
https://notif-ai-app-daftcode.herokuapp.com/messages/<id>

metoda: DELETE

argumenty: message.pk

### Lista wiadomości
https://notif-ai-app-daftcode.herokuapp.com/messages

metoda: GET


