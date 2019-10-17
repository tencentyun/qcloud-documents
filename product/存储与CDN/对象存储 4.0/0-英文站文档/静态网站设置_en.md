## Basic Concepts

By configuring a Bucket for website hosting, you can host a static website on Tencent Cloud COS (Bucket with a custom domain only). A static website contains only static content (such as HTML) or client-side scripts, while a dynamic website contains server-side scripts that rely on server-side for processing, such as PHP, JSP, or ASP.NET. Tencent Cloud COS supports the hosting of static websites, but does not support programing server-side script.

> To deploy a dynamic website, please use Tencent Cloud CVM for server-side code deployment.

To host a static website, you need to create a Bucket first and then upload its content to this Bucket and customize the domain before you can access the different resources on the static website through a specific address:

Assume that you has created a Bucket, customized its domain (say, `www.example.com`) and enabled the static website function.  The following example URL will provide access to different website contents.

`http://www.example.com/` or `http://example.com` will return the default index file configured by the user for that website;


`http://example.com/photo.jpg` will request the photo.jpg file located in the root directory of the Bucket; if this file is not found, an error file indicated with 404 error will be returned;


`http://example.com/docs/doc1.html` will request the docs/doc1.html file located in the root directory of the Bucket; if an error is returned, the error file indicated with the error code will be returned.

To configure a Bucket for hosting a static website, you should add the website configuration to the Bucket. This configuration contains the following items.

## Static Access

When you access the Bucket file resource via a custom domain (CNAME or CDN binding), the file is directly opened by a browser by default. Picture browsing and static html file hosting are supported.

![](https://mc.qcloudimg.com/static/img/fe07f2899c8e418414776cebed904b9b/image.png)

Static website function helps to configure the way to open a file. When this function is enabled, a file will be opened by a browser by default after downloaded rather than being saved to local storage.

**Note**: This feature is only relevant when a custom domain is set for the Bucket. When the default domain (CDN accelerated domain and COS direct access domain) is used to access the resource, a download box will **always** pop up. Only after [binding a custom domain](/doc/product/436/6252) and enabling the static website function, you can opened file resources directly in the browser.

Assume that you have created a Bucket, uploaded test.html to the root directory, and bound the custom domain `www.example.com` to the Bucket through CNAME or CDN console. If the static website function is not enabled, download box will pop up when you access `http://www.example.com/test.html`, and you can choose to save the file to the local machine; after the static website function is enabled, you can view the page contents of test.html directly in the browser when accessing the file `http://www.example.com/test.html` via a custom domain.

## Index Document

When you enter a URL such as `http://example.com`, you are not requesting a specific page. In this case, the Web server will provide a default page that contains the directory where the table of contents of the requested website is stored. This default page is called an index document and is named index.html.

When any Bucket directory including the root directory is accessed using a custom domain (CNAME or CDN binding) with URL address ending with /, the index.html in this directory will be automatically matched at first, and then the index.htm. If both files do not exist, a 404 error is returned.

Index document is the webpage that is returned when a request is made to the root directory or any of the subdirectories of the website. For example, if you enters `http://www.example.com` in the browser, you do not request any specific page. In this case, you can enable the static website service in COS and provides an index page to direct the access to the specified page. You can upload an object named `index.html` or `index.htm` and configure it to public-read. Please refer to [Configure Static Access](/doc/product/436/6249) for details on enabling static website functions.

![](//mccdn.qcloud.com/static/img/e56e0999c45bd38601b5e29316fee84c/image.jpg)

End slash of the root level URL is optional. For example, if you configure a website with index.html as an index document, any of the following URLs will return index.html.

`http://example.com/`

`http://example.com`

If you create a folder structure in the Bucket (please refer to [Bucket Overview - Folders and Objects in Bucket](/doc/product/436/6244)), you may need to add an index document at each level. When accessing any Bucket directory including the root directory using a custom domain (CNAME or CDN binding), and the URL address ends with /, it will, by priority, automatically match index.html in the directory, followed by index.htm. If both files do not exist, a 404 error is returned.

> Note: Accessing a resource ending in `/` using [CDN Accelerated Address](/doc/product/436/6252) or [COS Direct Access Address](/doc/product/436/6252) will return an error.

## Error Document

When a Bucket is accessed through a custom domain (CNAME or CDN binding), if a 404 or 403 error is triggered, you can optionally provide a custom error document that provides additional guidance to the customer.

Currently only files under the **root directory** of a Bucket can be specified; please use files such as .html and .htm that can be recognized by browsers. If the file is unrecognizable to the browser, the browser will usually return an error `INVALID_RESPONSE`.

After using the custom domain function, you can customize a specific page to be returned by Tencent Cloud COS when an error occurs. The following table lists the HTTP error codes supported by the current custom page.

| HTTP error code | Description                                       |
| -------- | ---------------------------------------- |
| 403 | Forbidden.  It can be regarded as that users do not have the permission to access this website; the server rejects your request for service. This error usually occurs when the object has been configured a specific [access permission](/doc/product/436/6259).  |
| 404 | Not Found. The server did not find the requested resource. This usually happens in the following scenarios:<br> - The requested object does not exist<br> - No index page is specified when the COS root or folder directory is requested<br> - The Bucket specified in the URL does not exist.  |

You can specify a custom return page for 403 and 404 errors. Make sure that the page has been uploaded to the Bucket configured as a website and set the permissions to ***Public Read***. Thus, when you access Bucket via a custom domain (CNAME or CDN binding) and trigger a 404 or 403 error, the specified content will be returned.

If you use the CDN Accelerated Address or COS Direct Access Address for access and a 403/404 error occurs, the configured error page will not take effect.

> Note: If the error code points to a file unrecognizable to the browser, such as a .zip file, most of the browsers will display an error indicating the access request is disabled or denied.

![](//mccdn.qcloud.com/static/img/efd9fd50380bcdb575772622a4ecffea/image.jpg)

## Example

### Configuring Static Access

You have created a Bucket and bound the custom domain `www.example.com` to the Bucket via CNAME or CDN console. You have placed an index.htm file in the root directory.

**Before enabled**

> If you use a custom domain to access the file `http://www.example.com/index.htm`, a download box will pop up, where you can save the index.htm file to the local machine.

![](//mccdn.qcloud.com/static/img/939165a47b8da3c678577a9ff945e80a/image.png)

**After enabled**

> If you use a custom domain to access the file `http://www.example.com/index.htm`, the content of index.htm will be directly displayed in the browser.

![](//mccdn.qcloud.com/static/img/42eac89413e3916d7c160020037b6783/image.png)

### Configuring Index Document

You have created a Bucket and bound the custom domain `www.example.com` to the Bucket via CNAME or CDN console. You have placed the following documents:

> index.html
>
> dir/index.htm
>
> dir/index.html
>
> dir2/
>
> dir3/index.htm

**Before enabled**

> Visit `http://www.example.com` and the 404 error returns.
>
> Visit `http://www.example.com/dir` and the 404 error returns, because the dir file does not exist under the root directory.
>
> Visit `http://www.example.com/dir/` and the 404 error returns.
>
> Visit `http://www.example.com/dir2/` and the 404 error returns.
>
> Visit `http://www.example.com/dir3/` and the 404 error returns.

**After enabled**

> Visit `http://www.example.com` and the content of the index.html file returns.
>
> Visit `http://www.example.com/dir` and the 404 error returns, because the dir file does not exist under the root directory.
>
> Visit `http://www.example.com/dir/` and the content of the dir/index.html file returns, because the index.html has higher priority than the index.htm.
>
> Visit `http://www.example.com/dir2/` and the 404 error returns because the index file to be matched does not exist.
>
> Visit `http://www.example.com/dir3/` and the contents of the dir3/index.htm file returns.

### Configuring Error Document

You have created a Bucket and bound the custom domain `www.example.com` to the Bucket via CNAME or CDN console.

You have placed the 404.htm file under the root directory and configure 404 error pointing to 404.html. Assume that there is no abcd.txt file under the root directory.

**Before enabled**

> Visit `http://www.example.com/abcd.txt` and the status code 404 returns, including the default error message.

**After enabled**

> Visit `http://www.example.com/abcd.txt` and the specified 404.htm page returns; the HTTP status code is still 404.


