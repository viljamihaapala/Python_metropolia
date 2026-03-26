sanat = ["auto", "lentokone", "vaappu", "tietokone", "hyrrakela", "ahven", "puu"]

laskuri = 0

for sana in sanat:

    if len(sana) > 5:
        laskuri += 1

print(f"Listassa oli {laskuri} sanaa, joissa on yli 5 kirjainta.")