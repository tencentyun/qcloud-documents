
## 1. Layer-4 Troubleshooting

Under TCP protocol, cloud load balancer uses SYN packet for the check, while under UDP protocol, it uses Ping command for the check.

When a CLB back-end CVM port is marked "Unhealthy" in the page, you should conduct troubleshooting using the following procedure:

- Check whether the CLB back-end CVM is configured with a firewall that affects the service. If yes, please disable it. 
- Use Netstat command to check if there is a process listening on the back-end CVM port. If no such process is found, restart the service.

## 2. Layer-7 Troubleshooting
For Layer-7 services (HTTP protocol), when an exception is detected in the health check by a listener process, the troubleshooting can be performed in the following ways:

- CLB's Layer-7 health check service communicates with the back-end CVMs via private network, so you need to log in to the server to check whether the application server port is being listened on normally at the private network address; if not, you should move the listening of application server port to the private network address to ensure the normal communication between the CLB system and back-end CVM.

Assume that the CLB front-end port is 80, the CVM back-end port is 80, and CVM's private IP is 1.1.1.10

The server on Windows system uses the following command:

```
netstat -ano | findstr :80
```

The server on Linux system uses the following command:

```
netstat -anp | grep :80
```

If you can see the listening status at 1.1.1.10:80 or 0.0.0.0:80, the configuration is considered normal.

- Make sure that the relevant port has been opened on back-end CVM, which must be consistent with the back-end port you configured in the CLB listener configuration.

For a Layer-4 CLB, it is considered normal as long as the back-end port telnet gives a response. You can use `telnet 1.1.1.10 80` to test. For a Layer-7 CLB, such HTTP status codes as 200 indicate a normal state. The test is conducted as follows:

On Windows system, you can directly input private IP in a CVM browser to test whether it is normal. In this example, `http://1.1.1.10` is input.
On Linux system, you can check whether the status is HTTP / 1.1 200 OK through the`curl-I` command. In this example, `curl -I 1.1.1.10` is used.

- Check whether there is a firewall or other security software inside the back-end CVM. Such software can easily block local IP address of the CLB system, causing the failure of the CLB system to communicate with the back-end CVM.

Check whether the firewall of private network on the CVM allows port 80. You can temporarily disable the firewall for the test.

For Windows system, run the `firewall.cpl' entry to disable the firewall
For Linux system, input `/etc/init.d/iptables stop` to disable the firewall

- Check whether the settings of the CLB health check parameters are correct. It is recommended to complete the settings by referring to the health check default parameter values provided [here](http://cloud.tencent.com/doc/product/214/%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D#2.2.-.E5.81.A5.E5.BA.B7.E6.A3.80.E6.9F.A5).
- The recommended test file specified for health check is a simple page in html form and is only used for check return results. Dynamic scripting languages such as php are not recommended.
- Check whether there is a high load on the back-end CVM that leads to slow response of CVM to provide service.

