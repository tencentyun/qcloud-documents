SSML 是一种基于 XML 的语音合成标记语言。使用 SSML 可以更加准确、具体的定义合成音频的效果。
>? 
>- 腾讯云语音合成服务的 SSML 实现，基于 [W3C](https://www.w3.org/TR/speech-synthesis/) 的语音合成标记语言版本1.1。
>- 目前只有中文合成支持 SSML 功能。

## 使用方式
将带标签的文本作为 text 参数值，上传至语音合成服务，发送给语音合成服务的请求内容如下：
```
{
 "Action" : "TextToVoice",
 "AppId" : 12345,
 "Codec" : "mp3",
 "Expired" : 1603271036,
 "ModelType" : 1,
 "PrimaryLanguage" : 1,
 "ProjectId" : 0,
 "SampleRate" : 8000,
 "SecretId" : "AKID****",
 "SessionId" : "1234",
 "Speed" : 0,
 "Text" : "<speak>电话号码是<say-as interpret-as=\"telephone\">4008110510</say-as>。</speak>",
 "Timestamp" : 1603184636,
 "VoiceType" : 1002,
 "Volume" : 5
}
```

语音合成支持的 SSML [标签](#jump)。其中 `<speak>` 标签中的未定义标签不合成，且 XML 格式错误可能会导致`<speak>` 标签的合成停止。

语音合成的 SSML 功能支持多个 `<speak>` 标签闭合嵌套于文本之中。例如：
```
<speak>她叫<say-as interpret-as="name">任盈盈</say-as>。
她的电话号码是<say-as interpret-as="telephone">+86-15188888888</say-as>。
她今年<say-as interpret-as="cardinal">22</say-as>岁了。
她有一个快递，单号是<say-as interpret-as="digits">5648234514237588</say-as>。
她的地址是<say-as interpret-as="address">深南大道10000号3单元304</say-as>。
</speak>再补充一下，<speak>
她的用户名是<say-as interpret-as="characters">b888_uαβγ</say-as>。
</speak>
```

[](id:jump)
## 标签
### &lt;speak&gt;
#### 描述
```
<speak>标签是所有待支持SSML标签的根节点。一切需要调用SSML标签的文本都要包含在“<speak></speak>”中。speak标签不支持属性。
```

#### 语法
```
<speak>需要调用SSML标签的文本</speak>
```

#### 标签关系
`<speak>` 标签可以包含文本和以下标签：`<break>`、`<phoneme>`、`<say-as>`、`<sub>`。

#### 示例
```
<speak>需要调用SSML标签的文本。</speak>
```
音频效果：[SSML-speak1.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/SSML-speak1.wav)

### &lt;sub&gt;
#### 描述
使用别名替换标签内文本。

#### 语法
```
<sub alias="别名">文本</sub>
```

#### 属性
<table>
<thead>
<tr>
<th>属性名称</th>
<th>属性类型</th>
<th>属性值</th>
<th>是否必选</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>alias</td>
<td>String</td>
<td>替换后的内容</td>
<td>是</td>
<td>用于替换标签内的文本。</td>
</tr>
</tbody></table>

#### 标签关系
标签仅包括文本。

#### 示例
```
<speak><sub alias="语音合成">TTS</sub></speak>
```
音频效果：[SSML-sub.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/SSML-sub.wav)

### &lt;break&gt;
#### 描述
用于在文本中插入停顿，该标签是可选标签。

#### 语法
```
<break time="string"/>
```

#### 属性
<table>
<thead>
<tr>
<th>属性名称</th>
<th>属性类型</th>
<th>属性值</th>
<th>是否必选</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>time</td>
<td>String</td>
<td>[number]s/[number]ms</td>
<td>是</td>
<td>以秒/毫秒为单位设置停顿的时长 （如“2s“、“50ms”）。[number]s：以秒为单位，[number]取值范围为[1, 10]的整数。[number]ms：以毫秒为单位，[number]取值范围为[50, 10000]的整数。</td>
</tr>
</tbody></table>

#### 标签关系
`<break>`是空标签，不能包含任何标签。

#### 示例
```
<speak>请闭上眼睛休息一下<break time="500ms"/>好了，请睁开眼睛。</speak>
```

### &lt;phoneme&gt;
#### 描述
用于控制标签内文本的读音，该标签是可选标签。

#### 语法
```
<phoneme alphabet="py" ph="拼音串">文本</phoneme>
```
<table>
<thead>
<tr>
<th>属性名称</th>
<th>属性类型</th>
<th>属性值</th>
<th>是否必选</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>alphabet</td>
<td>String</td>
<td>py</td>
<td>是</td>
<td>“py”表示拼音。</td>
</tr>
<tr>
<td>ph</td>
<td>String</td>
<td>标签内文本对应的拼音串</td>
<td>是</td>
<td>拼音用法的赋值规范：<br>- 字与字的拼音用空格分隔，拼音的数目必须与字数相等。<br>- 每个拼音由发音和音调组成，音调为1~5的数字编号，其中“5”表示轻声。</td>
</tr>
</tbody></table>

#### 标签关系
`<phoneme>`标签仅包括文本。

#### 示例
```
<speak>
现状是各地的经济水平是<phoneme alphabet="py" ph="cen1 ci1 bu4 qi2">参差不齐</phoneme>的。需要缩小较弱地域和较强地域的<phoneme alphabet="py" ph="cha1 ju4">差距</phoneme>。要做好这个<phoneme alphabet="py" ph="chai1 shi4">差事</phoneme>可不容易啊。
</speak>
```
音频效果：[SSML-phoneme.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/SSML-phoneme.wav)

### &lt;say-as&gt;
#### 描述
用于指示出标签内文本的信息类型，进而按照该类型的默认发音方式发音。

#### 语法
```
<say-as interpret-as="string">文本</say-as>
```
<table>
<thead>
<tr>
<th>属性名称</th>
<th>属性类型</th>
<th>属性值</th>
<th>是否必选</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>interpret-as</td>
<td>String</td>
<td>cardinal/digits/telephone/name/address/<br>id/characters/punctuation/<br>date/time/currency/measure</td>
<td>是</td>
<td>指示出标签内文本的信息类型：<br>• cardinal：按整数或小数发音。<br>• digits：按数字发音。<br>• telephone：按电话号码常用方式发音。<br>• name：按人名发音。<br>• address：按地址发音。<br>• id：适用于账户名、昵称等。<br>• characters：将标签内的文本按字符一一读出。<br>• punctuation：将标签内的文本按标点符号的方式读出来。<br>• date：按日期发音。<br>• time：按时间发音。<br>• currency：按金额发音。<br>• measure：按计量单位发音。</td>
</tr>
</tbody></table>

#### 各 &lt;say-as&gt;类型支持范围
- cardinal
 <table>
<tr>
<th>格式</th>
<th>示例</th>
<th>输出</th>
<th>说明</th>
</tr>
<tr>
<td>数字串</td>
<td>1487</td>
<td>一千四百八十七</td>
<td rowspan="8">整数输入范围：[-18446744073709551615,18446744073709551615]。<br>小数输入范围：对小数点后小数的位数没有特殊限制，建议不超过10位。</td>
</tr>
<tr>
<td>负号+数字串</td>
<td>-1487</td>
<td>负一千四百八十七</td>
</tr>
<tr>
<td>以逗号分隔3位数字串</td>
<td>10,500</td>
<td>一万零五百</td>
</tr>
<tr>
<td>负号+以逗号分隔3位数字串</td>
<td>-10,500</td>
<td>负一万零五百</td>
</tr>
<tr>
<td>数字串+小数点+2个零</td>
<td>9.00</td>
<td>九</td>
</tr>
<tr>
<td>负号+数字串+小数点+2个零</td>
<td>-110.00</td>
<td>负一百一十</td>
</tr>
<tr>
<td>数字串+小数点+数字串</td>
<td>88.090</td>
<td>八十八点零九</td>
</tr>
<tr>
<td>负号+数字串+小数点+数字串</td>
<td>-88.001</td>
<td>负八十八点零零一</td>
</tr>
</table>
- digits
 <table>
<tr>
<th>格式</th>
<th>示例</th>
<th>输出</th>
<th>说明</th>
</tr>
<tr>
<td>数字串</td>
<td>356210985</td>
<td>三五六二一零九八五</td>
<td>对数字串的长度没有特殊限制。<br>建议不超过20位，且当数字串超过10位时，每个数字后插入停顿。</td>
</tr>
</table>
- telephone
 <table>
<tr>
<th>格式</th>
<th>示例</th>
<th>输出</th>
<th>说明</th>
</tr>
<tr>
<td rowspan="6">座机号</td>
<td>5605560</td>
<td>五六零 五五六零</td>
<td rowspan="6">支持7~8位座机号，支持空格和’-‘作为分隔符。<br>其中：7位座机号支持“3-4”的数字分隔方式。8位座机号支持“4-4”的数字分隔方式。</td>
</tr>
<tr>
<td>560 5560</td>
<td>五六零 五五六零</td>
</tr>
<tr>
<td>560-5560</td>
<td>五六零 五五六零</td>
</tr>
<tr>
<td>55605560</td>
<td>五五六零 五五六零</td>
</tr>
<tr>
<td>5560 5560</td>
<td>五五六零 五五六零</td>
</tr>
<tr>
<td>5560-5560</td>
<td>五五六零 五五六零</td>
</tr>
<tr>
<td rowspan="4">座机号+分机号</td>
<td>55605560-105</td>
<td>五五六零 五五六零 转幺零五</td>
<td rowspan="4">支持1~4位分机号。</td>
</tr>
<tr>
<td>55605560转105</td>
<td>五五六零 五五六零 转幺零五</td>
</tr>
<tr>
<td>55605560分机105</td>
<td>五五六零 五五六零 转幺零五</td>
</tr>
<tr>
<td>55605560分机号105</td>
<td>五五六零 五五六零 分机号幺零五</td>
</tr>
<tr>
<td rowspan="6">区号+座机号</td>
<td>01055605560</td>
<td>零幺零 五五六零 五五六零</td>
<td rowspan="6">支持区号：010、02x、03xx、04xx、05xx、07xx、08xx、09xx。</td>
</tr>
<tr>
<td>010 55605560</td>
<td>零幺零 五五六零 五五六零</td>
</tr>
<tr>
<td>010-5560-5560</td>
<td>零幺零 五五六零 五五六零</td>
</tr>
<tr>
<td>(010)55605560</td>
<td>零幺零 五五六零 五五六零</td>
</tr>
<tr>
<td>031955605560</td>
<td>零三幺九 五五六零 五五六零</td>
</tr>
<tr>
<td>0319-55605560</td>
<td>零三幺九 五五六零 五五六零</td>
</tr>
<tr>
<td rowspan="6">区号+座机号+分机号</td>
<td>010 33878528-1054</td>
<td>零幺零 三三八七 八五二八 转幺零五四</td>
<td rowspan="6">无</td>
</tr>
<tr>
<td>010-33878528-1054</td>
<td>零幺零 三三八七 八五二八 转幺零五四</td>
</tr>
<tr>
<td>(010)33878528-1054</td>
<td>零幺零 三三八七 八五二八 转幺零五四</td>
</tr>
<tr>
<td>(010)33878528转1054</td>
<td>零幺零 三三八七 八五二八 转幺零五四</td>
</tr>
<tr>
<td>(010)33878528分机1054</td>
<td>零幺零 三三八七 八五二八 分机幺零五四</td>
</tr>
<tr>
<td>(010)33878528分机号1054</td>
<td>零幺零 三三八七 八五二八 分机号幺零五四</td>
</tr>
<tr>
<td rowspan="5">国家代码+区号+座机号</td>
<td>86-010-33878528</td>
<td>八六 零幺零 三三八七</td>
<td rowspan="5">支持国家代码：86、(86)、+86、(+86)、0086。并统一读为“八六”。</td>
</tr>
<tr>
<td>(86)10-33878528</td>
<td>八六 幺零 三三八七 八五二八</td>
</tr>
<tr>
<td>+86-010-33878528</td>
<td>八六 零幺零 三三八七 八五二八</td>
</tr>
<tr>
<td>0086-10-33878528</td>
<td>八六 幺零 三三八七 八五二八</td>
</tr>
<tr>
<td>(+86)-10-3387 8528</td>
<td>八六 幺零 三三八七 八五二八</td>
</tr>
<tr>
<td rowspan="5">国家代码+区号+座机号+分机号</td>
<td>(86)21-33878528-1054</td>
<td>八六 二幺 三三八七 八五二八 转幺零五四</td>
<td rowspan="5">无</td>
</tr>
<tr>
<td>(86)021-3387-8528-1054</td>
<td>八六 零二幺 三三八七 八五二八 转幺零五四</td>
</tr>
<tr>
<td>(86)021-33878528转1054</td>
<td>八六 零二幺 三三八七 八五二八 转幺零五四</td>
</tr>
<tr>
<td>(86)21-3387-8528分机号1054</td>
<td>八六 二幺 三三八七 八五二八 分机号幺零五四</td>
</tr>
<tr>
<td>+86-021-3387-8528分机1054</td>
<td>八六 零二幺 三三八七 八五二八 分机幺零五四</td>
</tr>
<tr>
<td rowspan="3">手机号</td>
<td>151 8828 1075</td>
<td>幺五幺八八二八 幺零七五</td>
<td rowspan="3">支持11位手机号，支持3-3-5、3-4-4两种数字分隔方式</td>
</tr>
<tr>
<td>151-882-81075</td>
<td>幺五幺 八八二 八幺零七五</td>
</tr>
<tr>
<td>151-8828-1075</td>
<td>幺五幺八八二八 幺零七五</td>
</tr>
<tr>
<td rowspan="4">国家代码+手机号</td>
<td>+86-15188281075</td>
<td>八六 幺五幺 八八二八 幺零七五</td>
<td rowspan="4">无</td>
</tr>
<tr>
<td>(+86)-151-8828-1075</td>
<td>八六 幺五幺 八八二八 幺零七五</td>
</tr>
<tr>
<td>+8615188281075</td>
<td>八六 幺五幺 八八二八 幺零七五</td>
</tr>
<tr>
<td>0086-151 882 81075</td>
<td>八六 幺五幺 八八二 八幺零七五</td>
</tr>
<tr>
<td rowspan="5">服务号</td>
<td>110</td>
<td>幺幺零</td>
<td rowspan="5"><ul><li/>支持常用的服务号如110。<li/>支持以400/800开头的10位服务号，支持以“3-3-4”的数字分隔方式。<br><li/>支持以12530/17951/12593开头的16位号码。</ul></td>
</tr>
<tr>
<td>95566</td>
<td>九五五六六</td>
</tr>
<tr>
<td>4008110280</td>
<td>四零零 八幺幺 零二八零</td>
</tr>
<tr>
<td>800-810-8888</td>
<td>八零零 八幺零 八八八八</td>
</tr>
<tr>
<td>1253013520638377</td>
<td>幺二五三零 幺三五 二零六三 八三七七</td>
</tr>
<tr>
<td>其他</td>
<td>(86)(21)8832-80976-0907</td>
<td>八六 二幺 八八三二 八零九七六 零九零七</td>
<td>支持“数字串+分隔符（左右括号、-）”方式。</td>
</tr>
</table>
- address
 <table>
<tr>
<th>格式</th>
<th>示例</th>
<th>输出</th>
<th>说明</th>
</tr>
<tr>
<td rowspan="5">常用地址格式</td>
<td>深南大道1000号103-3</td>
<td>深南大道 幺零零零号幺零三杠三</td>
<td rowspan="5">支持常用地址格式。此处地址指标准的邮寄地址。</td>
</tr>
<tr>
<td>高新中四道377弄1137-1128号</td>
<td>高新中四道三七七弄幺幺三七杠幺幺二八号</td>
</tr>
<tr>
<td>华润城六期3-1-3805</td>
<td>华润城六期三杠一杠三八零五</td>
</tr>
<tr>
<td>大族云峰大厦2幢2106室</td>
<td>大族云峰大厦二幢二幺零六室</td>
</tr>
<tr>
<td>高新中三道151弄19号</td>
<td>高新中三道幺五幺弄十九号</td>
</tr>
</table>
- id
 <table>
<tr>
<th>格式</th>
<th>示例</th>
<th>输出</th>
<th>说明</th>
</tr>
<tr>
<td rowspan="3">字符串</td>
<td>dell3301</td>
<td>D E L L 三 三 零 一</td>
<td rowspan="3">大小写英文字符、阿拉伯数字0~9、下划线。<br>输出的空格表示每个字符之间插入停顿，即字符一个一个地读。</td>
</tr>
<tr>
<td>tencent_1998</td>
<td>T E N C E N T 下划线 一 九 九 八</td>
</tr>
<tr>
<td>AiDemo</td>
<td>A I D E M O</td>
</tr>
</table>
- characters
 <table>
<tr>
<th>格式</th>
<th>示例</th>
<th>输出</th>
<th>说明</th>
</tr>
<tr>
<td rowspan="8">字符串</td>
<td>ISO 1-001-095498-1</td>
<td>I S O 一 杠 零 零 一 杠 零 五 四 零 九 八 杠 一</td>
<td rowspan="8">支持中文汉字、大小写英文字符、阿拉伯数字0~9以及部分全角和半角字符。<br>输出的空格表示每个字符之间插入停顿，即字符一个一个地读。标签内的文本如果包含XML的特殊字符，需要做字符转义。常用的共有5个：<br>&amp;lt;<br>&amp;gt;<br>&amp;amp;<br>&amp;quot;<br>&amp;apos;<br>分别对应<、>、& 、"、'。
</td>
</tr>
<tr>
<td>x10u2385_u</td>
<td>x 一 零 u 二 三 八 五 下划线 u</td>
</tr>
<tr>
<td>v1.1.1</td>
<td>v 一 点 一 点 一</td>
</tr>
<tr>
<td>版本号2.0</td>
<td>版本号二 点 零</td>
</tr>
<tr>
<td>粤B BA000</td>
<td>粤B B A 零 零 零</td>
</tr>
<tr>
<td>空中客车A330</td>
<td>空中客车A 三 三 零</td>
</tr>
<tr>
<td>型号B01 B02和B03</td>
<td>型号B 零 一 B 零二 和B 零 三</td>
</tr>
<tr>
<td>αβγ</td>
<td>阿尔法 贝塔 伽玛</td>
</tr>
</table>
- punctuation
 <table>
<tr>
<th>格式</th>
<th>示例</th>
<th>输出</th>
<th>说明</th>
</tr>
<tr>
<td rowspan="7">标点符号</td>
<td>…</td>
<td>省略号</td>
<td rowspan="7">支持常见中英文标点。输出的空格表示每个字符之间插入停顿，即字符一个一个地读。<br>标签内的文本如果包含XML的特殊字符，需要做字符转义。常用的共有5个：<br>&amp;lt;<br>&amp;gt;<br>&amp;amp;<br>&amp;quot;<br>&amp;apos;<br>分别对应<、>、& 、"、'。
</td>
</tr>
<tr>
<td>……</td>
<td>省略号</td>
</tr>
<tr>
<td>!"#$%&</td>
<td>叹号 双引号 井号 dollar 百分号 and</td>
</tr>
<tr>
<td>‘()*+</td>
<td>单引号 左括号 右括号 星号 加号</td>
</tr>
<tr>
<td>,-./:;</td>
<td>逗号 杠 点 斜杠 冒号 分号</td>
</tr>
<tr>
<td><=>?@</td>
<td>小于 等号 大于 问号 at</td>
</tr>
<tr>
<td>[\]^_</td>
<td>左方括号 反斜线 右方括号 脱字符 下划线</td>
</tr>
</table>
- date
 <table>
<tr>
<th>格式</th>
<th>示例</th>
<th>输出</th>
<th>说明</th>
</tr>
<tr>
<td rowspan="6">xx年</td>
<td>71年</td>
<td>七一年</td>
<td rowspan="6">支持2位和4位年份。其中：<ul><li>2位年份支持60年~99年、00年~09年、10年~19年。
<li>4位年份支持1000年~1999年、2000年~2099年。</ul>
</td>
</tr>
<tr>
<td>08年</td>
<td>零八年</td>
</tr>
<tr>
<td>20年</td>
<td>二零年</td>
</tr>
<tr>
<td>2020年</td>
<td>二零二零年</td>
</tr>
<tr>
<td>1998年</td>
<td>一九九八年</td>
</tr>
<tr>
<td>2008年</td>
<td>二零零八年</td>
</tr>
<tr>
<td rowspan="4">xx年xx月</td>
<td>08年5月</td>
<td>零八年五月</td>
<td rowspan="4">当月份为1到9月时，支持开头带”0”和不带”0”两种写法。例如”1908年4月”和”1908年04月”。</td>
</tr>
<tr>
<td>2020年04月</td>
<td>二零二零年四月</td>
</tr>
<tr>
<td>08年8月</td>
<td>零八年八月</td>
</tr>
<tr>
<td>2020年8月</td>
<td>二零二零年八月</td>
</tr>
<tr>
<td rowspan="4">xx年xx月xx日<br>xx年xx月xx号</td>
<td>98年4月23日</td>
<td>九八年四月二十三日</td>
<td rowspan="4">当日期为1到9日时，支持开头带”0”和不带”0”两种写法。例如”1908年4月8日”和”1908年04月08日”。</td>
</tr>
<tr>
<td>2020年08月23日</td>
<td>二零二零年八月二十三日</td>
</tr>
<tr>
<td>20年8月8号</td>
<td>二零年八月八号</td>
</tr>
<tr>
<td>2020年08月08号</td>
<td>二零二零年八月八号</td>
</tr>
<tr>
<td rowspan="2">xx月xx号</td>
<td>8月20日</td>
<td>八月二十日</td>
<td rowspan="2">无</td>
</tr>
<tr>
<td>08月08号</td>
<td>八月八号</td>
</tr>
<tr>
<td rowspan="3">年月缩写</td>
<td>2020/08</td>
<td>二零二零年八月</td>
<td rowspan="6">支持”/“、”-“、”.”作为缩写的分隔符。</td>
</tr>
<tr>
<td>2020-08</td>
<td>二零二零年八月</td>
</tr>
<tr>
<td>2020.08</td>
<td>二零二零年八月</td>
</tr>
<tr>
<td rowspan="3">年月日缩写</td>
<td>2020/08/09</td>
<td>二零二零年八月九日</td>
</tr>
<tr>
<td>2020-8-9</td>
<td>二零一八年八月八日</td>
</tr>
<tr>
<td>2020.08.09</td>
<td>二零一八年八月九日</td>
</tr>
<tr>
<td rowspan="2">xx年xx月xx日~xx年xx月xx日<br>xx年xx月xx号~xx年xx月xx号</td>
<td>20年8月9日~30日</td>
<td>二零年八月九日至三十日</td>
<td rowspan="8">支持”~”、”-“作为”至”的缩写标志。</td>
</tr>
<tr>
<td>2020年08月09号-2020年09月09号</td>
<td>二零二零年八月九月一号至二零二零年九月九</td>
</tr>
<tr>
<td rowspan="2">xx年xx月~xx年xx月</td>
<td>20年04月~21年04月</td>
<td>二零年四月至二一年四月</td>
</tr>
<tr>
<td>2020年04月~2021年04月</td>
<td>二零二零年四月至二零二一年四月</td>
</tr>
<tr>
<td rowspan="2">xx月xx日~xx月xx日<br>xx月xx号~xx月xx号</td>
<td>10月1日~10月7日</td>
<td>十月一日至十月七日</td>
</tr>
<tr>
<td>10月01号~10月07号</td>
<td>十月一号至十月七号</td>
</tr>
<tr>
<td rowspan="2">xx月xx日~xx日<br>xx月xx号~xx号</td>
<td>10月1日~7日</td>
<td>十月一日至七日</td>
</tr>
<tr>
<td>10月01号~07号</td>
<td>十月一号至七号</td>
</tr>
<tr>
<td rowspan="2">年月日缩写~年月日缩写</td>
<td>2020/03/03~2021/03/03</td>
<td>二零二零年三月三日至二零二一年三月三日</td>
<td rowspan="5">支持”/“、”.”作为缩写的分隔符，支持”~””-“作为”至”的缩写标志。</td>
</tr>
<tr>
<td>2020.9.9~2021.9.9</td>
<td>二零二零年九月九日至二零二一年九月九日</td>
</tr>
<tr>
<td>月日缩写~月日缩写</td>
<td>10/20~10/31</td>
<td>十月二十日至十月三十一日</td>
</tr>
<tr>
<td rowspan="2">xx~xx月xx月~xx月</td>
<td>1~10月</td>
<td>一至十月</td>
</tr>
<tr>
<td>1月~10月</td>
<td>一月至十月</td>
</tr>
<tr>
<td>月日年缩写</td>
<td>10/25/2020</td>
<td>二零二零年十月二十五日</td>
<td>仅支持4位的年份，仅支持“/”作为日期的分隔符，仅支持”月/日/年”的书写方式。</td>
</tr>
</table>
- time
 <table>
<tr>
<th>格式</th>
<th>示例</th>
<th>输出</th>
<th>说明</th>
</tr>
<tr>
<td rowspan="5">时刻</td>
<td>12:00</td>
<td>十二点</td>
<td rowspan="14">支持常用时间和时间范围格式。</td>
</tr>
<tr>
<td>12:00:00点</td>
<td>十二点</td>
</tr>
<tr>
<td>10:25分</td>
<td>十点二十五分</td>
</tr>
<tr>
<td>10:25:30</td>
<td>十点二十五分三十秒</td>
</tr>
<tr>
<td>09:25:14</td>
<td>九点二十五分十四秒</td>
</tr>
<tr>
<td rowspan="9">时刻~时刻</td>
<td>11:00~12:00</td>
<td>十一点到十二点</td>
</tr>
<tr>
<td>09:00-14:00</td>
<td>九点到十四点</td>
</tr>
<tr>
<td>11:00~11:30</td>
<td>十一点到十一点三十分</td>
</tr>
<tr>
<td>11:00-15:18</td>
<td>十一点到十五点十八分</td>
</tr>
<tr>
<td>10:30~11:00</td>
<td>十点三十分到十一点</td>
</tr>
<tr>
<td>09:28-10:00</td>
<td>九点二十八分到十点</td>
</tr>
<tr>
<td>10:20~11:20</td>
<td>十点二十分到十一点二十分</td>
</tr>
<tr>
<td>06:00~08:00</td>
<td>六点到八点</td>
</tr>
<tr>
<td>上午10:20~下午13:30</td>
<td>上午十点二十分到下午十三点三十分</td>
</tr>
<tr>
<td rowspan="18">时间缩写</td>
<td>5:00am</td>
<td>凌晨五点</td>
<td rowspan="18">当缩写为 am 时，小时在[0,5]范围内读作凌晨；<br>当单位为 am 时，小时在[6,11]范围内读作上午。<br>当缩写为 pm 时，小时为12时读作中午；<br>当单位为 pm 时，小时在[1,5]范围内读作下午；小时在[6,11]范围内读作晚上。</td>
</tr>
<tr>
<td>5:30am</td>
<td>凌晨五点三十分</td>
</tr>
<tr>
<td>5:20:12am</td>
<td>凌晨五点二十分十二秒</td>
</tr>
<tr>
<td>7:00am</td>
<td>上午七点</td>
</tr>
<tr>
<td>7:30AM</td>
<td>上午七点半</td>
</tr>
<tr>
<td>7:20:25a.m.</td>
<td>上午七点二十分二十五秒</td>
</tr>
<tr>
<td>07:08:12A.M.</td>
<td>上午七点零八分十二秒</td>
</tr>
<tr>
<td>5:00pm</td>
<td>下午五点</td>
</tr>
<tr>
<td>5:30PM</td>
<td>下午五点三十分</td>
</tr>
<tr>
<td>5:20:12p.m.</td>
<td>下午五点二十分十二秒</td>
</tr>
<tr>
<td>05:09:12P.M</td>
<td>下午五点零九分十二秒</td>
</tr>
<tr>
<td>9:00pm</td>
<td>晚上九点</td>
</tr>
<tr>
<td>9:30pm</td>
<td>晚上九点三十分</td>
</tr>
<tr>
<td>9:20:12PM</td>
<td>晚上九点二十分十二秒</td>
</tr>
<tr>
<td>9:02:12P.M.</td>
<td>晚上九点零二分十二秒</td>
</tr>
<tr>
<td>12:00pm</td>
<td>中午十二点</td>
</tr>
<tr>
<td>12:30p.m.</td>
<td>中午十二点三十分</td>
</tr>
<tr>
<td>12:20:12PM</td>
<td>中午十二点二十分十二秒</td>
</tr>
</table>
- currency
 <table>
<tr>
<th>格式</th>
<th>示例</th>
<th width="150px">输出</th>
<th>说明</th>
</tr>
<tr>
<td rowspan="5">数字+金额标识符</td>
<td>12.00RMB</td>
<td>十二人民币</td>
<td rowspan="5">支持 AUD（澳元） 、CAD（加元）、 HKD（港币）、JPY（日元）、USD（美元）、CHF（瑞士法郎）、NOK（挪威克朗）、SEK（瑞典克朗）、GBP（英镑）、 RMB（人民币）、CNY（元）和 EUR（欧元）。<br>支持的数字格式包括：整数、小数以及以逗号分隔的国际写法。</td>
</tr>
<tr>
<td>12.50RMB</td>
<td>十二点五人民币</td>
</tr>
<tr>
<td>15,000,000RMB</td>
<td>一千五百万人民币</td>
</tr>
<tr>
<td>15,000,000.00RMB</td>
<td>一千五百万人民币</td>
</tr>
<tr>
<td>12,000.35RMB</td>
<td>一万两千点三五人民币</td>
</tr>
<tr>
<td rowspan="6">金额标识符+数字</td>
<td>$12</td>
<td>十二美元</td>
<td rowspan="6">支持 CAD（加元）、$（美元）、$（美元）、Fr（法郎）、kr（丹麦克朗）、£（英镑）、¥（元）￥（元）和 €（欧元）。<br>支持的数字格式包括：整数、小数以及以逗号分隔的国际写法。</td>
</tr>
<tr>
<td>$12.00</td>
<td>十二美元</td>
</tr>
<tr>
<td>$12.12</td>
<td>十二点一二美元</td>
</tr>
<tr>
<td>$12,000</td>
<td>一万两千美元</td>
</tr>
<tr>
<td>$12,000.00</td>
<td>一万两千美元</td>
</tr>
<tr>
<td>$12,000.99</td>
<td>一万两千点九九美元</td>
</tr>
<tr>
<td rowspan="8">其他默认读法</td>
<td>1213</td>
<td>一千二百一十三</td>
<td rowspan="8">无</td>
</tr>
<tr>
<td>1213KML</td>
<td>一千二百一十三K M L</td>
</tr>
<tr>
<td>1213.00KML</td>
<td>一千二百一十三K M L</td>
</tr>
<tr>
<td>1213.9KML</td>
<td>一千二百一十三点九K M L</td>
</tr>
<tr>
<td>1,000KML</td>
<td>一千K M L</td>
</tr>
<tr>
<td>1,000.00KML</td>
<td>一千K M L</td>
</tr>
<tr>
<td>1,000.98KML</td>
<td>一千点九八K M L</td>
</tr>
<tr>
<td>12,000</td>
<td>一万两千</td>
</tr>
</table>
- measure
 <table>
<tr>
<th>格式</th>
<th>示例</th>
<th>输出</th>
<th>说明</th>
</tr>
<tr>
<td rowspan="7">数字+中文单位</td>
<td>2片</td>
<td>两片</td>
<td rowspan="21">支持常见中文单位及单位缩写</td>
</tr>
<tr>
<td>120公顷</td>
<td>一百二十公顷</td>
</tr>
<tr>
<td>100多毫克</td>
<td>一百多毫克</td>
</tr>
<tr>
<td>100来米</td>
<td>一百来米</td>
</tr>
<tr>
<td>100余人</td>
<td>一百余人</td>
</tr>
<tr>
<td>1厘米20毫米</td>
<td>一厘米二十毫米</td>
</tr>
<tr>
<td>120.00平方公里</td>
<td>一百二十平方公里</td>
</tr>
<tr>
<td rowspan="3">数字+单位缩写</td>
<td>120.56cm²</td>
<td>一百二十点五六平方厘米</td>
</tr>
<tr>
<td>120㎡56cm²</td>
<td>一百二十平方米五十六平方厘米</td>
</tr>
<tr>
<td>100m12cm6mm</td>
<td>一百米十二厘米六毫米</td>
</tr>
<tr>
<td rowspan="4">范围</td>
<td>10~15kg</td>
<td>十至十五千克</td>
</tr>
<tr>
<td>10.24~789.82亩</td>
<td>十点二四至七百八十九点八二亩</td>
</tr>
<tr>
<td>10米~15米</td>
<td>十米至十五米</td>
</tr>
<tr>
<td>10.24cm~19.08cm</td>
<td>十点二四厘米至十九点零八厘米</td>
</tr>
<tr>
<td rowspan="3">数字+单位+"/"+单位</td>
<td>10元/斤</td>
<td>十元每斤</td>
</tr>
<tr>
<td>199~299元/件</td>
<td>一百九十九至二百九十九元每件</td>
</tr>
<tr>
<td>299.99元/g~399.99元/g</td>
<td>二百九十九点九九元每克至三百九十九点九九元每克</td>
</tr>
<tr>
<td rowspan="4">其他默认读法</td>
<td>12扎</td>
<td>十二扎</td>
</tr>
<tr>
<td>30rm</td>
<td>三十r m</td>
</tr>
<tr>
<td>4万万同胞</td>
<td>四万万同胞</td>
</tr>
<tr>
<td>12.897微克</td>
<td>十二点八九七微克</td>
</tr>
</table>

#### &lt;say-as&gt; 常见符号读法
<table>
<thead>
<tr>
<th>符号</th>
<th>读法</th>
</tr>
</thead>
<tbody><tr>
<td>!</td>
<td>叹号</td>
</tr>
<tr>
<td>“</td>
<td>双引号</td>
</tr>
<tr>
<td>#</td>
<td>井号</td>
</tr>
<tr>
<td>$</td>
<td>dollar</td>
</tr>
<tr>
<td>%</td>
<td>百分号</td>
</tr>
<tr>
<td>&amp;</td>
<td>and</td>
</tr>
<tr>
<td>‘</td>
<td>单引号</td>
</tr>
<tr>
<td>(</td>
<td>左括号</td>
</tr>
<tr>
<td>)</td>
<td>右括号</td>
</tr>
<tr>
<td>*</td>
<td>星</td>
</tr>
<tr>
<td>+</td>
<td>加</td>
</tr>
<tr>
<td>,</td>
<td>逗号</td>
</tr>
<tr>
<td>-</td>
<td>杠</td>
</tr>
<tr>
<td>.</td>
<td>点</td>
</tr>
<tr>
<td>/</td>
<td>斜杠</td>
</tr>
<tr>
<td>:</td>
<td>零冒号</td>
</tr>
<tr>
<td>;</td>
<td>分号</td>
</tr>
<tr>
<td>&lt;</td>
<td>小于</td>
</tr>
<tr>
<td>=</td>
<td>等号</td>
</tr>
<tr>
<td>&gt;</td>
<td>大于</td>
</tr>
<tr>
<td>?</td>
<td>问号</td>
</tr>
<tr>
<td>@</td>
<td>at</td>
</tr>
<tr>
<td>[</td>
<td>左方括号</td>
</tr>
<tr>
<td>\</td>
<td>反斜线</td>
</tr>
<tr>
<td>]</td>
<td>右方括号</td>
</tr>
<tr>
<td>^</td>
<td>脱字符</td>
</tr>
<tr>
<td>_</td>
<td>下划线</td>
</tr>
<tr>
<td>`</td>
<td>反引号</td>
</tr>
<tr>
<td>{</td>
<td>左花括号</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>}</td>
<td>右花括号</td>
</tr>
<tr>
<td>~</td>
<td>波浪线</td>
</tr>
<tr>
<td>！</td>
<td>叹号</td>
</tr>
<tr>
<td>“</td>
<td>左双引号</td>
</tr>
<tr>
<td>”</td>
<td>右双引号</td>
</tr>
<tr>
<td>‘</td>
<td>左单引号</td>
</tr>
<tr>
<td>’</td>
<td>右单引号</td>
</tr>
<tr>
<td>（</td>
<td>左括号</td>
</tr>
<tr>
<td>）</td>
<td>右括号</td>
</tr>
<tr>
<td>，</td>
<td>逗号</td>
</tr>
<tr>
<td>。</td>
<td>句号</td>
</tr>
<tr>
<td>—</td>
<td>杠</td>
</tr>
<tr>
<td>：</td>
<td>冒号</td>
</tr>
<tr>
<td>；</td>
<td>分号</td>
</tr>
<tr>
<td>？</td>
<td>问号</td>
</tr>
<tr>
<td>、</td>
<td>顿号</td>
</tr>
<tr>
<td>…</td>
<td>省略号</td>
</tr>
<tr>
<td>……</td>
<td>省略号</td>
</tr>
<tr>
<td>《</td>
<td>左书名号</td>
</tr>
<tr>
<td>》</td>
<td>右书名号</td>
</tr>
<tr>
<td>￥</td>
<td>人民币符号</td>
</tr>
<tr>
<td>≥</td>
<td>大于等于</td>
</tr>
<tr>
<td>≤</td>
<td>小于等于</td>
</tr>
<tr>
<td>≠</td>
<td>不等于</td>
</tr>
<tr>
<td>≈</td>
<td>约等于</td>
</tr>
<tr>
<td>±</td>
<td>加减</td>
</tr>
<tr>
<td>×</td>
<td>乘</td>
</tr>
<tr>
<td>π</td>
<td>派</td>
</tr>
<tr>
<td>Α</td>
<td>阿尔法</td>
</tr>
<tr>
<td>Β</td>
<td>贝塔</td>
</tr>
<tr>
<td>Γ</td>
<td>伽玛</td>
</tr>
<tr>
<td>Δ</td>
<td>德尔塔</td>
</tr>
<tr>
<td>Ε</td>
<td>艾普西龙</td>
</tr>
<tr>
<td>Ζ</td>
<td>捷塔</td>
</tr>
<tr>
<td>Ε</td>
<td>依塔</td>
</tr>
<tr>
<td>Θ</td>
<td>西塔</td>
</tr>
<tr>
<td>Ι</td>
<td>艾欧塔</td>
</tr>
<tr>
<td>Κ</td>
<td>喀帕</td>
</tr>
<tr>
<td>∧</td>
<td>拉姆达</td>
</tr>
<tr>
<td>Μ</td>
<td>缪</td>
</tr>
<tr>
<td>Ν</td>
<td>拗</td>
</tr>
<tr>
<td>Ξ</td>
<td>克西</td>
</tr>
<tr>
<td>Ο</td>
<td>欧麦克轮</td>
</tr>
<tr>
<td>∏</td>
<td>派</td>
</tr>
<tr>
<td>Ρ</td>
<td>柔</td>
</tr>
<tr>
<td>∑</td>
<td>西格玛</td>
</tr>
<tr>
<td>Τ</td>
<td>套</td>
</tr>
<tr>
<td>Υ</td>
<td>宇普西龙</td>
</tr>
<tr>
<td>Φ</td>
<td>fai</td>
</tr>
<tr>
<td>Χ</td>
<td>器</td>
</tr>
<tr>
<td>Ψ</td>
<td>普赛</td>
</tr>
<tr>
<td>Ω</td>
<td>欧米伽</td>
</tr>
<tr>
<td>α</td>
<td>阿尔法</td>
</tr>
<tr>
<td>β</td>
<td>贝塔</td>
</tr>
<tr>
<td>γ</td>
<td>伽玛</td>
</tr>
<tr>
<td>δ</td>
<td>德尔塔</td>
</tr>
<tr>
<td>ε</td>
<td>艾普西龙</td>
</tr>
<tr>
<td>ζ</td>
<td>捷塔</td>
</tr>
<tr>
<td>η</td>
<td>依塔</td>
</tr>
<tr>
<td>θ</td>
<td>西塔</td>
</tr>
<tr>
<td>ι</td>
<td>艾欧塔</td>
</tr>
<tr>
<td>κ</td>
<td>喀帕</td>
</tr>
<tr>
<td>λ</td>
<td>拉姆达</td>
</tr>
<tr>
<td>μ</td>
<td>缪</td>
</tr>
<tr>
<td>ν</td>
<td>拗</td>
</tr>
<tr>
<td>ξ</td>
<td>克西</td>
</tr>
<tr>
<td>ο</td>
<td>欧麦克轮</td>
</tr>
<tr>
<td>π</td>
<td>派</td>
</tr>
<tr>
<td>ρ</td>
<td>柔</td>
</tr>
<tr>
<td>σ</td>
<td>西格玛</td>
</tr>
<tr>
<td>τ</td>
<td>套</td>
</tr>
<tr>
<td>υ</td>
<td>宇普西龙</td>
</tr>
<tr>
<td>φ</td>
<td>fai</td>
</tr>
<tr>
<td>χ</td>
<td>器</td>
</tr>
<tr>
<td>ψ</td>
<td>普赛</td>
</tr>
<tr>
<td>ω</td>
<td>欧米伽</td>
</tr>
</tbody></table>

#### &lt;say-as&gt; 常见计量单位
<table>
<tr>
<th>格式</th>
<th>类别</th>
<th>示例</th>
</tr>
<tr>
<td rowspan="9">缩写</td>
<td>长度</td>
<td>nm（纳米）、μm（微米）、mm（毫米）、cm（厘米）、m（米）、km（千米）、ft（英尺）、in（英寸）</td>
</tr>
<tr>
<td>面积</td>
<td>cm²（平方厘米）、㎡（平方米）、km²（平方千米）、SqFt（平方英尺）</td>
</tr>
<tr>
<td>体积</td>
<td>cm³（立方厘米）、m³（立方米）、km³（立方千米）、mL（毫升）、L（升）、gallon（加仑）</td>
</tr>
<tr>
<td>重量</td>
<td>μg（微克）、mg（毫克）、g（克）、kg（千克）</td>
</tr>
<tr>
<td>时间</td>
<td>min（分）、sec（秒）、ms（毫秒）</td>
</tr>
<tr>
<td>电磁</td>
<td>μA（微安）、mA（毫安）、Ω（欧姆）、Hz（赫兹）、KHz（千赫兹）、MHz（兆赫兹）、GHz（吉赫兹）、V（伏）、kV（千伏）、kWh（千瓦时）</td>
</tr>
<tr>
<td>声音</td>
<td>dB（分贝）</td>
</tr>
<tr>
<td>气压</td>
<td>Pa（帕）、kPa（千帕）、Mpa（兆帕）</td>
</tr>
<tr>
<td>中文单位</td>
<td>支持不限于上述类别的中文单位，例如“米”、“秒”、“美元”、“毫升每瓶”等。以及中文量词，例如“架”、“场”、“头”、“部”、“盆”等。</td>
</tr>
</table>

#### 标签关系
`<say-as>`标签仅包括文本。

#### 示例
- cardinal
```
<speak>
 <say-as interpret-as="cardinal">12345</say-as>
</speak>
```
音频效果：[say-as-cardinal.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/say-as-cardinal.wav)
- digits
```
<speak>
<say-as interpret-as="digits">12345</say-as>
</speak>
```
音频效果：[say-as-digits.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/say-as-digits.wav)
- telephone
```
<speak>
  <say-as interpret-as="telephone">12345</say-as>
</speak>
```
音频效果：[say-as-telephone.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/say-as-telephone.wav)
- name
```
<speak>
  她的曾用名是<say-as interpret-as="name">曾小凡</say-as>
</speak>
```
音频效果：[say-as-name.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/say-as-name.wav)
- address
```
<speak>
  <say-as interpret-as="address">深南大道10000号1号楼3单元304</say-as>
</speak>
```
音频效果：[say-as-address.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/say-as-address.wav)
- id
```
<speak>
  我的用户名是<say-as interpret-as="id">tencent_8858</say-as>
</speak>
```
音频效果：[say-as-id.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/say-as-id.wav)
- characters
```
<speak>
  希腊字母<say-as interpret-as="characters">αβ</say-as>
</speak>
```
音频效果：[say-as-characters.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/say-as-characters.wav)
- punctuation
```
<speak>
  我最常用的标点是<say-as interpret-as="punctuation">，</say-as>
</speak>
```
音频效果：[say-as-punctuation.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/say-as-punctuation.wav)
- date
```
<speak>
  <say-as interpret-as="date">2020-10-10</say-as>
</speak>
```
音频效果：[say-as-date.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/say-as-date.wav)
- time
```
<speak>
  <say-as interpret-as="time">5:30am</say-as>
</speak>
```
音频效果：[SSML-say-as_time.mp3](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/say-as-time.wav)
- currency
```
<speak>
  <say-as interpret-as="currency">15,000.00RMB</say-as>
</speak>
```
音频效果：[say-as-currency.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/say-as-currency.wav)
- measure
```
<speak>
  <say-as interpret-as="measure">100m²15cm²</say-as>
</speak>
```
音频效果：[say-as-measure.wav](https://ssml-demo-1300466766.cos.ap-guangzhou.myqcloud.com/say-as-measure.wav)

