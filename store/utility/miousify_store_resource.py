from requests import post, get, request
from ..models import MStore
from django.shortcuts import get_object_or_404
import os
from ..models import MStore

miousify_server_endpoint=os.environ.get("MIOUSIFY_RESOURCE_URL", "http://localhost:5000")

def create_store_and_commit( miousify_domain_name, phone, email, password):
    # create store resource
    created_store_data = createStoreResource(email=email, miousify_domain_name=miousify_domain_name);

    if created_store_data == False:
        raise Exception("Did not create store successfully  fault from miousify resource service");
    # key reference in database
    try:
        #save
        store = MStore(miousify_store_resource_id=created_store_data['_id'],
                       miousify_domain_name=miousify_domain_name,
                       email=email,
                       phone=phone,
                       password=password,
                       user_account="general");
        store.save();
        return True
    except Exception as identifier:
        #could not save
        raise Exception("could not save model data");


# store resource, store components, what makes up the store
def createStoreResource(email, miousify_domain_name):
    ' creates resource for this store '

    # Create  store resource
    response = post(miousify_server_endpoint +"/store", data={
        "miousify_domain_name": miousify_domain_name,
        "owner": email
        # other store related data would go here
    });

    if response.status_code == 200:
        ' store resource successfully created '

        response_json= response.json();
        # after store have being created
        # return data for further processing
        return response_json
    elif response.status_code == 500:
        print("Store route responsed with 500")
        return False




def delete_store_and_commit(miousify_domain_name):

    store = get_object_or_404(MStore, pk=miousify_domain_name);

    response = request("DELETE", miousify_server_endpoint+"/store/"+store.miousify_store_resource_id);

    if response.status_code == 200:
        store.delete();
        return True;
    else:
        return False
