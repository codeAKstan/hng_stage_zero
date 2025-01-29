from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
# Create your views here.


def get_info(request):
    response = {
        "email": "anigbomosesstan@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/codeAKstan/hng_stage_zero.git"
    }
    return JsonResponse(response)