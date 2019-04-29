BM load balancer is a service used to distribute traffic to multiple CPMs. BM load balancer can extend the external service capabilities of application systems through traffic distribution and improve their availability by eliminating single point of failure.

BM load balancer virtualizes multiple CPM resources located in the same availability zone into an application service pool with high-performance and high-availability by setting a virtual IP (VIP), and distributes the network requests from the client to the CPM pool in a way specified by the application. BM load balancer can check the health status of CPMs in the server Pool, and automatically isolate abnormal CPMs, thus dealing with the single point of failure of a single CPM and improving the overall service capability of applications.

## Key Features
* Multi-tenant isolation using Vxlan
* IP Convergence in FULLNAT mode
* High reliability through cluster disaster recovery and session synchronization
* Anti-DDoS attacks with Aegis and synproxy

## Application Scenarios
* Scaling-out service capabilities of the application system, applicable to all kinds of web servers and App servers. 
* Eliminating single point of failure on the application system. If some of the CPMs crash, the application system can still work properly.

## Supported Protocols
BM load balancer is provided by its listeners. The listeners monitor requests on BM load balancer instance and distribute traffic to backend servers based on policies. The listeners are classified into Layer-4 and Layer-7 listeners. The Layer-4 listener uses transport layer protocol and receives requests and distributes traffic to the backend servers via VIP and ports, while the Layer-7 listener uses application-layer protocol and distributes traffic based on the application-layer information such as URL and HTTP header.

**1. Layer-4 Listener**
Supports TCP and UDP protocols. If TCP/UDP protocol is used for forwarding, the BM load balancer instance forwards the request directly to the backend instance without modifying any packets.

**2. Layer-7 Listener**
Supports HTTP and HTTPS protocols. Layer-7 listeners must establish a connection with the client as a proxy of the backend server (three-way handshake) to receive the message containing real application layer content from client, and then determines the backend forwarding server according to the specific fields in the message plus the server selection method.

## Balancing Mode
Balancing mode refers to the algorithm with which the BM load balancer distributes traffic to the backend server.

**1. Layer-4 Protocol**
Supports round-robin by weight. Round-robin by weight means scheduling requests to different servers in sequence in a round-robin approach. It uses weight values to represent the performance level of each server and distribute requests to the servers according to these weight values and round-robin approach. Servers with high weight values will receive connections first, and they process more connections than those with low weight values. Servers with the same weight value will process the same number of connections.

**2. Layer-7 Protocol**
Supports round-robin by weight and IP HASH. IP HASH means using the source IP address of the request as Hash Key and finding the corresponding server from the statically distributed hash table. The request will be sent to this server if the server is available and not overloaded, otherwise the response will be empty.

## Health Check
BM load balancer instances send ping to backend servers periodically, makes attempts to connect with them or sends requests to them to test for their running status.

If it is concluded that a backend server instance is unhealthy, BM load balancer instance will not forward requests to the instance. But health check will be performed on all backend servers, whether healthy or unhealthy, and when the unhealthy instance recovers to normal status, BM load balancer instance will resume forwarding new requests to it.

**1. Layer-4 Protocol**
BM load balancer initiates an access request to the server port specified in the configuration. If the access to the port is normal, the backend server is considered normal, otherwise it is considered abnormal. For TCP services, SYN packet is used for the check. For UDP services, ping command is used for the check.
* Response timeout: 2-60 seconds
* Check interval: 5-300 seconds
* Unhealthy threshold: 2-10 timeouts (When the response timeout has happened to a healthy backend server for the specified number of times, the backend server is considered unhealthy)
* Healthy threshold can be 2-10 successful responses (default to 3 responses). When an unhealthy server returns successful responses of the specified number of times, the backend server is considered healthy.

**2. Layer-7 Protocol**
BM load balancer sends an HTTP request to the backend server to check the backend services. BM load balancer determines the running status of the service based on whether the HTTP returned value is http_xxx (set by users). Users can, based on business needs, define http_1xx and http_2xx as normal status and the values from http_3xx to http_5xx as abnormal status.
* Response timeout is 3 seconds (can not be configured).
* Check interval can be 5-300 seconds (default to 6 seconds)
* Unhealthy threshold can be 2-10 timeouts (default to 3 timeouts). When the occurrence of response timeouts reach the specified threshold, the backend server is considered unhealthy.
* Healthy threshold can be 2-10 successful responses (default to 3 responses). When an unhealthy server returns successful responses of the specified number of times, the backend server is considered healthy.

## Session Persistence
Allows the requests from the same IP to be forwarded to the same backend server.

**1. Layer-4 Protocol**
Layer-4 forwarding supports session persistence based on source address. The session persistence duration can be set to any integer value within the range of 30-3600 seconds. If the time threshold is exceeded, the session persistence will expire.

**2. Layer-7 Protocol**
Layer-7 forwarding supports session persistence based on cookie insertion (the cookie is stuffed into the client by BM load balancer). Session duration range is 30-3600s.

## Obtaining Client IP
**1. Layer-4 Protocol**
- Public network generic/Private network LB: Obtains client IP by installing a TOA module on the backend server when TCP protocol is used and the backend server is Linux. BM LB end is disabled by default.
- Public network enhanced LB: Client IP can be obtained when TCP/UDP protocol is used and the backend server is Linux/Windows.

**2. Layer-7 Protocol**
Obtains client IP through X-Forwarded-For. BM LB end is enabled by default.

## Service Limits
Limits on the usage of BM LB are as follows:
<table class="table-striped">
	<tobdy>
		 <tr>
      <th width="90">LB Type</th>
      <th>Layer-4 Listener</th>
      <th>Layer-7 Listener</th>
      <th>General Use Limits</th>
   </tr>
		 <tr>
		 <td align="center" >Private network LB</td>
		  <td rowspan="3" frame=vsides>
			A maximum of 50 listeners can be created for one LB.<br/>
			A maximum of 200 servers can be connected to one listener.<br/>
			A maximum of 200 ports of the same server can be bound to one listener.</td>
			<td rowspan="2" >
			A maximum of 50 listeners can be created for one LB.<br/>
			A maximum of 100 forwarding domain names can be configured under one listener.<br/>
			A maximum of 100 forwarding URLs can be configured under one forwarding domain name.<br/>
			A maximum of 255 servers can be configured under one forwarding URL.<br/>
			A maximum of 255 ports of the same server can be bound to one URL.</td>
			<td rowspan="3">The upper purchase limit is 100 for each type in each zone.</td>
		 <tr><td >Public network generic LB</td></tr>
		<tr><td >Public network enhanced LB</td><td>Not supported</td></tr>
		</tr>
	 </tbody>
</table>

