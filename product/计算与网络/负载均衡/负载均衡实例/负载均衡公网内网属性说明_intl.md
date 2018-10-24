## Public Network Load Balancer Instances

Public network load balancer instances get requests from the client over the Internet, and allocates these requests to the backend CVMs bound with listeners. After a public network load balancer is created, Tencent Cloud assigns a public network domain name (traditional) and a VIP address to the load balancer. At the same time, DNS server resolves the domain name and VIP address. A public network load balancer also supports binding CNAME and A Record, and mapping them to user-readable custom domain names. Each public network load balancer instance is assigned a fixed BGP public IP and can receive the HTTP, HTTPS, TCP, and UDP requests forwarded from the client. Such instances also support all Tencent Cloud Load Balance services such as session persistence and health check. For more information on the use limits of public network load balancer instances, please see [Use Limits](/doc/product/214/6187).

You can add multiple [load balancer listeners](/doc/product/214/6151) to a public network load balancer instance to forward different requests.

### Public network DNS domain name

Each traditional public network load balancer instance is assigned a fixed domain name with the following format by default:

```
<name>.<region>.<number>.clb.myqcloud.com
```

`<name>` and `<number>` are system-generated strings, and `<region>` is the ID of the region where the load balancer instance resides.

### Application scenarios
- When a server cluster is used to provide services to the public network, a single entry needs to be provided, and public network user requests need to be properly allocated to the server cluster;
- When fault tolerance and fault recovery are needed for the server cluster;
- When connecting the users of different ISPs to the networks closest to them to improve the network access speed;

In the above cases, it is recommended to use public network load balancers with a fixed IP.

### Billing
- A traditional or application-based public network load balancer instance costs 0.003 USD/hour.
- Any public network bandwidth/traffic generated with this service is charged to the bill for backend CVMs. For more information, please see [Purchase Network Bandwidth](https://cloud.tencent.com/doc/product/213/509).

### Create a public network load balancer instance
For more information on how to create a public network load balancer instance, please see [Creating a Load Balancer Instance](/doc/product/214/6149).

## Private Network Load Balancer Instances

Private network load balancers can only be accessed from within Tencent Cloud, and cannot be accessed over the Internet (No public network domain name or public IP is available). A private network load balancer properly allocates the requests that are sent from private network client to CVMs to the CVM cluster via the corresponding VIP.

A private network load balancer routes the traffic to the backend CVMs in the same region by using [private IP](/doc/product/213/5225), and this is how an internal CVM cluster is formed. If the application has a multi-layered architecture (such as Web servers that can communicate with the Internet and database servers that can only communicate with each other via private networks but cannot communicate with the Internet), you can design an architecture with both private network and public network load balancer instances. You can connect all the Web servers to the public network load balancer instance, and connect the database servers to the private network one. The public network load balancer instance receives requests from the Internet and sends them to the backend Web servers. After processing, the requests for databases are sent to the private network load balancer, which then routes the requests to the database servers.

### Application scenarios

The client and server of private network load balancer are both inside Tencent Cloud and can be accessed via the private network of Tencent Cloud. The main scenarios are as follows:
- When Tencent Cloud has more than one internal servers and the requests from client need to be allocated to the servers properly;
- When fault tolerance and fault recovery are needed for the internal server cluster;
- When the service provider wants to block its own physical IP address and provide transparent services to the client;

In the above cases, it is recommended to use private network load balancer.

### Billing

Private network load balancers are free of charge.

### Create a private network load balancer instance
For more information on how to create a private network load balancer instance, please see [Creating a Load Balancer Instance](/doc/product/214/6149).
