### What is implicit/explicit forwarding?

Take the redirect from `http://a.com` to `https://cloud.tencent.com/ ` as an example.

**Implicit forwarding:** It uses iframe framework and non-redirect technologies. When you enter `http://a.com` in the browser address bar and press **Enter**, the website content displayed is the content of the target website `https://cloud.tencent.com/`, but the address bar still shows the current address `http://a.com`.
>**Note:**
>You cannot use implicit forwarding if nested target address is not allowed (for example, implicit forwarding can't be used in Qzone). 
 
**Explicit forwarding:** It uses 301 redirect technology. When you enter `http://a.com` in the browser address bar and press **Enter**, the content of the target website `https://cloud.tencent.com/` is displayed, and the address bar shows the target address `https://cloud.tencent.com/`.
### How to add implicit/explicit forwarding records?
1. Enter the sub-domain name prefix as the host name.
2. Record type is implicit URL/explicit URL.
3. Line type. This is required by default. If it is left empty, some users will not be able to resolve the domain name.
4. The record value must be a complete address (as shown below, it must contain protocol, domain name, and may contain port number and Uniform Resource Locater).
5. MX priority is not required.
6. TTL is not required as the system will automatically generate one. Default is 600 seconds. TTL (Time to Live) is the duration for cache. The smaller the value is, the faster the modified record takes effect.
![](//mc.qcloudimg.com/static/img/b1201d381985067214ad99c688de459e/image.png)
![](//mc.qcloudimg.com/static/img/4bc770b92f945758f3d0cce05d5c5b4f/image.png)

### When do I need to use URL forwarding?
You need to add a URL record if you want to direct a domain name to another existing site.
