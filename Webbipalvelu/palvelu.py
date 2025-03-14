from wsgiref.simple_server import make_server
"""
Itse koodi alkaa tästä

Tämä on Osa Code03 kurssia 13.3.2025
"""
def app(environ, respond):
    respond('200 OK', [('Content-type', 'text/html; charset=utf-8')])

    # Haetaan käyttäjän syöttämät tiedot
    query_string = environ.get("QUERY_STRING", "")
    params = dict(qc.split("=") for qc in query_string.split("&") if "=" in qc)
    
    nimi = params.get("nimi", "").replace("+", " ")  # Poistetaan URL-enkoodaus (+ -> väli)
    henkilötunnus = params.get("henkilötunnus", "")

    if nimi and henkilötunnus:
        # Tulostetaan palvelimen terminaaliin
        print(f"Käyttäjän nimi: {nimi}, Henkilötunnus: {henkilötunnus}")

        # Näytetään sivulla käyttäjän syöttämät tiedot
        yield f"<p>Hei, {nimi}! Henkilötunnuksesi on {henkilötunnus}.</p>".encode('utf-8')
    else:
        # Näytetään lomake, jos tietoja ei ole vielä syötetty
        yield """
        <form method="GET">
            <label for="nimi">Nimesi:</label>
            <input type="text" id="nimi" name="nimi" required>
            <br>
            <label for="henkilötunnus">Henkilötunnus:</label>
            <input type="text" id="henkilötunnus" name="henkilötunnus" required>
            <br>
            <input type="submit" value="Lähetä">
        </form>
        """.encode("utf-8")

if __name__ == '__main__':
    with make_server("localhost", 8000, app) as server: 
        server.serve_forever()


