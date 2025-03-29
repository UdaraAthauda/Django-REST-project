from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets

# Create your views here.

def index(request):
    students = Student.objects.all()
    employees = Employee.objects.all()

    context = {'students': students, 'employees': employees}
    return render(request, 'index.html', context=context)

# # function based API view
# @api_view(['GET'])
# def studentView(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# using REST_Framework mixins get and create details
class studentView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
# using REST_Framework mixins retrieve, edit and delete details
class studentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)

'''
# class based views - REST APIView
class Employees(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''   
    
# using generics operations get and create
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# using generics operations retrieve, update and delete
class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'


# using viewsets that handle all CRUD operation
class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer 