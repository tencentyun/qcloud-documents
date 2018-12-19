## Add a Listener
In **Access Management** page, click "ID/Name" of a specified connection. In the **HTTP/HTTPS Listener Management** tab, and click **New**. The default pop-up window is as shown below:
![](https://main.qcloudimg.com/raw/42613670f204b3d3c7299feb76611331.jpg)
- When HTTP is selected, enter the input port, and the listener will forward it according to the HTTP protocol by default.
- When HTTPS is selected, additional certificates and other information are required to be configured, as shown below:
![](https://main.qcloudimg.com/raw/8b36f41a960a20af548fc99125fdf526.jpg)
- **Use HTTP between listener and origin**: HTTPS protocol is used between the client and the acceleration connection VIP, while the HTTP protocol is used between the VIP and the origin, which requires the origin server to enable HTTP protocol port. **Use HTTPS between listener and origin** means that the HTTPS protocol is used between the client and the origin server, and the HTTPS protocol port should be enabled for the origin server. The main difference is that the linkage delay of the former is lower.
- **SSL parsing method**: Only unidirectional verification is supported, that is, server verification on the client.
- **Server certificate**: You need to purchase or upload in Tencent Cloud's **SSL Certificate Management** products, and then choose the corresponding certificate from the drop-down list.

## Settings
On the **HTTP/HTTPS Listener Management** tab, click **Settings** to go to the next page for domain name and URL management.
![](https://main.qcloudimg.com/raw/622d4a679528dc0e67f1f03ac7cb15cf.jpg)
### Add a rule</span>
Click **Add a rule** to add the domain name and corresponding URL. You can add up to 20 URL rules under the same domain name, as shown below:
1. Basic configuration
![](https://main.qcloudimg.com/raw/66540758feaa6ecfac76d292e08111a3.jpg)
**Domain name**: Exact match rule. It can contain 3-80 characters, including `a-z`, `0-9`, ` _`, ` .`, ` -`.
**URL**: 1-80 characters, including: a-z, A-Z, 0-9, _, ., -, /.
**Origin Type**: Supports two types of origin servers, IP and domain name. The difference between the two types is the same as the description of TCP/UDP listener.
2. Processing policy for origin server
Set the forwarding processing rules of the origin server to support polling, polling weighting, and minimum connections. The description of the specific policy is the same as the description of TCP/UDP listener.
![](https://main.qcloudimg.com/raw/d611626dc7c90302873fa068ae6e6b70.jpg)
3. Origin server health check mechanism
The monitoring check mechanism can be enabled. For the current domain name, an independent check URL can be set. The request mode supports HEAD and GET. The check status code supports http_1xx, http_2xx, http_3xx, http_4xx, and http_5xx, and one or multiple selections can be made. When the specified status code is detected, the listener considers that the backend origin server is in normal status. If no status code is detected, the listener considers that the backend origin server is exceptional.
![](https://main.qcloudimg.com/raw/e0861983ad47057b37b9998d22bd96b0.jpg)

### Modify a domain name
You can modify a domain name as shown in the following figure:
![](https://main.qcloudimg.com/raw/119b5d8248743099a5033a9470151979.jpg)

### Delete a domain name
When deleting a domain name, if a rule under the domain name is bound with the origin server, you need to check "Force deletion of rules bound with origin servers".
![](https://main.qcloudimg.com/raw/0517936b3d3c43c7d5a3a243aa3353a0.jpg)

### Modify a rule
See [Add a Rule](#Add a Rule). The main difference is that the domain name and origin server type cannot be modified.

### Bind origin server
See [Bind Origin Server](https://cloud.tencent.com/document/product/608/17849#.E7.AC.AC.E5.9B.9B.E6.AD.A5.EF.BC.9A.E7.BB.91.E5.AE.9A.E6.BA.90.E7.AB.99). You can bind different ports with different origin servers.

### Delete a rule
If there is an origin server bound under the rule, check the "Force deletion of rules bound with origin servers" first.
![](https://main.qcloudimg.com/raw/f47213d47f5c43243d4f8a6261ee9b0d.jpg)

## Deleting a Listener
Click **Delete** on the **HTTP/HTTPS Listener Management** tab to delete a specified listener. Any listener that is bound with an origin server can be deleted only when "Allow force deletion of listeners bound with origin servers" is selected. After deletion, the acceleration of the port for the listener stops.
![](https://main.qcloudimg.com/raw/4d73b13d363cb386f53e450f3b8660b4.jpg)

## Modifying a Listener
On the **HTTP/HTTPS Listener Management** tab, click **Modify** to modify the listener information.
HTTP listener: Supports modifying the name of the listener, as shown below:
![](https://main.qcloudimg.com/raw/dd73390b823f3008fedf35d2e21880a5.jpg)
HTTPS listener: Supports modifying the name and protocol between the listener and the origin server, and updating the certificate, as shown below:
![](https://main.qcloudimg.com/raw/4714cac4e0d1514bb21e0d64478103e3.jpg)

