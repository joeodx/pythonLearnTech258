# What are API's? 

![api's](https://appmaster.io/api/_files/PqV7MuNwv89GrZvBd4LNNK/download/)

APIs are mechanisms that enable two software components to communicate with each other using a set of definitions and protocols. For example, the weather bureau’s software system contains daily weather data. The weather app on your phone “talks” to this system via APIs and shows you daily weather updates on your phone.

API stands for Application Programming Interface. In the context of APIs, the word Application refers to any software with a distinct function. Interface can be thought of as a contract of service between two applications. This contract defines how the two communicate with each other using requests and responses. Their API documentation contains information on how developers are to structure those requests and responses.

## How do API's work?

API architecture is usually explained in terms of client and server. The application sending the request is called the client, and the application sending the response is called the server. So in the weather example, the bureau’s weather database is the server, and the mobile app is the client. 

There are four different ways that APIs can work depending on when and why they were created.

* **SOAP APIs** : 
These APIs use Simple Object Access Protocol. Client and server exchange messages using XML. This is a less flexible API that was more popular in the past.

  
* **RPC APIs** : 
These APIs are called Remote Procedure Calls. The client completes a function (or procedure) on the server, and the server sends the output back to the client.


* **Websocket APIs** : 
Websocket API is another modern web API development that uses JSON objects to pass data. A WebSocket API supports two-way communication between client apps and the server. The server can send callback messages to connected clients, making it more efficient than REST API.


* **REST APIs** :
These are the most popular and flexible APIs found on the web today. The client sends requests to the server as data. The server uses this client input to start internal functions and returns output data back to the client. Let’s look at REST APIs in more detail below.

APIs are surprisingly significant in the current world as they dictate how software developers create new applications that utilize web services like Facebook, Google Maps, and many more. APIs are also great time savers. They offer a tremendous level of accessibility in many ways.

## What is a REST API?

A REST API (Representational State Transfer Application Programming Interface) is a type of API that follows the principles of REST architecture. REST is an architectural style for designing networked applications. RESTful APIs adhere to these principles, making them easy to use, scalable, and interoperable with other systems.

Here are the key principles that make an API RESTful:
* **Client-Server Architecture** : The client and server are separate entities, each with its concerns. Clients are not concerned with data storage, while servers are not concerned with user interfaces.


* **Statelessness**: Each request from a client to the server must contain all the necessary information to understand the request. The server should not store any client context between requests. This simplifies the server implementation and improves scalability.


* **Manipulation of Resources Through Representations** : Clients interact with resources by exchanging representations of the resource's state. For example, using HTTP methods like GET, POST, PUT, DELETE to perform CRUD operations (Create, Read, Update, Delete) on resources.

<br>
Example of a REST API in action : 
<br> 



![api's](diagram.jpg)

<br>
As for REST API guidelines, they often include best practices for designing APIs that adhere to REST principles, here are a few below :

* Use nouns to represent resources (e.g., /users for a collection of users).
* Use HTTP methods (GET, POST, PUT, DELETE) to perform CRUD operations on resources.
* Version your API to allow for changes without breaking existing clients (e.g., /v1/users).
* Document your API thoroughly, including endpoints, request and response formats, and authentication methods.
* Use security measures like HTTPS and authentication mechanisms to protect your API from unauthorized access.


## What is HTTP... and how is it different to HTTPS?


![http](https://snobmonkey.com/wp-content/uploads/2019/04/main-qimg-3f16c3d0b203e53638cf38a7a7042da1.png)

<br>
The Hypertext Transfer Protocol (HTTP) is the foundation of the World Wide Web, and is used to load webpages using hypertext links. HTTP is an application layer protocol designed to transfer information between networked devices and runs on top of other layers of the network protocol stack. A typical flow over HTTP involves a client machine making a request to a server, which then sends a response message.

Hypertext transfer protocol secure (HTTPS) is the secure version of HTTP, which is the primary protocol used to send data between a web browser and a website. HTTPS is encrypted in order to increase security of data transfer. This is particularly important when users transmit sensitive data, such as by logging into a bank account, email service, or health insurance provider.

HTTPS uses an encryption protocol to encrypt communications. The protocol is called Transport Layer Security (TLS), although formerly it was known as Secure Sockets Layer (SSL). This protocol secures communications by using what’s known as an asymmetric public key infrastructure. This type of security system uses two different keys to encrypt communications between two parties:

* **The private key** - this key is controlled by the owner of a website and it’s kept, as the reader may have speculated, private. This key lives on a web server and is used to decrypt information encrypted by the public key.
* **The public key** - this key is available to everyone who wants to interact with the server in a way that’s secure. Information that’s encrypted by the public key can only be decrypted by the private key.





