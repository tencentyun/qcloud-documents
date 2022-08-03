### OkHttp
OkHttp 提供了 DNS 接口，用于向 OkHttp 注入 DNS 实现。得益于 OkHttp 的良好设计，使用 OkHttp 进行网络访问时，实现 DNS 接口即可接入 HTTPDNS 进行域名解析，在较复杂场景（HTTP/HTTPS/WebSocket + SNI）下也不需要做额外处理，侵入性极小。示例如下：


```Java
mOkHttpClient =
    new OkHttpClient.Builder()
        .dns(new Dns() {
            @NonNull
            @Override
            public List<InetAddress> lookup(String hostname) {
                Utils.checkNotNull(hostname, "hostname can not be null");
                String ips = MSDKDnsResolver.getInstance().getAddrByName(hostname);
                String[] ipArr = ips.split(";");
                if (0 == ipArr.length) {
                    return Collections.emptyList();
                }
                List<InetAddress> inetAddressList = new ArrayList<>(ipArr.length);
                for (String ip : ipArr) {
                    if ("0".equals(ip)) {
                        continue;
                    }
                    try {
                        InetAddress inetAddress = InetAddress.getByName(ip);
                        inetAddressList.add(inetAddress);
                    } catch (UnknownHostException ignored) {
                    }
                }
                return inetAddressList;
            }
        })
        .build();
```

<dx-alert infotype="notice" title="">
实现 DNS 接口，即表示所有经由当前 OkHttpClient 实例处理的网络请求都会经过 HTTPDNS。如果您只有少部分域名是需要通过 HTTPDNS 进行解析，建议您在调用 HTTPDNS 域名解析接口之前先进行过滤。
</dx-alert>


### Retrofit + OkHttp
Retrofit 实际上是一个基于 OkHttp，对接口做了一层封装桥接的 lib。因此只需要仿 OkHttp 的接入方式，定制 Retrofit 中的 OkHttpClient，即可方便地接入 HTTPDNS。示例如下：

```Java
mRetrofit =
    new Retrofit.Builder()
        .client(mOkHttpClient)
        .baseUrl(baseUrl)
        .build();
```
