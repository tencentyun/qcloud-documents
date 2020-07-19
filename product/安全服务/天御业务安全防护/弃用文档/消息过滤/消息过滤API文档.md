## 1.接口描述
识别用户产生的内容中是否含有敏感、色情、欺诈广告等关键词，并进一步根据用户行为判断行为是否有恶意。
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：UgcAntiSpam

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://cloud.tencent.com/document/product/295/7279)页面。
<br> 其中，此接口的Action字段为UgcAntiSpam。
<table class="t">
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>是否必须</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> messageStruct
</td><td> <font color=red> 必选 </font color=red>
</td><td> String
</td><td> 用户产生的内容，参考消息结构体介绍
</td></tr>
<tr>
<td> messageId
</td><td> <font color=red> 必选 </font color=red>
</td><td> String
</td><td> 用户产生内容的ID，消息内容的唯一ID用于标识某条消息。
</td></tr>
<tr>
<td> postIp
</td><td><font color=red> 必选 </font color=red>
</td><td> String
</td><td> 操作来源的外网IP
</td></tr>
<tr>
<td> accountType
</td><td> <font color=red> 必选 </font color=red>
</td><td> UInt
</td><td> 用户账号类型
<br> 0：其他账号
<br> 1：QQ开放帐号
<br> 2：微信开放帐号
<br> 4：手机号
<br> 6：手机动态码
<br> 7：邮箱
</td></tr>
<tr>
<td> uid
</td><td> <font color=red> 必选 </font color=red>
</td><td> String
</td><td> 用户ID
<br> accountType不同对应不同的用户ID。如果是QQ或微信用户则填入对应的openId
</td></tr>
<tr>
<td> appId
</td><td> 可选
</td><td> String
</td><td> accountType是QQ或微信开放账号时，该参数必填，表示QQ或微信分配给给网站或应用的appId，用来唯一标识网站或应用
</td></tr>
<tr>
<td> associateAccount
</td><td> 可选
</td><td> String
</td><td> accountType是QQ或微信开放账号时，用于标识QQ或微信用户登录后关联业务自身的账号ID
</td></tr>
<tr>
<tr>
<td> nickName
</td><td> 可选
</td><td> String
</td><td> 昵称，utf8编码
</td></tr>
<td> phoneNumber
</td><td> 可选
</td><td> String
</td><td> 手机号；国家代码-手机号，如0086-15912345687. 注0086前不需要+号
</td></tr>
<tr>
<td> emailAddress
</td><td> 可选
</td><td> String
</td><td> 用户邮箱地址（非系统自动生成）
</td></tr>
<tr>
<td> registerTime
</td><td> 可选
</td><td> UInt
</td><td> 注册时间戳，单位秒
</td></tr>
<tr>
<td> registerIp
</td><td> 可选
</td><td> String
</td><td> 注册来源的外网IP
</td></tr>
<tr>
<td> toAccountType
</td><td> 可选
</td><td> UInt
</td><td> 接收者的账号类型，同accountType相类
<br> 4：手机号
<br> 0：其他账号
<br> 1：QQ开放帐号
<br> 2：微信开放帐号
<br> 6：手机动态码
<br> 7：邮箱
</td></tr>
<tr>
<td> toUid
</td><td> 可选
</td><td> String
</td><td> 接收者的ID，同uid相类
</td></tr>
<tr>
<td> relationship
</td><td> 可选
</td><td> UInt
</td><td> 发送者和接收者之间的关系
<br> 1：C2C好友
<br> 2：C2C非好友
<br> 3：群组
<br> 4：公开
<br> 5：B2C
<br> 6：C2B
</td></tr>
<tr>
<td> postTime
</td><td> 可选
</td><td> UInt
</td><td> 操作时间戳，单位秒
</td></tr>
<tr>
<td> loginSource
</td><td> 可选
</td><td> UInt
</td><td> 登录来源
<br> 0：其他
<br> 1：PC网页
<br> 2：移动页面
<br> 3：APP
<br> 4：微信公众号
</td></tr>
<tr>
<td> loginType
</td><td> 可选
</td><td> UInt
</td><td> 登录方式
<br> 0：其他
<br> 1：手动帐号密码输入
<br> 2：动态短信密码登录
<br> 3：二维码扫描登录
</td></tr>
<tr>
<td> vendorId
</td><td> 可选
</td><td> String
</td><td> 手机制造商ID，如果手机注册，请带上此信息
</td></tr>
<td> imei
</td><td> 可选
</td><td> String
</td><td> 手机设备号
</td></tr>
<tr>
<td> businessId
</td><td> 可选
</td><td> UInt
</td><td> 业务ID
<br> 网站或应用在多个业务中使用此服务，通过此ID区分统计数据
</td></tr>
</td></tr></tbody></table>

## 3.输出参数
<table class="t">
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<td> code
</td><td> Int
</td><td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/document/product/295/7285
"target="black">公共错误码</a>
</td></tr>
<tr><td> codeDesc
</td><td> String
</td><td> 业务侧错误码。成功时返回Success，错误时返回具体业务错误原因。
</td></tr>
<td> message
</td><td> String
</td><td> 模块错误信息描述，与接口相关
</td></tr>
<tr>
<td> postIp
</td><td> String
</td><td> 操作来源的外网IP
</td></tr>
<tr>
<td> postTime
</td><td> String
</td><td> 作时间戳，单位秒
</td></tr>
<tr>
<td> messageId
</td><td> String
</td><td> 用户产生内容的ID。如果传入此ID，将可以通过恶意结果查询接口获取进一步的信息。
</td></tr>
<tr>
<td> uid
</td><td> String
</td><td> 用户ID
<br> accountType不同对应不同的用户ID。如果是QQ或微信用户则填入对应的openId
</td></tr>
<tr>
<td> associateAccount
</td><td> String
</td><td> accountType是QQ或微信开放账号时，用于标识QQ或微信用户登录后关联业务自身的账号ID
</td></tr>
<tr>
<td> level
</td><td> Int
</td><td> 0：表示无恶意<br>1～4：恶意等级由低到高
<tr>
<td> type
</td><td> Int
</td><td> 系统命中关键词类别
<br> 0 其他
<br> 1 广告
<br> 2 色情
<br> 3 敏感
<br> 4 灌水
<br> 5 跨站追杀
<br> 6 个性
<tr>
<td> selfType
</td><td> Int
</td><td> 用户自定义关键词分类
</td></tr>
<tr>
<td> beatTips
</td><td> String
</td><td> 打击原因，如命中的关键词
</td></tr>
</tbody></table>

## 4. 消息结构介绍
消息结构体用于存储用户输入的文本、图片、视频和系统表情等内容，使用 TLV 格式存储，其中 Type 是 4 个字节，Length 是 4 个字节，Value 的值通过 Length 指定，Type 和 Length 都是网络字节序，其中所有的中文字符均为 UTF8 编码。目前支持的 Type 类型如下：
<table class="t">
<tbody><tr>
<th> <b>值</b>
</th><th> <b>类型</b>
</th><th> <b>说明</b>
</th></tr>
<tr>
<td> 1
</td><td> 文字
</td><td> 字符串内容，使用UTF8编码。
</td></tr>
<tr>
<td> 2
</td><td> 图片超链接
</td><td> 如果无法提供超链接，通过 Length=0表示存在图片。
</td></tr>
<td> 3
</td><td> 视频超链接
</td><td> 如果无法提供超链接，通过 Length=0表示存在图片。
</td></tr>
<td> 4
</td><td> 音频超链接
</td><td> 如果无法提供超链接，通过 Length=0表示存在图片。
</td></tr>
<td> 5
</td><td> 网站超链接
</td><td> 如果无法提供超链接，通过 Length=0表示存在图片。
</td></tr>
<td> 6
</td><td> 系统表情
</td><td> 无需传入系统表情编码，通过 Length=0表示存在系统表情
</td></tr>
<td> 7
</td><td> 文章标题
</td><td> 字符串内容，使用UTF8编码。
</td></tr>
<td> 8
</td><td> 位置
</td><td> 无需传入位置，通过 Length=0表示存在位置。
</td></tr>
<td> 9
</td><td> 第三方定义
</td><td> 无需传入第三方内容，通过 Length=0表示存在第三方内容。
</td></tr>
<td> 10
</td><td> 文件
</td><td> 无需传入文件，通过 Length=0表示存在文件。
</td></tr>
<td> 1000
</td><td> 其他
</td><td> 无需传入其他内容，通过 Length=0表示存在其他内容。
</td></tr>
</td></tr></tbody></table>

## 5. 示例代码
代码下载：  [Python示例](https://mc.qcloudimg.com/static/archive/c7e31b9f2ba2850b7cd66c8a81d1229a/UgcAntiSpam.py.zip) [Java示例](https://mc.qcloudimg.com/static/archive/7f16dcb3ed56e8fd0adc4bfdafbe3edd/UgcAntiSpam.java.zip) [.Net示例](https://mc.qcloudimg.com/static/archive/545fc3dfa7473218c79de8ab9a123c7d/UgcAntiSpam.cs.zip)
<br> 一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。这里只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的说明可见[公共请求参数](https://cloud.tencent.com/document/product/295/7279)小节。
```
请求示例 ：
https://csec.api.qcloud.com/v2/index.php?Action=UgcAntiSpam
&<公共请求参数>
&secretId=AKID*********2iBS8s2DCzazCD2g7OUq4Zw
&accountType=1
&uid=D692D87319F2098C3877C3904B304706
&messageId=dgsfjajdahqywjqn
&postIp=127.0.0.1
&messageStruct=AAAAAQAAAELmtYvor5Xlj5HluJbvvIzmnInkurrmiZPlh7vkuYjvvJ
```
## 6.响应示例
```
{
"Nonce":829504212,
"associateAccount":"373909726",
"beatTips":"",
"code":0,
"codeDesc":"success" ,
"level":0,
"message":"NoError",
"messageId":"ieafdasfk",
"postIp":"14.17.22.32",
"postTime":"1436664316",
"selfType":0,
"type":0,
"uid":"D692D87319F2098C3877C3904B304706"
}
```
