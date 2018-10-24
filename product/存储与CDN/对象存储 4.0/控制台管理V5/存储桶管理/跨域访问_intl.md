## Basic Concepts

Cross-domain Access (CORS: Cross-Origin Resource Sharing) refers to an HTTP request initiated by a resource for the resource from a different domain than the one which the first resource itself serves.

Cloud object storage used for cross-domain access supports response to OPTIONS request, and returns the specifically configured rules to the browser according to the rules set by the developer. But the server **will not verify** whether the subsequently initiated cross-domain request is in compliance with these rules.

For more details, please refer to [HTTP Access Control at Mozilla Developer Network](https://developer.mozilla.org/en-us/docs/Web/HTTP/Access_control_CORS).

## Configuration Instructions

Configurations for responding to the OPTIONS request are provided in the console and multiple rules are supported.

![](https://mc.qcloudimg.com/static/img/f8a60472225f2ebd0cbdf894a38839c2/image.png)

Click **New Rule** button or **Modify** button, a window for rule editing will pop-up.

![](https://mc.qcloudimg.com/static/img/1f474c86d6c409497173a9daa90db6b7/image.png)

### Allow-Origin

Refer to origins that are allowed. Match of multiple origin domains in a rule is supported, with one domain per line.

For example: `http://image.qq.com` or `http://*.qq.com`

A single wildcard `*` is also supported. This will allow requests from all origins. When the Origin configuration allows all origins, the Allow-Credentials option cannot be checked for True.

### Allow-Method

It indicates which (one or more) methods can be used for resource requests.

For example: `PUT` and `POST`


### Allow-Credentials

It is used to inform the client to respond to requests with credentials (HTTP cookies and authentication information) if the request contains Credentials as True; otherwise, its response will be ignored.

When the origin is unlimited (i.e. configured as `*`), this option should not be checked.


### Allow-Headers

When an OPTIONS request is sent, the option is used to notify the server end about which custom HTTP request headers are allowed to be used by subsequent requests.

For example: `x-cos-meta-md5`


### Expose-Headers

Configure what kind of custom header information from the server end can be received by the browser.

For example: `x-cos-acl`

### Max-Age

Configure validity period for OPTIONS request to be responded.

For example: `600`

## Example

### Simple Request

The following instance is when Allow-Origin is configured as *, how a GET request is sent and gets responded.

```http
<
GET /resources/public-data/ HTTP/1.1
Host: bar.other
Connection: keep-alive
Referer: http://foo.example/examples.html
Origin: http://foo.example
>
HTTP/1.1 200 OK
Connection: Keep-Alive
Access-Control-Allow-Origin: *
[data]
```

### Pre-request

When the request meets one of the following conditions, it will be regarded as a pre-request, and then an OPTIONS request is sent to the server in advance to verify whether cross-domain operations are possible:

- A request is initiated in a way **other than** GET, HEAD, or POST
- Though POST is used, the request data is of type other than `application/x-www-form-urlencoded`, `multipart/form-data` or `text/plain`
- A custom request header is used

For example, try to send a cross-origin POST request with text/xml content:

```http
<
OPTIONS /resources/post-here/ HTTP/1.1
Host: bar.other
Origin: http://foo.example
Connection: keep-alive
Access-Control-Request-Method: POST
Access-Control-Request-Headers: X-PINGOTHER
>
HTTP/1.1 200 OK
Date: Mon, 01 Dec 2008 01:15:39 GMT
Access-Control-Allow-Origin: http://foo.example
Access-Control-Allow-Methods: POST, GET, OPTIONS
Access-Control-Allow-Headers: X-PINGOTHER
Access-Control-Max-Age: 1728000
Connection: Keep-Alive
Content-Type: text/plain
<
POST /resources/post-here/ HTTP/1.1
Host: bar.other
Connection: keep-alive
X-PINGOTHER: pingpong
Content-Type: text/xml; charset=UTF-8
Referer: http://foo.example/examples/preflightInvocation.html
Content-Length: 55
Origin: http://foo.example
[data]
```

## References

For cross-domain configuration and detailed rules, please refer to external information [HTTP Access Control at Mozilla Developer Network](https://developer.mozilla.org/en/docs/Web/HTTP/Access_control_CORS).


