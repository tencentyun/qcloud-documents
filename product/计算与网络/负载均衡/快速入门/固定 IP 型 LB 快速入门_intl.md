This document will use an example to help new users understand how to use Tencent Cloud's Cloud Load Balance: Create a public network-based (with daily rate) cloud load balancer instance named `clb-test`, and bind it to a custom domain to forward HTTP request to the two backend CVMs when this domain is accessed.

## Preconditions
- Cloud load balancer is only responsible for forwarding the traffic, and is not capable of processing requests. Therefore, you need a running CVM instance to process user's requests. Here, you just need two CVM instances. You can also specify the number of CVMs to which the requests are forwarded. In this example, two CVM instances, `rs-1` and `rs-2`, have been created in Beijing region. For information on how to create a CVM instance, refer to [Purchase and Enable CVM Instance](/doc/product/213/4855).
- Here we take HTTP forwarding as an example. A Web server, such as Apache, Nginx and IIS, must be deployed on the CVMs. In this example, for the purpose of result verification, Apache is deployed on both `rs-1` and `rs-2`, with HTML text "This is rs-1" and "This is rs-2" returned respectively. For more information on how to deploy services on CVM, refer to [Installation and Configuration of IIS and PHP on Windows](https://cloud.tencent.com/doc/product/213/2755) and [Environment Configuration of Linux System (CentOS)](https://cloud.tencent.com/doc/product/213/2125).

> Note: In this example, the returned values vary with the services deployed on backend CVMs. In practice, the services deployed on CVMS are exactly the same to provide a consistent experience for all users.

## Purchasing and Creating a Cloud Load Balancer Instance
> Please note that the cloud load balancer can only forward the traffic to the CVM instances within the same region. So please create the cloud load balancer instances within the same region where both CVMs reside in as described in "Preconditions".

1) Log in to Tencent Cloud, go to [Cloud Load Balance Purchase Page](https://buy.cloud.tencent.com/lb).

2) In this example, select "North China (Beijing)", where the CVMs reside in, as the region, select "Public Network (with Daily Rate)" as the instance type, and select "Basic Network" as the network environment.

3) Click "Buy Now" to make the payment.

For more information on cloud load balancer instances, refer to [Public Network-based Cloud Load Balancer Instance](/doc/product/214/6147) and [Private Network-based Cloud Load Balancer Instance](/doc/product/214/6148).

## Creating Cloud Load Balancer Listener
The cloud load balancer listener forwards the requests via specified protocol and port. In this example, the cloud load balancer listener will be set to forward HTTP requests from client.

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/) and click "Cloud Products" - "Cloud Load Balance" to enter the Cloud Load Balance console.

2) In the "LB instance list", find the public network-based (with daily rate) cloud load balancer instance you just created, and click its ID to enter the cloud load balancer details page.

3) In "Basic Info", click the icon next to the name to change the name to "clb-test".

4) In "Listener", click "Create" button to create a new cloud load balancer listener.

5) Enter the following information:

- The custom name is "Listener1";
- The listened protocol and port are `HTTP: 80`
- The backend port is `80`;
- The balancing method is `Weighted Round Robin`;
- Do not check "Session Persistence";
- Check "Health Check".

Click "OK" to complete the creation of cloud load balancer listener.

For more information on cloud load balancer listeners, refer to [Cloud Load Balancer Listener Overview](/doc/product/214/6151).

## Binding Backend CVM

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/) and click "Cloud Products" - "Cloud Load Balance" to enter the Cloud Load Balance console.

2) In the "LB instance list", find `clb-test` you just created, and click its ID to enter the cloud load balancer details page.

3) In "Bind to CVM", click "Bind to CVM" button, then select the CVM instances `rs-1` and `rs-2` within the same region described in "Preconditions", and set the weight to 10 (default).

4) Click "OK".

## Testing Cloud Load Balancer
Enter the public network domain name (`www.qcloudtest.com`) configured for the cloud load balancer instance in the browser. Check the test result to verify whether the cloud load balancer instance has been configured successfully.

According to the following figures, the cloud load balancer can access the two bound backend CVMs based on the configurations made by the user.
- If the user enables the session persistence feature, or disables this feature but selects "ip_hash" for scheduling, the requests will be allocated to one backend CVM all the time.
- If the user disables the session persistence feature and selects "Weighted Round Robin" for scheduling, the requests will be allocated to multiple backend CVMs in sequence.





