# Django rest sms auth

## Requirements

+ Python >= 3.8
+ Django >= 3.0
+ Celery
+ Django rest framework
+ Django-phonenumber-field
 
## General concept
* User type phone number
* Validate and save phone number in a model with code
* Through `celery` send code to phone number via `sms provider`
* User got a code
* User send code with phone number
* Validate and send token