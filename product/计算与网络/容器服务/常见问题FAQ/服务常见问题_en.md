## FAQ on Service Creation
### 1. Why must service name be unique?
A service name is a unique service identifier under the current cluster. Services access each other by using their service names and access ports.

### 2. Can I use a third-party image instead of Tencent Cloud or Dockerhub image when creating service?
You can log in to your CVM and execute the command "docker login" to log in to third-party image warehouse and pull the image.
The feature for using third-party image from the console will become available soon.

### 3. What are the preconditions for using Internet services?
Ensure that CVMs in the cluster have Internet bandwidth. Otherwise Internet service creation will fail.

### 4. How to configure memory and CPU limits?
For more information, please see [Limits on CCS Resources](https://www.qcloud.com/document/product/457/6767).

## FAQ on Updating the Number of Service Containers
### 1. Anything should I take note of when I update the number of containers?
Confirm if CPU and memory resources are sufficient. Otherwise container creation will fail.
### 2. Can I configure the number of containers as 0?
Yes. You can set the number to 0 and save the service configuration to free up resources.

## FAQ on Updating Service Configurations
### 1. Is rolling update supported?
Both rolling update and quick update are supported.

## FAQ on Service Deletion
### 1. When I delete a service, will the load balancer created by the service also be terminated?
All containers and Internet load balancers under a service will be terminated upon service deletion. Please back up the data in advance.







