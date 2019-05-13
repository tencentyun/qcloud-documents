## Problem Description
The latency is too long when users log in to CVMs located in North America.
Due to the small number of international routing egresses within the country and other factors, high concurrency may cause serious congestion of the international linkage and make the access unstable. Tencent Cloud has reported this issue to the ISP. If you need to manage and operate a CVM located in North America at home, in the short term, you can purchase a CVM located in Hong Kong and use it as a transfer point to log in to the CVM located in North America.

![](//mccdn.qcloud.com/static/img/45317b09510d34fc92eb1cf3f0ac9568/image.png)

## Solution
 1. [Purchase](https://buy.cloud.tencent.com/cvm?tabIndex=1) a Windows CVM located in Hong Kong as a jump server in the custom configuration page (Windows operating systems support login to both Windows and Linux CVMs located in North America).
	>**Note:**
	>You need to buy at least 1 Mbps bandwidth, or you will be unable to log in to the jump server.

 2. After the purchase is made successfully, log in to the Windows CVM located in Hong Kong:
[Log in to a Windows CVM with a public IP from a Windows machine](/doc/product/213/Windows%E6%9C%BA%E5%99%A8%E7%99%BB%E5%BD%95%E6%9C%89%E5%85%AC%E7%BD%91IP%E7%9A%84Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)
[Log in to a Windows CVM from console VNC](/doc/product/213/%E6%8E%A7%E5%88%B6%E5%8F%B0VNC%E7%99%BB%E5%BD%95Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)

 3. Log in to your CVM located in North America from the Windows CVM located in Hong Kong:

	- Log in to a Linux CVM located in North America
[Log in to a Linux CVM with a public IP from a Windows machine using password](/doc/product/213/Windows%E6%9C%BA%E5%99%A8%E4%BD%BF%E7%94%A8%E5%AF%86%E7%A0%81%E7%99%BB%E5%BD%95%E6%9C%89%E5%85%AC%E7%BD%91IP%E7%9A%84Linux%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)
[Use key to log in to a Linux CVM with a public IP from a Windows machine](/doc/product/213/2036)
  - Log in to a Windows CVM located in North America 
[Log in to a Windows CVM with a public IP from a Windows machine](/doc/product/213/Windows%E6%9C%BA%E5%99%A8%E7%99%BB%E5%BD%95%E6%9C%89%E5%85%AC%E7%BD%91IP%E7%9A%84Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)
[Log in to a Windows CVM from console VNC](/doc/product/213/%E6%8E%A7%E5%88%B6%E5%8F%B0VNC%E7%99%BB%E5%BD%95Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)

