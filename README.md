# Show Me The Spuhs

This script is meant to show you all spuhs, slashes, or hybrids which are higher in the taxonomy tree than any taxon leaves you've previously identified. In short, it is meant to answer: "what spuhs could I use?" It can also tell you what you have used, and what you should look out for.

Why is this important? Knowing that you can identify higher than the species _makes you a better birder_. If you're always looking for species, you lose out on asking yourself the crucial question of how you know what you know. Was it really a Robin, or was it just thrush-shaped? Did you see the black on the back of the head? Could it have been a Catharus sp., instead? Why not? These questions help teach us how to bird better, how to look for detail we're missing. As with all science - showing what you know by describing what you see is the way to learn.

Ideally, this script will be of use at some point in a web page, where people can upload their data or choose their jurisdiction to see what spuhs might apply where they are.

## Implementatoin

Writing it is somewhat difficult, because the eBird taxonomy is not three dimensional.

- It's not obvious if there are slashes or subspecies for a given species.
- It's not clear which generic spuh(s) match a given species.
- It's not clear if any genus should have a corresponding spuh in the same family.
- It's not clear if any genus should have a corresponding spuh in the same order.

The script will need to check each of these before listing all spuhs, slashes, or hybrids that might match a given observed species. Right now, it doesn't do that well, but I am tired of working so I am stopping.

## Installation

You'll need the [eBird taxonomy](https://www.birds.cornell.edu/clementschecklist/introduction/updateindex/october-2023/download/). Get the larger joint one, as a .csv.

You'll also need [to download your own eBird data](https://ebird.org/downloadMyData).

Then just using Python 3 should work.

## Contribute

Help would be great!

## License

GPL. It's not worth using industrially.