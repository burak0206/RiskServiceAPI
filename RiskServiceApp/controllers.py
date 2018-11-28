from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt

import datetime
import json

from RiskServiceApp.services import LogPopulateService
from RiskServiceApp.services import GettingRiskValuesService


def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')


def is_user_known(request):
    if request.method == 'GET':
        try:
            username = request.GET.get("username")
            getting_risk_values_service = GettingRiskValuesService()
            result = getting_risk_values_service.is_user_known(username)
            response = json.dumps([{ 'Is User Known?': result }])
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


def is_client_known(request):
    if request.method == 'GET':
        try:
            clientid = request.GET.get("clientid")
            getting_risk_values_service = GettingRiskValuesService()
            result = getting_risk_values_service.is_client_known(clientid)
            response = json.dumps([{'Is ClientID Known?': result}])
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


def is_ip_known(request):
    if request.method == 'GET':
        try:
            ip = request.GET.get("ip")
            getting_risk_values_service = GettingRiskValuesService()
            result = getting_risk_values_service.is_ip_known(ip)
            response = json.dumps([{'Is IP Known?': result}])
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


def is_ip_internal(request):
    if request.method == 'GET':
        try:
            ip = request.GET.get("ip")
            getting_risk_values_service = GettingRiskValuesService()
            result = getting_risk_values_service.is_ip_internal(ip)
            response = json.dumps([{'Is IP Internal?': result}])
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


def get_last_successful_login_date(request):
    if request.method == 'GET':
        try:
            username = request.GET.get("username")
            getting_risk_values_service = GettingRiskValuesService()
            date_time = getting_risk_values_service.get_last_successful_login_date_by_username(username)
            if date_time is None:
                response = json.dumps([{'Error': 'User has not never logged'}])
            else:
                response = json.dumps([{'datetime': date_time}], cls=DjangoJSONEncoder)
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


def get_last_failed_login_date(request):
    if request.method == 'GET':
        try:
            username = request.GET.get("username")
            getting_risk_values_service = GettingRiskValuesService()
            date_time = getting_risk_values_service.get_last_failed_login_date_by_username(username)
            if date_time is None:
                response = json.dumps([{'Error': 'There is no that User can not login'}])
            else:
                response = json.dumps([{'datetime': date_time}], cls=DjangoJSONEncoder)
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


def get_failed_login_count_lastweek(request):
    if request.method == 'GET':
        try:
            number_of_weeks = 1
            if 'weeks' in request.GET:
                number_of_weeks = request.GET.get("weeks")
            getting_risk_values_service = GettingRiskValuesService()
            count = getting_risk_values_service.failed_login_count_last_week(number_of_weeks)
            response = json.dumps([{ 'count': count}])
        except:
            response = json.dumps([{ 'Error': 'No person with that name'}])
    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def log(request):
    if request.method == 'POST' and request.FILES['logfile']:
        logfile = request.FILES['logfile']
        log_populate_service = LogPopulateService();
        log_populate_service.populate_log_into_risk_values_model(logfile)
        response = json.dumps([{'Success': "Risk Values are changed"}])
    return HttpResponse(response, content_type='text/json')