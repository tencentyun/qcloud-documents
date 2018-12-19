Elastic public IP addresses are static IPs designed for dynamic cloud computing. It is a fixed public IP of a certain area. With flexible public IP addresses, you can quickly remap addresses to another CVM instance in your account (or [NAT Gateway](https://cloud.tencent.com/doc/product/215/%E7%BD%91%E5%85%B3#2.-nat.E7.BD.91.E5.85.B3) instance), thereby blocking instance failures.

Your elastic IP address is associated with a Tencent Cloud account, not with a CVM instance, and it remains associated with your Tencent Cloud account until you choose to explicitly release it or if you owe fees for more than 7 days.

## Scope

The elastic public IP address applies to both the CVM instance of the underlying network and private network, and the [NAT Gateway](/doc/product/215/4975) instance in the private network. An elastic public IP address can only be bound to a CVM/NAT Gateway instance in the same region. Dynamic binding and unbinding are supported.

>Note:
- One elastic public IP can be bound to only one CVM/NAT Gateway at the same time
- One CVM/NAT Gateway instance can bind only one elastic public IP at the same time

When binding an elastic IP to a CVM instance, the current public IP of the instance will be released to the public IP address pool of the underlying network. If you choose to reassign the public IP when the IP address is unbound from the CVM instance, the instance will be automatically assigned to a new public IP (there is no guarantee that it will be consistent with the public IP before binding). In addition, the destruction of an instance will also disassociate it from the elastic IP.

## Use constraints


- The number of daily purchases available for Tencent Cloud accounts in each region is (quota * 2) times.
- Each Tencent Cloud account can create up to 20 elastic public network IPs in each region.
- When unbinding EIP, the number of free public IP re-assignments that you can do for each Tencent Cloud account is 10 times per day. 

## Release elastic public IP

- Users can release an elastic public IP through the console or cloud API;

- Owed fees release: When an elastic IP is not bound to a resource, it will be charged by the hour. If the user account amount starts at less than 0RMB at any time and continues for more than ** 2 ** hours, and is not recharged to greater than 0RMB, all elastic IPs will remain inactive for the next (24\*7) hours (until the account balance is >0). If the amount is negative for the past (2+24\*7) hours, all elastic public IPs will be released automatically;

## Investigation method for elastic public IP block reasons
An elastic public IP block usually has the below reasons: 

- Elastic public IP is not bound to a cloud resource. For details, see the following.

- Check to see if there are security policies ([Security Group](/doc/product/213/5221) or [Network ACL](/doc/product/215/5132)); in effect, if the cloud product instance is bound, for example: prohibit 8080 port access, then the elastic public IP 8080 port will also be inaccessible.

## Elastic public IP billing
When an elastic IP has been purchased, but <font color="red">is not yet bound to a cloud product instance (CVM or NAT Gateway) </font> yet, a small amount of resource usage will be charged using the below chart (anything less than 1 hour will be charged by 1 hour's time; will be billed once every hour). <font color="red">Elastic IPs used for binding cloud product instances (CVM or NAT Gateways) are free. </font>We recommend that you stop all use of elastic public IPs immediately, to ensure rational use of IP resources, and to save costs.


| Elastic public IP location | Unbound price |
|---------|---------|---------|
| Beijing area, Shanghai area, Guangzhou area | 0.20RMB/hour | 
| Hongkong Region | 0.30RMB/hour | 
| North America Region | 0.25RMB/hour | 
| Singapore Region | 0.30RMB/hour | 

## Apply for elastic public IP

1) Open CVM [CVM console](https://console.cloud.tencent.com/cvm).
	
2) In the navigation pane, click Elastic Public IP.

3) Click the [Apply] button.

4) After the application is finished, you can see the EIP of your application in the EIP list.

## Binding elastic public IP to cloud product

1) Open CVM [CVM console](https://console.cloud.tencent.com/cvm).

2) In the navigation pane, click Elastic Public IP.

3) Click the [Bind] button next to the cloud product EIP list item you want to bind. If this elastic IP is bound to a cloud product instance, the button will be unavailable. Please unbind it first.
	
4) In the pop-up box, select the cloud product type you need to bind, and select the corresponding cloud product instance ID; click the "Bind" button to complete binding with the cloud product.

## Unbind elastic public IP to cloud product

1) Open CVM [CVM console](https://console.cloud.tencent.com/cvm).

2) In the navigation pane, click Elastic Public IP.

3) Click the [Unbind] button next to the cloud product EIP list item that is already bound.

4) Click [OK].

At this point, the cloud product instance may be assigned a new public IP, and the specific details will be based on differences in cloud resources, with the actual situation being the correct one.

## Release for elastic public IP
1) Open CVM [CVM console](https://console.cloud.tencent.com/cvm).

2) In the navigation pane, click Elastic Public IP.

3) Click the [Release] button next to the EIP list item you want to release.

4) Click [OK].
