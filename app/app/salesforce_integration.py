from simple_salesforce import Salesforce

username = 'your_username'
password = 'your_password'
security_token = 'your_security_token'
client_id = 'your_client_id'
client_secret = 'your_client_secret'

record_id = 'your_record_id'

new_data = {
    'Status': 'Updated',
}

sf = Salesforce(username=username, password=password, security_token=security_token,
                client_id=client_id, client_secret=client_secret)

sf.evttracker_EvtTrackrTicket.update(record_id, new_data)
