## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: CreateEip

创建弹性公网IP（EIP），弹性公网 IP是专为动态云计算设计的静态IP地址。借助弹性公网IP，您可以快速将EIP重新映射到您的另一个实例上，从而屏蔽实例故障。
您的弹性公网 IP 与腾讯云账户相关联，而不是与某个实例相关联，而且在您选择显式释放该地址，或欠费超过7天之前，它会一直与您的腾讯云账户保持关联。
>注：
平台对用户每地域能申请的EIP最大配额有所限制（可参见<a href="/doc/product/213/1941" title="/doc/product/213/1941">EIP产品简介</a>）。上述配额可通过 <a href="http://www.qcloud.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E9%85%8D%E9%A2%9D" title="DescribeEipQuota">DescribeEipQuota</a>接口获取。


## 2. 输入参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> goodsNum <td> 否 <td> Int <td> 单次申请数量（默认为1, 最大为5）
</tbody></table>

 

## 3. 输出参数
  | 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考<a href="/document/product/213/6982" title="错误码">错误码</a>。 |
| message |   String | 错误信息 |
| data |   Array | 返回数组 |

Data结构


<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> data.eipIds <td> Array <td> 创建的EIP实例ID列表
</tbody></table>

 

## 4. 示例
 
输入
```
 https://eip.api.qcloud.com/v2/index.php?
 &<公共请求参数>
```

输出
```

{
    "code": 0,
    "message": "",
    "data": {
        "eipIds": [
            "eip-m44ku5d2"
        ]
    }
}

```

