from simple_salesforce import Salesforce

username = 'your_username'
password = 'your_password'
security_token = 'your_security_token'

record_id = 'a0OJ7000000L08BMAS'

new_data = {
    'evttrackr_Status__c': 'Not registered'
}

from simple_salesforce import Salesforce

def my_salesforce_function():
    sf = Salesforce(username=username, password=password, security_token=security_token)

    try:
        sf.evttrackr_EvtTrackrTicket__c.update(record_id, new_data)
        return True, "Record updated successfully"
    except Exception as e:
        return False, f"Failed to update record: {str(e)}"
