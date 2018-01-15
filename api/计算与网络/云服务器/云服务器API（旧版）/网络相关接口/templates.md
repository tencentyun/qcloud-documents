## 1. 接口描述

本接口 ({{name_of_api}}) 用于{{desc_of_api}}。

接口请求域名：<font style="color:red">{{domain_of_api}}</font>
{%for keypoint in keypoint_of_api%}
* {{keypoint}}。{%endfor%}

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://cloud.tencent.com/doc/api/229/1230)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
{%for arg in input_args_of_api%}|{{arg.name}}|{%if
arg.has%}是{%else%}否{%endif%}|{{arg.type}}|{{arg.desc}}|
{%endfor%}

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
{%for arg in output_args_of_api%}|{{arg.name}}|{{arg.type}}|{{arg.desc}}|
{%endfor%}

## 4. 示例
 
输入

```
  https://{{domain_of_api}}/v2/index.php?Action={{name_of_api}}
    {%for arg in input_args_of_api%}{%if arg.has%}&{{arg.name}}={{arg.sample}}{%endif%}{%endfor%}
    &<公共请求参数>

```

输出

```
{{output_json}}
```

