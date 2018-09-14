## Constructing a Web Application Using Tencent Kubernetes Engines


This document shows how to build a simple Web application in Tencent Cloud's TKE

### The Web Application Consists of Two Sections:

1. Frontend service, used to handle query and write requests from clients.
2. Data storage service, which uses redis to store data written into the storage to redis-master, while read operations access redis-slave. redis-master and redis-slave ensure data synchronization through master-slave replication.
The application is an example that comes with the kubernetes project. Link: https://github.com/kubernetes/kubernetes/tree/release-1.6/examples/guestbook.

### 1. Creating Container Cluster

Step 1: Go to the cluster creation page and create [Container Cluster](https://console.cloud.tencent.com/ccs/cluster):
Step 2: Enter cluster name and specify its location (Guangzhou, Shanghai, Beijing and so on).
Step 3: Specify node network for the cluster. The node network must be within a certain VPC. If you don't have one, [Create a VPC](https://console.cloud.tencent.com/vpc) first and create a subnet in this VPC.
Step 4: Specify container network.
Step 5: Select model for the cluster node (CPU and memory).
Step 6: Set cluster node configurations such as its disk space and bandwidth. Configure password and security group.
Step 7: Select the number of nodes for the cluster.
Step 8: Wait for several minutes for the cluster to be created.
![](https://mc.qcloudimg.com/static/img/fe9384a44101d0d01078a59c91a956ab/ccs_revise_3.jpg)
![](https://mc.qcloudimg.com/static/img/7f563298d97f80a35b38bdda088bfab6/2.jpg)
![](https://mc.qcloudimg.com/static/img/fda579b3a63b015d88f9eafd6f60a0f0/3.jpg)

### 2. Creating Web Application

#### (1) Create redis-master Service

Step 1: Specify service name: redis-master.
Step 2: Choose the cluster we just created as the cluster.
Step 3: Configure pod information for the service (a pod may include multiple containers):
- Add a container named "master".
- Specify image "ccr.ccs.tencentyun.com/library/redis" for the master container. Version is "latest".

Step 4: Configure the number of pods to run for the service. Here, we choose "1", as the redis-master service needs to run one pod.
Step 5: Select access method for the service. Since our redis service is an internal service which only provides access to other services within the cluster, we choose "Access Within Cluster Only".
Step 6: Lastly, configure service access port. Our service pod includes 1 redis container which listens the port 6379, so we configure the mapping container port as 6379, and set the service port to the same value as the container port, which is also 6379. When this is done, other services will be able to access our container "master" using its service name (redis-master) and port (6379).

![](https://mc.qcloudimg.com/static/img/5b07ff233d2b528dc248ac29a42e9d64/ccs_revise_4.jpg)


#### (2) Create redis-slave Service

Step 1: Specify service name: redis-slave.
Step 2: Choose the "cls-km7rvck4(yunyxiao_test)" we just created as the cluster.
Step 3: Configure pod information for the service:
  - Add a container called "slave".
  - Specify image "ccr.ccs.tencentyun.com/library/gb-redisslave" for the slave container. Version is "latest".
  - Specify maximum CPU and memory (optional) available for the container. You can also configure these limits for the master container mentioned above.
  - For operation commands and launch parameters, you may leave them empty since we can use the default ones in the image.
  - Add an environment variable with the name "GET_HOSTS_FROM" and the value "dns". This is mandatory because the variable is required by programs in the gb-redisslave image.

Step 4: Configure the number of pods to run for the service. Here, we choose "1", as the redis-slave service needs to run one pod.
Step 5: Select access method for the service. Since our redis slave service is an internal service which only provides access to other services within the cluster, we choose "Access Within Cluster Only".
Step 6: Lastly, configure service access port. Our service pod includes 1 redis slave container which listens the port 6379, so we configure the mapping container port as 6379, and set the service port to the same value as the container port, which is also 6379. When this is done, other services will be able to access our slave container "redis-slave" using its service name (redis-master) and port (6379).

![](https://mc.qcloudimg.com/static/img/cb20b7af15096fc4edc9a0057a209ac2/ccs_revise_5.jpg)

#### (3) Create frontend Service

Step 1. Specify service name: frontend
Step 2: Choose the "cls-km7rvck4(yunyxiao_test)" we just created as the cluster.
Step 3: Configure pod information for the service:
  - Add a container called "frontend".
  - Specify image "ccr.ccs.tencentyun.com/library/gb-frontend" for the slave container. Version is "latest".
  - Add an environment variable with the name "GET_HOSTS_FROM" and the value "dns". This is mandatory because the variable is required by programs in the gb-frontend image.
 
Step 4: Configure the number of pods to run for the service. Here, we choose "1", as the frontend service needs to run one pod.
Step 5: Select access method for the service. Since our frontend needs to provide access to Internet browsers, we choose "Public Network Load Balancer Access".
Step 6: Lastly, configure service access port. Our service pod includes 1 frontend container which listens the port 80, so we configure the mapping container port as 80, and set the service port to the same value as the container port, which is also 80. When this is done, users will be able to access our frontend container when they access our load balancer IP through browsers.

![](https://mc.qcloudimg.com/static/img/bd5571ad5b6186c5aa58cf3880004a03/ccs_revise_6.jpg)

#### (4) View Service

Click "Service" in the left panel to see the three services we just created. We can access the frontend service via public network because we specified "Public Network Load Balancer Access" as its access method. However, the redismaster and redisslave services can only be accessed by other services within the cluster, since we configured their access method as "Access Within Cluster Only".
![](https://mc.qcloudimg.com/static/img/2503d62c155bbe49472a371fde6c92b6/7.jpg)
We note that there are two IP addresses displayed in the attributes of frontend service:  A public IP "211.159.213.194" and a private IP "10.20.255.125", while there is only a private IP for redisslave and redismaster. This is because the access method for frontend service is "Public Network Load Balancer Access", so we assigned a public network load balancer for this service. The public IP is the IP of the public network load balancer. Since the access port of the frontend service is 80, we can simply enter the public IP "211.159.213.194" in the browser, and see the following:
![](https://mc.qcloudimg.com/static/img/1d2bee6cf0a05db0e12d409cc83995b7/image.png)
This means we can access the frontend service normally. Now, try to type a random string in the input box, you can find that what you just entered is saved and displayed at the bottom of the page. When we open another browser page and access the load balancer IP address again, you can see that the data you entered is still there, which means the string you entered has been stored into redis.

### 3. Development Practice

```php
 'tcp',
      'host'   => $host,
      'port'   => 6379,
    ]);
    $client->set($_GET['key'], $_GET['value']);
    print('{"message": "Updated"}');
  } else {
    $host = 'redis-slave';
    if (getenv('GET_HOSTS_FROM') == 'env') {
      $host = getenv('REDIS_SLAVE_SERVICE_HOST');
    }
    $client = new Predis\Client([
      'scheme' => 'tcp',
      'host'   => $host,
      'port'   => 6379,
    ]);
    $value = $client->get($_GET['key']);
    print('{"data": "' . $value . '"}');
  }
} else {
  phpinfo();
} ?>

```
This is the complete code for the guestbook app frontend service, it's relatively simple. When the frontend service receives an HTTP request, it determines whether the request is a "set" command. If so, the service takes the "key" and "value" from the parameter, connects to redis-master service and set the "key" and "value" into redis master. If the request is not a "set" command, the service connects to redis-slave service and acquire the corresponding "value" of parameter "key" from redis slave, then displays it to the client.
**There are two points to note from the Web app example**:
1. frontend connects to the **service name and port** when accessing redis-master and redis-slave services. Our cluster includes DNS service, which resolves the service name into corresponding service IP and performs load balancing according to this IP. Suppose the redis-slave service contains three pods, when we access this service we actually connect to "redis-slave" and "6379", in which case DNS service resolves "redis-slave" as the service IP of the "redis-slave" service (this is a floating IP, similar to a load balancer IP) and automatically performs load balancing based on this IP, then sends the request to a certain redis-slave service pod.
2. We can configure environment variables for containers. In this example, when the frontend container runs, it reads the GET_HOSTS_FROM environment variable. If the variable value is "dns", then the connection is made by using service name (recommended), otherwise it acquires the domain of redis-master or redis-slave from another environment variable.
