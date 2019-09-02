## 什么是cookie? 
HTTP协议是无状态的，也就是说客户端和服务器端不需要建立持久的连接。由于客户端和服务器端的连接是基于一种请求应答模式，即客户端和服务器建立一个连接-客户端提交一个请求-服务器端收到请求后返回一个响应，然后二者就断开连接。

若客户端和服务器在完成一次请求以后就断开了连接，二者之间就不再有任何关系了；那么，当用户在页面1进行了登录后跳转到了同一个Web应用的页面2时，如何在页面2知道用户已经进行了登录呢？亦即当客户端再次发起请求的时候，服务器端如何判断两次不同的请求来自同一个客户端呢？

HTTP协议下，服务器是无法区分每一次请求之间的联系的。要判断这种联系就需要有一个状态来标识每一次请求，如果两次请求的状态标识是一样的，这就表明这两个请求是从同一个客户端发起的。

Cookie就是这样一个用来标识每一次请求的状态位。经过多年的发展Cookie变得越来越规范，后来直接成为了一个通用标准。

## cookie的工作原理

![](//mccdn.qcloud.com/static/img/58f3b8fb6182198e549315f3192bd11a/image.png)

1) 当首次向腾讯云发起请求时，HTTP请求头如下：

```
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8 
Accept-Encoding:gzip, deflate, sdch 
Accept-Language:en,zh-CN;q=0.8,zh;q=0.6 
Connection:keep-alive 
Host:cloud.tencent.com
```

2) 请求到达腾讯云的服务器以后，腾讯云的服务器生成响应，并在响应的头部写入cookie信息：

```
Set-Cookie:BD_HOME=1; path=/ 
Set-Cookie:__bsi=14934756243064632384_00_0_I_R_174_0303_C02F_N_I_I_0; expires=Thu, 19-Nov-15 14:14:50 GMT; domain=www.qcloud; path=/ 
Set-Cookie:BDSVRTM=172; path=/
```

3) 当客户端浏览器接收到响应头以后，会将cookie信息写入本地进行管理。

4) 再次向服务器发起请求时，客户端通过发送一个带有Cookie: name=value; name2=value2的HTTP请求头将之前存在本地的cookie一起发送过去。请求的头部信息为：

```
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8 
Accept-Encoding:gzip, deflate, sdch 
Accept-Language:en,zh-CN;q=0.8,zh;q=0.6 
Connection:keep-alive 
Cookie:BD_HOME=1; BDSVRTM=0; BD_LAST_QID=1507196234531915875957057 
Host:cloud.tencent.com
```

5) 服务器接收到请求以后，从请求头中获得cookie信息，分析cookie数据后向客户端返回响应。

以上就是cookie在客户端和服务器之间进行传递信息的基本过程。

## cookie的生命周期

cookie是有生命周期的。一旦到了cookie的失效日期，客户端的cookie就会被删除，服务器在创建cookie时可以控制一个cookie可以在客户端“存活”多长时间。在以下几种情况下，cookie都会结束它自己的生命周期：

- 未指定过期时间的cookie。当服务器创建一个cookie的时候没有指定对应的过期时间时，客户端会将这类cookie写入浏览器开辟的一块内存中，当关闭浏览器以后，这块内存也就被释放了，对应的cookie也就是结束了它的生命；

- 指定过期时间的cookie。当服务器创建一个cookie的时候指定了对应的过期时间时，当到达了过期时间时，对应的cookie就会被删除；

- 当浏览器中的cookie数量达到了限制时。浏览器会按照某种策略删除一些旧的cookie，腾出空间来创建新的cookie；

- 也可以人为删除cookie。

## cookie管理
服务器端创建一个cookie时，一般都会指定以下两个选项：

- domain 
- path

这两个选项决定了创建的cookie属于哪个域名下的哪个位置。

对于domain选项，默认情况下，domain会被设置为创建该cookie的页面所在的域名。当客户端再次给相同域名发送请求时，cookie会一起被发送至服务器。当cookie的domain选项被设置为一个一级域名时，此域名下的所有二级都将同时拥有相同的cookie，经常会出现顶级域名和二级域名的cookie冲突问题。

我们在发送请求时，浏览器会把domain的值与请求的域名做一个尾部比较（即从字符串的尾部开始比较），并将匹配的cookie发送至服务器。

- 当我们未指定domain时，默认的domain为访问地址的域名。如果是顶级域名访问，那么设置的cookie也可以被其他二级域名所共享，因此登录等操作一般都在顶级域名下进行操作。

- 二级域名可以读取设置了domain为顶级域名或者自身的cookie，但是不能读取其他二级域名domain的cookie，因此想要cookie在多个二级域名中共享的时候，需要设置domain为顶级域名，这样就可以在所有二级域名里面使用该cookie。这里需要注意的是顶级域名只能获取到domain设置为顶级域名的cookie，无法获取domain设置为二级域名的cookie。

说完domain，再来说说path选项。path选项规定，客户端请求的URL只有在存在path指定的路径时，才会发送cookie消息头，它决定了客户端发送cookie到服务器端的匹配规则。通常是将path选项的值与请求的URL从头开始逐字符比较，如果字符匹配，则发送cookie消息头。需要注意的是，只有在domain选项满足之后才会对path属性进行比较。path属性的默认值是发送Set-Cookie消息头所对应的URL中的path部分。

以上从浏览器本身的限制和生成cookie时的选项对cookie的管理进行了简单的总结。接下来就通过一些简单的代码来演示如何创建和获取cookie。

### 服务器端创建cookie
腾讯云服务器通过发送一个带有Set-Cookie的HTTP消息响应头来创建一个cookie。例如：

```
// 创建一个cookie对象 
Cookie co = new Cookie(“site”, “http://cloud.tencent.com“); 
co.setDomain(“test.com”); 
// 通过响应头，将cookie发送到客户端 
response.addCookie(co);

Cookie co = new Cookie(“site”, “http://qcloud.com“); 
co.setDomain(“test.com”); 
co.setPath(“/pages”); 
co.setMaxAge(3600); // 单位为秒 
co.setHttpOnly(true); 
co.setSecure(false); 
response.addCookie(co);
```

### 客户端读取cookie
客户端向服务器发起请求时，在domain和path匹配的情况下，会将对应的cookie一起发送到服务器端。如果一个path下设置的cookie太多，就可能出现http请求头超长的问题。请求到达服务器端以后，我们可以这样读取cookies：

```
Cookie[] cookies = request.getCookies(); 
if (cookies != null) { 
for (int i = 0; i < cookies.length; ++i) { 
// 获得具体的Cookie 
Cookie cookie = cookies[i]; 
// 获得Cookie的名称 
String name = cookie.getName(); 
String value = cookie.getValue(); 
out.print(“Cookie名:” + name + ”   Cookie值:” + value + “
”); 
} 
}
```