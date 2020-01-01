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
    print("about to create store")
    # create store
    password = request.POST.get('password')
    hashed_password = make_password(password=password);
    # don't implement yet
    email = request.POST.get('email');
    phone = request.POST.get('phone');
    miousify_domain_name = request.POST.get('miousify_domain_name')

    try:
        domain = MStore.objects.get(miousify_domain_name=miousify_domain_name);
        print(domain);
        return HttpResponse("Store aleady exists");
        pass
    except ObjectDoesNotExist:
        # can continue
        # do nothing
        print("store does not exist with name")
        pass

    # check if store with domain name already exist
    try:
        created_store = create_store_and_commit(email=email, miousify_domain_name=miousify_domain_name, phone=phone,
                                 password=hashed_password);

        if created_store == True:
            print("Created successfully");
            return HttpResponse("created");
        else:
            return JsonResponse(data=False);
        pass
    except Exception as exceptio:
        print(exceptio)
        return HttpResponse("did not create store successfully")

def stores_get(request: HttpRequest):
    # get stores list
    stores= []
    try:
        stores=  MStore.objects.all();
    except Exception:
        print("no stores available")
        return HttpResponse("no stores available")

    return JsonResponse(data=stores.count(), safe=False);
    pass