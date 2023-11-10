from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class OmborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ombor
        fields = "__all__"


class MaxsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maxsulot
        fields = "__all__"

class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = "__all__"

class StatistikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistika
        fields = "__all__"

    def validate_mijoz(self, qiymat):
        if qiymat.qarz > 500000:
            raise ValidationError("Mahsulot olib ketishingiz mumkin emas")
        return qiymat