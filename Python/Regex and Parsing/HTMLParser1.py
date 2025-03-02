# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr, value in attrs:
            print(f"-> {attr} > {value if value is not None else 'None'}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr, value in attrs:
            print(f"-> {attr} > {value if value is not None else 'None'}")


html_code = "\n".join(input() for _ in range(int(input())))

parser = MyHTMLParser()
parser.feed(html_code)