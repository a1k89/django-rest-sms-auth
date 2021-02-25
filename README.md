# Django rest sms auth

* Authentication users in Django through SMS code
* Change user phone nuber

## Requirements

+ Python >= 3.0
+ Django >= 2.0
+ Celery
+ Djangorestframework
+ Django-phonenumber-field
 
## Concept
1. Client side send phone number (web/ios/android)
2. `smsauth` validate phone number and create `sms code` with life time
3. `smsauth` send `sms code` (through `sms provider`)
4.  User got `sms code`. Send it
5.  `smsauth` validate `{sms code + phone number}`
6.  Send to client info (`jwt token`)

## Notes
* Library use `celery`. [Instruction](https://github.com/a1k89/blog/wiki/Make-django-asynchronous-through-celery)
* To use `twilio` install [extra library](https://www.twilio.com/docs/libraries/python)
* You may add your own provider inherit from `SMSProvider`

## Installation
```commandline
pip install django-rest-sms-auth
```
If you want to use `twilio`:
```commandline
pip install twilio
```

`settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'sms_auth',  # you have to add this
    'sms_auth.providers.twilio' # if twilio provider
    'sms_auth.providers.megafon' # if megafon provider
]

SMS_AUTH_SETTINGS = {
    "SMS_CELERY_FILE_NAME": "run_celery", # your system celery file,
    "SMS_AUTH_SUCCESS_KEY": "jwt_token", # property from user model
    "SMS_AUTH_PROVIDER_FROM": "ex: +7542222222", # sms signature
    
    # If twilio
    "SMS_AUTH_ACCOUNT_SID": "Twilio SID"
    "SMS_AUTH_AUTH_TOKEN": "Twilio token"
    
    # If another provider
    "SMS_AUTH_PROVIDER_LOGIN":"SMS provider login"
    "SMS_AUTH_PROVIDER_PASSWORD": "SMS provider password"
}
```

Add `celery` configuration file:  [Instruction](https://github.com/a1k89/blog/wiki/Make-django-asynchronous-through-celery)

run migrations:
```python
python manage.py makemigrations sms_auth && python manage.py migrate
```
`urls.py`
```python
path('auth/', include('sms_auth.api.urls'))
```

Library is ready to use.

## Usage
1. Sign-in / sign-up:
```command
POST /auth/sign-in/
body: {
    "phone_number":"user phone number"
}
result: 200/400 response
```
2. Code validation and get token:
```command
POST /auth/auth/
body: {
    "phone_number":"user phone number",
    "code":sms_code
}
result: 200/400 response (with token)
```

3. Change phone number:
```command
POST /auth/change-phonenumber/
body: {
    "new_phone_number":"user new phone number"
}
result: 200/400 response
```

## Extra
To clear all expired sms codes
```python
python manage.py clear_expired
```
Additional settings:
```
"SMS_AUTH_CODE_LEN": int (default: 4)
"SMS_DEBUG": bool (default: False)
"SMS_DEBUG_CODE": int (when debug, default 1111)
"SMS_USER_FIELD": "username" 
"SMS_TIMELIFE": 60 # life time of each sms code
"SMS_CODE_NOT_FOUND": "Some text when code not found"
"SMS_WAIT_TIME": "Some text when sms was sended"
"SMS_REQUEST_SUCCESS": "Some text when success phone validatioin and sms sended to user"
```