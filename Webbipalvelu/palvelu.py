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
    ika = params.get("ika", "")

    if nimi and ika:
        # Tulostetaan palvelimen terminaaliin
        print(f"Käyttäjän nimi: {nimi}, Ikä: {ika}")

        # Näytetään sivulla käyttäjän syöttämät tiedot
        yield f"<p>Hei, {nimi}! Olet {ika} vuotta vanha.</p>".encode('utf-8')
    else:
        # Näytetään lomake, jos tietoja ei ole vielä syötetty
        yield """
        <form method="GET">
            <label for="nimi">Nimesi:</label>
            <input type="text" id="nimi" name="nimi" required>
            <br>
            <label for="ika">Ikäsi:</label>
            <input type="number" id="ika" name="ika" required>
            <br>
            <input type="submit" value="Lähetä">
        </form>
        """.encode("utf-8")

if __name__ == '__main__':
    with make_server("localhost", 8000, app) as server: 
        server.serve_forever()


