#### 1. What are the differences between the resource pool (management) and the idle server pool?
Resource pool (management): After a server is imported (or synchronized from a Tencent Cloud project), it is put into resource pool management by default and does not belong to any business. Servers in the resource pool management can be assigned to the business of any developer. Idle server pool: It contains servers that belong to a business but not assigned to a specific cluster or module.

#### 2. The public IP is not displayed after imported.
The public IP is a user-defined field and needs to be mapped to a field supported by [Configuration Platform](http://o.qcloud.com/console?app=cc-new):
![](//mccdn.qcloud.com/static/img/7194de42c8209a047fb65d3f0ab94acd/image.png)


