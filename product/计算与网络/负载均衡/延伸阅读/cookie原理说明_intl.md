
## What Is a Cookie? 

HTTP is a stateless protocol, which means that the client and the server do not need to establish a persistent connection. The connection between the client and the server is based on a request-response mode: the client and the server establish a connection - the client submits a request - the server returns a response after receiving a request, and then they are disconnected.

So, if the client and the server will be disconnected and no longer have any relationship after a request is completed, when a user logs in on page 1 and then is navigated to page 2 of the same Web application, how does page 2 know that the user has already logged in? In other words, when the client initiates another request, how does the server determine whether the two different requests are from the same client?

Under HTTP protocols, the server is unable to identify the relationship between requests. To determine the relationship, a status is necessary to identify each request. If the status IDs of two requests are the same, it means that the two requests are initiated from the same client.

Cookie is a status bit used to identify each request. After years of development, cookie becomes more and more standardized, and has been regarded as a universal standard.

## How Do Cookies Work?

![](//mc.qcloudimg.com/static/img/72f96871e29f8a509cd0904d74d63bf3/image.png)

1) When a request is initiated to Tencent Cloud for the first time, the HTTP request header is as follows:

```
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8 
Accept-Encoding:gzip, deflate, sdch 
Accept-Language:en,zh-CN;q=0.8,zh;q=0.6 
Connection:keep-alive 
Host:cloud.tencent.com
```

2) After the request reaches Tencent Cloud server, Tencent Cloud server will generate a response, and write cookie information in the response header:

```
Set-Cookie:BD_HOME=1; path=/ 
Set-Cookie:__bsi=14934756243064632384_00_0_I_R_174_0303_C02F_N_I_I_0; expires=Thu, 19-Nov-15 14:14:50 GMT; domain=www.qcloud; path=/ 
Set-Cookie:BDSVRTM=172; path=/
```

3) After receiving the response header, the client browser will write the cookie information to the local for management.

4) When initiating another request to the server, the client will send a HTTP request header containing Cookie:  name=value; name2=value2 together with the cookie stored in the local previously. The request header information includes:

```
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8 
Accept-Encoding:gzip, deflate, sdch 
Accept-Language:en,zh-CN;q=0.8,zh;q=0.6 
Connection:keep-alive 
Cookie:BD_HOME=1; BDSVRTM=0; BD_LAST_QID=1507196234531915875957057 
Host:cloud.tencent.com
```

5) After receiving the request, the server will get the cookie information from the request header, analyze the cookie data and then return a response to the client.

This is how cookies are used to transmit information between the client and the server.

## Cookie Lifetime

Cookies have a lifetime. Once the expiration date is reached, the cookie on the client will be deleted. The server can determine how long a cookie can "survive" on the client when creating the cookie. The cookie will be ended in the following cases:

- Cookies for which the expiration time is not specified. If the server does not specify the expiration time of a cookie when creating a cookie, the client will write such cookie in a chunk of memory opened by the browser. When the browser is closed, the memory will be freed, and the corresponding cookie will be ended; 

- Cookies for which the expiration time is specified. If the server specifies the expiration time when creating a cookie, when the expiration time is reached, the corresponding cookie will be deleted;

- The number of cookies in the browser reaches the limit. The browser will delete some old cookies by a certain policy to make room for new cookies;

- You can also delete cookies by yourself.

## Cookie Management
When creating a cookie, the server will generally specify the following two options:

- domain 
- path

These two options determine the domain and location of the created cookie.

By default, "domain" will be set to the domain under which the page creating the cookie is located. When the client sends a request to the same domain again, the cookie will be sent to the server. When the "domain" of a cookie is set to a first-level domain, all the second-level domains under this domain will have the same cookie. There are often cookie conflicts between the top-level and second-level domains.

When a request is sent, the browser will make an end comparison of the "domain" value and the requested domain (that is, compare the domains from the end of string), and send the matched cookie to the server.

- When not specified, "domain" is the domain of the access address by default. If it is a top-level domain access, the cookie set can also be shared by other second-level domains. So login and other operations are generally performed under the top-level domain.

- Second-level domains can read cookies that set "domain" to a top-level domain or to themselves, but cannot read the cookies of other second-level domains. Therefore, if you want to share a cookie among multiple second-level domains, you need to set "domain" to a top-level domain, and then, you can use the cookie in all second-level domains. One thing to note here is that the top-level domain can only get the cookies that set "domain" to a top-level domain, but cannot get the cookies that set "domain" to a second-level domain.

As for the "path", it stipulates that a cookie message header can be sent for the URL requested by the client only when there is a path specified by "path". It determines the matching rule for the client to send a cookie to the server. Generally, the "path" value will be compared with the requested URL from the beginning by character, and if the characters are matched, the cookie message header will be sent. It should be noted that the "path" attribute will be compared only if the "domain" option is satisfied. The default value for the "path" attribute is to send the path part of the URL corresponding to the Set-Cookie message header.

The above is a summary for the management of cookies with respect to the limitations of browsers and the options for generating cookies. Next, we will show you how to create and get cookies with some simple codes.

### The server creates a cookie
The Tencent Cloud server creates a cookie by sending an HTTP message response header with Set-Cookie. For example:

```
// Create a cookie object 
Cookie co = new Cookie("site", "http://cloud.tencent.com"); 
co.setDomain("test.com"); 
// Send the cookie to the client via the response header 
response.addCookie(co);

Cookie co = new Cookie("site", "http://qcloud.com"); 
co.setDomain("test.com"); 
co.setPath("/pages"); 
co.setMaxAge(3600); // In seconds 
co.setHttpOnly(true); 
co.setSecure(false); 
response.addCookie(co);
```

### The client reads the cookie
When the client initiates a request to the server, it will also send corresponding cookies to the server if the "domain" and "path" are matched. If there are too many cookies under the same "path", the http request header may be overlong. After the request reaches the server, we can read cookies like this:

```
Cookie[] cookies = request.getCookies(); 
if (cookies != null) { 
for (int i = 0; i < cookies.length; ++i) { 
// Get a specific cookie 
Cookie cookie = cookies[i]; 
// Get the name of the cookie 
String name = cookie.getName(); 
String value = cookie.getValue(); 
out.print("Cookie name: " + name + "   Cookie value:" + value + "
"); 
} 
}
```
