# Building a Pokedex with Python

#### How are we going to do this?
In order to even “find” the Game Boy screen in our query image we are first going to make use of many image processing 
and computer vision techniques. For example, we’ll be using techniques such as:

- Edge detection
- Thresholding
- Perspective warping

We’ll characterize the shape of the Pokemon by using shape descriptors. In this way we can abstractly represent the 
Pokemon using only a list of numbers (i.e. an image feature vector).


#### Building our Pokedex will be a six step process:
1) An introduction to building a Pokedex (that’s this blog post)
2) Scraping the web and building our Pokemon sprite database
3) Indexing our database using shape descriptors
4) Finding the Game Boy screen in our image (Part 1)
5) Finding the Game Boy screen (Part 2)
6) Searching and identifying the Pokemon

#### Libraries you will need

- NumPy and SciPy
- OpenCV with Python bindings
- Scikit-Image
- requests
- BeautifulSoup

####

python parse_and_download.py --pokemon-list pokemon_list.html --sprites sprites

