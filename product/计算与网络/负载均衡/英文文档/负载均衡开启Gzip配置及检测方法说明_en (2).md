In the **public network application-based and public network (with static IP) cloud load balancer** instances, **HTTP/HTTPS protocol** is supported to enable gzip compression by users by default. Compressing web pages via the gzip feature can effectively reduce the amount of data transmitted on the network and improve the access speed of the client browser. When using the feature, please keep the following in mind:

### 1. Notes

- **GZIP of back-end CVM is required to be enabled synchronously**
For common Nginx service containers, you must enable GZIP in their configuration files (nginx.conf by default) and restart the service
```
gzip on;
```
- **Now the cloud load balancer supports file types below. And you can specify the file type in the gzip_types configuration item for compressing**
```
application/atom+xml application/javascript application/json application/rss+xml application/vnd.ms-fontobject application/x-font-ttf application/x-web-app-manifest+json application/xhtml+xml application/xml font/opentype image/svg+xml image/x-icon text/css text/plain text/x-component;
```
Note: GZIP support for the above file types must be enabled synchronously in the backend CVM business software of cloud load balancer.
- **A compression request flag must be contained in the client request**
You need to enable compression, and the client must carry the following flag for requests:
```
Accept-Encoding: gzip,deflate,sdch
```

### 2. Example of GZIP Enabling Process by Backend CVM

Operating environment of example Cloud Vitural Machine: Debian 6

1. Use vim to open the Nginx configuration file by user path:
```
vim /etc/nginx/nginx.conf
```
2. Find the following codes:
```
gzip on;
gzip_min_length 1k;
gzip_buffers 4 16k;
gzip_http_version 1.1;
gzip_comp_level 2;
gzip_types text/html application/json;
```
Detailed syntax of the above codes:
gzip: enable or disable gzip module.

> 	Syntax: gzip on/off
>   Scope: http, server, location

gzip_min_length: Set the minimum bytes for a page allowed to be compressed. The number of bytes for a page is obtained from the Content-Length of header. The default value is 1k.

> 	Syntax: gzip_min_length length
>   Scope: http, server, location

gzip_buffers: Set how many units of cache are used by system to store the gzip compressed result data flow. 4 16k represents the unit is 16k, and memory is applied by four times of 16k according to the original data size.

> 	Syntax: gzip_buffers number size
>   Scope: http, server, location

gzip_comp_level: gzip compression ratio. The range is 1 ~ 9. 1 presents the minimum compression ratio with the fastest processing speed, while 9 presents the maximum compression ratio with the slowest processing speed (faster transmission but more CPU consumption).

> 	Syntax: gzip_comp_level 1..9
>   Scope: http, server, location

gzip_http_level: The lowest version of HTTP allowed to use the gzip feature. If HTTP/1.0 is set, the gzip feature can be used for HTTP/1.0 and is upward compatible with HTTP/1.1. Since Tencent Cloud now supports HTTP/1.1 across the network, no changes are required.

>   Syntax: gzip_http_version 1.0 | 1.1;
>   Scope: http, server, location

gzip_types: Match MIME types for compression. "text/html" type will be compressed by default. In addition, gzip under Nginx does not compress static resource files such as javascript and images by default. You can specify the MIME types to be compressed via gzip_types, and other types will not be compressed. ***For example, if json format data needs to be compressed, you need to add application/json data in this statement***
The supported types are as follows:
>   text/html text/plain text/css application/x-javascript text/javascript application/xml

>   Syntax: gzip_types mime-type [mime-type ...]
>   Scope: http, server, location

3 . If the configuration changes, save the file and exit, go to the Nginx bin file directory, and execute the following command to reload Nginx
```
./nginx -s reload
```
4. Use the curl command to test whether gzip was successfully enabled
```
curl -I -H "Accept-Encoding: gzip, deflate" "http://cloud.tencent.com/example/"
```
