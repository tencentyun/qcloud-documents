When creating or editing a cloud function, you can modify the network configuration in the advanced configurations to allow the cloud function access VPC.

## Editing Network Configuration

When creating or editing a function, click the **Show Advanced Settings** button to show the advanced settings.

Go to **Advanced Settings** -> **Network**, select the needed VPC network and subnet. If no VPC network exists in the current region, click **New Network** to enter the VPC console to create one. You can also click **New Subnet** to create a subnet under the VPC network.

You can switch the network environment of cloud function back to the current independent network environment by selecting `No` in the network options.

## Viewing Network Configuration

After the network configuration of cloud function is completed, you can learn about the specific configurations by checking the **Network** and **Subnet**.

## Using VPC Network

After the configuration is completed and the VPC network starts to be used, the network environment of this cloud function will be switched from the current independent network environment to the user's VPC. When the cloud function is running, it will occupy the IP in the user's VPC subnet as the IP in the operating environment of cloud function.

> **Note** 
> Make sure that there are enough available idle IPs in the subnet. The IP allocation failure caused by insufficient idle IP will lead to cloud function running failure.



After the cloud function is running, other products within the VPC can be accessed through codes, such as [Redis](https://cloud.tencent.com/product/crs?idx=1), [CDB](https://cloud.tencent.com/product/cdb-overview), or the products or services that are configured to be accessed via VPC (e.g. CVM in VPC). They can be accessed directly through the VPC IP. Here is an sample code for accessing [Redis](https://cloud.tencent.com/product/crs?idx=1), where the IP of Redis instance in the VPC is `10.0.0.86`.

```
# -*- coding: utf8 -*- 
import redis

def main_handler(event,context):
    r = redis.StrictRedis(host='10.0.0.86', port=6379, db=0,password="crs-i4kg86dg:abcd1234")
    print(r.set('foo', 'bar'))
    print(r.get('foo'))
    return r.get('foo')
```

After the cloud function is switched to the VPC network environment, it will be unable to access the public network as in the original independent network environment. If it needs to access the public network, you can configure [Public Gateway](https://cloud.tencent.com/document/product/215/11119) and [NAT Gateway](https://cloud.tencent.com/document/product/215/4975).

## Application Scenarios

* VPC Service Access: Access to databases, Redis, Kafka and other products or services in VPC to ensure data security and safe connection.
* Access Control: Access the public network via the same VPC IP.

