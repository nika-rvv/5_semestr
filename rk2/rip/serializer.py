from rip.models import Language
from rip.models import DevTool
from rest_framework import serializers


class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["id", "name", "year", "lang_dev"]

class DevToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevTool
        fields = ["id", "name_tool"]