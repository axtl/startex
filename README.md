# StarTeX #

A starting template for [USENIX][] conferences, based off the [organization's own][usetla]. The included `Makefile` originally from [latex-makefile][] where you may find a newer version — it's included here for convenience.

Body typeface is Palatino, the paper title in Helvetica. PDF hyperlinks and code highlighting are free bonuses.


To see the rendered base file, refer to [the sample PDF][pdf].

## Usage ##

Fill in the sections in `paper.tex` and the appropriate bibliography in `bibliography.bib`, then run

    make

and you should have your output in `paper.pdf`

## Changes ##

Limited changes should be made to `style.sty` as it may otherwise interfere with the USENIX guidelines. Other than that, if you know ways of making this better, please make it happen!

[latex-makefile]: https://latex-makefile.googlecode.com/
[USENIX]: http://www.usenix.org/
[usetla]: http://www.usenix.org/events/osdi08/cfp/requirements.html
[pdf]: blob/master/paper.pdf