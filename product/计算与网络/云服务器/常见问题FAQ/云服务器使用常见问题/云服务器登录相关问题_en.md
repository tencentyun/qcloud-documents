### 1. How to solve the long latency problem when logging in to a CVM located in North America?
At present, long latency occurs quite often if you need to manage and operate a CVM located in North America at home. Due to the small number of international routing egresses within the country and other factors, high concurrency may cause serious congestion of the international link and make the access unstable. Tencent Cloud has reported this issue to the operator. In the short term, improvement can be made by purchasing a CVM located in Hong Kong and using this CVM as a transfer point to log in. 

![](//mccdn.qcloud.com/static/img/45317b09510d34fc92eb1cf3f0ac9568/image.png)


1) First, you need to purchase a Windows CVM located in Hong Kong (those with a Windows system are recommended since they support logging in to both Windows and Linux CVMs located in North America) and use it as a "jump sever".
>Note: You need to buy at least 1Mbps bandwidth, or you will not be able to log in to the jump server.

2) After the purchase is made successfully, log in to the Windows CVM located in Hong Kong.
For details, see:
[Log in to a Windows CVM with public IP from a Windows machine](http://www.qcloud.com/doc/product/213/Windows%E6%9C%BA%E5%99%A8%E7%99%BB%E5%BD%95%E6%9C%89%E5%85%AC%E7%BD%91IP%E7%9A%84Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)
[Log in to a Windows CVM with Console VNC](http://www.qcloud.com/doc/product/213/%E6%8E%A7%E5%88%B6%E5%8F%B0VNC%E7%99%BB%E5%BD%95Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)

3) Log in to your CVM located in North America from a Windows CVM located in Hong Kong.

You can use the methods below to log in to your CVM located in North America from a Windows CVM located in Hong Kong:

- Log in to a Linux CVM located in North America
[Use password to log in to a Linux CVM with public IP from a Windows machine](http://www.qcloud.com/doc/product/213/Windows%E6%9C%BA%E5%99%A8%E4%BD%BF%E7%94%A8%E5%AF%86%E7%A0%81%E7%99%BB%E5%BD%95%E6%9C%89%E5%85%AC%E7%BD%91IP%E7%9A%84Linux%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)
[Use key to log in to a Linux CVM with public IP from a Windows machine](http://www.qcloud.com/document/product/213/2036)


- Log in to a Windows CVM located in North America 
[Log in to a Windows CVM with public IP from a Windows machine](http://www.qcloud.com/doc/product/213/Windows%E6%9C%BA%E5%99%A8%E7%99%BB%E5%BD%95%E6%9C%89%E5%85%AC%E7%BD%91IP%E7%9A%84Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)
[Log in to a Windows CVM with Console VNC](http://www.qcloud.com/doc/product/213/%E6%8E%A7%E5%88%B6%E5%8F%B0VNC%E7%99%BB%E5%BD%95Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)
