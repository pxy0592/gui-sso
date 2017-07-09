import requests

# proxy = {
#     'http': 'socks5://127.0.0.1:7777',
#     'https': 'socks5://127.0.0.1:7777'
# }
#
# cws_url = 'http://cws-74.ma.platformlab.ibm.com:8080/platform'
#
# r0 = requests.get(cws_url, proxies=proxy)
# # print("status_code: %s\nurl: %s" % (r0.status_code, r0.url))
# # print("response body: %s" % (r0.content))
#
# r1 = requests.post(cws_url + '/gui/internal/rest/SSO/auth/logout', proxies=proxy, auth=('Admin', 'Admin'))
# print("status_code: %s\nurl: %s" % (r1.status_code, r1.url))
# # print("response body: %s" % (r1.headers))
# print("cookies: %s" % (r1.cookies.get_dict()))

# QWRtaW46QWRtaW4=

# ego_url = 'http://jpmc01.eng.platformlab.ibm.com:8180'
# payload = {'Accept': 'application/json'}
#
# ego_auth_url = ego_url + '/platform/rest/ego/v1/auth/logon'
#
# cws_url = 'http://jpmc01.eng.platformlab.ibm.com:8280'
# cws_auth_url = cws_url + '/platform/rest/conductor/v1/auth/logon'
#
# r0 = requests.get(cws_auth_url, headers=payload, auth=('Admin', 'Admin'))
#
# print("status_code: %s" % r0.status_code)
# print("csrftoken: %s" % r0.json()['csrftoken'])
# cws_headers = {'csrftoken': r0.json()['csrftoken']}
#
# sig_list_url = 'http://jpmc01.eng.platformlab.ibm.com:8080/conductorgui/spark/instance/toSparkInstanceList.action'
# r1 = requests.get(sig_list_url, headers=cws_headers)
# print("status_code: %s" % r1.status_code)
# print("body: %s" % r1.content)

cws_url = 'http://jpmc01.eng.platformlab.ibm.com:8080/platform'
r0 = requests.request('GET', cws_url)
print(r0.status_code)
print(r0.url)

r1 = requests.request('GET', r0.url)
print(r1.status_code)
print(r1.url)

s = requests.Session()

req = requests.Request('POST', r1.url, headers=r1.headers)
prepped = req.prepare()

# do something with prepped.body
prepped.body = 'name=Admin&pwd=Admin&commit=Login'

resp = s.send(prepped)

print(resp.status_code)
print(resp.content)
