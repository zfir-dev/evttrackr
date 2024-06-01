from django.shortcuts import render
from .salesforce_integration import get_status, set_status


def register(request, record_id):
    print("register view called")
    # record_id = request.GET.get('record_id')
    if not record_id:
        return render(
            request, "error.html", {"result": {"message": "Record ID is required"}}
        )
    success, message, record = get_status(record_id)
    if not success:
        return render(request, "error.html", {"result": {"message": message}})
    return render(
        request, "update.html", {"result": {"message": message, "record": record, "status": record["evttrackr_Status__c"]}}
    )
    # success, message, record_id = set_status(record_id, "Registered")
    # return render(
    #     request, "update.html", {"result": {"message": message, "record_id": record_id}}
    # )
