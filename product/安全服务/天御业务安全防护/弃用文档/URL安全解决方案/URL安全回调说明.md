采用主动回调的方式，用户注册回调域名，腾讯云后台天御服务会把被拦截的URL或域名主动回调给用户。

## 一、接口描述
协议：HTTP
<br> 请求类型：POST
<br> 回调地址：客户提交的回调地址。
<br> 数据加密方式： AES（128位），密钥为用户预留在URL方案的密钥。

## 二、使用方式
1. 客户回调服务器接收到天御的回调请求后，获取request的data字段。
<br> 天御URL安全回调示例：http://www.xx.com/callback?data=xx
其中：http://www.xx.com/callback 为客户预留地址，data为回调加密报文。
2. 对data字段执行以下3步获取报文：
<br>（1）对data字段（16进制）转换为2进制数据。
<br>（2）对（1）获得的2进制数据做AES解密获得解密报文。
<br>（3）对解密报文尾端做去除空格处理。
<br> 示例解密代码：
```
 class prpcrypt():
    def __init__(self,key):
        self.key = key#密钥
        self.mode = AES.MODE_CBC
     
    #解密后，去掉补足的空格用strip()
    def decrypt(self,text):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        plain_text  = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')
```

3. 解密报文说明
<br> 报文示例：
```{"evil_type": 1, "url": "http://www.qq.com/1.html", "site": "qq.com", "source": "BspUrl", "modify_time": "2017-03-24 00:00:00", "evil_lvl": 1}
```
<table class="t">
<tbody><tr><th><b>参数</b></th>
<th><b>数据类型</b></th>
<th><b>描述</b></th></tr>
<tr><td>evil_type</td>
<td>Int</td>
<td>恶意类型，参考附录：恶意类型说明</td></tr>
<tr><td>url</td>
<td>String</td>
<td>被封禁的url</td></tr>
<tr><td>site</td>
<td>String</td>
<td>URL所属域名</td></tr>
<tr><td>source</td>
<td>String</td>
<td>来源：用于标识为天御URL安全回调<br>默认值：BspUrl</td>
<tr><td>modify_time</td>
<td>String</td>
<td>更新时间</td>
<tr><td>evil_lvl</td>
<td>Int</td>
<td>恶意等级，参考附录：封禁级别</td>
</td></tr>
</tbody></table>

### 附录
A. 恶意类型说明

<table class="t">
<tbody><tr><th><b>恶意类型ID</b></th>
<th><b>恶意描述</b></th>
<th><b>详细描述</b></th></tr>
<tr><td>1</td>
<td>社工欺诈</td>
<td>社工欺诈（仿冒、账号钓鱼、中奖诈骗）</td></tr>
<tr><td>2</td>
<td>信息诈骗</td>
<td>信息诈骗（虚假充值、虚假兼职、虚假金融投资、虚假信用卡代办、网络赌博诈骗）</td></tr>
<tr><td>3</td>
<td>虚假销售</td>
<td>虚假销售（男女保健美容减肥产品、电子产品、虚假广告、违法销售）</td></tr>
<tr><td>4</td>
<td>恶意文件</td>
<td>恶意文件（病毒文件，木马文件，恶意apk文件的下载链接以及站点，挂马网站）</td>
<tr><td>5</td>
<td>博彩网站</td>
<td>博彩网站（博彩网站，在线赌博网站）</td>
<tr><td>6</td>
<td>色情网站</td>
<td>色情网站（涉嫌传播色情内容，提供色情服务的网站）</td>
<tr><td>7</td>
<td>风险网站</td>
<td>风险网站（弱类型，传播垃圾信息的网站, 如果客户端有阻断，不建议使用这个数据）</td>
<tr><td>8</td>
<td>非法内容</td>
<td>非法内容（根据法律法规不能传播的内容，主要为政治敏感内容，默认内部使用））</td>
</td></tr>
</tbody></table>

B. 封禁级别说明
<table class="t">
<tbody><tr><th><b>封禁级别</b></th>
<th>封禁级别描述</b></th></tr>
<tr><td>1</td>
<td>链接黑</td></tr>
<tr><td>2</td>
<td>Cgi黑</td></tr>
<tr><td>3</td>
<td>路径黑</td></tr>
<tr><td>4</td>
<td>整站黑</td></tr>
<tr><td>5</td>
<td>整域黑</td></tr>
</td></tr>
</tbody></table>
