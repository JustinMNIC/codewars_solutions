"""Your job is to group the words in anagrams.

What is an anagram ?
star and tsar are anagram of each other because you can rearrange the letters for star to obtain tsar.

Example
A typical test could be :

// input
["tsar", "rat", "tar", "star", "tars", "cheese"]

// output
[
  ["tsar", "star", "tars"],
  ["rat", "tar"],
  ["cheese"]
]
Hvae unf !"""

def group_anagrams(words):
    d = {}
    for word in words:
        key = ''.join(sorted(word))
        d[key] = d.get(key, []) + [word]
    return list(d.values())