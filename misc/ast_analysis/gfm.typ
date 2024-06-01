= H1
<h1>
== H2
<h2>
=== H3
<h3>
==== H4
<h4>
===== H5
<h5>
====== H6
<h6>
Alternatively, for H1 and H2, an underline-ish style:

= Alt-H1
<alt-h1>
== Alt-H2
<alt-h2>
Emphasis, aka italics, with #emph[asterisks] or #emph[underscores,
right].

Strong emphasis, aka bold, with #strong[asterisks] or
#strong[underscores].

Combined emphasis with #strong[asterisks and #emph[underscores]].

Strikethrough uses two tildes. #strike[Scratch this.]

+ First ordered list item

+ Another item

  - Unordered sub-list.

+ Actual numbers don\'t matter, just that it\'s a number

  + Ordered sub-list

+ And another item.

  You can have properly indented paragraphs within list items. Notice
  the blank line above, and the leading spaces (at least one, but we\'ll
  use three here to also align the raw Markdown).

  To have a line break without a paragraph, you will need to use two
  trailing spaces. \
  Note that this line is separate, but within the same paragraph. \
  (This is contrary to the typical GFM line break behaviour, where
  trailing spaces are not required.)

- Unordered list can use asterisks

- Or minuses

- Or pluses

#link("https://www.google.com")[I\'m an inline-style link]

#link("https://www.google.com")[I\'m an inline-style link with title]

#link("https://www.mozilla.org")[I\'m a reference-style link]

#link("../blob/master/LICENSE")[I\'m a relative reference to a repository file]

#link("http://slashdot.org")[You can use numbers for reference-style link definitions]

Or leave it empty and use the
#link("http://www.reddit.com")[link text itself].

URLs and URLs in angle brackets will automatically get turned into
links. #link("http://www.example.com") or
#link("http://www.example.com") and sometimes example.com (but not on
Github, for example).

Some text to show that the reference links can follow later.

#image("Untitled.jpg")

Here\'s our logo (hover to see the title text):

Inline-style:
#image("https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png")

Reference-style:
#image("https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png")

Inline `code` has `back-ticks around` it.

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```

```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```

Here is a simple footnote#footnote[My reference.].

A footnote can also have multiple lines#footnote[Every new line should
be prefixed with 2 spaces.].

You can also use words, to fit your writing style more
closely#footnote[Named footnotes will still render with numbers instead
of the text but allow easier identification and linking. \
This footnote also has been made with a different syntax using 4 spaces
for new lines.].

Colons can be used to align columns.

#align(center)[#table(
  columns: 3,
  align: (col, row) => (auto,center,right,).at(col),
  inset: 6pt,
  [Tables], [Are], [Cool],
  [col 3 is],
  [right-aligned],
  [\$1600],
  [col 2 is],
  [centered],
  [\$12],
  [zebra stripes],
  [are neat],
  [\$1],
)
]

There must be at least 3 dashes separating each header cell. The outer
pipes (|) are optional, and you don\'t need to make the raw Markdown
line up prettily. You can also use inline Markdown.

#align(center)[#table(
  columns: 3,
  align: (col, row) => (auto,auto,auto,).at(col),
  inset: 6pt,
  [Markdown], [Less], [Pretty],
  [#emph[Still]],
  [`renders`],
  [#strong[nicely]],
  [1],
  [2],
  [3],
)
]

#blockquote[
Blockquotes are very handy in email to emulate reply text. This line is
part of the same quote.
]

Quote break.

#blockquote[
This is a very long line that will still be quoted properly when it
wraps. Oh boy let\'s keep writing to make sure this is long enough to
actually wrap for everyone. Oh, you can #emph[put] #strong[Markdown]
into a blockquote.
]

Three or more...

#horizontalrule

Hyphens

#horizontalrule

Asterisks

#horizontalrule

Underscores

Here\'s a line for us to start with.

This line is separated from the one above by two newlines, so it will be
a #emph[separate paragraph].

This line is also a separate paragraph, but... This line is only
separated by a single newline, so it\'s a separate line in the
#emph[same paragraph].
