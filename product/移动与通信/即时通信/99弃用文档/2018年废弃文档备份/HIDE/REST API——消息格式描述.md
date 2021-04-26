## 消息内容MsgBody说明

MsgBody中所填写字段是消息内容。腾讯即时通信支持一条消息中包括多种消息元素类别。如一条消息中既包括文本消息元素，还包括表情消息元素。因此MsgBody定义为Array格式，可按照需求加入多类消息元素。消息元素名称为TIMMsgElement，消息元素TIMMsgElement组成MsgBody例子见下文章节消息内容MsgBody实例。
消息元素TIMMsgElement的格式统一为
```
{
    "MsgType": "TIMTextElem", 
    "MsgContent": { }
}
```
<table style="width:100%;">
		<tbody>
			<tr>
				<td style="width:15%;">
					字段
				</td>
				<td style="width:15%;">
					类型
				</td>
				<td>
					说明
				</td>
			</tr>
			<tr>
				<td>
					MsgType<br />
				</td>
				<td>
					String
				</td>
				<td>
					消息元素类别；<span style="line-height:1.5;">目前支持的消息对象包括：</span><span style="line-height:1.5;">TIMTextElem(文本消息)，TIMFaceElem(表情消息)，</span><span style="line-height:1.5;">TIMLocationElem(位置消息)，TIMCustomElem(自定义消息)。</span><br />
				</td>
			</tr>
			<tr>
				<td>
					MsgContent<br />
				</td>
				<td>
					Object
				</td>
				<td>
					消息元素的内容，不同的MsgType有不同的MsgContent格式，具体参见下文。
				</td>
			</tr>
		</tbody>
	</table>
目前支持消息类别MsgType有
<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:15%;">
					MsgType的值<br />
				</td>
				<td>
					类型
				</td>
			</tr>
			<tr>
				<td>
					TIMTextElem<br />
				</td>
				<td>
					文本消息。<br />
				</td>
			</tr>
			<tr>
				<td>
					TIMLocationElem<br />
				</td>
				<td>
					地理位置消息。<br />
				</td>
			</tr>
			<tr>
				<td>
					TIMFaceElem<br />
				</td>
				<td>
					表情消息。
				</td>
			</tr>
			<tr>
				<td>
					<p>
						TIMCustomElem
					</p>
				</td>
				<td>
					自定义消息，当接收方为IOS系统且应用处在后台时，此消息类型可携带除文本以外的字段到APNS。<br />
				</td>
			</tr>
		</tbody>
	</table>
	
## 消息元素TIMMsgElement

### 文本消息元素

```
{
            "MsgType": "TIMTextElem", 
            "MsgContent": {
                "Text": "red packet"
            }
        }
```
<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:15%;">
					字段
				</td>
				<td style="width:15%;">
					类型
				</td>
				<td>
					说明
				</td>
			</tr>
			<tr>
				<td>
					Text
				</td>
				<td>
					String
				</td>
				<td>
					消息内容。当接收方在后台时，做IOS离线Push时文本展示。
				</td>
			</tr>
		</tbody>
	</table>
	
当接收方为IOS系统且应用处在后台时，json请求包体中的Text字段作为离线推送文本（用户收到推送是 ”昵称：推送文本“）。

### 地理位置消息元素

```
{
    "MsgType": "TIMLocationElem", 
    "MsgContent": {
        "Desc": "someinfo", 
        "Latitude": 3235345, 
        "Longitude": 232323
    }
}
```
<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:15%;">
					字段&nbsp;&nbsp;&nbsp;&nbsp;<br />
				</td>
				<td style="width:15%;">
					类型<br />
				</td>
				<td>
					说明
				</td>
			</tr>
			<tr>
				<td>
					Desc
				</td>
				<td>
					String
				</td>
				<td>
					地理位置描述信息<br />
				</td>
			</tr>
			<tr>
				<td>
					Latitude<br />
				</td>
				<td>
					Number
				</td>
				<td>
					纬度
				</td>
			</tr>
			<tr>
				<td>
					Longitude<br />
				</td>
				<td>
					Number
				</td>
				<td>
					经度
				</td>
			</tr>
		</tbody>
	</table>
	
当接收方为IOS系统且应用处在后台时，中文版离线推送文本为“昵称：[位置]”，英文版推送文本为“[Location]”（用户收到推送是 ”昵称：推送文本“）。

### 表情消息元素

```
{
    "MsgType": "TIMFaceElem", 
    "MsgContent": {
        "Index": 1, 
        "Data": "content"
    }
}
```
<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:15%;">
					字段
				</td>
				<td style="width:15%;">
					类型
				</td>
				<td style="width:20px;">
					说明
				</td>
			</tr>
			<tr>
				<td>
					Index<br />
				</td>
				<td>
					Number
				</td>
				<td>
					表情索引，用户自定义<br />
				</td>
			</tr>
			<tr>
				<td>
					Data<br />
				</td>
				<td>
					String
				</td>
				<td>
					额外数据
				</td>
			</tr>
		</tbody>
	</table>

当接收方为IOS系统且应用处在后台时，中文版离线推送文本为“[表情]”，英文版为“[Face]”（用户收到推送是 ”昵称：推送文本“）。

### 自定义消息元素

```
{
    "MsgType": "TIMCustomElem", 
    "MsgContent": {
        "Data": "message", 
        "Desc": "notification", 
        "Ext": "/:url"
    }
}
```
<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:15%;">
					<span style="white-space:nowrap;">字段</span> 
				</td>
				<td style="width:15%;">
					<span style="white-space:nowrap;">类型</span> 
				</td>
				<td>
					<span style="white-space:nowrap;">说明</span> 
				</td>
			</tr>
			<tr>
				<td>
					<span style="white-space:nowrap;">Data</span> 
				</td>
				<td>
					<span style="white-space:nowrap;">String</span> 
				</td>
				<td>
					<span style="white-space:nowrap;">自定义消息数据。<br />
</span> 
				</td>
			</tr>
			<tr>
				<td>
					<span style="white-space:nowrap;">Desc</span> 
				</td>
				<td>
					<span style="white-space:nowrap;">String</span> 
				</td>
				<td>
					<p>
						<span style="white-space:nowrap;">自定义消息描述信息；当接收方在后台时，做IOS离线Push时文本展示。</span> 
					</p>
				</td>
			</tr>
			<tr>
				<td>
					<span style="white-space:nowrap;">Ext</span> 
				</td>
				<td>
					<span style="white-space:nowrap;">String</span> 
				</td>
				<td>
					<p>
						<span style="white-space:nowrap;">扩展字段；当接收方为IOS系统且应用处在后台时，此字段作为APNS请求包payload中的ext键值下发，Ext的协议格式由业务方确定，APNS只做透传。</span> 
					</p>
				</td>
			</tr>
		</tbody>
	</table>
	
当接收方为IOS系统且应用处在后台时，Desc作为推送文本， Ext字段作为APNS请求包payload中的ext键值下发（用户收到推送是 ”昵称：推送文本“））。

## MsgBody消息内容实例

### 单一文本元素消息

消息中只包括一中文本消息元素，文本内容为hello world。

```
{
    "MsgBody": [
        {
            "MsgType": "TIMTextElem", 
            "MsgContent": {
                "Text": "hello world"
            }
        }
    ]
}
```

### 组合消息

消息中包括两个文本消息元素和一个表情元素，即文本+表情+文本。

```
{
    "MsgBody": [
        {
            "MsgType": "TIMTextElem", 
            "MsgContent": {
                "Text": "hello"
            }
        }, 
        {
            "MsgType": "TIMFaceElem", 
            "MsgContent": {
                "Index": 1, 
                "Data": "content"
            }
        }, 
        {
            "MsgType": "TIMTextElem", 
            "MsgContent": {
                "Text": "world"
            }
        }
    ]
}
```