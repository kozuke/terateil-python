import requests

base_url = "http://virtual-youtuber.userlocal.jp/document/ranking?page="

# headerを含めると400(Bad requetが返却されました。)
# headers = {
#     "user-agent": "",
#     "accept": "",
#     "connection": "",
#     "accept-encoding": "",
#     "accept-language": "",
#     "cookie": "",
#     "host": "",
#     "if-none-match": '',
# }
# res = requests.get(url=base_url, headers=headers)
res = requests.get(url=base_url)

print(res.status_code)
