from wsgiref.simple_server import make_server
"""
Itse koodi alkaa tästä

Tämä on Osa Code03 kurssia 13.3.2025
"""

def app(environ, respond):
    respond('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    yield "Älä katso tänne!".encode('utf-8')
    polku = environ["PATH_INFO"].strip('/')
    salanimi = polku.replace("a","aca").replace("i", "hani").replace("n","Nano")
    yield "<p>moikka<p>".encode('utf-8')
    yield (f"<BR>Salainen nimesi on: <b>{salanimi}</b>".encode('utf-8'))
    #for key in environ:
    #    yield ("%s: %s\n" % (key, environ[key])).encode('utf-8')


if __name__ == '__main__':
    with make_server("localhost", 8000, app) as server: 
        server.serve_forever()


