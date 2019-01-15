# Wedding guest bingo game generator

Project to generate different templates for the wedding game "Guest bingo"

## Files
* bingo.py: Python source code for generating PDFs
* source.txt: Fun facts or descriptions about guests, one per line, resulting in table
* prefix.txt: LaTeX-source that comes before the table that is generated
* postfix.txt: LaTeX-source that comes after the table that is generated
* image.txt: LaTeX-source for inputting a figure in the center-cell of the table. Could point to other images if desirable
* heart.png: Image source file for the heart inputted in the image.txt-file

The template consists of fun facts about, or descriptions of, guests. Change source.txt, a figure (image.txt) and a custom font

## Getting Started

* Clone project
* Add your font. Either
  *Add Showtime.tff to the same directory as bingo.py
  * Add your custom font to the same directory as bingo.py and change "Showtime" in prefix.txt to the name of your new font. You need the tff file.
* Run python bingo.py to check that project runs - it will generate a pdf with the name of bingo<some-hash>.pdf
* Add the fun facts about, or descriptions of, your guests in source.txt
* Run python bingo.py again - it will generate a new pdf for each time your run it


### Prerequisites

What things you need to install the software and how to install them

```
Python
LaTeX
```

### Example result templates
* [bingo79a6d038.pdf](https://baier.github.io/guest-bingo/examples/bingo79a6d038.pdf)
* [bingob562d1c1.pdf](https://baier.github.io/guest-bingo/examples/bingob562d1c1.pdf)



## Authors

* **Beate Baier** - *Initial work* - [Baier](https://github.com/baier)


## Acknowledgments

* Thanks to Erik for suggestions to code improvements and for inspiring me to automate whenever possible :)

