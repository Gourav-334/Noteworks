# $\fbox{Chapter 3: Node.js \& Express.js}$





## **Topic - 1: Introduction To Node.js**

### <u>Introduction</u>

- **<u>Node package manager</u>:** Runtime environment for JavaScript.
- It is open-source & runs cross-platform.
- Also Node.js are used for implementing servers.


### <u>Key Features</u>

- **<u>Asynchronous & event-driven</u>:** Handles non-blocking & concurrent operations.
- **<u>Single threaded</u>:** Uses single threaded event loop.
- **<u>Built on V8 engine</u>:** V8 JavaScript engine is made by Google Chrome for high performance.

>**<u>NOTE</u>:**
>V8 engine compiles JS code to native machine code.


### <u>Use Cases</u>

- Real-time application
- Scalable APIs & microservices
- Server-side scripting


### <u>Console Based Example</u>

- To run the application, write as following.

```sh
node filename.js
```


### <u>Web-Based Example</u>

- Try running the following in `localhost:8080`.

```js
var http = require('http');

http.createServer(function (req, res)
{
	res.writeHead(
		200,
		{'Content-Type': 'text/html'}
	);
	
	res.end('Hello World!');
}).listen(8080);
```

- This program prints `Hello, World!` on that page.



## **Topic - 2: Introduction To Express.js**

### <u>Introduction</u>

- Express.js is a web framework for Node.js.
- Its fast & minimalist.
- Provides pre-built features to implement.


### <u>Key Features</u>

- **<u>Routing</u>:** Easily defines routes to handle HTTP requests.
- **<u>Middleware</u>:** Uses middleware for efficient workflow in request-response cycle.
- **<u>Template engine</u>:** Generates dynamic HTML content.


### <u>Use Cases</u>

- Building web-applications & APIs
- Single-page applications (SPAs)
- Real-time applications using Socket.io
- Setting architecture for microservices


### <u>Installation</u>

```sh
npm install npm -global
npm init
npm install express
```


### <u>Basic Example</u>

```js
const express = require('express');
const appv = express();

app.get('/',(req,res) => {
	res.send("Welcome to Express");
});

app.listen(4000,() => {
	console.log("listening to port 4000");
});
```

- Run it using the same `npm filename.js` command on `localhost:4000`.



## **Topic - 3: Middleware**

### <u>Introduction</u>

- Middleware handles tasks during request-response cycle in Express.js.
- It has access to the request & response objects, which they can also modify.


### <u>Middleware Function</u>

- Middleware can make changes to request-response cycles.
- And also calls next middleware function in stack.


### <u>Types Of Middleware</u>

1. Application-level middleware
2. Router-level middleware
3. Error-handling middleware
4. Built-in middleware
5. Third party middleware
6. Method specific middleware
7. Multiple callback middleware


### <u>Application-Level Middleware</u>

- Application-level middleware executes for all requests.
- It maintains a log for each request as shown below.

```js
app.use((req, res, next) => {
	console.log('This is an application-level middleware');
	next();
})
```

- `next()` passes control to next middleware control.


### <u>Router-Level Middleware</u>

- Router-level middleware are specific to particular type of router.

```js
const router = express.Router();

app.use((req, res, next) => {
	console.log('This is an application-level middleware');
	next();
})
```


### <u>Error-Handling Middleware</u>

- This one has an extra parameter, the first one being `err` representing error.
- It logs encountered errors too & sends them as response.

```js
app.use((err, req, res, next) => {
	console.error(err.stack);
	res.status(500).send('Something went wrong!');
});
```


### <u>Built-In Middleware</u>

- Provides many built-in functions.
- Code below shows JSON & form data parsing.

```js
app.use(express.json());
app.use(express.urlencoded({extended: true }));
app.use(express.static(' public'));
```


### <u>Third-Party Middleware</u>

- For example body-parser, helmet & morgan.
- One can use it with `app.use()`.

```js
const bodyParser = require('body-parser');
const helmet = require('helmet');
const morgan = require('morgan');

app.use(bodyParser.json());
app.use(helmet());
app.use(morgan('combined'));
```


### <u>Method-Specific Middleware</u>

- This middleware works only for specific protocols & routes.
- Following code is specific to GET request to `/route` path.

```js
app.get('/route', (req, res, next) => {
	console.log('Specific to the GET method for /route');
	next();
});
```


### <u>Multiple Callback Middleware</u>

- This middleware can be chain multiple functions together & executed sequentially.
- Following code executes function `middleware1` & then `middleware2` before reaching route handler.

```js
app.get('/route', middleware1, middleware2, (req, res) => {
	// Route handler
	res.send('Response from the route handler');
});
```



## **Topic - 4: Routing**

### <u>Introduction</u>

- Routing maps HTTP methods like GET, POST, PUT & DELETE to URL patterns.
- There is an object called app, which provides functionalities for routing.


### <u>Key Features</u>

- Route parameters
- Query parameters
- Route middleware
- Router objects
- Route handlers & middleware chains
- Express route module


### <u>Basic Route Handling</u>

- Define routes using HTTP methods & corresponding URL patterns.

```js
app.get('/', (req, res) => { res.send('Hello, World!'); });
app.post('/submit', (req, res) => {
	// Handle POST request to /submit
});
```


### <u>Route Parameters</u>

- Captures values from URL using parameters.

```js
app.get('/users/:userId', (req, res) => {
	const userId = req.params.userId;
	res.send(`User ID: ${userId}`);
});
```


### <u>Query Parameters</u>

- Can access query part from URL.

```js
app.get('/search', (req, res) => {
	const query = req.query.q;
	res.send(`Search Query: ${query}`);
});
```


### <u>Route Middleware</u>

- We can use `app.use()` for applying middleware to specific routes.

```js
const middlewareFunction = (req, res, next) => {
	// Middleware logic next();
};

app.get('/protected', middlewareFunction, (req, res) => {
	res.send('Protected Route');
});
```


### <u>Router Objects</u>

- Organizes routes into modular routers with `express.Router()`.

```js
const router = express.Router();

router.get('/', (req, res) => {
	// Handle GET request to /
});

app.use('/api', router);    // Mount the router at /api
```


### <u>Route Handlers & Middleware Chains</u>

- Chains multiple route handlers (middleware functions) to a single route.

```js
app.get('/example', (req, res, next) => {
	// First middleware
	next();
}, (req, res) => {
	// Second middleware or route handler
	res.send('Example Route');
});
```


### <u>Express Route Module</u>

- Express router module is used for organizing more complex routes.

```js
/* routes/user.js */
const express = require('express');
const router = express.Router();

router.get('/:userId', (req, res) => {
	// Handle GET request to /user/:userId
});

module.exports = router;

/* app.js */
const userRouter = require('./routes/user');
app.use('/user', userRouter);
```



## **Topic - 5: Error Handling & Logging**

### <u>Introduction</u>

- **<u>Logging</u>:** Printing or record information during execution for debugging purposes.


### <u>Error Handling In Node.js</u>

#### Try-catch blocks:

- Try-catch blocks can be used to handle synchronous errors.

```js
try {
	// Your code that might throw an error
}

catch (error) {
	// Handle the error console.error(error);
}
```

#### Promises:

- Try-catch blocks for handling asynchronous errors can be written in promises.

```js
someAsyncFunction().then(result => {
	// Handle success
}).catch(error => {
	// Handle error console.error(error);
});
```

#### Event emitters:

- For handling errors encountered when emitting events.

```js
const emitter = new EventEmitter();

emitter.on('error', (error) => {
	console.error(error);
});

/* Trigger error */
emitter.emit('error', new Error('Something went wrong'));
```


### <u>Error Handling In Express.js</u>

#### Express error middleware:

- Uses middleware of Express.js for handling errors.
- Make a middleware function in application with parameters `(err, req, res, next)`.
- This middleware must be the last one in sequence.

```js
app.use((err, req, res, next) => {
	console.error(err.stack);
	res.status(500).send('Something went wrong!');
});
```

#### Async/await middleware:

- Used for handling asynchronous errors in middleware.
- This one is little complex.

```js
const asyncMiddleware = (fn) => (req, res, next) => {
	Promise.resolve(fn(req, res, next)).catch(next);
};

app.get('/', asyncMiddleware(async (req, res, next) => {
	// Your asynchronous code
}));
```


### <u>Logging In Node.js & Express.js</u>

#### Winston & Morgan:

- Both Winston & Morgan are used for logging.
- But Morgan is used specifically logging HTTP requests in Express.js.

```js
const winston = require('winston');
const morgan = require('morgan');

// Configure Winston logger
const logger = winston.createLogger ({
	transports: [
		new winston.transports.Console(),
		new winston.transports.File ({
			filename: 'error.log', level: 'error'
		}),
		new winston.transports.File ({
			filename: 'combined.log'
		}),
	],
});

/* Use Morgan for HTTP request logging. */
app.use(morgan('combined'));

/* Log an error. */
logger.error('This is an error message');
```

#### Custom logging middleware:

```js
app.use((req, res, next) => {
	logger.info(`${req.method} ${req.url}`);
	next();
});
```

---
