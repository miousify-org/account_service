from django.http import HttpResponse, HttpRequest, Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from ..models import MStore
from ..utility.miousify_tower import start_trial_server_for_store, deactivate_server, activate_server


def _get_store(request: HttpRequest, store_domain):
    # get store details
    store = get_object_or_404(MStore, pk=store_domain);
    return HttpResponse(store.miousify_store_resource_id);


def _update_store(store_name, data):
    pass


def _activate_store(request: HttpRequest, store_domain):
    store = get_object_or_404(MStore, pk=store_domain);

    plan= store.plan
    store_resource_id= store.miousify_store_resource_id
    miousify_domain_name= store.miousify_domain_name

    pass


def _deactivate_store(request: HttpRequest, store_domain):
    pass


def _start_trial(request: HttpRequest, store_domain):
    # start trial here
    store = get_object_or_404(MStore, pk=store_domain);

    pass

def _delete_store(request: HttpRequest, store_domain):

    store = get_object_or_404(MStore, pk= store_domain);

    store_resource_id= store.miousify_store_resource_id;

    # check permission in token
    pass

def _login(request: HttpRequest):

    miousify_domain_name= request.POST.get("miousify_domain_name");
    password= request.POST.get("password");

    store = get_object_or_404(MStore, pk= miousify_domain_name);

    check= check_password(password=password, encoded=store.password)

    if check is True:
        # generate access token

        payload = {
                "miousify_domain_name": store.miousify_domain_name,
                "email": store.email,
                "miousify_store_resource_id": store.miousify_store_resource_id,
            "isValid": True
        }



        auth_cert= {
            "miousify_domain_name": store.miousify_domain_name,
            "email": store.email,
            "miousify_store_resource_id":store.miousify_store_resource_id
        }
        return JsonResponse(data=auth_cert);

    print(check);

    return HttpResponse(str(check));

    pass


def _check_domain(request: HttpRequest, domain_name):
    store = get_object_or_404(MStore, pk=domain_name)

    if bool(store.miousify_domain_name) is True:
        return HttpResponse("Exists")
    pass