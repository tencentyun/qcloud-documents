### 同步解析接口
```Java
/**
 * HTTPDNS 同步解析接口
 * 首先查询缓存，若存在则返回结果，若不存在则进行同步域名解析请求
 * 解析完成返回最新解析结果
 * 返回值字符串以“;”分隔，“;”前为解析得到的 IPv4 地址（解析失败填“0”），“;”后为解析得到的 IPv6 地址（解析失败填“0”）
 * 返回示例：121.14.77.221;2402:4e00:1020:1404:0:9227:71a3:83d2
 * @param domain 域名（如www.qq.com）
 * @return 域名对应的解析 IP 结果集合
 */
String ips = MSDKDnsResolver.getInstance().getAddrByName(domain);

/**
 * HTTPDNS 同步解析接口（批量查询）
 * 首先查询缓存，若存在则返回结果，若不存在则进行同步域名解析请求
 * 解析完成返回最新解析结果
 * 返回值 ipSet 即解析得到的 IP 集合
 * ipSet.v4Ips 为解析得到 IPv4 集合, 可能为 null
 * ipSet.v6Ips 为解析得到 IPv6 集合, 可能为 null
 * 单独域名返回结果示例：IpSet{v4Ips=[121.14.77.201, 121.14.77.221], v6Ips=[2402:4e00:1020:1404:0:9227:71ab:2b74, 2402:4e00:1020:1404:0:9227:71a3:83d2], ips=null}
 * 多域名返回结果示例：IpSet{v4Ips=[www.baidu.com:14.215.177.39, www.baidu.com:14.215.177.38, www.youtube.com:104.244.45.246], v6Ips=[www.youtube.com.:2001::1f0:5610], ips=null}
 * @param domain 支持多域名，域名以“,”分割，例如：qq.com,baidu.com
 * @return 域名对应的解析 IP 结果集合
 */
Ipset ips = MSDKDnsResolver.getInstance().getAddrsByName(domain);
```

### 异步解析接口

```Java
//  异步回调，注意所有异步请求需配合异步回调使用
MSDKDnsResolver.getInstance().setHttpDnsResponseObserver(new HttpDnsResponseObserver() {
    @Override
    public void onHttpDnsResponse(String tag, String domain, Object ipResultSemicolonSep) {
        long elapse = (System.currentTimeMillis() - Long.parseLong(tag));
        String lookedUpResult = "[[getAddrByNameAsync]]:ASYNC:::" + ipResultSemicolonSep +
                ", domain:" + domain +  ", tag:" + tag +
                ", elapse:" + elapse;
    }
});

/**
 * HTTPDNS 异步解析接口（需配合异步回调使用）
 * 首先查询缓存，若存在则返回结果，若不存在则进行异步域名解析请求
 * 解析完成会在异步回调返回最新解析结果
 * @param domain 域名（如www.qq.com）
 */
MSDKDnsResolver.getInstance()
    .getAddrByNameAsync(hostname, String.valueOf(System.currentTimeMillis()))

/**
 * HTTPDNS 异步解析接口（批量查询，需配合异步回调使用）
 * 首先查询缓存，若存在则返回结果，若不存在则进行同步域名解析请求
 * 解析完成会在异步回调返回最新解析结果
 * @param domain 支持多域名，域名以“,”分割，例如：qq.com,baidu.com
 */
MSDKDnsResolver.getInstance()
    .getAddrsByNameAsync(hostname, String.valueOf(System.currentTimeMillis()))
```
