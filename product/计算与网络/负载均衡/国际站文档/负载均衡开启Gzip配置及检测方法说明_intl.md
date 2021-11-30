In **public network-based (with daily rate)** cloud load balancer instance, *http/https protocol* supports the user to enable Gzip compression function.  After Gzip compression is enabled, the browser does not need to be configured (mainstream browsers all support Gzip).  For CVM, users need to configure http 1.0 as the lowest http version supporting Gzip.  If the configuration is not made on client RS side and thus the default nginx (http1.1 version) is used, incompatible issues will then occur as Tencent Cloud uses http1.0 protocol internally. The following example shows how to modify Gzip configuration. 

Example RS Operating Environment: Debian 6 
1. Use vim to open the Nginx configuration file by user path: 
```
vim /etc/nginx/nginx.conf
```
2. Find the following code to modify: 
```
gzip on;
gzip_min_length 1k;
gzip_buffers 4 16k;
gzip_http_version 1.0;
gzip_comp_level 2;
```
Part of the code function is as follows: 
Line 1: Enable Gzip 
Line 2: Generally no need to change, which means that data at the critical value is not compressed and only data more than 1K is compressed
Line 3: No need to change the buffer
Line 4: nginx defaults to HTTP/1.1, but the lowest version supported by Tencent Cloud is HTTP/1.0, so it should be changed to **gzip_http_version 1.0**
Line 5: compression level, 1-10. The greater the number, the better the compression and the longer the time 

3. Save the file and exit, go to the Nginx bin file directory, and execute the following command to reload Nginx 
```
./nginx -s reload
```
4. Use the curl command to test whether Gzip was successfully enabled
```
curl -I -H "Accept-Encoding: gzip, deflate" "http://cloud.tencent.com/example/"
```

