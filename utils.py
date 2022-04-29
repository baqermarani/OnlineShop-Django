from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin




def send_otp(phone_number, code):
    try:
        api = KavenegarAPI('6E36756B314E5948676939382F3974684370394E54504569497565574A5839475A44586C4D646E627459553D')
        params = {
            'sender': '',  # optional
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message': f'کد تایید شما : {code}',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)



class IsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin