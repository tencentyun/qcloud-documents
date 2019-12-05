Tencent Cloud's cloud load balancer instances can periodically send Ping to back-end CVMs, makes attempts to connect with them or sends requests to them to test for their running status. This is called "health check". 

If it is concluded that a back-end CVM instance is unhealthy, the cloud load balancer instance will not forward requests to the instance.  But health check will be performed on all back-end CVMs, whether healthy or unhealthy, and when the unhealthy instance returns to normal state, the cloud load balancer instance will resume forwarding new requests to it. 

Auto scaling group regularly checks the running status of instances within each group in a similar way.  For more information, refer to [Auto Scaling Product Documentation](https://cloud.tencent.com/doc/product/377). 

## Definitions of Health Check Configuration Fields 

**Response Timeout:** The maximum time-out for the response to health check.  If back-end CVM does not respond properly within the time limit, it is considered that the health check failed.

**Health Check Interval: **Time interval between health checks. 

**Unhealthy Threshold: **If a failure result is returned for the health check for n consecutive times (n is the input value), the back-end CVM is identified as unhealthy and marked "Unhealthy" on the console. 

**Healthy Threshold: **If a success result is returned for the health check for n consecutive times (n is the input value), the back-end CVM is identified as healthy and marked "Healthy" on the console. 

**Normal Status Code: **This is only applicable to HTTP check method.  Specify the HTTP status code used to verify that the health check is normal.  Option values include `http_1xx`, `http_2xx`, `http_3xx`, `http_4xx` and `http_5xx`. Multiple choices are allowed.  By default or if no choice is made, it is set to `http_2xx`. 

## Health Check Configuration for Layer-4 Forwarding 

Under the health check mechanism for Layer-4 forwarding, cloud load balancer initiates an access request to the CVM port specified in the configuration. If the access to the port is normal, the back-end CVM is considered normal, otherwise it is considered abnormal.  For TCP services, SYN packet is used for the check.  For UDP services, Ping command is used for the check. 

- Response timeout:   2-60 seconds  
- Check interval:   5-300 seconds  
- Unhealthy threshold: 2-10 times (When the response timeout has happened to a healthy back-end CVM for the specified number of times, the back-end CVM is considered unhealthy)
- Healthy threshold: 2-10 times (When the response timeout has happened to an unhealthy back-end CVM for the specified number of times, the back-end CVM is considered healthy) 

## Health Check Configuration for Layer-7 Forwarding

Under the health check mechanism for Layer-7 forwarding, the cloud load balancer sends an HTTP request to the back-end CVM to check the back-end services. The cloud load balancer determines the running status of the service based on whether the HTTP returned value is `http_2xx` or `http_4xx`.  In the future, users will be allowed to customize the descriptions of the statuses represented by response codes. For example, in a certain scenario, HTTP returned values include `http_1xx`, `http_2xx`, `http_3xx`, `http_4xx` and `http_5xx`. Users can, based on business needs, define `http_1xx` and `http_2xx` as normal status and the values from `http_3xx` to `http_5xx` as abnormal status. 

- Response timeout cannot be set currently. Default is 5s.  
- Check interval is 6-300s. Default is 6s.  
- Unhealthy threshold: 2-10 times, default is 3 times (When the response timeout has happened to a healthy back-end CVM for the specified number of times, the back-end CVM is considered unhealthy)
- Healthy threshold: 2-10 times, default is 3 times (When the response timeout has happened to an unhealthy back-end CVM for the specified number of times, the back-end CVM is considered healthy)

## How to Troubleshoot in Health Check 
### Layer-4 Troubleshooting

Under TCP protocol, cloud load balancer uses SYN packet for the check, while under UDP protocol, it uses Ping command for the check.

When a back-end CVM port is marked "unhealthy" in the page, you should conduct troubleshooting using the following procedure:

- Check whether the service of back-end CVM is affected by a configuration or security group.  For information on how to ensure the normal operation of service by controlling the access to back-end CVM, refer to [Back-end CVM Access Control](/doc/product/214/6157). 
- Use the `netstat` command to check if there is a process listening on the back-end CVM's port. If no such process is found, restart the service. 

### Layer-7 Troubleshooting
For Layer-7 services (HTTP/HTTPS protocol), when an exception is detected in the health check by a listener process, the troubleshooting can be performed in the following ways: 

1) The Layer-7 health check service of cloud load balancer communicates with the backend CVM via private network, so you need to log in to the server to check whether the application server port is being listened on normally at the private network address; if not, you should move the listening of application server port to the private network address to ensure the normal communication between cloud load balancer system and back-end CVM. 

Assuming that the cloud load balancer's front-end port is 80, and CVM back-end port is also 80, the CVM's private IP is: 1.1.1.10 

The server on Windows system uses the following command: 

```
netstat -ano | findstr :80
```

The server on Linux system uses the following command: 

```
netstat -anp | grep :80
```

If you can see the listening status at 1.1.1.10:80 or 0.0.0.0:80, the configuration is considered normal. 

2) Make sure that the back-end port configured in the cloud load balancer listener has been enabled on the back-end CVM. 

For Layer-4 cloud load balance, it is considered normal as long as the back-end port telnet gives a response. You can use `telnet 1.1.1.10 80` to test.  For Layer-7 cloud load balance, such HTTP status codes as 200 indicate a normal state. The test is conducted as follows: 

- On Windows system, directly input private IP in the CVM browser to check whether it is normal. In this example, `http://1.1.1.10` is input; 
- On Linux system, use the `curl-I` command to check if the status is ` HTTP/1.1 200 OK`. In this example, `curl -I 1.1.1.10` command is used 

3) Check whether there is a firewall or other security software inside the back-end CVM. This type of software can easily block the local IP address of the cloud load balancer system, causing the failure of cloud load balancer system to communicate with the back-end CVM. 

Check whether the firewall of private network on server allows port 80. You can temporarily disable the firewall for the test. 

- For Windows system, run the `firewall.cpl' entry to disable the firewall
- For Linux system, input `/etc/init.d/iptables stop` to disable the firewall

4) Check if the parameter settings of cloud load balancer health check are correct; it is recommended to complete the settings by referring to the health check default parameter values provided in this document. 

5) It is recommended that the test file specified for health check is a simple HTML page and only be used to check the returned result.  It is not recommended to use php and other dynamic script languages. 

6) Check whether there is a high load on the back-end CVM that leads to slow response of CVM to provide service. 

