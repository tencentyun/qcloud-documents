策略(policy)由若干元素构成，用来描述授权的具体信息。核心元素包括委托人(principal)、操作(action)、资源(resource)、生效条件(condition)以及效力(effect)。
**说明 ：**

	- 元素仅支持小写。它们在描述上没有顺序要求。
	- 对于策略没有特定条件约束的情况， condition 元素是可选项。
	- 在控制台中不允许写入 principal 元素，仅支持在策略管理 API 中和策略语法相关的参数中使用 principal 。

### 版本 version

描述策略语法版本。目前仅允许值为 2.0。该元素是必填项。

### 委托人 principal

用于描述策略授权的实体。包括用户（开发商、子账号、匿名用户）、用户组，仅支持在策略管理 API 中策略语法相关的参数中使用该元素。

### 语句 statement

用于描述一条或多条权限的详细信息。该元素包括 action 、 resource 、 condition 、 effect 等多个其他元素的权限或权限集合。一条策略有且仅有一个 statement 元素。该元素是必填项。

### 操作 action

用于描述允许或拒绝的操作。操作可以是 API （以 name 前缀描述）或者功能集（一组特定的 API ，以 permid 前缀描述）。该元素是必填项。

### 资源 resource

用于描述授权的具体数据。资源是用用六段式描述。每款产品的资源定义详情会有所区别。有关如何指定资源的信息，请参阅您编写的资源声明所对应的产品文档。该元素是必填项。

### 生效条件 condition

用于描述策略生效的约束条件。条件包括操作符、操作键和操作值组成。条件值可包括时间、 IP 地址等信息。有些服务允许您在条件中指定其他值。该元素是非必填项

### 效力 effect
	
用于描述声明产生的结果，包括 allow (允许)和 deny (显式拒绝)两种情况。该元素是必填项。

### 策略样例
	
以下示例表示：
允许属于开发商 ID 1238423 下的子账号 ID 3232523 以及组 ID 18825， 在访问 IP 网段 `10.121.2.10/24` 时，对北京地域的 COS 存储桶 bucketA 和广州地域的 COS 对象 object2 ，拥有所有 COS 读 API 、写对象、以及发送消息队列的权限。


```
{	 
        "version":"2.0", 
        "principal":{"qcs":["qcs::cam::uin/1238423:uin/3232523", 
                        "qcs::cam::uin/1238423:groupid/18825"]}, 
        "statement": 
        [ 
           { 
              "effect":"allow", 
              "action":["name/cos:PutObject","permid/280655"], 
              "resource":["qcs::cos:bj:uid/1238423:prefix/bucketA/*", 
                        "qcs::cos:gz:uid/1238423:prefix/bucketB/object2"], 
               "condition": {"ip_equal":{"qcs:ip":"10.121.2.10/24"}} 
           }, 
          { 
             "effect":"allow", 
             "action":"name/cmqqueue:Sendmessages", 
             "resource":"*" 
          } 
       ] 
} 
```