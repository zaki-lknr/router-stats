import os
import urllib.request

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    _link = False
    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag:", tag)
        for attr in attrs:
            # print(attr)
            if (attr[0] == 'name' and attr[1] == 'InternetWiredLink'):
                # print(attrs)
                self._link = True

    # def handle_endtag(self, tag):
    #     print("Encountered an end tag :", tag)

    def handle_data(self, data):
        # print("Encountered some data  :", data)
        if self._link:
            print(data)
            self._link = False

addr = os.environ.get("ROUTER_ADDR")
username = 'admin'
password = os.environ.get("ROUTER_PASS")

# 情報一覧画面
info_page = 'http://' + addr + '/info.html'

# 認証画面
auth_page = 'http://' + addr + '/login.html'
# セッション情報は持っておらず、認証すると同一ソースIPからのアクセスを一定時間許可する方式

logout_page = 'http://' + addr + '/logout.html'

# login access
auth_data = {
    'nosave_Username': username,
    'nosave_Password': password,
    'nosave_session_num': ''
}
auth_req = urllib.request.Request(auth_page, urllib.parse.urlencode(auth_data).encode('ascii'))
auth_resp = urllib.request.urlopen(auth_req)

# get stats
stats_req = urllib.request.Request(info_page)
with urllib.request.urlopen(stats_req) as stats_resp:
    html = stats_resp.read().decode('utf-8')
    parser = MyHTMLParser()
    parser.feed(html)

# logout
logout_req = urllib.request.Request(logout_page)
urllib.request.urlopen(logout_req)
