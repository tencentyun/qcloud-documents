## Product Overview
#### What is WS/WSS?
WebSocket is a protocol which performs full-duplex communication over the single TCP connection.
WebSocket makes it easier to exchange data between client and server, and allows active data push from server to client. In WebSocket API, only one handshake between browser and server is required before a persistent connection between them is created and two-way data transmission is carried out.

#### Why do we use WS/WSS?
Without WebSocket, the client had to pull data from the server through polling when data on the server are needed.
There are two shortcomings in this data exchanging method:
1. Low efficiency. When real-time data are needed, the client has to initiate Ajax requests frequently to pull data.
2. The server cannot push data actively.
WebSocket is designed to solve these problems. WebSocket is a new protocol released with HTML5. It achieves full-duplex communication between browser and server, and can transmit message-based texts and binary data. WebSocket solves the above problems of HTTP at protocol level.

Key advantages of WebSocket:
1. Lower control cost After the connection is established, the header used for control is small. A complete header is required in each HTTP request, but there is no such requirement in WebSocket, so the corresponding cost can be reduced significantly.
2. Satisfactory real-timeness. As a full-duplex protocol, WebSocket can achieve the real-time data push from server to client.
3. Capable of maintaining connection status.

## Product Purchase
#### How is WS/WSS billed?
CLB supports WS/WSS by default and no additional fee will be charged.

## Product Implementation
#### How to enable WS/WSS on CLB?
**WS/WSS is enabled by default and no additional configuration is required**.
If the listener listens to HTTP, WS is supported by default. If it listens to HTTPS, WSS is supported by default.
When WSS is used, CLB will unmount SSL.

#### Which regions support WS/WSS?
WS/WSS protocols are supported for **All regions**.


