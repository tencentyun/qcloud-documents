## Business Process Chart

The Layer-7 business process and Layer-4 business process of the public network application-based CLB are displayed as follows:

![](https://mc.qcloudimg.com/static/img/de6af7fca35640ed6d0937f05f5039d2/image.png)

- In the Layer-7 forwarding http/https of the public network application CLB, you can add a domain name for the new forwarding rule in the listener of a LB instance.
- When only one forwarding rule is created, you can access the service by accessing VIP + URL, for it can correspond to the appropriate forwarding rule.
- When multiple forwarding rules are created, you will be prompted that a random domain name + URL may be accessed by simply accessing VIP+URL. You should access domain name + URL directly to enable the specified forwarding rules to take effect. In other words, when more than one forwarding rules are set, it is not recommended to access service by means of VIP + URL, because a VIP may correspond to multiple domain names. Instead, you should use specific domain name + URL to access the service.

## Notes about Configuration of Forwarding Rules

### Domain Configuration Rules
In the public network application CLB, when a domain is configured using the forwarding rules of Layer-7 listener, a regular expression should be adopted with a length of 1-80 characters.

- Character sets supported in non-regular domain names are as follows:
`a-z` `0-9` `.` `-` 
			
- A wild card domain name only supports  
`*.example.com` or `www.example.*`. Only one \* can occur in a single domain name. 		

- Character sets not supported in the regular expression of domain names are as follows:
`"` `{` `}` `;` `~` `'` ` ` ` `blank space` 

- The followings is an example of regular domain names supported by application-based cloud load balancers:
`~^www\d+\.example\.com$`

### Health Check Configuration Rules

If the domain name you entered is a wildcard or regular one, you need to specify a fixed domain name for the health check. The character sets supported in a domain name for health check are as followings:
`a-z` `0-9`  `_` `.` `-` 

In the public network application CLB, when a health check path is configured using the forwarding rules of Layer-7 listener, Default is "/" and must start with "/" with a maximum of 80 characters. Regular expression is not supported. It is recommended to specify a fixed URL path (static page) for health check. The character sets supported in path configuration for health check are as followings:
`a-z` `A-Z` `0-9` `_` `.` `-` `/` `=` `?`

### Example of Domain Name Matching Rules:

1. Enter IP instead of domain name in the forwarding rule, and configure multiple URLs in the forwarding group. The service is accessed via VIP + URL.

2. Configure the full domain name in the forwarding rule and configure multiple URLs in the forwarding group. The service is accessed via Domain + URL.

3. Configure wildcard domain name in the forwarding rule and configure multiple URLs in the forwarding group. The service is accessed via matching Domain + URL. When customers want to point different domain names to the same URL, this method applies. Take example.qcould.com as an example, the format is as follows:
	`example.qcloud.com` exactly matches the example.qcloud.com domain name
  `\*.qcloud.com` matches all domain names ending in qcloud.com
 `example.qcloud.\*` matches all domain names beginning with example.qcloud
  >Note: If the requested domain name does not match any of the forwarding rules, a 403 error is returned.

4. Configure the domain name in the forwarding rule and configure the fuzzy matching URL in the forwarding group. Use the prefix match to add the wildcard $ at the end for complete match.
For example, a customer wants to match any file that ends with gif, jpg, or bmp by configuring the forwarding group URL ~* \.(gif|jpg|bmp)$.

## Notes about Forwarding Group URL Matching Rules

### URL Configuration Rules

In the public network application CLB, the forwarding path URL of Layer-7 listener is "/" by default and must start with "/" with a maximum of 80 characters. Regular expressions are supported.

A non-regular URL needs to start with "/ "and supports the following character sets:
`a-z` `A-Z` `0-9` `_` `.` `-`  `/` `=` `?`
		
A regular URL does not support the following character sets:
`"` `{` `}` `;` `\` ` ` ` `~`  `'` `blank space`   

### Example of URL Matching Rules

![](//mc.qcloudimg.com/static/img/1c01dcd0959105dd7821f4e22f5cd796/image.png)

 
1. Match rules: Exact match should be prior to the fuzzy match

	Example: After configuring forwarding rules and forwarding groups according to the following figure, the following requests will be matched to different forwarding groups in sequence:
  
	a. example.qloud.com/test1/image/index1.html The request is forwarded to the backend CVM associated with forwarding group 1 due to the exact match of the URL rule set by forwarding group 1. Port 80 for RS1 and RS2 is illustrated in the figure.
	
  b. example.qloud.com/test1/image/hello.html Since this request does not exactly match the first rule, it continues to match the rules in forwarding group 2 and finds that the fuzzy match succeeds. Therefore, the request will be forwarded to the backend CVM associated with forwarding group 2. Port 81 for RS2 and RS3 is illustrated in the figure.
  
  c. example.qloud.com/test2/video/mp4/ Since this request does not match exactly the first two rules, it continues to match downwards and finds that it can do a fuzzy match with the rules in forwarding group 3. Therefore, the request will be forwarded to the backend CVM associated with forwarding group 3. Port 90 for RS4 is illustrated in the figure.
  
  d. example.qloud.com/test3/hello/index.html Since this request does not match the rules in the first three forwarding groups, a match with the common rule "default URL" set by the user should apply. nginx will serve as a reverse proxy server to forward the request to the backend application server such as FastCGI (php) and tomcat (jsp).
  
  e. example.qloud.com/test2/ Since this request does not exactly match the rules in the first three forwarding groups, a match with the common rule "default URL" set by the user should apply.

2. If the service does not work properly in the user's URL rules, it will not be redirected to other pages after the successful match.
For example: If the client requests example.qloud.com/test1/image/index1.html and matches the URL rules of forwarding group 1, but the backend CVM of forwarding group 1 is running abnormally and shows 404 error page. Then, the user may only see 404 error page rather than other pages when accessing.

3. ***It is recommended that you point the default URL to a stable page (such as a static page and homepage) and bind it to all backend CVMs.*** If none of the rules match, the system points the request to the default URL page. Otherwise, a 404 error page may appear.

4. If you do not configure the default URL, and none of the forwarding rules match, a 404 error is returned when you access the service.

