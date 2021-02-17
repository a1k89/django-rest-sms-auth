import base64
import ssl

import requests

from ..base import SMSProvider


class Megafon(SMSProvider):
    @property
    def _hash(self):
        hash_byte = base64.b64encode(
            f"{self.conf.SMS_PROVIDER_LOGIN}:{self.conf.SMS_PROVIDER_PASSWORD}".encode(
                "utf-8"
            )
        )
        return str(hash_byte, "utf-8")

    def _prepare_headers(self):
        if hasattr(ssl, "_create_unverified_context"):
            ssl._create_default_https_context = ssl._create_unverified_context

    def send_megafon_sms(self):
        self._prepare_headers()
        req = requests.post(
            self.conf.SMS_PROVIDER_URL,
            json={
                "from": self.conf.SMS_PROVIDER_FROM,
                "to": self.to,
                "message": self.message,
            },
            headers={"Authorization": f"Basic {self._hash}"},
        )

        return req

    def send_sms(self):
        return self.send_megafon_sms()
