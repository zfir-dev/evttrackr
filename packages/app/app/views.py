import qrcode
from io import BytesIO
import base64
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
        request,
        "update.html",
        {
            "result": {
                "message": message,
                "record": record,
                "status": record["evttrackr_Status__c"],
            }
        },
    )


def show(request, record_id):
    if not record_id:
        return render(
            request, "error.html", {"result": {"message": "Record ID is required"}}
        )

    success, message, record = get_status(record_id)
    if not success:
        return render(request, "error.html", {"result": {"message": message}})

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data("https://localhost:8000/register/" + record_id)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    buffered = BytesIO()
    qr_img.save(buffered, format="PNG")
    qr_img_base64 = base64.b64encode(buffered.getvalue()).decode()

    return render(
        request,
        "show.html",
        {
            "result": {
                "message": message,
                "record": record,
                "status": record["evttrackr_Status__c"],
                "qr_code": qr_img_base64,
            }
        },
    )
