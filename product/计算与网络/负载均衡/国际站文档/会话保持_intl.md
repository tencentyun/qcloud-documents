Session persistence allows the requests from the same IP to be forwarded to the same backend CVM. By default, load balancer routes each request to a different backend CVM instance. However, you can use session persistence feature to route requests from a specific user to the same backend CVM instance, so that some applications (such as shopping cart) that need to maintain the session state can work properly.

## Layer-4 Session Persistence
Layer-4 forwarding scenario supports simple session persistence. The session persistence duration can be set to any integer value within the range of `30-3600` seconds. If the time threshold is exceeded and there is no new request in the session, the session will be disconnected.

## Layer-7 Session Persistence
Layer-7 forwarding scenario supports session persistence based on cookie insertion (the cookie is stuffed into the client by load balancer). Session duration range is 30-3600s. For more information on session persistence based on cookie insertion, please see [Session Persistence Principles](https://cloud.tencent.com/document/product/214/2736).

## Connection Timeout
HTTP connection timeout (keepalive_timeout) is not adjustable and the default is `75` seconds. If there is no data transfer in the session for a period exceeding the time threshold, the session will be disconnected.
TCP connection timeout is not adjustable and the default is `900` seconds. If there is no data transfer in the session for a period exceeding the time threshold, the session will be disconnected.

## Configuring Session Persistence
1. Log in to the [CLB Console](https://console.cloud.tencent.com/loadbalance), then click the ID of the load balancer instance that needs session persistence configurations to go to its details page.

2. Click the **Modify** button next to the load balancer listener that needs session persistence configurations.

3. Set whether to enable the session persistence feature. Click the button to enable it, then enter the persistence duration, and click **OK**.

## Relationship Between Persistent Connection and Session Persistence

### Scenario 1: HTTP Layer-7 Business

**Assume that the client access protocol is HTTP/1.1, and "Connection: keep-alive" is set in the header information. If the backend CVM is accessed through the CLB with session persistence disabled, is it possible to access the same CVM next time?**

**A:** No.

First of all, HTTP keep-alive means that the TCP connection remains connected after requests are sent. Therefore, the browser can continue to send requests over the same connection. Keeping connected can save the time and bandwidth taken to set up a new connection for each request. The default timeout for a CLB cluster is `75` seconds(if there is no new request within `75` seconds, the TCP connection is disconnected by default).

HTTP keep-alive is established by the client with the CLB. If the cookie session persistence is disabled, the CLB will randomly select a backend CVM according to the polling policy. The previous persistent connection is in vain.

Therefore, it is recommended to enable session persistence.

If the cookie session persistence is set to `1,000` seconds and the client initiates another request, TCP connection needs to be re-established, because it has been more than 75s since the last request is sent. The application layer finds the same CVM by cookie, and the CVM accessed by the client is still the one used for the last access.

### Scenario 2: TCP Layer-4 Business

**Assume that the client initiates the access using TCP as the transport layer protocol, and persistent connection is enabled, but source IP-based session persistence is disabled, can the same client access the same CVM next time?**

**A:** Uncertain.

First of all, according to the layer-4 implementation mechanism, if the persistent connection is enabled for TCP and remains connected, the same CVM can be accessed, because the two accesses use the same connection. However, if the first connection is released due to some reason (network restart or connection timeout), the second access may be dispatched to other backend CVMs. Besides, the global timeout for persistent connection is `900` seconds by default, which means that the persistent connection will be released if there is no new request.
