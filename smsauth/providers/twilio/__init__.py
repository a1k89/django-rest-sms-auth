from ..base import SMSProvider


class Twilio(SMSProvider):
    def send_sms(self):
        from twilio.rest import Client

        client = Client(self.conf.SMS_AUTH_ACCOUNT_SID, self.conf.SMS_AUTH_AUTH_TOKEN)
        message = client.messages.create(
            to=f"{self.to}", from_=self.conf.SMS_PROVIDER_FROM, body=self.message
        )

        return message
