oferte = [
    {"hotel": "Granada Luxury Resort", "preț": 1200, "destinație": "Alanya"},
    {"hotel": "Oz Hotels Sui Resort", "preț": 950, "destinație": "Antalya"},
    {"hotel": "Hotel Delphin Deluxe", "preț": 1350, "destinație": "Alanya"}
    ]
hoteluri = list(map(lambda oferta: oferta["hotel"], oferte))
print(hoteluri)

curs_valutar = 5.0565 # Exemplu: 1 euro = 5.0565 lei
preturi_lei = list(map(lambda oferta: {"hotel": oferta["hotel"], "preț": oferta["preț"] * curs_valutar}, oferte))

print(preturi_lei)

oferte = [
    {"hotel": "Granada Luxury Resort", "preț": 1200},
    {"hotel": "Oz Hotels Sui Resort", "preț": 950},
    {"hotel": "Hotel Delphin Deluxe", "preț": 1350}
]

oferte_buget = list(filter(lambda oferta: oferta["preț"] < 1000, oferte))
print(oferte_buget)