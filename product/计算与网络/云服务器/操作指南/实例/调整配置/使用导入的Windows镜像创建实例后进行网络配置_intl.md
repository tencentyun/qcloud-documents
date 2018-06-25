After importing Windows images and creating a CVM, you can log in to the CVM by clicking the **Log In** button next to [CVM list in the console](https://console.cloud.tencent.com/cvm) and configure the network.

Network configuration information of Windows servers is saved in the file `C:\qcloud-network-config.ini`, which is structured as follows:

```
[ip]
ip= x.x.x.x
mask = x.x.x.x
gateway = x.x.x.x
 
[dns]
dns = x.x.x.x
```

Modify the network based on this configuration file.

