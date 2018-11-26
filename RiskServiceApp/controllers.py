from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt

import json
import datetime

from RiskServiceApp.services import LogPopulateService
from RiskServiceApp.services import GettingRiskValuesService


def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')


def is_user_known(request):
    if request.method == 'GET':
        try:
            username = request.GET.get("username")
            if (username == "UserA"):
                response = json.dumps([{ 'Is User Known?': True }])
            else:
                response = json.dumps([{'Is User Known?': False}])
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


def is_client_known(request):
    if request.method == 'GET':
        try:
            clientid = request.GET.get("clientid")
            if (clientid == "fe80::84c:15f9:f9f5:12c3"):
                response = json.dumps([{ 'Is Client Known?': True }])
            else:
                response = json.dumps([{'Is Client Known?': False}])
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


def is_ip_known(request):
    if request.method == 'GET':
        try:
            ip = request.GET.get("ip")
            if (ip == "192.168.101.5"):
                response = json.dumps([{'Is IP Known?': True}])
            else:
                response = json.dumps([{'Is IP Known?': False}])
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


def is_ip_internal(request):
    if request.method == 'GET':
        try:
            ip = request.GET.get("ip")
            if (ip == "192.168.101.5"):
                response = json.dumps([{'Is IP Internal?': True}])
            else:
                response = json.dumps([{'Is IP Internal?': False}])
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


def get_last_successful_login_date(request):
    if request.method == 'GET':
        try:
            date_time = datetime.datetime.now()
            response = json.dumps([{'datetime': date_time}], cls=DjangoJSONEncoder)
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


def get_last_failed_login_date(request):
    if request.method == 'GET':
        try:
            date_time = datetime.datetime.now()
            response = json.dumps([{'datetime': date_time}], cls=DjangoJSONEncoder)
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


def get_failed_login_count_lastweek(request):
    if request.method == 'GET':
        try:
            response = json.dumps([{ 'count': 4}])
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def log(request):
    if request.method == 'POST' and request.FILES['logfile']:
        logfile = request.FILES['logfile']
        log_populate_service = LogPopulateService();
        log_populate_service.populate_log_into_risk_values_model(logfile)
        #log_service.print_logs()
        log_populate_service.handle_uploaded_file()
        getting_risk_values_service = GettingRiskValuesService()
        getting_risk_values_service.handle_uploaded_file()
        response = json.dumps([{'Success': "Risk Values are changed"}])
    return HttpResponse(response, content_type='text/json')