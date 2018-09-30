
Many enterprises have a secure gateway to block Internet access of enterprise internal network. But all Tencent Cloud solutions are accessed over the Internet. To solve this problem, a proxy server is required:

![](https://main.qcloudimg.com/raw/22550909ad08fbf301390a23220eb501.png)

## Step 1: Build an audio/video proxy server (for transparent data transmission)

NAT port mapping is used to map the servers in the private network to the port of the proxy server which forwards audio/video data packets between the private network and Tencent Cloud.

First, download the python script <a href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/WebEXE/Proxy/QueryNearestIP.py">QueryNearestIP.py</a> that queries the optimal IP, and execute the script as shown below.

![IP list](https://main.qcloudimg.com/raw/df1b45b0b6c2d01cce3001fb9e3528a2.png)

Then, download Bash script <a href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/WebEXE/Proxy/NATConfig.sh">NATConfig.sh</a>. Open the file, specify the IP of the ENI received by the proxy server, obtain the IP list according to the previous step, then select the IP with the fastest ping, set the value of IP as follows, and execute the script using the root permission to complete the configuration process.

![](https://main.qcloudimg.com/raw/4269dd13c39fdcaee593c4c16ab08397.png)


## Step 2: Build a Socks5 proxy server (for transparent signaling)

Socks 5 proxy server is like building a bridge between a private network server and a Tencent CVM. The network data packets are the pedestrians on the bridge. Walking across the bridge, they can talk and communicate with each other on both sides. Build a Socks5 proxy server by downloading and executing our Bash script and binding the ENI that receives proxy requests and port of egress ENI.

If your proxy server is Ubuntu, download Bash script <a href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/WebEXE/Proxy/Socks5Config_Ubuntu.sh">Socks5Config_Ubuntu.sh</a>, and if your proxy server is CentOS, download Bash script <a href="http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/WebEXE/Proxy/Socks5Config_CentOS.sh">Socks5Config_CentOS.sh</a>. Open the file, and specify the ENI that receives proxy requests, as shown below. Then, use the root permission to execute the script to complete the configuration of Socks5.

![Port](https://main.qcloudimg.com/raw/3a5c5d01f2f2f38a8dddd24ef526d1dd.png)


## Step 3: Configure the proxy server using EXEStarter.js

Configure the proxy parameters of the Web page, pass proxy_ip and proxy_port parameters to the API createExeAsRoom of EXEStarter.js, and specify the IP and port of the proxy server respectively.

```javascript
EXEStarter.createExeAsRoom({
    //...
    custom: {
     	proxy_ip: "x.x.x.x", 	// (Optional) Proxy IP. Proxy is disabled by default.
     	proxy_port: 1080,	    // (Optional) Proxy Port. Proxy is disabled by default.
    }
});
```
