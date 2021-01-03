from rest_framework import serializers
from webapp.models import show


class showfetch(serializers.ModelSerializer):
    
    class Meta:
        model = show
        fields =  [f.name for f in show._meta.get_fields()]

