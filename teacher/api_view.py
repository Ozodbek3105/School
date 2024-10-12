from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from teacher.models import Teacher
from teacher.serializer import ProfessorSer


class ProfessorsAPIView(APIView):
    def get(self, request, *args,):
        print(request.query_params)
        print(request.data)
        data = Teacher.objects.all()
        print(data)
        ser = ProfessorSer(data, many=True)
        return Response(ser.data)
    
    def post(self, request):
        ser = ProfessorSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
    def patch(self, request, *args, **kwargs):
        print('this is patch')
        print(request.data) # Wrong
        print(kwargs, args, kwargs.get('pk')) # Wrong
        print(request.query_params.get('pk')) # Right
        data = request.data
        teacher = Teacher.objects.get(pk=request.query_params.get("pk"))
        ser = ProfessorSer(teacher, data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    

class ProfessorAPIView(APIView):
    def get(self, request, pk) -> Response:
        teacher = Teacher.objects.get(pk=pk)
        ser = ProfessorSer(teacher)
        return Response(ser.data)


class ProfessorViewset(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = ProfessorSer
    pagination_class = PageNumberPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["first_name", 'last_name']
