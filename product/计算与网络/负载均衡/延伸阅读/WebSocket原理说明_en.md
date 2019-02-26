Web application communication is typically made as such: the client browser sends a request; the server receives the request, process it, and return the result to the client; and then the client browser displays such information. This mechanism is suitable for applications that do not need to change information frequently, but it can barely handle applications that require quick real-time response and massive concurrent requests, especially in the fast-growing mobile-Internet industry where massive concurrent requests and real-time response are the two major problems often encountered by Web applications, such as real-time information on financial securities, geo-location access in Web navigation applications and real-time messaging of social networks.

In the traditional request-response mode, Web developers often use real-time communication to deal with such business scenario. A commonly-used solution is Round Robin. That is, the client sends requests to the server at a certain time interval to synchronize data between the client and the server, which is very easy to understand. However, this solution has an obvious weak point. When the client sends a request at a fixed frequency, the data in the server may not be updated, which causes plenty of unnecessary requests, waste of bandwidth and low efficiency.

Another solution is to use Flash/AdobeFlash. It achieves real-time transmission by implementing data exchange via Socket and exposing relevant APIs to JavaScript for calling. This solution is more efficient than Round Robin, for Flash has relatively high installation rate and broad application scenarios. However, Flash is not well supported on mobile-Internet terminals. It cannot be compatible with IOS system, and does not perform well on Android system due to high requirements on hardware configurations. In 2012, Adobe announced to cease development of Flash for Android 4.1 and above, which indicates the "death" of Flash on mobile terminals.

As traditional Web modes fail to meet the requirement of massive concurrent requests and quick real-time response, the industry is in urgent need for a highly efficient and energy-saving two-way communication mechanism that can keep real-time data transmission. That's where the HTML5 WebSocket (Web TCP) comes in. There was not a standard HTML5 in early development. Each browser and application server providers had a unique but similar application, such as IBM's MQTT and Comet open source framework. It was until 2014 that a standard HTML5 was formulated and put into practice by all application server and browser providers. A standard WebSocket protocol was also implemented in JavaEE7. From then on, the WebSocket has become available on both the client and the server. For more information on the new HTML protocol and WebSocket support, refer to [HTML5 Protocol](https://www.w3schools.com/html/default.asp).

## WebSocket Mechanism
The following is a brief introduction to the principle and operating mechanism of WebSocket.

WebSocket is a new protocol under HTML5. It provides full-duplex communication between the browser and the server, which can save server resources and bandwidth and achieve real-time communication. WebSocket and HTTP both transmit data via established TCP connections. Their differences are:
- WebSocket is a two-way communication protocol. Like Socket, WebSocket server and client can send/receive data to/from each other after establishing connections;
- WebSocket, like TCP, should establish connections before communicating with each other.

Traditional HTTP client-server request-response mode is shown as follows:
![](//mccdn.qcloud.com/static/img/c99efde0caccb49814ea83c126b0e18a/image.jpg)

WebSocket client-server request-response mode is shown as follows:
![](//mccdn.qcloud.com/static/img/e4128e588c6c21216319351ee7eb0bac/image.jpg)

As can be seen from the figures above, traditional HTTP mode should establish connections between the client and the server for each request - response session, while WebSocket uses a TCP persistent connection communication mode similar to Socket. Once the WebSocket connection is established, subsequent data is transmitted using a sequence of frames. The client/server does not need to re-send the connection request before the client/server disconnects the WebSocket connection. When dealing with massive concurrent requests or heavy client-server interaction traffic loads, WebSocket can significantly save network bandwidth resources, which is an obvious performance advantage. In addition, it enables the client to send and receive messages from one persistent connection, demonstrating great real-timeness.

WebSocket distinguishes itself from HTTP persistent connection in the following aspects:
- WebSocket is a true full-duplex mode, in which the client and the server are equal and can send/receive requests from/to each other after establishment of connections;  while the HTTP-based persistent connection is a traditional one-way mode in which only the server can send requests.
- In the HTTP persistent connection, whenever exchanging necessary data, the server and the client have to exchange a large number of HTTP headers, which leads to low data exchange efficiency;  On the contrary, the WebSocket protocol does not need to exchange HTTP headers any more after the establishment of TCP connections by the first request, provided that the server and the client are updated and their browsers support HTML5. Besides, WebSocket has some new functions including multiplexing and re-use of one WebSocket connection by different URLs,  which are impossible in HTTP persistent connection.


Now let's make a comparison between WebSocket and traditional HTTP based on their messages interacted between the client and the server:

The new WebSocket instantiates a new WebSocket client object on the client, and requests a WebSocket URL similar to ws://yourdomain:port/path from the server. The client WebSocket object automatically parses and recognizes the WebSocket requests, connects to the server port, and implements handshake process. The client sends data in the following format:

```
GET /webfin/websocket/ HTTP/1.1
Host: localhost
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: xqBt3ImNzJbYqRINxEFlkg==
Origin: http://localhost:8080
Sec-WebSocket-Version: 13
```

As can be seen from the above, the WebSocket connection message initiated by the client is similar to the traditional HTTP message. `Upgrade: websocket` indicates that this is a WebSocket type request. `Sec-WebSocket-Key` indicates that it is a base64-encoded message sent by the WebSocket client. The server must return a corresponding encrypted `Sec-WebSocket-Accept` response; otherwise, the client will throw the`Error during WebSocket handshake` error and close the connection.

After receiving the message, the server returns the data in the following format:

```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: K7DJLdLooIwIG/MOpvWFB3y3FE8=
```

`Sec-WebSocket-Accept` is the value returned to the client after calculated by the server using the same key as the client. `HTTP/1.1 101 Switching Protocols` indicates that the server accepts the client connection via the WebSocket protocol. After the completion of such request-response processing, the WebSocket connection between the server and the client successfully performs handshake, and the TCP communication will be established. For more information on the format of data interacted between the client and the server via WebSocket, refer to [WebSocket Protocol Stack](http://tools.ietf.org/html/rfc6455).

It's easy to create a WebSocket API. You need to instantiate the WebSocket, establish a connection, and then the server and the client can send/respond messages to each other. You can see the detailed WebSocket API and code implementation in WebSocket Implementation and Case Study.

Tencent Cloud public network-based (with daily rate) Layer-7 CLB is capable of forwarding Websocket requests. Currently, multiple companies including Calibur of Spirit and Yinhan Games have access to such capability. Please modify the WebSocket configuration if it is not compatible with your system. WebSocket server does not check the fields encircled in the following figure:

![](//mccdn.qcloud.com/static/img/53d8a8462bdf6d4ebe8e1134e40919ef/image.png)

If you want to apply WebSocket in your video business, you should:
- Use heartbeat to maintain the WebSocket link to detect whether the client's Internet stars/VJs are online
- Set proxy_read_timeout of Layer-7 CLB to 60s
- Set the heartbeat to 50s, so that the WebSocket can be connected for a long time

A custom configuration section for Websocket will be available in the future.
