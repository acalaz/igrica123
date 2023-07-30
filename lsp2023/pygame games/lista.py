global studenti
studenti= {
        "RA 112/2021" :{
            "ime": "Petar",
            "prez": "Petrovic",
            "godina":2,
            "ocene":[1, 2, 3, 4],
            "prosek": "2.5"
    },
    "IN 112/2020" :{
            "ime": "Marko",
            "prez": "Kraljevic",
            "godina":4,
            "ocene":[10, 10, 10, 10],
            "prosek": "10.0"
    },
    "LF 001/2021" :{
            "ime": "Dzordz",
            "prez": "Vasington",
            "godina":1,
            "ocene":[1,1,1,1,1],
            "prosek": "1.0"
    }
}
def dodavanje(ime:str,prez:str,index:str):
    studenti[index] = {"ime" : ime, "prezime": prez, "godina":1,"ocene":list() }
dodavanje("Kim Jon", "Un", "IN 123/2021")
print(studenti)