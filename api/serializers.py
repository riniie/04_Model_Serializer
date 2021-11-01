from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    # Validators
    def starts_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name must start with r!')

    name = serializers.CharField(max_length=50, validators=[starts_with_r])

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

    # Field Level Validation
    def validate_roll(self, roll):
        if roll > 100:
            raise serializers.ValidationError('Seat Full')
        return roll

    # Object Level Validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'nina' and city != 'LA':
            raise serializers.ValidationError('Nina must live in LA')
        return data
