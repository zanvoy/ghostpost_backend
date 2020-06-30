from django.shortcuts import render
from api_app.serializers import BroastSerializer
from api_app.models import Broast
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from api_app.forms import BroastForm


class BroastViewSet(ModelViewSet):
    serializer_class = BroastSerializer
    basename = 'broast'
    queryset = Broast.objects.all()

    @action(detail=True,methods=['post'])
    def upvote(self, request, pk):
        target = self.get_object()
        target.up += 1
        target.save()
        return Response({'upvote': target.up})

    @action(detail=True,methods=['post'])
    def downvote(self, request, pk):
        target = self.get_object()
        target.down += 1
        target.save()
        return Response({'downvote': target.down})

    @action(detail=False)  
    def order_best(self, request):
        data = sorted(Broast.objects.all(), key=lambda i: i.score, reverse=True)
        serializer = BroastSerializer(data, many=True)
        return Response(serializer.data)

    @action(detail=False)  
    def order_boast(self, request):
        data = Broast.objects.filter(is_roast=False)
        serializer = BroastSerializer(data, many=True)
        return Response(serializer.data)
        
    @action(detail=False)  
    def order_roast(self, request):
        data = Broast.objects.filter(is_roast=True)
        serializer = BroastSerializer(data, many=True)
        return Response(serializer.data)
    
    @action(detail=False)  
    def order_new(self, request):
        data = Broast.objects.all().order_by('-date')
        serializer = BroastSerializer(data, many=True)
        return Response(serializer.data)

    @action(detail=False)  
    def new_post(self, request):
        
        return Response('')