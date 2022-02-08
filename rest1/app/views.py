from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.request import  Request
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# Create your views here.

# @api_view()
# def usersApi(request):
#     users=[{
#         "name":"ashwin",
#         "language":"malayalam"
#     }]
#     return Response(users)

# @api_view(['POST'])
# def addemployees(request):
#     students = forms.employeeform()
#     body = json.loads(students)
#     re = addemployeeSerializer(data=body)
#     if re.is_valid():
#         inst = re.save()
#         res = addemployeeSerializer(inst)
#         return Response(res.data)


# class BuildingCreateView(CreateView):
#     model = Building
#     form_class = BuildingForm
#     success_url = reverse_lazy('results')

#     def form_valid(self, form):
#         resp = super().form_valid(form)
#         form.instance.area = form.length * form.width
#         form.save()
#         return resp
from rest_framework import generics
from app.serializers import BucketlistSerializer
from app.models import Bucketlist


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        # serializer.save()
        serializer = BucketlistSerializer(data=Request.query_params)
        serializer.is_valid(raise_exception=True)

        # Get the model input
        data = serializer.validated_data
        model_input = data["name"]

        # Perform the complex calculations
        complex_result = model_input + "xyz"
        complex_result.save()
        # Return it in your custom format
        # return Response({
        #     "complex_result": complex_result,
        # })

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
