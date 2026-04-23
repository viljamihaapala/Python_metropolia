kirjasto = {
    "Sota ja rauha": ["Leo Tolstoi", 1869, "Romaani"],
    "Hobitti": ["J.R.R. Tolkien", 1937, "Fantasia"],
    "1984": ["George Orwell", 1949, "Dystopia"]
}

print(kirjasto["Sota ja rauha"][0])
print(kirjasto["Hobitti"][2])

kirjasto["1984"][2] = "Sci-fi"

kirjasto["Harry Potter"] = ["J.K. Rowling", 1997, "Fantasia"]

del kirjasto["Hobitti"]

print(kirjasto)
