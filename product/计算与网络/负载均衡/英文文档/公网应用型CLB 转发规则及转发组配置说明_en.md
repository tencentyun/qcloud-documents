
## Public Network Application-based CLB - Flow Chart

The Layer-7 business process and Layer-4 business process of the public network application-based CLB are displayed as follows:

![](//mc.qcloudimg.com/static/img/f0fa90984d263a9f7e26d4f6ee3b6c5f/image.png)

- In the Layer-7 forwarding http/https of public network application-based CLB, the user may add a corresponding domain name when creating a new forwarding rule in the listener of a LB instance.
- When only one forwarding rule is created, you can access the service by accessing VIP + URL, for it can correspond to the appropriate forwarding rule.
- When multiple forwarding rules are created, you will be prompted that a random domain name + URL may be accessed by simply accessing VIP+URL. You should access domain name + URL directly to enable the specified forwarding rules to take effect. (In other words, when more than one forwarding rules are set, it is not recommended to access service by means of VIP + URL, for a VIP may correspond to multiple domain names. Instead, you should use specified domain name + URL to access the service.)

## Public Network Application-based CLB - Forwarding Rules Configuration

### Domain Configuration Rules:
In the public network application-based CLB, when a domain is configured using the forwarding rules of Layer-7 listener, a regular expression should be adopted with a length of 1-80 characters, and only letters, numbers, "-", and "." can be contained.

## Health Check Configuration Rules
In the public network application-based CLB, when a health check path is configured using the forwarding rules of Layer-7 listener, it is / by default and must start with /; the length range is between 1 and 80 characters; regular expressions are currently not supported; it is recommended to develop a fixed URL path (static page) for health check; and letters, numbers, "*", ".", "-", "&", "#", "？",  "%", "/", "~", "^", "!", "+", ")", "(" and "|" can be contained.

### Example of Domain Matching Rules:
1. Enter IP instead of domain name in the forwarding rule, and configure multiple URLs in the forwarding group. The service is accessed via VIP + URL

2. Configure the full domain name in the forwarding rule and configure multiple URLs in the forwarding group. The service is accessed via Domain + URL

3. Configure wildcard domain name in the forwarding rule and configure multiple URLs in the forwarding group. The service is accessed via matching Domain + URL. When customers want to point different domain names to the same URL address, this method applies. Take example.qcould.com as an example, the format is as follows:
	
  	example.qcloud.com exactly matches the example.qcloud.com domain name
  
	\*.qcloud.com matches all domain names ending in qcloud.com
  
	example.qcloud.\* matches all domain names beginning with example.qcloud
  
Note: If the requested domain name does not match any of the forwarding rules, a 403 error will be returned.

2. Configure the domain name in the forwarding rule and configure the fuzzy matching URL in the forwarding group. Use the prefix match to add the wildcard $ for complete match.
For example, a client wants to match any file that ends with gif, jpg, or bmp by configuring the forwarding group URL ~* \.(gif|jpg|bmp)$.

## Public Network Application-based CLB - Forwarding Group URL Matching Rules

### URL Configuration Rules:
In the public network application-based CLB, the forwarding path URL of Layer-7 listener is / by default and must start with /; the length range is between 1 and 80 characters; a regular expression should be adopted, and letters, numbers, "$", "=", "*", ".", "-", "&", "#", "？", "%", "/", "~", "^", "!", "+", ")", "(" and "|" can be contained.

### Example of URL Matching Rule:
![](//mc.qcloudimg.com/static/img/5e322824d13d70c55f12c5d34f066d4a/image.png)
 
1. Match rules: Exact match should have precedence over fuzzy match

	Example: After configuring forwarding rules and forwarding groups according to the following figure, the following requests will be matched to different forwarding groups in sequence:
  
	a. example.qloud.com/test1/image/index1.html The request is forwarded to the back-end CVM associated with forwarding group 1 due to the exact match of the URL rule set by forwarding group 1. Port 80 for RS1 and RS2 is illustrated in the figure.
	
  b. example.qloud.com/test1/image/hello.html Since this request does not exactly match the first rule, it continues to match the rules in forwarding group 2 and find that the fuzzy match succeeds. Therefore, the request will be forwarded to the back-end CVM associated with forwarding group 2. Port 81 for RS2 and RS3 is illustrated in the figure.
  
  c. example.qloud.com/test2/video/mp4/ Since this request does not match exactly the first two rules, it continues to match downwards and find that it can do a fuzzy match with the rules in forwarding group 3. Therefore, the request will be forwarded to the back-end CVM associated with forwarding group 3. Port 90 for RS4 is illustrated in the figure.
  
  d. example.qloud.com/test3/hello/index.html Since this request does not match the rules in the first three forwarding groups, a match with the common rule "default URL" set by the user shall apply. nginx will serve as a reverse proxy server to forward the request to the back-end application server such as FastCGI (php) and tomcat (jsp).
  
  e. example.qloud.com/test2/ Since this request does not exactly match the rules in the first three forwarding groups, a match with the common rule "default URL" set by the user shall apply.

2. If the service does not work properly in the user's URL rules, it will not be redirected to other pages after the successful match.
For example: If the client makes a request on example.qloud.com/test1/image/index1.html and matches the URL rules of forwarding group 1, but the back-end CVM of forwarding group 1 is running abnormally and shows 404 error page, then the user may only see 404 error page rather than other pages when accessing.

3. ***It is recommended that you point the default URL to a stable page (such as a static page, homepage, etc.) and bind it to all back-end CVMs.*** If none of the rules match, the system will point the request to the default URL page; otherwise, a 404 error page may appear.

4. If the user does not set the default URL, and none of the forwarding rules match, a 404 error will be returned when accessing the service.

