The working principle of load balancing which is based on the resolution is to return different IP addresses to users. Take the following resolution for example:

| Host Name | Record Type | Line Type | Record Value | TTL |
|---|---|---|---|---|
| www | A | Default | 200.202.101.1 | 600 |
| www | A | Default | 200.202.101.2 | 600 |
| www | A | Default | 200.202.101.3 | 600 |
| www | A | Default | 200.202.101.4 | 600 |

The IP address acquired from the returned resolution result is an address randomly acquired by polling, and it is not assigned according to the server load and operation status. If there are multiple servers under the same line and access traffic needs to be equally allocated to each server, you can use Cloud DNS to achieve load balancing.

>**Note:**
> The number of load balancers that can be configured is different for different dns packages.

| DNS Package  | Minimum TTL |
|---|---|
| Free Package | 2 |
| Individual Professional Package | 10 |
| Enterprise Basic Package | 15 |
| Enterprise Standard Package | 30 |
| Enterprise Ultimate Package | 60 |

