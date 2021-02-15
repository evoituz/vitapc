from rest_framework.authtoken.models import Token

from apps.users import models as user_models


def account_verification(data):
    phone = data['phone']
    code = data['code']
    user = user_models.User.objects.get(phone=phone)
    if user.code == code:
        user.phone_verified = True
        user.save(update_fields=['phone_verified'])
        token, created = Token.objects.get_or_create(user_id=user.id)
        status = 201 if created else 200
        return {'token': token.key}, status
    return {"message": "Неверный код"}, 404
