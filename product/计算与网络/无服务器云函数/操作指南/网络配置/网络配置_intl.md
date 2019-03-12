When creating or editing an SCF, you can modify the network configuration in the advanced settings to allow the SCF to access VPCs.

## Editing Network Configuration

When creating or editing an SCF, click the **Display Advanced Settings** button to display the advanced settings.

You can select an appropriate VPC and subnet via **Advanced Settings** -> **Network**. If no VPC network exists in the current region, click **New Network** to enter the VPC console to create one. You can also click **New Subnet** to create a subnet under the VPC network.

You can switch the network environment of an SCF back to the current independent network environment by selecting `None` in the network options.

## Viewing Network Configuration

After the SCF's network configuration is completed, you can see the specific configurations via **Network** and **Subnet**.

## Using VPC Network

After the configuration is completed and the VPC network is put into use, the network environment of this SCF will be switched from the current independent network environment to the user's VPC. When the SCF starts running, the IP of the user's VPC subnet is used as the IP of the operating environment.

> **Note** 
> Make sure idle IPs in the subnet are sufficient. The IP allocation failure caused by insufficient idle IPs will lead to SCF running failure.



After the SCF is launched, other products within the VPC can be accessed through codes, such as [Redis](https://cloud.tencent.com/product/crs?idx=1), [CDB](https://cloud.tencent.com/product/cdb-overview), or products or services (e.g. CVM in VPC) that are configured to be accessed via VPC. They can be accessed directly through the VPC IP. The following is a sample code for accessing [Redis](https://cloud.tencent.com/product/crs?idx=1). The IP of the Redis instance in the VPC is `10.0.0.86`.

```
# -*- coding: utf8 -*- 
import redis

def main_handler(event,context):
    r = redis.StrictRedis(host='10.0.0.86', port=6379, db=0,password="crs-i4kg86dg:abcd1234")
    print(r.set('foo', 'bar'))
    print(r.get('foo'))
    return r.get('foo')
```

After the SCF is switched to the VPC network environment, it will be unable to access the public network as in the original independent network environment. To allow the SCF to access the public network, [configure the public gateway](https://cloud.tencent.com/document/product/215/11119) or [configure the NAT Gateway](https://cloud.tencent.com/document/product/215/4975).

### Name server Configuration in VPC

After the network attribute of the SCF is set to VPC, to access the self-built services in the VPC via domain name, you need to implement domain name resolution with the custom name server.

You can use the `OS_NAMESERVER` environment variable to customize the name server configuration within the SCF environment.

| Environment variable name | Value setting rule | Feature |
| --- | --- | --- |
| OS_NAMESERVER | One or more IPs/domain names (separated with semicolons ";"). A maximum of 5 custom name servers can be configured. | Configure custom name server |

Check whether the configuration has taken effect by printing the output file /etc/resolv.conf.

```
with open("/etc/resolv.conf") as f:
    print(f.readlines())
```


## Application Scenarios

* VPC Service Access: Access databases, Redis, Kafka and other products or services in VPCs to ensure data and connection security.
* Access Control: Access the public network via the same VPC IP.

