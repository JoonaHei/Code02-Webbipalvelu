from wsgiref.simple_server import make_server
"""
Itse koodi alkaa tästä

Tämä on Osa Code03 kurssia 13.3.2025
"""
def app(environ, respond):
    respond('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    
    # Tarkistetaan, onko nappia painettu
    query_string = environ.get("QUERY_STRING", "")
    nappi_painettu = "napin_arvo=1" in query_string  # Tarkistaa, onko lomake lähetetty

    yield "<p>Älä katso tänne!</p>".encode('utf-8')

    polku = environ.get("PATH_INFO", "").strip('/')
    salanimi = polku.replace("a", "aca").replace("i", "hani").replace("n", "Nano")

    yield f"<p>Salainen nimesi on: <b>{salanimi}</b></p>".encode('utf-8')

    if nappi_painettu:
        yield "<p><b>Oikeasti! Saat 5€! (tai sitten et)</b></p>".encode('utf-8')
    else:
        yield """
        <form method="GET">
            <input type="hidden" name="napin_arvo" value="1">
            <input type="submit" value="Paina niin saat 5€">
        </form>
        """.encode("utf-8")

if __name__ == '__main__':
    with make_server("localhost", 8000, app) as server: 
        server.serve_forever()


