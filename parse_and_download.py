
from bs4 import BeautifulSoup
import argparse
import requests


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-p", "--pokemon-list", required=True, help="Path to where the raw Pokemon HTML file resides")
ap.add_argument("-s", "--sprites", required=True, help="Path where the sprites will be stored")
args = vars(ap.parse_args())

# construct the soup and initialize the list of pokemon
# names
soup = BeautifulSoup(open(args["pokemon_list"]).read())
names = []

# loop over all link elements
for link in soup.findAll("a"):
    # update the list of pokemon names
    names.append(link.text)

for name in names:
    # initialize the parsed name as just the lowercase
    # version of the pokemon name
    parsedName = name.lower()  # sanitizing the Pokemon name is to convert it to lowercase

    # if the name contains an apostrophe (such as in Farfetch'd, just simply remove it)
    parsedName = parsedName.replace("'", "")

    # if the name contains a period followed by a space (as is the case with Mr. Mime), then replace it with a dash
    parsedName = parsedName.replace(". ", "-")

    # handle the case for Nidoran (female)
    if name.find(u'\u2640') != -1:
        parsedName = "nidoran-f"
    # and handle the case for Nidoran (male)
    elif name.find(u'\u2642') != -1:
        parsedName = "nidoran-m"

# construct the URL to download the sprite
    print("[x] downloading {0}.".format(name))
    url = "http://img.pokemondb.net/sprites/red-blue/normal/{0}.png".format(parsedName)
    r = requests.get(url)
    # if the status code is not 200, ignore the sprite
    if r.status_code != 200:
        print("[x] Error downloading {0}.".format(name))
        continue
    # write the sprite to file
    f = open("{0}/{1}.png".format(args["sprites"], name.lower()), "wb")
    f.write(r.content)
    f.close()
