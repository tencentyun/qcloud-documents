
This section describes how to install applications in CPM.

## Installing and Starting nginx

Enter the command "yum install nginx" to install nginx, and enter "y" to confirm when required.</br>
![](http://mc.qcloudimg.com/static/img/bcbc2a1efa0ee48d95d7523c3ecc90de/image.png)

![](http://mc.qcloudimg.com/static/img/9c53c65d74936fb9f48f568e5583c564/image.png)

*YUM source, NTP service, DNS service are provided within the private network of Tencent Cloud for free. You don't need to set up manually*

Enter "service nginx start" to start nginx service.</br>
![](http://mc.qcloudimg.com/static/img/24a8f432b79735ca3205aa8d8f9ea1c3/image.png)

Enter "wget `http://127.0.0.1`" to test nginx service.</br>
![](http://mc.qcloudimg.com/static/img/769eddd75ce79dc2b94ba0427be16e25/image.png)

## Accessing Default Web Page
Installation is successful if you see a sample page of nginx when accessing the public IP in a browser.
![](http://mc.qcloudimg.com/static/img/022a7e6c68969321e7b0483008c4cf12/image.png)

