## FAQ on Service Creation
### 1. Why must service name be unique?
A service name is a unique service identifier under the current cluster. Services access each other by using their service names and access ports.

### 2. Can I use a third-party image instead of Tencent Cloud or Dockerhub image when creating service?
You can log in to your CVM and execute the command "docker login" to log in to third-party image registry and pull the image.
The feature for using third-party image from the console will become available soon.

### 3. What are the preconditions for using Internet services?
Ensure that CVMs in the cluster have Internet bandwidth. Otherwise the creation of Internet service may fail.

### 4. How to configure memory and CPU limits?
For more information, please see [Limits on CCS Resources](https://cloud.tencent.com/document/product/457/6767).

### 5. What does "Privilege" mean?
If this option is enabled, applications in the container can have real root permission. You are recommended to enable this option when you need to perform higher-level system operation on the applications in the container, for example, building NFS server.

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
All containers and Internet load balancers under a service are terminated upon service deletion. Back up the data in advance.

## FAQ on Service Operation
### 1. How to set the container system time to Beijing time?
Containers use the UTC time by default. If the problem of an 8-hour difference between container system time and Beijing time always occurs when you use container, please create a time zone file in dockerfile.
```
RUN echo "Asia/shanghai" > /etc/timezone;
```

### 2. Some of Dockerhub images, such as ubuntu, php and busybox encounter exceptions in CCS
This is because no startup command is set or default startup command is bash, so that the container exits after the startup procedure is completed. To keep the container running, the process in the container with PID set to 1 must be the permanent process, otherwise, the container exits when this process ends. For some images like Centos, you can create service by using /bin/bash as running command and -c sleep 800000 as running parameter. "-c" and "sleep 800000" must be entered in different rows in the console.

For now, the images that cannot be started using default parameters include: clearlinux, ros, mageia, amazonlinux, ubuntu, clojure, crux, gcc, photon, java, debian, oraclelinux, mono, bash, buildpack-deps, golang, sourcemage, Swift, openjdk, centos, busybox, docker, alpine, ibmjava, php and python.

