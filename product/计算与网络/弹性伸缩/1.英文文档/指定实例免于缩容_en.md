## Introduction

You can specify a submachine in the scaling group to be protected from being scaled down in the scale-down activity. If a scale-down activity occurs, AS will choose a submachine to be scaled down from other CVMs.

You can enable instance protection configuration for one or more scaling group instances. You can modify the scaling group or the instance protection configuration at any time.

If the scaling activity occurs when all the remaining instances in the scaling group are protected from being scaled down, AS will decrease the required capacity instead of removing any instances.

## Applicable Scenario

Normally, the CVMs in the scaling group are stateless, and can be removed at any time. In practice, however, the following conditions are applicable to protect specified instances from being scaled down:

- **One server for multiple uses:** In consideration of costs, apart from the tasks specified by the cluster, a server in the cluster is also used for other purposes. For example, the server may be used for storing the data generated in the cluster, so this server is actually stateful.

- **Avoid misoperation:** If you worry that the service will be affected due to policy setup failure, you can set "scale-down exemption" for some servers. In this way, AS will never scale these servers down, and the tunnel "Request-LB-Submachine" will remain unblocked.

## Setup
In the list of submachines of the scaling group, you can directly set:
![](https://mc.qcloudimg.com/static/img/62319473a1a05e98d51c64c22ca24424/0308113553.jpg)

