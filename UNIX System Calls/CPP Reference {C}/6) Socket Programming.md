# $\fbox{Chapter 6: SOCKET PROGRAMMING}$





## **Topic – 1: Client-Server Model**

### <u>Introduction</u>

- All the discussed library in this note is called **BSD Socket API**.
- These header files aren't standard, running primarily on Linux.


### <u>Concept</u>

- Means two processes communicating with each other.
- Client connects to server for requesting information access.
- We only require server’s address to connect, though both can communicate with each other.
- **<u>Socket</u>:** An end point of an inter-process communication channel.
- So, both end of a channel can be called as two different sockets.
- Two processes can communicate **only** when their sockets are of same type.


### <u>Establishing Client Socket</u>

1. Create a socket using `socket()` system call.
2. Connect socket to server’s address using `connect()`.
3. Send and receive data using `read()` and `write()` system calls respectively.


### <u>Establishing Server Socket</u>

1. Create a socket using `socket()` system call.
2. Bind socket to an address (port number of host’s machine) using `bind()` system call.
3. Listen (look) for connections using `listen()` system call.
4. Accept a connection using `accept()` system call, which can’t be called again during the time a client is connecting to the server.
5. Send & receive data.



## **Topic – 2: Domain**

### <u>Types Of Domains</u>

- UNIX domain
- Internet domain


### <u>Differences Between Two</u>

| **UNIX Domain**                                                                        | **Internet Domain**                                                        |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Two processes present at common file system communicate with each other.               | Two physically separate processes on internet communicate with each other. |
| Socket address is a character array (string), which provides entry to the file system. | Socket address consists of IP address of the host machine (32-bits).       |
| Doesn’t require port number.                                                           | A port number (16-bits) is required.                                       |

>**<u>NOTE</u>:**
>1. Lower numbers in address (port numbers) are reserved in UNIX for standard services.
>2. Port number for FTP is 21.
>3. Port numbers above 2000 are more likely to be available & not being reserved.



## **Topic – 3: Sockets**

### <u>Socket Types</u>

- Stream sockets
- Datagram sockets


### <u>Stream Sockets</u>

- Reads messages character by character.
- Uses TCP (transmission control protocol) which is reliable & stream-oriented protocol.


### <u>Datagram Sockets</u>

- Reads messages all at once.
- Uses UDP (UNIX datagram protocol) which is unreliable & message-oriented protocol.



## **Topic – 4: Creating Server**

### <u>Basic Information</u>

- Keyword localhost is used to refer to our local machine.


### <u>Headers</u>

#### `sys/types.h`:

```c
#include <sys/types.h>
```

- Contains some special data types we will be using.
- Used in `sys/socket.h` & `netinet/in.h.

#### `sys/socket.h`:

```c
#include <sys/socket.h>
```

- Contains some socket structures definitions we will require.

#### `netinet/in.h`:

```c
#include <netinet/in.h>
```

- Contains constants & structures for internet domain address.


### <u>Main Function</u>

```c
int main(int argc, char *argv[])
```

- These parameters are required because we deal with user arguments.


### <u>Declaring Important Variables</u>

```c
int sockfd, newsockfd, portno, clilen, n;
char buffer[256];
```

- `sockfd` and `newsockfd` are file descriptors.
- `clilen` is client address size.
- `n` is the number or characters that will be read or written using `read()` & `write()`.


### <u>Address Structure</u>

```c
struct sockaddr_in server_addr, client_addr;
```

- `sockaddr_in` contains the internet address.


### <u>Definition In Netinet</u>

```c
/* Inside <netinet/in.h> */

struct sockaddr_in
{
	/* sin = Socket Internet */
	
	short sin_family;           // Set to AF_NET (uses IPv4).
	u_short sin_port;           // Port number being used.
	struct in_addr sin_addr;    // Internet address
	char sin_zero[8];           // Must be set to zero
}
```

- Notice that structure `in_addr` is a different structure in structure `sockaddr_in`.
- `in_addr` contains only one `unsigned long` called `s_addr`.
- Programmer must carefully code to check if all arguments are passed.


### <u>Creating Socket</u>

```c
sockfd = socket(AF_NET, SOCK_STREAM, 0);

if (sockfd<0) {perror("Problem creating socket!");}
```

- First argument is socket’s domain address.
- We could have also used `AF_UNIX` at first argument.
- Second argument is type of socket.
- We could have also used `SOCK_DGRAM` at second argument.
- Third argument is the protocol being used.
- Here, `0` means OS will decide which protocol to use.
- Otherwise, we can use `UDP` or `TCP`.


>**<u>Warning</u>:**
>1. It is advised to keep the 3<sup>rd</sup> argument as 0 until really necessary to specify.
>2. Function `socket()` returns a integer value to file descriptor table.
>3. This value is used to refer to our socket.
>4. In case the socket call fails, `-1` is returned.
>5. However, it is almost impossible for it to fail.


### <u>Flushing The Buffer</u>

```c
bzero((char*) &serv_addr, sizeof(serv_addr));
```

- First argument is pointer to the buffer.
- Second argument is the size of buffer.


### <u>Converting Port Number</u>

```c
portno = atoi(argv[1]);
```

- User passed the argument as a string, we converted it to integer.


### <u>Server Address Structure</u>

```c
serv_addr.sin_family = AF_NET;
```

- `sin_family` member of our server address structure must always be set to `AF_NET`.

```c
serv addr.sin port = htons(portno);
```

- Function `htons()` is used to convert an integer in host byte number to network byte order.
- This is a compulsory step to perform.
- **<u>HTONS</u>:** Host To Network Short.

```c
serv_addr.sin_addr.s_addr = INADDR_ANY;
```

- The unsigned long int `s_addr` contains the IP address of the host.
- Means the IP address of the server itself.
- `INADDR_ANY` is the symbolic constant which fetches it.


### <u>Binding Socket</u>

```c
if (bind(sockfd, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) < 0)
{
	perror("Problem binding the socket!");
}
```

- System call `bind()` binds a socket to an address.
- This address is IP address & port number of host system.
- 1st argument is a file descriptor, which described each socket separately.
- 2nd argument is pointer to structure of type `sockaddr`.
- This connection fails if the socket is already in use.


### <u>Looking For Connection</u>

```c
listen(sockfd, 5);
```

- 2nd argument is the size of backlog queue.
- **<u>Backlog queue</u>:** Request in queue waiting for connection with client.
- So, `5` in code above means maximum 5 requests can exist there.


### <u>Accepting Connection Request</u>

```c
clilen = sizeof(cli_addr);
newsockfd = accept(sockfd, (struct sockaddr*) &cli_addr, &clilen);

if (newsockfd<0) {
	perror("Error accepting connection!");
}
```

- System call `accept()` accepts a connection request & is blocked to other requests while accepting connection request.
- It returns a new file descriptor which must be used to communicate with it in future.
- 2nd argument is pointer to the address of client.
- Note that 3rd argument is passed by reference.


### <u>Initializing Buffer</u>

```c
bzero(buffer, 256);
n = read(newsockfd, buffer, 256);    // Reads from socket.

if (n<0) {
	perror("Error reading from socket!");
}

printf("Buffer message: %s", buffer);
```

- The code above is only valid if our connection is successfully established.
- Note that it uses the new file descriptor `newsockfd` returned by `accept()`.
- `read()` reads when client has executed `write()` system call.
- And while reading, other `write()` signals are blocked.


### <u>Writing To Socket</u>

```c
n = write(newsockfd, "I got your message", 18);

if (n<0) {
	perror("Error writing to the socket!");
	exit(EXIT_FAILURE);
}
```

- Both ends can read & write to the connection.
- 3rd argument (`18`) is the size of the message.



## **Topic – 5: Client-Side Programming**

### <u>Headers</u>

```c
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
```

- `netdb.h` defines structure of `hostent` which we will be using soon.


### <u>Main Function</u>

```c
int main(int argc, char *argv[])
{
	int sockfd, portno, n;
	struct sockaddr_in serv_adddr;
	struct hostent *server;
	
	/* Rest of the code... */
}
```

- `serv_addr` will contain the address of the server we want to connect to.
- Variable `server` is a pointer to a structure of type `hostent`.


### <u>Hostent Definition</u>

```c
struct hostent
{
	char *h_name;          // "Official" name of host.
	char **h_aliases;      // 0 terminated array of aliases.
	int h_addrtype;        // Mostly AF_NET
	int h_length;          // In bytes.
	char **h_addr_list;    // Pointer to list
	
	#define h_addr h_addr_list[0]
};
```

- `hostent` is for defining host computer on the internet.
- The last line is for backward compatibility.
- Means if someone uses `h_addr` which is actually an old macro, it works same as `h_addr_list[0]`, pointing to first address on list.
- These are returned in network byte order.


### <u>Common Code</u>

- This code is present in both server & client program.

```c
char buffer[256];

if (argc<3) {
	fprintf(stderr, "Enter portno for host %s", argv[0]);
	exit(EXIT_FAILURE);
}

portno = socket(AF_NET, SOCK_STREAM, 0);

if (sockfd<0) {
	perror("Error opening socket!");
}
```


### <u>Confirming Host Name</u>

```c
server = gethostbyname(argv[1]);

if (server==NULL) {
	fprintf(stderr, "There is no host named %s", server);
}
```


### <u>Function "Get Host By Name" Declaration</u>

```c
struct hostent *gethostbyname(char *name);
```

- This returns information related to host.
- Field `char *name` contains the IP address.
- Earlier, function `gethostbyname()` was used for finding file systems online.
- Now it is used for querying large databases around the country.


### <u>Converting Port Number</u>

```c
bzero((char*) &serv_addr, sizeof(serv_addr));
serv_addr.sin_family = AF_INET;

bcopy((char*)server->h_addr,               // IP address
	 (char*)&serv_addr.sin_addr.s_addr,    // Integer storing IP
	 server->h_length                      // Host address length
);

serv_addr.sin_port = htons(portno);
```

- Function `bcopy()` copies IP address from buffer to our structure member `s_addr`.


### <u>Function BCopy Definition</u>

```c
void bcopy(char *s1, char *s2, int length);
```


### <u>Connecting To Client Socket</u>

```c
if (connect(sockfd, &serv_addr, sizeof(serv_addr)) < 0)
{
	perror("Error connecting!");
}
```

- This function returns `0` if connected successfully, else `-1` if it fails.
- Client requires port number for the server but not for itself because that is automatically assigned to one during connection.


### <u>Remaining Code</u>

```c
	/* Upper part of the code... */
	
	printf("Please enter the message: ");
	bzero(buffer, 256);
	fgets(buffer, 255, stdin);
	
	n = write(sockfd, buffer, strlen(buffer));
	
	if (n<0) {
		perror("Error reading from socket!");
	}
	
	printf("%s", buffer);
	
	return 0;
}
```



## **Topic – 6: Server Code Enhancement**

### <u>Introduction</u>

- The server we created runs & dies after running once.
- Real world server must run indefinitely without dying & must be able to handle multiple connections.
- We can do this by forking off a new process to handle each connection.
- Let’s consider a dummy function `dostuff(int sockfd)` for doing this.


### <u>Indefinitely Running Server</u>

1. Make an infinite loop.
2. Establish a connection.
3. Call `fork()` to create new process.
4. Call `dostuff()` to establish a new connection.
5. Close the child process if required, the new connection will still remain.


### <u>The Zombie Problem</u>

- The code above might create zombie problem.
- If a lot of connections are accepted, then these connections create a zombie when terminated.
- **<u>Zombie process</u>:** A process which doesn’t fully die.
- Parent process may not let their child die & rather put them into wait state.
- These processes in wait state clog the process table.
- But the code preventing zombie processes varies across architectures.
- A dying child sends a `SIGCHLD` signal to its parent.

```c
signal(SIGCHLD, SIG_IGN);    // AIX systems
signal(SIGCHLD, wait3(NULL, WNOHANG, NULL));    // SunOS
```



## **Topic – 7: Alternatives**

### <u>Introduction</u>

- What we saw earlier was a stream socket.
- One major difference between stream socket & datagram socket is that datagram socket is used when only one message has to be sent from client to server or vice-versa.


### <u>Stream Sockets v/s Datagram Sockets</u>

| **Datagram Sockets**                                                                                                | **Stream Sockets**                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Unreliable, as it uses UDP protocol which has absence of acknowledgement system.                                    | Reliable as it has TCP protocol which detects lost packets through acknowledgement system & these messages are retransmitted. |
| Data has to reach the receiver all at once.                                                                         | Receiver can read it in chunks of byte(s).                                                                                    |
| Uses sendto() & receivefrom() system calls.                                                                         | Uses read() & write() system calls.                                                                                           |
| Less overhead due to no need of setting up & then disbanding connections, plus packets need not to be acknowledged. | High overhead due to various factors.                                                                                         |
| Used where short-term service is required.                                                                          | Used where long-term service is required.                                                                                     |


### <u>Differences In Code</u>

```c
sock = socket(AF_INET, SOCK_DGRAM, 0);
fromlen = sizeof(struct sockaddr_in);

while (1)
{
	n = recvfrom(sock, buf, 1024, 0, (struct sockaddr*)&from, &fromlen);
	
	if (n<0) {error("recvfrom");}
	
	/* More code below... */
```

- `recvfrom()` is used to read messages.
- It will block other system calls until the message is received.
- First three arguments are same as in `SOCK_STREAM`.
- 4th argument is integer for flags, `0` by default.
- 5th one is a pointer to `sockaddr` in structure.
- 6th one is the size required for structure in 5th argument, in number of bytes.
- The 6th argument however returns `-1` instead if any error is caused.


### <u>Differences In Code – II</u>

```c
	/* Upper part discussed previously */
	
	n = sendto(sock, "Got your message", 17, 0, (struct sockaddr *)&from, fromlen);
	
	if (n<0) {
		error("sendto");
	}
}
```

- In `sendto()`, first three arguments are same as it was in `write()`.
- 3rd argument is number of bytes to write.
- 4th argument is flag, set to zero by default.
- **5<sup>th</sup>** argument is pointer to structure `sockaddr_in`.
- 6th (last) argument is size of the structure.
- We have to retrieve the values from the structure through the `recvfrom()` call.
- Notice the differences that there is no `connect()` call.



## **Topic – 8: Sockets In The UNIX Domain**

```c
struct sockaddr_un
{
	short sun_family;      // AF_UNIX
	char sun_path[108];    // Path name (gag)
};
```

- `sun_path` has the path name in UNIX file system.
- So, the client & server must be running on same file system.
- A socket always remains until it is manually deleted.
- **<u>Named pipes</u>:** IPC supporting transfer of data using FIFO principle.



## **Topic – 9: Designing Servers**

### <u>Concurrent & Connection Oriented Servers</u>

- In general servers, a stream socket is created & a new process is forked each time to handle a connection when it is established.
- This model is good for telnet or FTP servers.
- TCP protocol is general has high overhead on kernel.
- Though having high overhead, the data transmission is reliable.


### <u>Iterative & Connectionless Servers</u>

- Servers with single message to be delivered to a client doesn’t involve forking.
- These include ***finger daemon***, ***timeofday*** or an ***echo***
  server.
- **<u>Finger daemon</u>:** A server model used earlier to retrieve basic user information from remote servers such as name, email etc.
- **<u>Timeofday</u>:** A server model used to synchronize time on computers connected over same server.
- **<u>Echo</u>:** A server that just echoes the message sent by the client.
- These methods have less overhead but are unreliable.


### <u>Single Process Concurrent Servers</u>

- Here only one process is required.
- The server listens for connections & replies them quickly before
  breaking it and listening for another connection.

---
