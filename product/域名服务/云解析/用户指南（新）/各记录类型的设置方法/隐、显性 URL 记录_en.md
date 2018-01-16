### What are Implicit/Explicit URL Forwarding?

Let's take the example where `http://a.com` is redirected to ` https://cloud.tencent.com/ `.

**Implicit URL forwarding:** It uses iframe framework and non-redirection technologies. When you enter `http://a.com` in the browser address bar and press **Enter**, the website you open shows the contents of the target website `https://cloud.tencent.com/`, while the address bar still shows the current address `http://a.com`.
>**Note:**
>You cannot use implicit forwarding if the target address isn't allowed to be nested (for example, implicit forwarding can't be used for Qzone). 
 
**Explicit URL forwarding:** It uses 301 redirection technology. When you enter `http://a.com` in the browser address bar and press **Enter**, the website you open shows the contents of the target website `https://cloud.tencent.com/`, and the address bar shows the target address `https://cloud.tencent.com/`.
### How to Add Implicit/Explicit Forwarding Record?
1. Enter sub domain name prefix as host name.
2. Record type is implicit URL/explicit URL.
3. Line type (this is required by default, otherwise certain users will not be able to resolve the domain).
4. The record value must be a complete address (as shown in the figure below, it must contain protocol, domain name, and it may contain port number and uniform resource locator).
5. MX priority is not required.
6. TTL is not required as the system will automatically generate one. Default is 600 seconds. TTL is the duration for cache. The smaller the value is, the faster the modified record will take effect.
![](//mc.qcloudimg.com/static/img/b1201d381985067214ad99c688de459e/image.png)
![](//mc.qcloudimg.com/static/img/4bc770b92f945758f3d0cce05d5c5b4f/image.png)

### When Do I Need to Use URL Forwarding?
You need to add URL record if you want to direct a domain name to another existing site.
