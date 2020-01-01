# tower actions
import requests
from django.shortcuts import get_object_or_404
from ..models import MStore

miousify_tower_url = "http://"

def start_trial_server_for_store(miousify_domain_name, plan, miousify_store_resource_id):

    check_ = _send_request_to_tower(data={
        "miousify_domain_name": miousify_domain_name,
        "plan":plan,
        "miousify_store_resource_id" : miousify_store_resource_id,
        "is_trial": True
    });


def activate_server(miousify_domain_name, plan, miousify_store_resource_id):

    check_ = _send_request_to_tower(data={
        "miousify_domain_name": miousify_domain_name,
        "plan":plan,
        "miousify_store_resource_id" : miousify_store_resource_id,
        "is_trial": False
    });


def deactivate_server(miousify_domain_name):
    response = requests.get(miousify_tower_url+"/deactivate");

    if (response.status_code == 200) is True:
        return True
        pass
    else:
        ' typically try again, something must have gone wrong on the tower '
        pass



def _send_request_to_tower(data,append=""):
    response = requests.post(miousify_tower_url+append, data=data);

    if (response.status_code == 200) is True:
        return True
        pass
    else:
        ' typically try again, something must have gone wrong on the tower '

        print("could not create store");
        return False
    pass