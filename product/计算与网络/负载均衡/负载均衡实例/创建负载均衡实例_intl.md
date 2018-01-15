After creating a cloud load balancer, the user can enter the [Cloud Load Balance Console](https://console.cloud.tencent.com/loadbalance) to configure [Cloud Load Balance Listener](/doc/product/214/6151) and [Back-end CVM Instance](/doc/product/214/6095). The connection protocols and ports that are respectively connected to the front-end (client-to-load balancer) and the back-end (load balancer to back-end instance) are assigned to configure a cloud load balancer listener. You can configure multiple listeners for the cloud load balancer. Determine the destination for routing requests by specifying the back-end server, please refer to [Adding, Modifying, and Unbinding Back-end Cloud Server](/doc/product/214/6156) for specific configuration procedures.

## Creating a Cloud Load Balancer Instance from the Purchase Page

#### 1. Select the region where the cloud load balancer instance resides
The load balancer only supports shunting within the same region. Please select the same region as that of the CVM instance to be bound.

#### 2. Select Instance Types
Tencent Cloud provides three different cloud load balancer instances, namely: public network with fixed IP, public network without fixed IP and private network. [Here](https://intl.cloud.tencent.com/document/product/214/8847) are the characteristics of each network. Please select the cloud load balancer instance type according to your needs.

#### 3. Select your network
Select the network of CVM to be bound to the cloud load balancer instance. The network types of Tencent Cloud are classfied as basic network and private network.

#### 4. Purchase
Select the number of instances to purchase. The cloud load balancer instance is charged monthly on the basis of the number of days used.

## API Purchase
Please refer to [CreateLoadBalancer API](https://cloud.tencent.com/doc/api/244/1254).

