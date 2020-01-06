from urllib import request, parse

resp = request.urlopen("https://wikipedia.org")
print(type(resp))
print(resp.code)
print(resp.length)  # length in Bits
print(resp.peek())  # shows first lines of the html. b = bits object
data = resp.read()
print(type(data))
print(len(data))
html = data.decode("UTF-8")
print(type(html))

# resp = request.urlopen("https://www.google.com/search?q=socratica")
# https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s
params = {"v": "EuC-yVzHhMI", "t": "5m56s"}
querystring = parse.urlencode(params)  # builds the path together.
print(querystring)
url = "https://www.youtube.com/watch" + "?" + querystring
resp = request.urlopen(url)
print(resp.isclosed())  # is there a connection to the server?
html = resp.read().decode("utf-8")
print(html[:500])
