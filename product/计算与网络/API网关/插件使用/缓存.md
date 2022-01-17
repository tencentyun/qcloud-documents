## 操作场景

通过配置缓存插件，API 网关可存储后端应答，当遇到相同请求参数的请求时，API 网关将直接返回缓存的应答，无需转发到后端服务，以此达到降低后端的负荷，减少时延，增加平滑度的目的。

## 操作步骤

### 步骤1：创建插件

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway)。
2. 在左侧导航栏，单击**插件—系统插件**，进入系统插件列表页。
3. 单击页面左上角的**新建**，选择插件类型为**缓存**，新建一个缓存插件。缓存插件的配置项如下：
<table>
<tr>
<th>参数</th>
<th>是否必填	</th>
<th>说明</th>
</tr>
<tr>
<td>缓存参数</td>
<td>必填	</td>
<td>根据参数或参数的组合区分缓存内容，参数位置支持选择 Header、Path、Query。</td>
</tr>
<tr>
<td>请求方法</td>
<td>必填	</td>
<td>支持 GET、POST、PUT、DELETE、HEAD 方法，支持多选。</td>
</tr> 
<tr>
<td>缓存状态码</td>
<td>必填	</td>
<td>仅缓存插件中填写的状态码的响应，其他状态码不缓存，多个状态码间用英文逗号隔开。</td>
</tr>
<tr>
<td>Cache-Control</td>
<td>必填	</td>
<td>通过 Cache-Control 请求头影响缓存策略，默认关闭。</td>
</tr>
<tr>
<td>缓存时间</td>
<td>必填	</td>
<td>缓存有效的时间，可填写大于0到3600之间的正整数。</td>
</tr>
</table>
<img src = "https://qcloudimg.tencent-cloud.cn/raw/a56706c16714848626b78618a7b52bf4.png">


### 步骤2：绑定 API 并生效

1. 在列表中选中刚刚创建好的插件，单击操作列的**绑定 API**。
2. 在绑定 API 弹窗中选择服务和环境，并选择需要绑定插件的 API。
   ![](https://main.qcloudimg.com/raw/d7fd3c3539d6f623f45ebfdf0674d97e.png)
3. 单击**确定**，即可将插件绑定到 API，此时插件的配置已经对 API 生效。

## PluginData

```json
{
	"cache_key_params": [{ // 区分缓存的参数，parameter来源是api定义的参数，position取值为[header,query,path]
		"parameter": "param1",
		"position": "header"
	}, {
		"parameter": "param2",
		"position": "query"
	}, {
		"parameter": "param3",
		"position": "path"
	}],
	"cacheable_methods": ["GET", "POST"], // 可取缓存的http method，取值[GET、POST、PUT、DELETE、HEAD]
	"cacheable_response_codes": [200, 301, 404], // 可缓存的http返回码
	"cache_control": false, // 是否开启http标准的cache control语义，开启后，request和response的cache control都会生效，生效时会忽略自定义的ttl
	"ttl": 300 // 自定义缓存有效期，cache_control为false时生效。取值范围 [1,3600]
}
```


## 注意事项

- API 网关做参数校验和命中缓存时，都是大小写不敏感的。
- 对于共享实例来讲，每个用户每个 Region 的缓存容量总限制为5M；每台专享实例的缓存容量总限制为1G。
- 当开启 `Cache-Control` 配置时，网关将遵守请求/响应头中的 Cache-Control 头的约定来处理缓存。在这种情况下，如果网关获取不到 Cache-Control 头，则默认进行缓存，并使用插件中配置的“缓存时间”字段作为缓存超期时间。
