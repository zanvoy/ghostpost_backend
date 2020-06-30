from api_app.models import Broast
from rest_framework.serializers import ModelSerializer

class BroastSerializer(ModelSerializer):
    class Meta:
        model = Broast
        fields = ('up','down','is_roast','content','score','date','id')
