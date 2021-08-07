# Introduction

Python 3 differs a lot in handling strings and bytes from Python 2 (you can read more about this in [this article](https://betterprogramming.pub/strings-unicode-and-bytes-in-python-3-everything-you-always-wanted-to-know-27dc02ff2686) or in this [Pragmatic Unicode talk](https://nedbatchelder.com/text/unipain.html)). Basically, strings (`str`) in Python 3 are Unicode by default and “bytes” (`bytes`) are lists of integers from 0 to 255 (lists of 8 bits). There is no implicit conversion between `str` and `bytes` in Python 3, so any conversion needs to be done explicitly using `encode` (`str` → `bytes`) and `decode` (`bytes` → `str`) functions.

Throughout Oppia, we typically use strings. However, you may come across bytes in places where there is an interaction with some outside library or API — for example, when standard input or output is read or written, or when data is read from or written to files. Some standard Python libraries also only accept bytes. 

# Rules for handling strings and bytes
## Bytes outside, strings inside

The general rule you should follow is to keep all text in Oppia as strings, where possible. If a conversion to bytes is necessary, that conversion should happen as close to the “edges” of the app as possible. So, for example:
- When you receive bytes from some library, immediately convert them to string using decode.
- If you need to use a function that needs bytes, use encode to convert the string to bytes immediately before you call the function.

## Use utf-8 (or ascii)

In the Oppia codebase all data (that we can decide about) should be encoded/decoded using utf-8 encoding (`encode('utf-8')`). If you find a case where utf-8 cannot be used, please raise this with the Core Maintainers team.

If, in some case, an external source returns or receives data with a different encoding, it is fine to use that encoding only for that source. However, please first be sure to investigate whether that source can be configured to use utf-8 instead.
