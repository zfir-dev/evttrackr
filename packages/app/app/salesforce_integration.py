from simple_salesforce import Salesforce

username = 'your_username'
password = 'your_password'
security_token = 'your_security_token'

sf = Salesforce(username=username, password=password, security_token=security_token)

def get_status(record_id):
    if not sf:
        return False, "Failed to connect to Salesforce"
    if not record_id:
        return False, "Record ID is required"
    try:
        record = sf.evttrackr_EvtTrackrTicket__c.get(record_id)
        return True, "Record fetched successfully", record, None
    except Exception as e:
        return False, f"Failed to fetch record: {str(e)}"

def set_status(record_id, status):
    if not sf:
        return False, "Failed to connect to Salesforce"
    if not record_id:
        return False, "Record ID is required"
    try:
        new_data = {
            "evttrackr_Status__c": status
        }
        sf.evttrackr_EvtTrackrTicket__c.update(record_id, new_data)
        return True, "Record updated successfully", record_id
    except Exception as e:
        return False, f"Failed to update record: {str(e)}", None
