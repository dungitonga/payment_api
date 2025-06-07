from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from .services import paypal

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PayPalViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'], url_path='process')
    def process_payment(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            try:
                result = paypal.process_payment(serializer.validated_data)
                return Response(result, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


