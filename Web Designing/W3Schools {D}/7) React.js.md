# $\fbox{React.js}$





## **Topic - 1: Basic Concepts**

### <u>Introduction</u>

- React is used for building single-page web applications.
- Also we can reuse a UI component.


### <u>Working</u>

- Before changing the browser DOM, the memory DOM is manipulated first.
- Then the changes are overwritten to the browser DOM.


### <u>Installation</u>

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash # or latest version
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf "${HOME}/.nvm" || printf "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
nvm install --lts # Install the latest LTS (Long Term Support) version of Node.js
nvm use --lts
node -v # Check if Node.js is installed
npm -v # Check if npm is installed
```

```sh
sudo apt update
sudo apt install nodejs npm
node -v
npm -v
```

```sh
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update
sudo apt install yarn
yarn -v
```


### <u>Start The Application</u>

```sh
npm start
```

- This automatically opens the browser with port.


### <u>Hello World</u>

```js
import logo from './logo.svg';
import './App.css';

function App() {
	return (
	    <div className="App">
		    <h1>Hello World!</h1>
		</div>
	);
}

export default App;
```



## **Topic - 2: ES6**

### <u>Introduction</u>

- **<u>ES6</u>:** ECMAScript 6
- It provides some important features to work with.

#### Features:

- Classes
- Arrow functions
- Variables
- Array methods
- Destructing
- Modules
- Ternary operator
- Spread operator


### <u>ES6 Classes</u>

#### Constructor & method:

```js
class Car
{
	constructor(company, colour)
	{
		this.company = company;
		this.colour = colour;
	}

	my_func()
	{
		console.log("Men are brave.");
	}
}
```

#### Initialization:

```js
const myCar = new Car("Suzuki", "Silver");
myCar.my_func();
```

#### Inheritance:

```js
class Model extends Car
{
	constructor(company, colour, price)
	{
		super(company);
		super(colour);
		this.price = price;
	}

	new_func()
	{
		return "Price is " + this.price;
	}
}
```


### <u>ES6 Arrow Functions</u>

#### Regular function:

```js
hello = function() {
	return "Hello, World!";
}
```

#### Arrow function (multiline):

```js
hello = () => {
	return "Hello, World!";
}
```

#### Arrow function (single-line):

```js
hello = () => "Hello, World!";
```

- We can write parameters within `()`.
- For a single parameter however, even the bracket is not required.


### <u>Array Methods</u>

#### `map()` method:

```jsx
const myArray = ['apple', 'banana', 'orange'];

const myList = myArray.map((item) => <p>{item}</p>)
```


### <u>Destructing</u>

#### Destructing array:

```jsx
const vehicles = ['mustang', 'f-150', 'expedition'];

const [car, truck, suv] = vehicles;    // Declare + Assign
const [var1,, var3] = vehicles    // "f-150" is skipped.
```

#### Destructing function:

```jsx
function calculate(a, b) {
  const add = a + b;
  const subtract = a - b;
  const multiply = a * b;
  const divide = a / b;

  return [add, subtract, multiply, divide];
}

const [add, subtract, multiply, divide] = calculate(4, 7);
```

#### Destructing objects:

```jsx
const vehicleOne = {
	brand: 'Ford',
	model: 'Mustang',
	type: 'car',
	year: 2021, 
	color: 'red'
}


myVehicle(vehicleOne);


// Though old method, but clearer
function myVehicle(vehicle)
{
	const message = 'My ' + vehicle.type + ' is a ' + vehicle.color + ' ' + vehicle.brand + ' ' + vehicle.model + '.';
}
```
