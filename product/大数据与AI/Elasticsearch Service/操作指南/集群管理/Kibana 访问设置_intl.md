For accessomg Kibana and its usage, see [Accessing Kibana](https://cloud.tencent.com/document/product/845/17146).

Since Kibana is accessed through the public network, certain security restrictions, including passwords and blacklist and whitelist of IPs, can be set up in the access control section of the details page, as shown below:
![Reset password](https://main.qcloudimg.com/raw/3fa85f997895ed2e21b1abe9f7c1f9ee.png)
## Password Verification and Modification
To access Kibana, you need to verify your login password. If you forget your password, you can reset the Kibana password in the basic information section of your cluster details page. A Kibana password is a combination of 8-16 characters comprised of at least two of the following types: letters, numbers and special symbols.


## Kibana Blacklist and Whitelist
Kibana is accessed via the public network. For security reasons, you can set blacklist and whitelist of IPs for access, which can be viewed and modified in the basic information section of your cluster details page. Configuration rules: A maximum of 10 IPs are supported, separated by commas, such as `192.168.0.1` and `192.168.0.0/24`. Blacklist and whitelist of IPs are set separately. You can set any one of them. The whitelist shall prevail if both lists are set.

