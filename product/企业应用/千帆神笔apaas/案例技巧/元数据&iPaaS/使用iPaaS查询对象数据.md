## 须知

本文承接《使用 iPaaS 写入数据（一）》，***相关对象描述参考前述文档***，主要讲通过 iPaaS 读取 aPaaS 数据

## 适用场景

通过 iPaaS 集成流千帆神笔连接器访问 aPaaS 数据

## 关键字

<font color ="#0abf5b">iPaaS 集成流&nbsp;&nbsp;</font>
<font color ="#ff7200">数据读取&nbsp;&nbsp;</font>

## 实施步骤

### iPaaS 配置

1.创建千帆连接器，选择 **根据复杂条件查询业务数据** 组件：

> <img src="https://qcloudimg.tencent-cloud.cn/raw/973aa62822000d90f7b6ff3d28790235.png"></img>
2.配置应用code和对象key，参考《使用 iPaaS 写入数据（一）》，效果如下：

> <img src="https://qcloudimg.tencent-cloud.cn/raw/cb3bb6af419a36cbd3f79ce1b86362cc.png"></img>
3.配置 **字段key列表**，如下：

>       提示：默认为 []，表示查询全部字段
>            只查询部分字段：["字段key1","字段key2","字段key3"]
>       <img src="https://qcloudimg.tencent-cloud.cn/raw/e745e5cb7d59829551440a3d7050c925.png"></img>
4.配置 **查询条件**，如下：

> 查询条件配置参考：https://help.apaas.cloud.tencent.com/docs/open-api/api%E6%8E%A5%E5%8F%A3%E5%88%97%E8%A1%A8/%E4%B8%9A%E5%8A%A1%E6%95%B0%E6%8D%AE%E6%93%8D%E4%BD%9C/%E6%8C%89%E7%85%A7%E8%BF%87%E6%BB%A4%E6%9D%A1%E4%BB%B6%E6%9F%A5%E8%AF%A2%E4%B8%9A%E5%8A%A1%E6%95%B0%E6%8D%AE
> <img src="https://qcloudimg.tencent-cloud.cn/raw/89593a8d665d9bcdecfaba633b909b2c.png"></img>
```python
def dw_process(msg):
    # 查询 text_field 包含 "文本字段"  且 int_field 等于 10的数据列
    return
    {
        "Connector":"AND",
        "Children":
        [
            {
                "Field":"text_field",
                "Operator":"CONTAINS",
                "Value":"文本字段"
            },
            {
                "Field":"int_field",
                "Operator":"EQ",
                "Value":10
            }
        ]
    }
```

5.配置 **分页排序**，如下：

> <img src="https://qcloudimg.tencent-cloud.cn/raw/3e1bc5d52627f114914282b91feee72a.png"></img>
``` python
def dw_process(msg):
    # 从第0条开始，查询10条数据，并按照 text_filed 字段正序排序
    return {
            "Limit":10,
            "Offset":0,
            "OrderBy":[
                {
                    "Field":"text_field",
                    "Order":"ASC"
                }
            ]
        }
```

### 运行态效果

1.请求iPaaS集成流，返回值如下：

> 共查出两条数据
> <img src="https://qcloudimg.tencent-cloud.cn/raw/ac529a05daf9f220b923f73e2f2acd08.png"></img>
```python
{
    "Response":{
        "Data":{
            "EntityRecordSet":[
                {
                    "MainField":"3",
                    "Id":"1458712091891462184",
                    "FieldValue":{
                        "UpdatedTime":{
                            "DisplayValue":1636619038000,
                            "Value":1636619038000
                        },
                        "Enum_field":{
                            "DisplayValue":[
                                null
                            ],
                            "Value":[
                                ""
                            ]
                        },
                        "UpdatedBy":{
                            "DisplayValue":"-1",
                            "Value":"-1"
                        },
                        "File_field":{
                            "DisplayValue":"[1458712089811087362]",
                            "Value":"[1458712089811087362]"
                        },
                        "CreatedBy":{
                            "DisplayValue":"-1",
                            "Value":"-1"
                        },
                        "Text_field":{
                            "DisplayValue":"文本字段测试123abc",
                            "Value":"文本字段测试123abc"
                        },
                        "CreatedTime":{
                            "DisplayValue":1636619038000,
                            "Value":1636619038000
                        },
                        "Int_field":{
                            "DisplayValue":"10",
                            "Value":"10"
                        },
                        "Id":{
                            "DisplayValue":"3",
                            "Value":"3"
                        },
                        "OwnerId":{
                            "DisplayValue":"-1",
                            "Value":"-1"
                        },
                        "Image_field":{
                            "DisplayValue":"[1458712089823670359]",
                            "Value":"[1458712089823670359]"
                        }
                    },
                    "Entity":"data_object"
                },
                {
                    "MainField":"4",
                    "Id":"1458712107393609772",
                    "FieldValue":{
                        "UpdatedTime":{
                            "DisplayValue":1636619042000,
                            "Value":1636619042000
                        },
                        "Enum_field":{
                            "DisplayValue":[
                                null
                            ],
                            "Value":[
                                ""
                            ]
                        },
                        "UpdatedBy":{
                            "DisplayValue":"-1",
                            "Value":"-1"
                        },
                        "File_field":{
                            "DisplayValue":"[1458712105363558416]",
                            "Value":"[1458712105363558416]"
                        },
                        "CreatedBy":{
                            "DisplayValue":"-1",
                            "Value":"-1"
                        },
                        "Text_field":{
                            "DisplayValue":"文本字段测试123abc",
                            "Value":"文本字段测试123abc"
                        },
                        "CreatedTime":{
                            "DisplayValue":1636619042000,
                            "Value":1636619042000
                        },
                        "Int_field":{
                            "DisplayValue":"10",
                            "Value":"10"
                        },
                        "Id":{
                            "DisplayValue":"4",
                            "Value":"4"
                        },
                        "OwnerId":{
                            "DisplayValue":"-1",
                            "Value":"-1"
                        },
                        "Image_field":{
                            "DisplayValue":"[1458712105376141387]",
                            "Value":"[1458712105376141387]"
                        }
                    },
                    "Entity":"data_object"
                }
            ],
            "TotalCount":2
        },
        "RequestId":"784f9f7e1218e0b0"
    }
}
```
