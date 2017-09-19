## 1. 接口描述

功能：单条或者批量提交用户行为数据  
接口：`https://sdtj.y.qq.com:8008/upload`   
方法：POST  

## 2. 输入参数  

**表 1：**
<table>
	<tr>
		<th>参数名称
		</th>
		<th>必选
		</th>
		<th>类型
		</th>
		<th>含义
		</th>
	</tr>
	<tr>
		<td>version</td>
		<td>是</td>
		<td>String</td>
		<td>上报接口版本 （1，2，3，4） ，当前版本为 1 </td>
	</tr>
	<tr>
		<td>seq_no</td>
		<td>否</td>
		<td>String</td>
		<td>请求标识，接口原样返回</td>
	</tr>
	<tr>
		<td>data_type</td>
		<td>是</td>
		<td>String</td>
		<td>协议类型： "1" - item, "2" – action，行为上报传 "2"</td>
	</tr>
	<tr>
		<td>token</td>
		<td>是</td>
		<td>String</td>
		<td>用作鉴权，由云推荐引擎分配</td>
	</tr>
	<tr>
		<td>data</td>
		<td>是</td>
		<td>JSONArray</td>
		<td>多条行为数据，详细参考表 2 </td>
	</tr>
</table>

**表 2：**
<table>
	<tr>
		<th colspan="2">参数名称</th>
		<th>必选</th>
		<th>类型</th>
		<th>含义</th>
	</tr>
	<tr>
		<td colspan="2">uid_type</td>
		<td>是</td>
		<td>String</td>
		<td>"0":QQ, "1":微信号，"2":openid, "3":IMEI/IDFA，
			"4":手机号，"5":app 唯一用户</td>
	</tr>
	<tr>
		<td colspan="2">uid</td>
		<td>是</td>
		<td>String</td>
		<td>uid_type 指定类型的用户标识，QQ 号，微信号等等</td>
	</tr>
	<tr>
		<td colspan="2">oper_time</td>
		<td>是</td>
		<td>String</td>
		<td>操作时间，UTC时间，例如 "1483200000"（2017年01月01日 00:00:00）</td>
	</tr>
	<tr>
		<td colspan="2">source</td>
		<td>是</td>
		<td>String</td>
		<td>用于分流的标识字段，区分用户的行为是来自哪个引擎；"0" :腾讯云推荐引擎，其他值业务自定义</td>
	</tr>
	<tr>
		<td colspan="2">test_id</td>
		<td>否</td>
		<td>String</td>
		<td>推荐场景 ID ，比如对于“猜你喜欢”、“首页推荐”等推荐场景，云推荐引擎会分配一个 ID 标识。推荐场景必须填写，此时该字段由推荐引擎的请求接口返回，业务上报时原样拷贝即可，例如 “1000190”</td>
	</tr>
	<tr>
		<td colspan="2">rule_id</td>
		<td>否</td>
		<td>String</td>
		<td>算法 ID ，推荐场景必须填写；通常一个推荐场景下会有多个算法 ID ，用于算法迭代</td>
	</tr>
	<tr>
		<td colspan="2">trace_id</td>
		<td>是</td>
		<td>String</td>
		<td>跟踪点击和曝光的自定义会话  ID ，为了保证点击跟曝光是同一个用户，对同一个 item 的操作行为，强烈建议每次曝光分配一个 trace_id</td>
	</tr>
	<tr>
		<td colspan="2">item_type</td>
		<td>否</td>
		<td>String</td>
		<td>物品类型，例如 APP 、商品等</td>
	</tr>
	<tr>
		<td colspan="2">action_id</td>
		<td>是</td>
		<td>String</td>
		<td>曝光:101, 点击:102, 下载:103, 阅读:104, 播放:105, 转发/分享:106, 点赞:107,
			评论:108, 支付:109, 收藏:110, 搜索:111, 关注:112, 回复:113, 安装:114, 打开:115,
			取消收藏:116, 加入购物车:117, 从购物车删除:118, 收藏, 铺:119, 取消收藏店铺:120, 关注:121,
			取消关注:122, 购买:123, 取消购买:124, 播放快进:125, 播放快退:126, 播放下一个:127, 重播:128</td>
	</tr>
	<tr>
		<td colspan="2">busi_id</td>
		<td>否</td>
		<td>String</td>
		<td>业务 ID ，由云推荐引擎分配</td>
	</tr>
	<tr>
		<td colspan="2">page_id</td>
		<td>否</td>
		<td>String</td>
		<td>页面 ID ，区分不同页面；如："1001" 表示直播首页</td>
	</tr>
	<tr>
		<td colspan="2">module_id</td>
		<td>否</td>
		<td>String</td>
		<td>操纵模块 ID，如："100102" 标识 banner</td>
	</tr>
	<tr>
		<td colspan="2">sub_module_id</td>
		<td>否</td>
		<td>String</td>
		<td>操作子模块 ID </td>
	</tr>
	<tr>
		<td colspan="2">platform</td>
		<td>否</td>
		<td>String</td>
		<td>"ios":ios 平台，"android":Android 平台，"h5":h5 页面</td>
	</tr>
	<tr>
		<td colspan="2">device</td>
		<td>否</td>
		<td>String</td>
		<td>设备型号描述</td>
	</tr>
	<tr>
		<td colspan="2">network_type</td>
		<td>否</td>
		<td>String</td>
		<td>网络型号。 "2G"：2G 网络，"3G"：3G 网络，"4G"：4G 网络，"WIFI"：WIFI 网络</td>
	</tr>
	<tr>
		<td colspan="2">app_version</td>
		<td>否</td>
		<td>String</td>
		<td>APP 的版本</td>
	</tr>
	<tr>
		<td colspan="2">report_source</td>
		<td>否</td>
		<td>String</td>
		<td>上报来源。"1" - 安卓终端，"2" - iOS 终端，"3" - 前端（外部分享页、Web)，"4" - 后台，"5" - 前端（客户端内）</td>
	</tr>
	<tr>
		<td rowspan="4">geo</td>
		<td>latitude</td>
		<td>否</td>
		<td>String</td>
		<td>用户发生行为的经纬度地理位置</td>
	</tr>
	<tr>
		<td>longtitude</td>
		<td>否</td>
		<td>String</td>
		<td>用户发生行为的经纬度地理位置</td>
	</tr>
	<tr>
		<td>country</td>
		<td>否</td>
		<td>String</td>
		<td>用户发生行为的经纬度地理位置</td>
	</tr>
	<tr>
		<td>city</td>
		<td>否</td>
		<td>String</td>
		<td>用户发生行为的经纬度地理位置</td>
	</tr>
	<tr>
		<td rowspan="4">extend（多个扩展字段，类型为JSONArray）</td>
		<td>key1</td>
		<td>否</td>
		<td>String</td>
		<td>用户自定义数据参数名称，例如用户发生行为的经纬度地理位置，latitude</td>
	</tr>
	<tr>
		<td>key2</td>
		<td>否</td>
		<td>String</td>
		<td>用户自定义数据参数名称，用户发生行为的经纬度地理位置，longtitude</td>
	</tr>
	<tr>
		<td>key3</td>
		<td>否</td>
		<td>String</td>
		<td>用户自定义数据参数名称，用户发生行为的经纬度地理位置，country</td>
	</tr>
	<tr>
		<td>...</td>
		<td>否</td>
		<td>String</td>
		<td>用户自定义数据参数名称，用户发生行为的经纬度地理位置，city</td>
	</tr>
	<tr>
		<td rowspan="5">item_action（多个item行为，类型为JSONArray）</td>
	 	<td>item_id</td>
		<td>是</td>
		<td>String</td>
		<td>物品 ID，物品唯一标识</td>
    </tr>
	<tr>
		<td>sub_item_id</td>
		<td>否</td>
		<td>String</td>
		<td>子物品唯一标识</td>
    </tr>
	<tr>
		<td>action_value</td>
		<td>否</td>
		<td>String</td>
		<td>操作行为值，例如商品价格、视频播放时长</td>
	</tr>
	<tr>
		<td>position_id</td>
		<td>否</td>
		<td>String</td>
		<td>物品在列表中的位置</td>
	</tr>
	<tr>
		<td>item_info（多个具体的 item 信息，类型为 JSONObject）</td>
		<td>否</td>
		<td>JSONObject</td>
		<td>所有都是 key-value 组成键值对，key 为 String 类型，value 为 String 类型</td>
    </tr>
</table>


## 3. 输出参数

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|--------|------------|
| seq_no | 否 | String | 请求标识，接口原样返回 | 
| code | 是 | String | 错误码，"0" 表示成功，非 "0"  表示失败 |
| message | 否 | String| 错误信息 |


## 4. 示例

输入：
```
{
"version" :"1",
"seq_no":"1",
 "data_type":"2",
 "token":"7d10d09d-be62-4979-9ee0-414f7a23086a",
 "data":[
   {
     "uid_type":"2",
     "uid":"00000000adfec3",
     "oper_time":"1483200000",
     "source":"0", 
     "test_id":"1000190",
     "rule_id":"200723",
     "trace_id":"345",
     "action_id":"101",
     "busi_id":"10034002",
     "item_action":[
       {
         "item_id": "item1",
         "position_id":"2",
         "item_info": {
           "price":"99", // 价格
           "group_id1":"1111", // 广告位
         }
       },
       {
         "item_id": "item2",
         "position_id":"5",
         "item_info": {
           "price":"99", // 价格
           "group_id2":"1111", // 广告位
         }
       }     
      ],
     "page_id":"https://www.xx.com/",
     "network_type":"4G",
     "extend":{
       "ext1":"800456",
       "ext2":"123423",
       "ext3":"https://www.yy.com"
     }
   }
 ]
}
```

输出：  
```{
{
	 "seq_no":"1",
	 "code":"0",
	 "message":null
}
```
