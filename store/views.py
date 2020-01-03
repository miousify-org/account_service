from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .utility.miousify_store_resource import create_store_and_commit
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password
from .models import MStore


# Create your views_unit here.

def stores_route(request: HttpRequest):
    if request.method == "GET":
        print("aobut to get soters")
        return stores_get(request)
        pass
    elif request.method == "POST":
        print("create store request")
        return stores_post(request)
        pass
    pass


def stores_post(request: HttpRequest):
    # create store
    password = None
    email = None;
    miousify_domain_name = None

    try:
        password = request.POST['password']
    except Exception as ex:
        raise ex;
        respone = HttpResponse("Password needed");
        respone.status_code(400);
    try:
        email = request.POST['email']
    except Exception as ex:
        raise ex;
        respone = HttpResponse("Email needed");
        respone.status_code(400);
        return HttpResponse();

    try:
        miousify_domain_name = request.POST['miousify_domain_name']
    except Exception as ex:
        respone = HttpResponse("miousify_domain_name needed");
        respone.status_code = 400;
        raise ex;

    hashed_password = make_password(password=password);

    # don't implement yet
    phone = request.POST.get('phone');

    try:
        domain = MStore.objects.get(miousify_domain_name=miousify_domain_name);
        response = HttpResponse("Store aleady exists");
        respone.status_code=403
        return respone;
        pass
    except ObjectDoesNotExist:
        print("Expected Exception Can creat store")
        pass

    # check if store with domain name already exist
    try:
        created_store = create_store_and_commit(email=email, miousify_domain_name=miousify_domain_name, phone=phone,
                                                password=hashed_password);
        if created_store is True:
            print("Created successfully");
            return HttpResponse("created");
        else:
            respone = JsonResponse(data=False)
            respone.status_code = 500
            return respone
        pass
    except Exception as exceptio:
        raise exceptio;
        response = HttpResponse("did not create store successfully try again or contact supports")
        response.status_code = 500
        return response


def stores_get(request: HttpRequest):
    # get stores list
    stores = []
    try:
        stores = MStore.objects.all();
    except Exception:
        print("no stores available")
        return HttpResponse("no stores available")

    return JsonResponse(data=stores.count(), safe=False);
    pass
