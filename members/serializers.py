


from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    # We define password separately to ensure it's write-only
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'profile_image', 'gender', 'country', 'city')

    def create(self, validated_data):
        # We pop the profile_image if it exists to pass it into create_user
        profile_image = validated_data.pop('profile_image', None)
        
        # Use the manager method you created earlier
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            profile_image=profile_image,
            gender=validated_data.get('gender', 'Prefer not to say'),
            country=validated_data.get('country', None),
            city=validated_data.get('city', None)
        )
        return user