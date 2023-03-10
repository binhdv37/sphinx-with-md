# Sphinx specific 

## Sphinx role

### Inline code
This is a {code}`highlighted text` using code role.

```
This is a {code}`highlighted text` using code role.
```
    
---

### Math
Since Pythagoras, we know that {math}`a^2 + b^2 = c^2`.

```
Since Pythagoras, we know that {math}`a^2 + b^2 = c^2`.
```

---

### Link to doc
Link to specific doc file using doc directive {doc}`md-cheatsheet`.

```
Link to specific doc file using doc directive {doc}`md-cheatsheet`.
```

---

### Reference to specific section using section name
Reference to specific section of a file {ref}`UML diagrams`

```
Reference to specific section of a file {ref}`UML diagrams`
```

---

## Sphinx directive
### Toctree
Use toctree (table of content tree) directive to setup table of content, usually used in home page

    ```{toctree}
    :caption: 'Contents:'
    :maxdepth: 2

    item1
    item2
    item3
    ```

---

### Include
```{include} ../../../README.md
:relative-images:
```

    ```{include} ../../../README.md
    :relative-images:
    ```

### Note
```{note}
this is a noted text
```

    ```{note}
    this is a noted text
    ```

---

### Warning
```{warning}
This is a warning area
```

    ```{warning}
    This is a warning area
    ```

---

### see also
```{seealso}
See also here
```

    ```{seealso}
    See also here
    ```

---

### version added
```{versionadded} 1.0
New functionality
```

    ```{versionadded} 1.0
    New functionality
    ```

---

### Version changed
```{versionchanged} 1.1
Change versions
```

    ```{versionchanged} 1.1
    Change versions
    ```

---

### deprecated
```{deprecated} 1.1
Deprecated version
```

    ```{deprecated} 1.1
    Deprecated version
    ```

---

### centered
```{centered} title
```

    ```{centered} title
    ```

---

### code-block
```{code-block} js
console.log('hello');
```

    ```{code-block} js
    console.log('hello');
    ```

```{seealso}
[Supported languages](https://support.codebasehq.com/articles/tips-tricks/syntax-highlighting-in-markdown)
```

---


### UML diagrams

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

```{mermaid}
sequenceDiagram
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

Bob-->Alice: Checking with John...
Alice->John: Yes... John, how are you?
```

    ```{mermaid}
    sequenceDiagram
    Alice ->> Bob: Hello Bob, how are you?
    Bob-->>John: How about you John?
    Bob--x Alice: I am good thanks!
    Bob-x John: I am good thanks!
    Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

    Bob-->Alice: Checking with John...
    Alice->John: Yes... John, how are you?
    ```

And this will produce a flow chart:

```{mermaid}
graph LR
A[Square Rect] -- Link text --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```

    ```{mermaid}
    graph LR
    A[Square Rect] -- Link text --> B((Circle))
    A --> C(Round Rect)
    B --> D{Rhombus}
    C --> D
    ```

---

<!-- ### glossary
```{glossary}
Muc 1
    Child 1
```

---

### hlist
```{hlist}
:columns: 3

* tu dong lam gon danh sach
* dong 2
* dong 3
* dong 4
* dong 5
* dong 6
```

--- -->

## Sphinx special name
Special sphinx document name (Please do not use these words):
- genindex, modindex, search
- every name start with _