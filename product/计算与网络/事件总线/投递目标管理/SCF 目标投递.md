通过事件规则，您可以将收集到的事件投递到指定的投递目标完成处理与消费，目前事件总线支持 [腾讯云云函数](https://cloud.tencent.com/product/scf) 作为投递目标，并提供了多个预设模版，帮助您完成事件的投递。

### 模版函数投递
选择函数模版，事件总线将根据提供的默认模版，为您创建一个目标函数，完成事件投递。目前，提供了 Ckafka 投递与 EIS 投递两个函数模版，您可以在**事件规则** > **事件目标**里进行选择与配置。
<dx-tabs>
::: Ckafka 投递模版
<dx-alert infotype="notice" title="">
如果您的目标 Ckafka 实例配有用户名密码，请注意填写的信息正确性，否则可能导致事件投递失败。
</dx-alert>
![](https://main.qcloudimg.com/raw/f77022aaed716a7ae67b412dbe59bb3d.png)
:::
::: SaaS 投递模版
![](https://main.qcloudimg.com/raw/2dfd372c14b4ff16709ee05b9aa5bf1f.png)
:::
</dx-tabs>



### 自定义函数投递
除了使用模版之外，您也可以将事件投递到您已经创建好的自定义函数里，完成更多业务逻辑的实现。
![](https://main.qcloudimg.com/raw/6834da9bee94b26747cfb4d2abcde56a.png)

### 开启批量投递
对于投递目标为云函数时，事件总线支持批量投递，您可以根据实际业务需求，选择投递方式。
![](https://main.qcloudimg.com/raw/a35c87785c5750569951756de91879db.png)
批量投递参数说明：
- **最长等待时间：** 单次触发的最长等待时间，最长等待时间范围（0-60s），默认为 0。
- **最大批量消息数：** 在拉取并批量投递给当前云函数时的最大消息数，目前支持最高配置为10000。结合消息大小、写入速度等因素影响，每次触发云函数并投递的消息数量不一定能达到最大值，而是处在1 - 最大消息数之间的一个变动值。




>! 开启批量投递功能后，事件将以数组形式投递，请注意事件消费端的格式适配。
<dx-tabs>
::: 未开启批量投递事件格式
<dx-codeblock>
:::  json
{
    "specversion": "1.0.2",
    "id": "13a3f42d-7258-4ada-da6d-023a333b4662",
    "type": "connector:apigw",
    "source": "apigw.cloud.tencent",
    "subjuect": "qcs::apigw:ap-guangzhou:uid1250000000/appidxxx:Serverid/Appid",
    "time": "1615430559146",
    "region": "ap-guangzhou",
    "datacontenttype": "application/json;charset=utf-8",
    "data":{
            $data_value
         }
}
:::
</dx-codeblock>
:::
::: 开启批量投递数组模式
<dx-codeblock>
:::  json
{
   "EventList":[
      {
        "specversion": "1.0.2",
        "id": "13a3f42d-7258-4ada-da6d-023a333b4662",
        "type": "connector:apigw",
        "source": "apigw.cloud.tencent",
        "subjuect": "qcs::apigw:ap-guangzhou:uid1250000000/appidxxx:Serverid/Appid",
        "time": "1615430559146",
        "region": "ap-guangzhou",
        "datacontenttype": "application/json;charset=utf-8",
        "data":{
              $data_value
         }
      },
      {
        "specversion": "1.0.2",
        "id": "13a3f42d-7258-4ada-da6d-023a333b4662",
        "type": "connector:apigw",
        "source": "apigw.cloud.tencent",
        "subjuect": "qcs::apigw:ap-guangzhou:uid1250000000/appidxxx:Serverid/Appid",
        "time": "1615430559146",
        "region": "ap-guangzhou",
        "datacontenttype": "application/json;charset=utf-8",
        "data":{
              $data_value
         }
      }
   ]
}
:::
</dx-codeblock>
:::
</dx-tabs>

