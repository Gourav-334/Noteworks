# $\fbox{Chapter 4: Node.js}$





## **Topic - 1: Basic Concepts**

### <u>Features</u>

- **Single-threaded**
- **<u>Non-blocking</u>:** Doesn't block any request & passes them immediately after previous request is over.
- **Uses asynchronous programming**
- **Memory efficient**


### <u>Abilities</u>

- Can create dynamic web pages.
- Make many operations on files in server.
- Can collect form data.
- Can work with database.


### <u>Role Of Node.js</u>

- A Node.js file defines the set of instructions to execute when certain server related change takes place.
- For example, what to do when someone is requesting to access a port.
- Node.js file must be the first file to be initiated in server.



## **Topic - 2: Node.js Modules**

### <u>Include Module</u>

- We can include a module using `require()` function.

```js
var http = require('http');
```


### <u>Sample Server</u>

```js
http.createServer(function (req, res) {
	res.writeHead(200, {'Content-Type': 'text/html'});  
	res.end('Hello World!');  
}).listen(8080);
```


### <u>Custom Module</u>

- We can create a custom module with help of `exports` keyword.

```js
exports.myDateTime = function () {
	return Date();  
};
```

- Save this file with name ***myModule.js***.

#### Including:

```js
var http = require('http');  
var dt = require('./myModule');  

http.createServer(function (req, res) {  
	res.writeHead(200, {'Content-Type': 'text/html'});  
	res.write("Date & time: " + dt.myDateTime());
	res.end();
}).listen(8080);
```



## **Topic - 3: Explaining HTTP Module**

### <u>Server Code Anatomy</u>

```js
/* Server object creation */
http.createServer(function (req, res) {
	
	// Optional, default font text otherwise. 200 is OK status.
	res.writeHead(200, {'Content-Type': 'text/html'});
	
	// Writing response to client.
	res.write("Hello, World!");
	
	// Ending response.
	res.end();
	
}).listen(8080);
```


### <u>Query String</u>

```js
// req is request, res is result.
http.createServer(function (req, res) {
	res.writeHead(200, {'Content-Type': 'text/html'});
	res.write(req.url);
	res.end();  
}).listen(8080);
```

- This code will result in showing of $/$ on page.
- Adding a string say `linux` to our URL `http://localhost:8080/` will show $/linux$ on page.


### <u>Parse & Display From URL</u>

```js
var http = require('http');  
var url = require('url');  
  
http.createServer(function (req, res) {  
	res.writeHead(200, {'Content-Type': 'text/html'});  
	var q = url.parse(req.url, true).query;
	var txt = q.year + " " + q.month;
	res.end(txt);  
}).listen(8080);
```

- The `url` module allows to parse information from web URL.
- For example, set URL as $http://localhost:8080/?year=2017\&month=July$
- Now the code we wrote will parse & fetch values of year & month.
