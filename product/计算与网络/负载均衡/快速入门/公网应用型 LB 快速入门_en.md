The public network application-based cloud load balancer launched by Tencent Cloud allows users to configure the domain name/URL-based forwarding rules for forwarding requests to different backend servers. In addition, the redirection feature of public network application-based cloud load balancer enables http requests to be redirected as https requests and some of http requests on the phone automatically returns https respond through the LoadBalance proxy. Here we show you the new features of public network application-based cloud load balancer via step by step configurations.

## 1. Creating CVMs and Building nginx Service.

### 1.1 Purchasing CVMs
On the [Purchasing CVMs](https://buy.cloud.tencent.com/cvm) page, select the appropriate models, images and others, and set the initial password of the CVM, then configure the security group (here for the convenience of test, you can enable all the ports to Internet first and make restrictions in the future). In addition, make sure to activate public network traffic when purchasing CVM, otherwise accesses may fail after LB is associated.

![](https://mc.qcloudimg.com/static/img/1ee252e5b02350e91e9aeec6bbf47e9c/001.png)

The CVM environment parameters used in this test are as follows (two CVMs were purchased):
>**CVM Information**
Region	Guangzhou
Availability zone	Guangzhou Zone 3
CVM billing method	Postpaid
Network billing method	Bill-by-traffic
Network	Basic network

>**Machine Configuration**
Operating system	CentOS 6.8 64-bit
CPU	1-core
Memory	2 GB
System disk	20 GB (cloud block storage)	
Data disk	380 GB (Premium cloud storage)
Public network bandwidth	1 Mbps

### 1.2 Building Environment
After purchasing, click the "Login" button on the CVM details page to directly log in to CVM, and then enter your user name and password to start building the nginx environment. Here we apply the easiest way to install nginx. If you need to install the latest version of nginx, you can go to the official website to download and extract for installation.
Install nginx:
```
yum -y install nginx  
```
Start nginx and an error occurs
```
service nginx start
```
Modify configuration files
```
vim /etc/nginx/conf.d/default.conf

listen       80 default_server; 
listen       [::]:80 default_server;

Change the configuration into:
listen       80;   #Listening port 80
#listen       [::]:80 default_server;
```
Restart nginx
```
sudo service nginx restart
```
Now visit the public IP address of the Cloud Virtual Machine, you can see the page below:

![](https://mc.qcloudimg.com/static/img/7bd527bd16e7a2c7a6f93d0e00e897ea/002.png)

The default root directory of nginx is located at /usr/share/nginx/html, so we can identify the particular page directly by modifying or moving the index.html static page under html.
```
vim /usr/share/nginx/html/index.html
```
Because application cloud load balancer can forward requests according to the path of the backend server, configuring services under different paths can facilitate subsequent request distribution by cloud load balancer. We deploy the static pages under /image/ path of CVM1 and /text/ path of CVM2 respectively as follows:

Relevant commands are as follows:
```
cd /usr/share/nginx/html/
mkdir image/
cp -r index.html image/    # For another CVM, you can deploy the page to the text path
```

### 1.3 Authentication Service
Now, if the deployed page displays when you access the CVM public network IP and path, deployment of the first step is successful.
CVM1 /image page

![](https://mc.qcloudimg.com/static/img/2e10d11bb030dc2627ade5656690a483/003.png)

CVM2 /text page

![](https://mc.qcloudimg.com/static/img/9f063edb7307936199eb44ba72958e8a/004.png)

## 2. Purchasing and Configuring Public Network Application LB

### 2.1 Purchasing Application Cloud Load Balancer
Select public network application cloud load balancer on the [Purchasing CLBs](https://buy.cloud.tencent.com/lb) page. Please note that after you select the cloud load balancer in a region (for example, LB in Guangzhou region), you can only bind intra-region backend CVMs of different availability zones (for example, CVMs of Guangzhou Zone 2 and Guangzhou Zone 3). After creating, you can explore the rich capabilities of application CLB!

![](https://mc.qcloudimg.com/static/img/0dc79d07fec5a1998b98f37bd17334d5/005.png)

### 2.2 Configuring Listeners, Forwarding Groups and Forwarding Rules, and Binding CVMs
After purchasing, you can view the information of listener bound to the LB instance on the "LB Details" -> "Listener Management" page. Click "New" to create an HTTP Listener.

![](https://mc.qcloudimg.com/static/img/847950e967c54f04d736f7cb7fac9c89/006.png)

Enter the listener name and listening port (here we enter port 80 by default) when creating the Layer-7 HTTP listener. After creating, click "Create Forwarding Rule" to configure a domain name and URL for the listener, where wildcard and regularization are supported, but there are some restrictions. For more information, see [Configuration Description](https://cloud.tencent.com/document/product/214/6744). For balancing mode, you can select polling by weight. When you do not want the connection to fall on the same backend CVM, you can disable the session persistence by default in the third step of configuration.

![](https://mc.qcloudimg.com/static/img/effd493443791f91e88a5cb661ab0809/008.png)

After creating, you can see that forwarding groups and forwarding rules of www.example.com/image/ have been configured under the listener. Then you can click "Bind CVM" to select the machine with configured service. When binding CVM, the backend port 80 is listened by default. Because the configuration of application cloud load balancer is flexible, you can bind CVMs of different backend ports under the same listener.

![](https://mc.qcloudimg.com/static/img/7b48c5c5f1cd6c98605cadb6e99a1326/009.png)

Next, we can continue to create an HTTPS listener, which requires at least a server certificate for one-way authentication. Here you can upload your own certificates, or select the existing certificates, or apply for a certificate in the SSL certificate platform. We set port 443 for HTTPS protocol by default.

![](https://mc.qcloudimg.com/static/img/c20fae06728afae71c1692e7b2a3d200/010.png)

The subsequent listener configuration steps are similar. After the configuration is complete, we can view the architecture under the LB:

![](https://mc.qcloudimg.com/static/img/62c9e3c9d392673c8757abe70f65ea17/011.png)


### 2.2 Authentication Service
After the configuration is complete, we can verify whether the architecture takes effect. First, we need to make hosts for domain names of the two listeners, and modify the hosts file in C:\Windows\System32\drivers\etc, and map the IP of LB instance to the two domains.

![](https://mc.qcloudimg.com/static/img/dbdf71ada5ab53a98150a1677e700770/012.png)

To verify whether the hosts are successful, you can type "cmd" into the search bar on the local machine with ping command to detect whether the domain name is successfully bound to the IP. If there is a data packet, the connection is successful.

![](https://mc.qcloudimg.com/static/img/8aa703e2da557010210f23b52da56f87/013.png)

Next, you can type `http://www.example.com/image/` and `https://www.example2.com/text/` to test whether a request can access backend server via LB. (Note: the "/" of image/ and text/ is very important, because it indicates image and text are two default directories instead of files with names of "image" and "text").

![](https://mc.qcloudimg.com/static/img/82360f96ea78984030d7378b35ee48e0/014.png)

![](https://mc.qcloudimg.com/static/img/bd9bc8b9d925c8cb54740d448eead43c/015.png)

The results shown in the above figure indicate that we can access different backend CVMs via different ***domain names + URLs*** under a LB instance, that is, ***content-based routing"*** feature is realized. Then, the redirection feature can work if you encounter two scenarios below:

1. Forced https: When Web service is accessed by PC and mobile browsers via http requests, you want https respond to be returned through LoadBalance proxy. By default, https is used by browsers to access web pages.

2. Custom redirection: When Web services need to be temporarily deactivated (in case of selling-out of e-commerce, page maintenance and upgrade), redirect capability is necessary. Without redirections, visitors can only get a `404/503` error message caused by old address in users' favorites and search engine database, which reduces user experience and results in access traffic loss. In addition, the search engine scores accumulated on this page will also be wasted.

Next, we can experience this feature through actual operations, that is, redirect the configured request for HTTP listener to the HTTPS listener.

## 3. Configuring Redirection

The redirection configuration is divided into manual redirection and automatic redirection. Automatic redirection is mainly designed for the situation that there are many paths under the domain name, and the system needs to automatically create an HTTP listener for the existing HTTPS: 443 listener for forwarding. After creating is successful, you can access via automatic redirection from HTTP: 80 address to HTTPS address: 443. This practice can be manually configured. For more information, refer to [Redirection Configuration](https://cloud.tencent.com/document/product/214/8839).

### 3.1 Manual Redirection Configuration
Select the redirection configuration tab in the LB details page, and create a new manual redirection configuration

![](https://mc.qcloudimg.com/static/img/eeba873c140531e1555d5bd5b736325e/016.png)

Then select the original access protocol, port and domain name, and specify the destination protocol, port and domain name.

![](https://mc.qcloudimg.com/static/img/b44d09f2ff05cd3ec2540098a534077a/017.png)

Click "Next" to select the original and redirected access paths. If there are many paths under the domain name, you can add multiple paths for redirection. Note: the path configuration does not allow loopback (that is, A-> B B-> C), and the operation can only be realized in the same LB instance for now.

![](https://mc.qcloudimg.com/static/img/e5282652048b382b19c3278ade549255/018.png)

After the redirection policy is configured, you can view the policy on the LB redirection configuration details page. In addition, you can find that in the original listener tree diagram, a redirection identifier is added to the path of the HTTP listener to indicate that the bound backend servers in this path will no longer receive requests because requests will be redirected to the HTTPS listener you just configured.

![](https://mc.qcloudimg.com/static/img/17a214beb19fc8593e4efc14574761cf/019.png)


### 3.2 Authentication Service
Finally, we can access `http://www.example.com/image/` to verify whether the request is automatically redirected to the address `https://www.example2.com/text/`
If the following page appears after you enter `http://www.example.com/image/`, congratulations. The redirection configuration is completed!

![](https://mc.qcloudimg.com/static/img/591798ef620f8a72d9904197ca06c9a2/020.png)

