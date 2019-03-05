## 接口名称
CreateClass

## 功能说明
1. 用于管理视频文件，增加分类；
2. 该操作为全局操作，不涉及具体文件的分类关联，如需修改文件的分类请使用[修改视频属性](/document/product/266/7828)接口。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| className | 是 | String | 分类信息 |
| parentId | 否 | Integer | 父分类的id号，若不填，默认生成一级分类 |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=CreateClass
&className=test
&parentId=-1
&COMMON_PARAMS
```
## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功, 其他值: 失败 |
| newClassId | String | 新生成的分类id，最上层分类的id为-1 |
| message | String | 错误信息 |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| 1000 | 无效参数  |
| 1903 | 默认分类下不能创建目录 |

### 应答示例
```javascript
{
    "code": 0,
    "message": "",
    "newClassId": "250"
}
```
