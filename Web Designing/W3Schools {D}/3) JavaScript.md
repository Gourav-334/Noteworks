# $\fbox{Chapter 1: JAVASCRIPT}$





## **Topic - 1: Getting Started**

### <u>First JS Program</u>

- Primary use of JS is to make websites dynamic.

```js
console.log("Hello, World!");
console.log("This is JS!");
```

#sololearn_returns

- The second line in code above is printed on another line.
- And no quotes are required for numbers like most of the languages.


### <u>Embedded JS In HTML</u>

```html
<body>
	<script>
	    console.log("JavaScript in HTML");
    </script>
</body>
```


### <u>Comments</u>

- Commenting syntax is same as legendary C.


### <u>Simple Operations</u>

- Operations can directly be printed through `console.log()`, similar to how the GOAT Python does.


### <u>Variables</u>

```js
let name;
name = "Gourav";
```

- We can also make both declaration & initialization in the same line.
- Older versions of JS used keyword `var` instead of `let`.


### <u>Constants</u>

```js
const name = 'Gourav';
```

- String can be written within single or double quotes, whether variable or constant.


### <u>Booleans</u>

- Booleans use keyword `true` & `false`.



## **Topic - 2: Operators & Strings**

### <u>Exponentiation</u>

```js
console.log(x**y);
```


### <u>Square Root</u>

```js
int a = 9, b = 1/2;

console.log(a**b);
```


### <u>Increment Operator</u>

```js
num++;
```


### <u>Assignment Operator</u>

- Operation shown below is valid.

```js
num += 3;
```


### <u>Enclosing Quotes</u>

```js
console.log('Lot of "Diwali" sweets!');
```

- Notice how substring `Diwali` is enclosed in double quotes.
- Opposite of it will also work (single quotes inside double).


### <u>Template Literals</u>

- Template literal are strings declared between $`$ (back-ticks).

```js
let str = `My string`;
```

- Also template variables can have embedded variables in it, using `$`.

```js
let score = `Score: ${points}`;
```

---
