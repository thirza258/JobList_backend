from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job, Requirement
from .serializers import JobSerializers, RequirementSerializers
import json

# Create your views here.
class JobList(APIView):
    def get(self, request):
        try :
            data = []
            job_model = Job.objects.all()
            for job in job_model:
                job_serializer = JobSerializers(job).data
                requirement_model = Requirement.objects.filter(job=job)
                requirement_serializer = RequirementSerializers(requirement_model, many=True).data
                job_serializer['requirements'] = requirement_serializer
                data.append(job_serializer)
            
            response_data = {
                "status": status.HTTP_200_OK,
                "message": "Success",
                "data": data
            }

            json_data = json.dumps(response_data)

            with open('app/src/main/res/raw/data.json', 'w') as json_file:
                json_file.write(json_data)

            return Response(response_data, status=status.HTTP_200_OK)
        except:
            response_data = {
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "Internal Server Error",
                "data": []
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)