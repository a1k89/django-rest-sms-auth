import requests
import json
import re
import hashlib
from urllib.parse import urljoin

from ..base import SMSProvider

URL = 'http://gate.smsaero.ru/'
TYPE_SEND = 2


class SmsAeroException(Exception):
    pass


class Smsaero(SMSProvider):
    def _request(self, endpoint, data):
        m = hashlib.md5(self.conf.SMS_PROVIDER_PASSWORD.encode())
        passwd = m.hexdigest()
        data.update({
            'from': self.conf.SMS_PROVIDER_FROM,
            'type_send': TYPE_SEND,
            'digital': 0,
            'user': self.conf.SMS_PROVIDER_LOGIN,
            'password': passwd,
            'answer': 'json',
        })

        url = urljoin(URL, endpoint)

        try:
            response = requests.post(url, data=data)
        except Exception:
            raise SmsAeroException('Error send sms')

        if not response.status_code == 200:
            raise Exception('Response status over 200')

        return json.loads(response.text)

    def send_sms(self):
        phone_number = str(self.to).replace( ' ', '' ) \
            .replace( '-', '' ) \
            .replace( '+', '' ) \
            .replace( '(', '' ) \
            .replace( ')', '' )

        match = re.search( '^\+?\d{11}$', phone_number)
        if not match:
            SmsAeroException('Phone number is not valid')
            return

        data = {
            'to': phone_number,
            'text': self.message,
        }

        return self._request('/send/', data)
