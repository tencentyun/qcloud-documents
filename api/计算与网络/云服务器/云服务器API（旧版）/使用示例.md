>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>


为了帮助用户快速使用云服务器（CVM）API，这里给出一个使用示例，能够引导用户使用API服务完整的创建并销毁一个实例。

## 1. 创建一个新的实例

在创建实例前，我们首先需要确定其配置，因为它决定了用户所创建实例的性能。有关配置用户可以参考[CVM实例机型](https://cloud.tencent.com/doc/product/213/497#3.-.E6.9C.BA.E5.9E.8B) 和 [CVM实例配置](https://cloud.tencent.com/doc/product/213/2177)。
如果我们想创建一个新的广州二区的 Windows 2008操作系统的按量计费实例，并具有1核心CPU，1GB的内存，需要的具体请求参数见下表：

| 参数名称 | 描述 | 取值 |
|---------|---------|---------|
| zoneId |[可用区](https://cloud.tencent.com/doc/api/229/1286)ID。| 100002 |
| imageId | 镜像ID，这里我们使用windows 2008（具体imageId对应何种操作系统可见[镜像列表](https://cloud.tencent.com/doc/api/229/1272)）。 | img-lkxqa4kj |
| cpu | CPU核数。 | 1 
|mem | 内存（GB）。| 1
| storageSize | 数据盘大小（GB）。| 0 |
| bandwidth |  公网带宽大小（Mbps） 。| 1 |
| password |  操作系统的系统管理员的的密码。 | @TQq191111118864+ |
如果对某些参数并不了解，可以详细参考[创建实例（按量计费）](https://cloud.tencent.com/doc/api/229/1350)页面，它详尽的解释了每个参数。

综上，结合公共请求参数和接口请求参数，最终得到的请求形式如下：

```
https://cvm.api.qcloud.com/v2/index.php?
Action=RunInstancesHour
&Region=gz
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&zoneId=100002
&imageId=img-lkxqa4kj
&cpu=1
&mem=1
&storageSize=0
&bandwidth=1
&password=@TQq191111118864+
```

上述请求的返回结果如下，由结果可知，新创建的实例的ID是ins-a19qoqqk。这个ID唯一标识了这个实例。后续将实例进行退还（删除实例）或是调整配置都需要通过它来指定对象。

```
  {
      "code" : 0,
      "message" : "ok",
      "unInstanceIds":[
          "ins-a19qoqqk"
      ]
  }
```

就这样我们创建了一个实例。拥有了它的实例ID。用户就可以通过VNC或是[远程桌面](https://cloud.tencent.com/doc/product/213/2154)去管理它了。

## 2. 主动退还一个已存在的实例。

由于按量计费类型的实例会实时计费，不需要的时候我们要主动退还它。
具体的接口请求参数见下表：

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|instanceId |是 |String |待操作CVM的实例ID。可通过<a href="http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeInstances">DescribeInstances</a>接口返回字段中的 unInstanceId 获取。|

结合公共请求参数和接口请求参数，最终得到的请求形式如下：

```
https://cvm.api.qcloud.com/v2/index.php?
Action=ReturnInstance
&Region=gz
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&instanceId=ins-a19qoqqk
```

上述请求的返回结果如下，由结果可知，新创建的实例的ID是ins-a19qoqqk。这个ID唯一标识了这个实例。后续将实例进行退还（删除实例）或是伸缩操作（调整配置）都需要通过它来指定对象。

```
  {
      "code" : 0,
      "message" : "ok"
  }
```



