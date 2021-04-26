## 1. 服务地址

腾讯云监控服务使用的域名访问地址为：monitor.api.qcloud.com。

## 2. 通信协议
腾讯云API的所有接口均通过HTTPS进行通信，提供高安全性的通信通道。

## 3. 请求方法
同时支持 POST 和 GET 请求，需要注意不能混合使用。即如果使用 GET 方式，则参数均从 Querystring 取得；如果使用 POST 方式，则参数均从 Request Body 中取得，Querystring 中的参数将忽略。两种方式参数格式规则相同，一般使用GET，当参数字符串过长时使用POST，请见各接口详细描述。

## 4. 字符编码
均使用UTF-8编码。


## 5. API请求结构
<table class="t">
<tbody><tr>
<th> <b>名称</b>
</th><th> <b>描述</b>
</th><th> <b>备注</b>
</th></tr>
<tr>
<td> API入口
</td><td> API调用的 WebService 入口
</td><td> https://monitor.api.qcloud.com/v2/index.php<br> 
</td></tr>
<tr>
<td> 公共参数
</td><td> 每个接口都包含的通用参数
</td><td> 详见 <a href="/doc/api/255/公共参数" title="公共参数">公共参数</a> 页面
</td></tr>
<tr>
<td> 指令名称
</td><td> API要执行的指令的名称，这里使用Action指定，<br>
<p>例如Action=DescribeMetrics
</p>
</td><td> 完整的指令请参见 <a href="/doc/api/255/API概览" title="API概览">API概览</a>
</td></tr>
<tr>
<td> 指令参数
</td><td> 每个特定的指令需要的参数
</td><td> 详见每个指令的接口文档
</td></tr></tbody></table>