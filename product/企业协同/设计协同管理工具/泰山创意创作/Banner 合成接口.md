## 接口描述
描述：传入指定的模板和素材链接生成 Banner 。
请求 URL：`http://taishan.oa.com/api/banner/generate`
请求方式：Get

## 请求参数

| 参数名    | 必选 | 类型   | 说明                                                         |
| :-------- | :--- | :----- | ------------------------------------------------------------ |
| pid       | 是   | string | 项目 ID。                                                       |
| tpid      | 是   | string | 模板 ID。                                                       |
| material  | 否   | object | 素材的图片集合。key 值为“main”(主体图)或“bgimg”(背景图)或“logo”。 |
| text      | 否   | array  | 素材的文案集合。文案可以为多组，每组文案可以由不同类型组成。   |
| size      | 否   | object | 生成的 Banner 尺寸。key 值为“width”和“height” 。                |
| pickColor | 否   | string | 根据指定的颜色来智能配色。                                     |
| tag       | 否   | array  | 标签列表。                                                     |
| format    | 否   | string | 输出的图片格式，默认为 jpg。可以设置为 png。                       |

### 请求参数示例
#### material 参数示例

```
 //素材
    "material": {
        //主体，必须
        "main": {
            "src": "http://wfqqreader.3g.qq.com/cover/868/215868/t3_215868.jpg" //主体图地址
        },
        //陪衬，可选
        "sub": {
            "src": "http://wfqqreader.3g.qq.com/cover/868/215868/t3_215868.jpg" //陪衬图地址
        },
        //背景图，可选
        "bgimg ": {
            "src": "http://wfqqreader.3g.qq.com/cover/868/215868/t3_215868.jpg" //背景图地址
        },
        //logo图，可选
        "logo ": {
            "src": "http://wfqqreader.3g.qq.com/cover/868/215868/t3_215868.jpg" //logo图地址
        },
    }
```


#### text 参数示例

```
"text": [
        //主文案必须
        {
            "type": "main",
            "name": "主文案",
            "value": "《 最强反套路》",
            //重点字
            "em": ["最强","套路"]
        },
        //描述文案可选
        {
            "type": "desc",
            "name": "描述文案",
            "value": " 我要做天空中最亮的星星" 
        },
        //标签文案可选
        {
            "type": "tag",
             "name": "标签文案",
            "value": "这是标签文案"
        }
    ]
```

#### size 参数示例


```
//尺寸，必须
    "size": {
        "width": 750,
        "height": 400
    }
```

## 请求示例 

```
http://taishan.oa.com/api/banner/generate?
&pid=5c6b64e05de19522f7e24ea5
&tpid=5cc6c2ccf01bec0918549379
&material={
    "main":[
            {"src":"http://wfqqreader.3g.qq.com/cover/868/215868/t3_215868.jpg"},
            {"src":"http://wfqqreader.3g.qq.com/cover/868/215868/t3_215868.jpg"}
        ],
    "sub":{"src":"http://wfqqreader.3g.qq.com/cover/868/215868/t3_215868.jpg"},
    "logo":{"src":"http://wfqqreader.3g.qq.com/cover/868/215868/t3_215868.jpg"}
}
&text=[
        {"type":"main","name":"主文案","value":"《最强反套路》"},
        {"type":"desc","name":"描述文案","value":"我要做天空中最亮的星星"}
]
&size={"width":750,"height":400}
&pickColor=#40bf67
&tag=["清新"]
&format=png

```

## 返回参数
### 返回参数说明

| 参数名 | 类型   | 说明                         |
| :----- | :----- | ---------------------------- |
| msg    | string |success：成功<br>error：错误。 |
| data   | object | 返回具体的数据。               |

**data 具体参数说明**

| 参数名 | 类型   | 说明               |
| :----- | :----- | ------------------ |
| id     | string | 泰山返回的 bannerId。  |

## 返回示例

```
{
    "msg": "success",
    "data": {
        "id": "5d2ee97d921b4c4bf6d552a6"
    }
}
```
