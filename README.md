Thumbtack 2013 PyCon Challenge
==============================

Or How I Learned To Stop Worrying and Love sorted()
---------------------------------------------------

I recently came across a Python challenge presented by [Thumbtack](1)
at PyCon 2013.  Write a Python script that finds anagram pairs in a
given text.  The complete rules, [copypasted](2):

> Read the text corpus from stdin and print the anagram pairs to stdout.

> Your solution should be case-insensitive – mug and Gum are considered
> anagrams.

> The words in each pair must not appear in the other pair.

> Treat all non-alphanumeric characters as whitespace – “He’s
> twenty-seven, and” would be considered five words: he, s, twenty,
> seven, and.

> Ignore all words with fewer than four letters.

Solution
--------

(Written without looking at any of the published solutions, I swear!)

`./anagram.py < text-file.txt`

Outputs the longest anagram pairs.  That is, say there's two sets
consisting of three pairs, and four sets consisting of two pairs.
Only the two sets of three pairs will be printed.  This behavior (and
a few other things) can be tweaked inside `anagram.py`.

[1]: http://www.thumbtack.com/engineering/pycon-2013-coding-challenge-roundup/).
[2]: http://www.jeffkramer.com/misc/thumbtack-pycon-2013-challenges/

