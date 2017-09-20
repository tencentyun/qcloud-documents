Session persistence allows the requests from the same IP (network segment) to be forwarded to the same back-end CVM.  By default, cloud load balancer routes each request to a different back-end CVM instance.  However, you can use session persistence feature to route requests from a specific user to the same back-end CVM instance, so that some applications (such as shopping carts) that need to maintain the session state can work properly. 



## Layer-4 Session Persistence
Layer-4 forwarding scenario supports simple session persistence. The session persistence duration can be set to any integer value within the range of `0-3600` seconds. If the time threshold is exceeded and there is no new request in the session, the session will be disconnected. 

## Layer-7 Session Persistence
Layer-7 forwarding scenario supports session persistence based on cookie insertion (the cookie is stuffed into the client by cloud load balancer) 

Session persistence duration is not adjustable currently and the default is `75` seconds.  If the time threshold is exceeded and there is no new request in the session, the session will be disconnected.  For more information on session persistence based on cookie insertion, refer to [here](https://www.qcloud.com/doc/product/214/%E4%BC%9A%E8%AF%9D%E4%BF%9D%E6%8C%81%E5%8E%9F%E7%90%86). 

## Configuring Session Persistence
1) Log in to [Cloud Load Balance Console](https://console.qcloud.com/loadbalance), click the cloud load balancer instance ID to be configured with session persistence and go to the cloud load balancer details page. 

2) Click the "Modify" button after the cloud load balancer listener to be configured with session persistence. 

3) Select whether to enable the session persistence feature, click the button to enable it, enter the persistence duration, and click "OK". 


