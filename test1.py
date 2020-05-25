import requests
import json

login_url = 'https://192.168.2.131:6443/api/v1/pods'
token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJrdWJlcm5ldGVzLWRhc2hib2FyZC10b2tlbi13enc1ZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6ImVjYWVlYjcwLTliZjQtMTFlYS04YzJlLTAwMGMyOWFhMzlhNSIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDprdWJlcm5ldGVzLWRhc2hib2FyZDprdWJlcm5ldGVzLWRhc2hib2FyZCJ9.BdOZCYzHCBNY1b5lbsR3swzp45lxhmW7ij7Ccx0DaZY9cLX4SAa-A9H4dOzm-RutdgmWwuvHQxLbpLsjd9TtmIyCu3mDwG6GpiUK0vJ8qxytMdDS7fsg45QKidd353CYGtC15vsOq5lfm3S5ksM3UM7TdoB67zmcGhsQAwwQzLZ-kuKSDUT5MAAxymu4IEFF7R0xXOdaACxWPcvAXTioxhXJ3baUORFAFb1iWiBJF0uQrL6EG6lXYlOlvHn05uapgusaerVCho1_l8FD7xGgRAHo1JPN1tf5KMG2f0WW2GX0T1ITvzyFJfVuCsZuy19tom4XQafTVV4AY9wQEqACmA'
headers = {
    'Authorization': 'Bearer ' + token
}

response = requests.get(login_url, verify=False, headers=headers)
content = str(response.content, 'utf-8')
content_json = json.loads(content)
print(json.dumps(content_json, sort_keys=True, indent=4))


class Inspect(object):
    def __init__(self, host, port, token):
        self.host = host
        self.port = port
        self.token = token
        self.pods = '/api/v1/pods'
        self.deployments = '/apis/extensions/v1beta1/deployments'
        self.daemonsets = '/apis/extensions/v1beta1/daemonsets'
        self.statefulsets = '/apis/apps/v1/statefulsets'
        self.replicationcontrollers = '/api/v1/replicationcontrollers'
        self.replicasets = '/apis/extensions/v1beta1/replicasets'
        self.jobs = '/apis/batch/v1/jobs'
        self.cronjobs = '/apis/batch/v1beta1/cronjobs'


    def json_format(self, str):
        print(json.dumps(str, sort_keys=True, indent=4))
