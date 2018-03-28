
#### 使用 HttpClient 请求

HttpClent 实例使用 WnsService.getWnsHttpClient()来获取,然后使用HttpClient.execute(HttpUriRequest httpUriRequest )来发起 http 请求

>注意：
>
>发送和接受数据大小限制为 512KB。
>
>业务侧最好打印出 response.getFirstHeader(WnsService.KEY_HTTP_RESULT)中的数据
以便于 bug 定位

**[注意]此模式下，sdk会自动将url设置为命令字，wns会统计每个命令字的成功率等信息，对应的，需要在控制台配置url域名对应的路由。路由配置请参考：http://cloud.tencent.com/doc/product/276/控制台说明**

如下图所示:
```
//[必须] 定义wns的引用，从而使用其内部方法
private final WnsService wns = WnsClientFactory.getThirdPartyWnsService(); 
//[注意] HTTP的收发包样例. 发送数据&接收数据大小限制为512KB
private void sendHttpReq() {
    Runnable run = new Runnable() {
        @Override
        public void run() {
          // [修改] 请求的url地址，完整地址。
          String url = "http://user.qzone.qq.com/xunren?a=b";    //控制台上需要配置user.qzone.qq.com对应的路由
          //[必须] 用wns的接口替换系统HttpClient
            HttpClient client = wns.getWnsHttpClient();      
            //[两个超时总和的请求，建议60秒         client.getParams().setParameter(CoreConnectionPNames.CONNECTION_TIMEOUT,30*1000);
            client.getParams().setParameter(CoreConnectionPNames.SO_TIMEOUT, 30*1000);
            HttpUriRequest request = new HttpGet(URI.create(url));
            try {
                //[必须] 同样的execute方法，发起http请求。
                HttpResponse response = client.execute(request);
                if (response.getStatusLine().getStatusCode() == HttpURLConnection.HTTP_OK)
                {
                    //[参考] 常见http回包解析方式，业务端可以保持自己代码不变
                    InputStream in = response.getEntity().getContent();
                    ByteArrayOutputStream out = new ByteArrayOutputStream();
                    byte[] buff = new byte[1024];
                    int len = -1;
                    while ((len = in.read(buff)) != -1) {
                        out.write(buff, 0, len);
                    }
                    in.close();

                     Log.d(“wns”,"http code " + response.getStatusLine().toString());
                     Log.d(“wns”,"http data " + out.toString().trim());
                }
                else
                {
                    Header header = response.getFirstHeader(WnsService.KEY_HTTP_RESULT);
                    String wnsCode = "";
                    if (header != null)
                    {
                        wnsCode = header.getValue();
                    }
                    Log.d(“wns”,"http code " + response.getStatusLine().toString() + ", wnscode " + wnsCode);
                }

            } catch (ClientProtocolException e) {
                e.printStackTrace();
                Log.e(TAG,"catch error:"+e.toString());
            } catch (IOException e) {
                e.printStackTrace();
                Log.e(TAG,"catch error:"+e.toString());
            }
        }
    };
    new Thread(run).start();
}
```

#### 使用 HttpUrlConnection 请求
使用 wns.getWnsHttpUrl()获取 URL 实例
>注意：
发送和接受数据大小限制为 512KB。

**[注意]此模式下，sdk 会自动将 url 设置为命令字，wns 会统计每个命令字的成功率等信息，对应的，需要在控制台配置 url 域名对应的路由。路由配置请参考：http://cloud.tencent.com/doc/product/276/控制台说明**
```
 //[必须] 定义 wns 的引用，从而使用其内部方法
private final WnsService wns = WnsClientFactory.getThirdPartyWnsService(); 
//[注意] HTTP的收发包样例. 发送数据&接收数据大小限制为 512KB
private void sendHttpUrlConnReq(final String url)
{
    Runnable run = new Runnable()
    {
        @Override
        public void run()
        {
            try
            {
                 //1.构造 URL，底层网络走 wns 通道,使用起来和 URL 是一样的。
                URL u = wns.getWnsHttpUrl(url);                   //需要在控制台上配置 url 对应域名的路由
                HttpURLConnection conn = (HttpURLConnection) u.openConnection();
                conn.addRequestProperty("User-Agent", "");

                //[两个超时总和的请求，建议60秒  
                conn.setConnectTimeout(30*1000);
                conn.setReadTimeout(30*1000);

                //如果是post方法，需要设置一下post参数,可选
                //conn.setDoOutput(true);
                //conn.getOutputStream().write("a=10&b=99".getBytes());
                //获取页面内容
                int rspcode = conn.getResponseCode();
                Log.d(TAG, "rspcode = " + rspcode);
                if (HttpURLConnection.HTTP_OK == rspcode)
                {
                    InputStream in = conn.getInputStream();
                    if (in == null)
                    {
                          return;
                    }
                    byte[] buff = new byte[1024];
                    ByteArrayOutputStream out = new ByteArrayOutputStream();
                    int len = -1;
                    while ((len = in.read(buff)) != -1)
                    {
                        out.write(buff, 0, len);
                    }
                    in.close();
                    final String content = out.toString().trim();
                    Log.w(TAG, content.substring(0, 100 > content.length() ? content.length() : 100));
                    Log.w(TAG, content.substring(content.length() > 100 ? content.length() - 100 : content.length()));

                } 
            } catch (MalformedURLException e)
            {
                e.printStackTrace();
            } catch (IOException e)
            {
                e.printStackTrace();
            }
        }
    };
    new Thread(run).start();
}```