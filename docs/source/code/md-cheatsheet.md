# Markdown cheatsheet

## Emphasis
Inline `code`

**This is bold text**

__This is bold text__

*This is italic text*

_This is italic text_

~~Strikethrough~~

```
Inline `code`

**This is bold text**

__This is bold text__

*This is italic text*

_This is italic text_

~~Strikethrough~~
```

---

## Heading

```
# Heading 1
## Heading 2
### Heading 3
```

---

## Block code
```
Sample text here...
```

    ```
    Sample text here...
    ```

---

## Link

[link text](https://console.sunteco.vn)

[link with title](http://console.sunteco.vn "title text!")

```
[link text](https://console.sunteco.vn)

[link with title](http://console.sunteco.vn "title text!")
```

---

## Image
![Image name here](../_static/image/logo/logo-dark.png)

```
![Image name here](../_static/image/logo/logo-dark.png)
```

---

## Block of text
    This is a block of text!
    Write plain text with indent to create this block of text.

---

## Single quote
> Single quote text

```
> Single quote text
```

---

## Blockquotes
> Blockquotes can also be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.

```
> Blockquotes can also be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.
```

## Lists

Unordered

+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!

```
+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!
```

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa


1. You can use sequential numbers...
1. ...or keep all the numbers as `1.`

Start numbering with offset:

57. foo
1. bar

```
1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa


1. You can use sequential numbers...
1. ...or keep all the numbers as `1.`

Start numbering with offset:

57. foo
1. bar
```

---

## Code
``` java
public static void main(String[] args) {
    System.out.println("Hello world!");
}
```

    ``` java
    public static void main(String[] args) {
    System.out.println("Hello world!");
    }
    ```
---

## Table

| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

    | Option | Description |
    | ------ | ----------- |
    | data   | path to data files to supply the data that will be passed into templates. |
    | engine | engine to be used for processing templates. Handlebars is the default. |
    | ext    | extension to be used for dest files. |


Right aligned columns

| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

    | Option | Description |
    | ------:| -----------:|
    | data   | path to data files to supply the data that will be passed into templates. |
    | engine | engine to be used for processing templates. Handlebars is the default. |
    | ext    | extension to be used for dest files. |