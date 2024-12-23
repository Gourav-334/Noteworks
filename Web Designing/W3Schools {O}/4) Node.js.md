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



## **Topic - 4: File System**

### <u>Reading File</u>

- We use string `fs` for using file system.

```js
var http = require("http");
var fs = require("fs");

http.createServer(function(req,res)
{
	fs.readFile("someText.html", function(err,data)
	{
		res.writeHead(200, {"Content-Type": "text/html"});
		res.write(data);
		
		return res.end();
	});
}).listen(8080);
```


### <u>All File Operations</u>

```js
var fs = require('fs');  


/* Opening a file */
fs.open('mynewfile2.txt', 'w', function (err, file)
{  
	if (err) throw err;
	console.log("File opened!");
});


/* Write to file */
fs.writeFile('mynewfile3.txt', 'Hello content!', function (err)
{
	if (err) throw err;
	console.log("Written to file!");
});


/* Append to file */
fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {  
	if (err) throw err;
	console.log("Appended to file!");
});


/* Renaming file */
fs.rename('mynewfile1.txt', 'myrenamedfile.txt', function (err)
{
	if (err) throw err;  
	console.log('File Renamed!');  
});


/* Delete a file */
fs.unlink('mynewfile2.txt', function (err)
{  
	if (err) throw err;
	console.log("File deleted!");
});
```



## **Topic - 5: URL Module**

```js
var url = require('url');  
var adr = 'http://localhost:8080/default.html?year=2017&month=february';  
var q = url.parse(adr, true);  
  
console.log(q.host);       //returns 'localhost:8080'
console.log(q.pathname);   //returns '/default.html'  
console.log(q.search);     //returns '?year=2017&month=february'

//returns an object: { year: 2017, month: 'february' }
var qdata = q.query; 
console.log(qdata.month);   //returns 'february'





var http = require('http');  
var url = require('url');  
var fs = require('fs');  
  
http.createServer(function (req, res)
{  
	var q = url.parse(req.url, true);  
	var filename = "." + q.pathname;  
	
	fs.readFile(filename, function(err, data)
	{  
		if (err)
		{  
			res.writeHead(404, {'Content-Type': 'text/html'});  
			return res.end("404 Not Found");  
		}   
		
		res.writeHead(200, {'Content-Type': 'text/html'});  
		res.write(data);  
		
		return res.end();  
	});  
}).listen(8080);
```



## **Topic - 6: Events**

### <u>Introduction</u>

- **<u>Event</u>:** An actions triggered through a computer program.
- We have to include `events` module for this purpose.


### <u>Steps Involved</u>

1. Create an `EventEmitter` object.
2. Make an event trigger.


### <u>Code Example</u>

```js
var events = require("events");
var event = new events.EventEmitter();


/* Event handler */
var handler = function() {
	console.log("Working on it...");
}


/* Setting trigger for handler */
event.on("work", handler);


/* Triggering event */
event.emit("work");      // OUTPUT: Working on it...
```



## **Topic - 7: Uploading Files**

### <u>Installation</u>

- Formidable module helps us upload files to server.

```sh
npm install formidable
```


### <u>Code Example</u>

```js
var http = require('http');  
var formidable = require('formidable');  
var fs = require('fs');  



http.createServer(function (req, res)
{  
	if (req.url == '/fileupload')
	{
		// Making a IncomingForm object.
		var form = new formidable.IncomingForm();
		
		form.parse(req, function (err, fields, files)
		{
			var oldpath = files.filetoupload.filepath;  
			var newpath = 'C:/Users/_Your Name_/' + files.filetoupload.originalFilename;  
			
			fs.rename(oldpath, newpath, function (err)
			{
				if (err) throw err;  
				res.write('File uploaded and moved!');  
				res.end();  
			});
		});
	}



	// HTML Forms
	else
	{  
	    res.writeHead(200, {'Content-Type': 'text/html'});  
	    res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');  
		res.write('<input type="file" name="filetoupload"><br>');
		res.write('<input type="submit">');
		res.write('</form>');  
		
		return res.end();  
	}
}).listen(8080);
```
