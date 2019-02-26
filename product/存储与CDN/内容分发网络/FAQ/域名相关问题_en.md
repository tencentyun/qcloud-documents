### 1. How to access a domain name?
You can access a domain name in the CDN console. For more information, please see [Access a Domain Name](https://cloud.tencent.com/document/product/228/5734).

### 2. Does CDN support accessing wildcard domain name?
CDN supports accessing wildcard domain name but a verification is needed. Upload the verification file provided by Tencent Cloud to the root directory of the website, and access the wildcard domain name after the verification is completed successfully.

### 3. How long does it take to configure CDN?
Generally, it takes not more than 30 minutes for the CDN configuration to take effect. If the configuration does not take effect within 30 minutes after you configure it, you can contact us by submitting a ticket.

### 4. Is there any requirement for accessing a domain name to CDN?
Before a domain name is accessed to CDN for acceleration, the ICP license from the MIIT is necessary, and the business contents on the origin server must be legal.

### 5. Can multiple origin server IPs be configured?
You can configure multiple origin server IPs. After you have configured multiple IPs, the CDN randomly accesses one of the IPs for an origin-pull request. When the number of failures of the origin-pull request to an IP exceeds the threshold, the IP will be isolated for 300 seconds by default and the origin-pull request will not be sent to the origin server any longer.

### 6. How to bind CNAME to a domain name after the domain name accesses CDN?
You can bind CNAME at your DNS service provider by referring to the instructions in [Configuring CNAME](https://cloud.tencent.com/doc/product/228/3121).

### 7. Why can a domain name only be disabled but cannot be deleted?
Please check whether the user is a collaborator. The collaborator's permission is configured by the creator of the CDN service. If the creator does not assign the relevant permission to the collaborator, the collaborator can not perform the operation. If you are sure that the user have been granted the permission, [submit a ticket](https://console.cloud.tencent.com/workorder/category) for the help from OPS personnel.

### 8. Does the domain name configuration be retained after the acceleration service is disabled?
After the acceleration service is disabled, the domain name configuration is retained, but no acceleration service is provided any longer. In this case, any request from user will be forwarded to the origin server for origin-pull.

### 9. Does the domain name configuration be retained after the accelerated domain name is deleted?
After the domain name is deleted, its configuration is not retained.

### 10. How to disable the acceleration service?
You can disable the acceleration service in the CDN console. For more information, please see [Disabling Acceleration Service](https://cloud.tencent.com/document/product/228/5736#.E5.85.B3.E9.97.AD.E5.8A.A0.E9.80.9F.E6.9C.8D.E5.8A.A1).

### 11. How to delete the accelerated domain name?
You can delete the accelerated domain name in the CDN console. For more information, please see [Deleting Accelerated Domain Name](https://cloud.tencent.com/document/product/228/5736#.E5.88.A0.E9.99.A4.E5.8A.A0.E9.80.9F.E5.9F.9F.E5.90.8D).

### 12. How to unlock the blocked domain name?
You need to [submit a ticket](https://console.cloud.tencent.com/workorder/category) for the help from OPS personnel.
