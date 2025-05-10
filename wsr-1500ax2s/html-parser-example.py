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

f = open('info.html')
html = f.read()
f.close()

parser = MyHTMLParser()
parser.feed(html)
