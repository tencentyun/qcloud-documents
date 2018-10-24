## Basic Concepts

Changing the HTTP Header of an Object will not change the content of the Object, except adding the key-value pair to the Object. The Object Header is a string sent by the server before it sends the HTML data to the browser using HTTP protocol. You can change the response mode of a page or send the configuration information by modifying the Header. For example, changing the cache expiration time will not change the file. For example, if the content-encoding in Header is changed to gzip, but the file has not been compressed with gz in advance, a decoding error will occur.

## About the Configuration

COS provides 5 types of header identifiers for configuration:

|       Header        |                  Description                  |                Example                |
| :-----------------: | :----------------------------------: | :------------------------------: |
|    Cache-Control    |            Caching mechanism of the file           |       no-cache; max-age=200       |
|    Content-Type     |             MIME information of the file           |            text/html             |
| Content-Disposition | Extension of MIME protocol | attachment; filename="fname.ext" |
| Content-Language   |                Language of the file                 |              zh-CN               |
|  Content-Encoding   |  Encoding format of the file   | UTF-8 |
|  x-cos-meta-custom content   |   Custom content    |              Custom content               |

## How to Make the Configuration

Enter the console, select "Bucket", then select "Object", and click **Set Header**.

![](https://mc.qcloudimg.com/static/img/dc304b8df347ff565f6424eb965ff8db/image.png)

Add parameters in the "Set Header" pop-up window, and select a type. For custom content, you need to enter the custom name. Enter the values, and click OK to save.

![](//mccdn.qcloud.com/static/img/3bb5a7c32049a07d8077477f7106fcf7/image.jpg)


## Example

A Bucket named test is created under the APPID 1250000000.

Object a.txt is uploaded to the Bucket root directory.

If you do not customize the Header, the browser or the client will get the following Object headers during download:

```http
> GET /a.txt HTTP/1.1
> Host: test-1250000000.file.myqcloud.com
> Accept: */*

< HTTP/1.1 200 OK
< Content-Language:zh-CN
< Content-Type: text/plain
< Content-Disposition: attachment; filename*="UTF-8''a.txt"
< Access-Control-Allow-Origin: *
< Last-Modified: Wed, 20 Apr 2016 18:23:35 GMT
```

If you add the following parameters:

![](//mccdn.qcloud.com/static/img/3bb5a7c32049a07d8077477f7106fcf7/image.jpg)

When you send another request, the browser or the client will get the following Object headers:

```http
> GET /a.txt HTTP/1.1
> Host: test-1250000000.file.myqcloud.com
> Accept: */*

< HTTP/1.1 200 OK
< Content-Language:zh-CN
< Cache-Control: no-cache
< Content-Type: image/jpeg
< Content-Disposition: attachment; filename*="abc.txt"
< x-cos-meta-md5: 1234
< Access-Control-Allow-Origin: *
< Last-Modified: Wed, 20 Apr 2016 18:23:35 GMT
```


