import pdb

from rest_framework import serializers

from apps.users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'avatar', 'name', 'birthday',
                  'gender', 'city',
                  'phone']

    def create(self, validated_data):
        # TODO: подключить смс-сервис
        validated_data['code'] = '12345'
        return User.objects.create(**validated_data)


class PhoneCodeSerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.CharField()

    def create(self, validated_data):
        """ Для подтверждения смс-кода """
        phone = validated_data['phone']
        code = validated_data['code']
        user = User.objects.get(phone=phone)
        if user.code == code:
            user.phone_verified = True
            user.save(update_fields=['phone_verified'])
            return user
        return {'ok': False}
