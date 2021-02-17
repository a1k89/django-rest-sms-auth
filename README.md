# Django rest sms auth

## Requirements

+ Python >= 3.8
+ Django >= 3.0
+ Celery
+ Django rest framework
+ Django-phonenumber-field
 
## Concept
1. User type phone number
2. `smsauth` validate phone number and create random `sms code`
3. Through `celery` send `sms code` to user at phone number
4. User type `sms code` and send to server
5. Server validate `sms code` + `phone number`
6. Finally, send to client some info (for example, `jwt token`)

## Notes
* Library use `celery` to send sms
* If you want to use `twilio` provider you must to install [extra library](https://www.twilio.com/docs/libraries/python)
* You may add your own provider inherit from `SMSProvider`
* You must provide correct `phone format`. Because library associated phone number with one of field from `User` model. By default: username

## Installation
```commandline
pip install django-rest-sms-auth
```
import by:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'smsauth',  # you have to add this
    'smsauth.providers.twilio' # if twilio provider
    'smsauth.provider.megafon' # if megafon provider
]
```
then:
```python
python manage.py makemigrations smsauth && python manage.py migrate
```
and add endpoints:
```python
path('auth/', include('smsauth.api.urls'))
```
in `settings.py`:
```python
SMS_AUTH_SETTINGS = {
    "SMS_CELERY_FILE_NAME": "run_celery", # your celery file,
    "SMS_AUTH_SUCCESS_KEY": "jwt_token", # property from user model
    
    # If twilio
    "SMS_AUTH_ACCOUNT_SID": "Twilio SID"
    "SMS_AUTH_AUTH_TOKEN": "Twilio token"
    
    # If another provider
    "SMS_AUTH_PROVIDER_LOGIN":"SMS provider login"
    "SMS_AUTH_PROVIDER_PASSWORD": "SMS provider password"
    "SMS_AUTH_PROVIDER_FROM": "ex: +7542222222"
}

Another settings:
"SMS_AUTH_CODE_LEN": int (default: 4)
"SMS_DEBUG": bool (default: False)
"SMS_DEBUG_CODE": int (when debug, default 1111)
"SMS_USER_FIELD": "username" 
"SMS_TIMELIFE": 60 # life time of each sms code
"SMS_CODE_NOT_FOUND": "Some text when code not found"
"SMS_WAIT_TIME": "Some text when sms was sended"
"SMS_REQUEST_SUCCESS": "Some text when success phone validatioin and sms sended to user"
```
Ok. Library installed.

## Usage
1. Sign-in / sign-up:
```command
POST /auth/sign-in/
body: {"phone_number":"user phone number"}
```
2. Code validation and get token:
```command
POST /auth/auth/
body: {"phone_number":"user phone number",
    "code":sms_code
}
```

## Commands
To clear all expired sms codes
```python
python manage.py clear_expired
```