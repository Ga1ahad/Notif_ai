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
- username (max_length=160)
- password(max_length=128, hash)


## Widoki
| URL  | Metoda HTTP | Żądanie HTTP | Opis |
| ------------- | ------------- | ------------- | ------------- |
| https://notif-ai-app-daftcode.herokuapp.com/auth/register/  | POST | {     "username": "str",     "password": "str" } | Żądanie tworzy nowego użytkownika i zwraca jego login i id |
| https://notif-ai-app-daftcode.herokuapp.com/auth/token/  | POST | {     "username": "str",     "password": "str" } | Żądanie zwraca token |
| https://notif-ai-app-daftcode.herokuapp.com/messages  | GET | nie dotyczy | Żądanie tworzy nowego użytkownika i zwraca jego login i id |
| https://notif-ai-app-daftcode.herokuapp.com/messages  | POST | {     "body": "str" } | Żądanie towrzy nową wiadmomość, wymagane jest podanie tokena. |
| https://notif-ai-app-daftcode.herokuapp.com/messages/<int:message_id>  | GET | nie dotyczy | Żądanie zwraca treść wiadomości i liczbę wyświetleń. |
| https://notif-ai-app-daftcode.herokuapp.com/messages/<int:message_id>  | POST | {     "body": "str" } | Żądanie tworzy nową wiadmomość, wymagane jest podanie tokena. |
| https://notif-ai-app-daftcode.herokuapp.com/messages/<int:message_id>  | PUT | {     "body": "str" } | Żądanie aktulizuje treść wiadomości i resetuje liczbę wyświetleń, wymagane jest podanie tokena. |
| https://notif-ai-app-daftcode.herokuapp.com/messages/<int:message_id>  | DELETE | nie dotyczy | Żądanie usuwa wiadomość, wymagane jest podanie tokena. |

## Deployment 

API zostało postwione na Heroku.

