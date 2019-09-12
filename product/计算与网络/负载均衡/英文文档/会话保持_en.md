Session persistence allows the requests from the same IP to be forwarded to the same backend CVM. By default, cloud load balancer routes each request to a different backend CVM instance. However, you can use session persistence feature to route requests from a specific user to the same backend CVM instance, so that some applications (such as shopping carts) that need to maintain the session state can work properly.

## Layer-4 Session Persistence
Layer-4 forwarding scenario supports simple session persistence. The session persistence duration can be set to any integer value within the range of `0-3600` seconds. If the time threshold is exceeded and there is no new request in the session, the session will be disconnected.

## Layer-7 Session Persistence
Layer-7 forwarding scenario supports session persistence based on cookie insertion (the cookie is stuffed into the client by cloud load balancer). Session duration range is 30-3600s. For more information on session persistence based on cookie insertion, refer to [Session Persistence Principles](https://intl.cloud.tencent.com/document/product/214/2736).

## Connection Timeout
HTTP connection timeout (keepalive_timeout) is not adjustable for now and its default is `75` seconds. If there is no data transfer in the session for a period exceeding the time threshold, the session will be disconnected.
TCP connection timeout is not adjustable for now and the default is `900` seconds. If there is no data transfer in the session for a period exceeding the time threshold, the session will be disconnected.

## Configuring Session Persistence
1. Log in to [Cloud Load Balance Console](https://console.cloud.tencent.com/loadbalance), then click the ID of the cloud load balancer instance that needs session persistence configurations to go to the cloud load balancer details page.

2. Click the "Modify" button next to the cloud load balancer listener that needs session persistence configurations.

3. Set whether to enable the session persistence feature. Click the button to enable it, then enter the persistence duration, and click "OK".

## Relationship Between Persistent Connection and Session Persistence

### Scenario 1: HTTP Layer-7 Business

**Assuming that Client access protocol is HTTP/1.1, and Connection: keep-alive is set in header information, if the backend CVM is accessed through the CLB with session persistence disabled, is it possible to access the same CVM next time?**

**A:**No. 

First of all, HTTP keep-alive means that the TCP connection will remain connected after requests are sent. Therefore, the browser can continue to send requests over the same connection. Keeping connected saves the time taken to set up a new connection for each request and also bandwidth. The default timeout for a CLB cluster is 75s (if there is no new request within 75s, the TCP connection is disconnected by default).

HTTP keep-alive is established by the Client with the CLB. If the cookie session persistence is disabled, the CLB will randomly select a backend CVM according to the polling policy. The previous persistent connection is in vain.

Therefore, it is recommended to enable session persistence.

If the cookie session persistence is set to 1000s and the Client initiates another request, TCP connection needs to be re-established, because it has been more than 75s since the last request. The application layer finds the same CVM by cookie and the CVM accessed by the Client is still the one for the last access.

### Scenario 2: TCP Layer-4 Business

**Assuming that client initiates the access with TCP as the transport layer protocol and persistent connection is enabled, but source IP-based session persistence is disabled, can the same Client access the same machine?**

**A:**Uncertain.

First of all, according to the Layer-4 implementation mechanism, if the persistent connection is enabled for TCP and keeps connected, the same machine can be accessed, because the two accesses use the same connection. But if the first connection is released due to some reason (network restart or connection timeout) during the second access, the second access may be dispatched to other backend CVMs. And the global timeout for persistent connection is 900s by default, which means that the persistent connection will be released if there is no new request.

