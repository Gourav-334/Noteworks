# <u>Chapter 1</u>: HYPER TEXT MARKUP LANGUAGE





## **Topic - 1: Basics**

### <u>General Format</u>

```
<!DOCTYPE html>

<html>

<head>
	<title> Page title </title>
</head>

<body>
	<h1> Heading </h1>
	<p> Paragraph </p>
</body>

</html>
```


### <u>Introduction</u>

- Invented by Tim Berners Lee in 1991.


### <u>Basics</u>

#### HTML links:

```
<a href="https://www.w3schools.com"> Link </a>
```

#### Images:

```
<img src="myimage.jpg" alt="Image" width="104" height="142">
```

- `alt` provides text for image, which is shown when image hasn't loaded.
- We call these parameters like `src`, `alt` etc as attributes.


### <u>Elements</u>

#### Breakpoint:

```
<p> Paragraph 1 </p> <br>
<p> Paragraph <br> 2 </p>
```

- None of the HTML tag is case-sensitive.
- Means we could have used `<BR>` instead `<br>` too.


### <u>Attributes</u>

#### Style:

```
<p style="color:red; font-size:60px;"> Red text. </p>
```

- We can also write `130%` for example instead `60px`.
- Text can be aligned to center using `text-align:center`.
#### Title:

- A title defines information about paragraph.

```
<p title="I'm for help"> Paragraph </p>
```


### <u>Paragraph</u>

- HTML automatically removes extra spaces from paragraphs.

#### Horizontal rule:

```
<p> Paragraph 1. </p>
<hr>
<p> Paragraph 2. </p>
```

- **<u>Empty tag</u>:** Tag having no end tag.

#### Pre tags:

- We can display formatting like spacing using `pre` tag instead `p`.


### <u>Formatting Elements</u>

- `<strong>` - Important text
- `<em>` - Emphasized text
- `<mark>` - Marked text
- `<small>` - Smaller text
- `<del>` - Strikethrough text
- `<ins>` - Inserted text
- `<sub>` - Subscript
- `<sup>` - Superscript
