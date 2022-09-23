腾讯云呼叫中心电话功能需要通信号码进行呼入/呼出，企业若已有号码可以与腾讯云呼叫中心对接。自有号码对接分为：[自有固话 SIP_Trunk 对接](https://cloud.tencent.com/document/product/679/73527) 与 [自有400号码对接](https://cloud.tencent.com/document/product/679/76428)。

腾讯云呼叫中心支持通过 SIP Trunk 的方式与企业自带的固话号码与进行对接，实现使用企业自有号码进行呼入和呼出。对接完成后企业自行与号码所属运营商结算该号码产生的通信费用，腾讯云呼叫中心不收取对接与号码产生的通信费用。

请联系您的号码运营商确认是否支持 SIP 中继，如不支持 SIP 中继，请咨询运营商能否协助变更为 SIP 中继方式与腾讯云呼叫中心对接，如无法变更，您可购买网关设备和 SIP 服务搭建一套 SIP 中继服务与腾讯云呼叫中心对接。

如您的设备无公网 IP，可按照此文档进行 SIP 账号注册模式接入，这里以 freeswitch gateway 接入作为示例。

## 操作步骤
### 步骤1：向 TCCC 申请开户，获取注册用户名密码
- 用户名：gatewayXX
- 域名：14xxxxx.tccc.qcloud.com (注：14开头的为 tccc 实例 ID）
- 服务器：sip.tccc.qcloud.com:35090
- 信令通道：TCP/UDP （推荐使用 tcp，udp 走公网可能会有设备拦截大包的问题）
- 信令参考：
![](https://qcloudimg.tencent-cloud.cn/raw/062708e2ef3aa304b9d67ff1510c1ba8.png)
- freeswitch 配置参考：
`/conf/sip_profiles/external/tccc_gw_register.xml`
```
<include>
<gateway name="tccc_gw_register"> 
    <param name="username" value="gateway01"/>
    <param name="realm" value="1400xxxxx.tccc.qcloud.com"/>
    <param name="from-domain" value="1400xxxxx.tccc.qcloud.com"/>
    <param name="password" value="xxxx"/>
    <param name="expire-seconds" value="120"/>
    <param name="register" value="true"/>
    <param name="register-transport" value="udp"/>
    <param name="register-proxy" value="sip.tccc.qcloud.com:35090"/>
    <param name="outbound-proxy" value="sip.tccc.qcloud.com:35090"/>
    <param name="rtp-autofix-timing" value="false"/>
    <param name="caller-id-in-from" value="true"/>
</gateway>

</include>
```

### 步骤2：第三方送呼叫给 TCCC
- requestURI：自有线路号码
- From：主叫号码
- To：自有线路号码
- Proxy-Authorization: 注册认证信息
- 信令参考：
![](https://qcloudimg.tencent-cloud.cn/raw/8f29cd972686adacb68b7d955ab42d4f.png)
- freeswitch 测试脚本：
```
originate {sip_invite_full_from=sip:主叫号码@1400264214.tccc.qcloud.com,sip_invite_to_uri=sip:线路号码@1400264214.tccc.qcloud.com,sip_cid_type=none}sofia/gateway/tccc_sbc_register/线路号码 &park
```

### 步骤3：TCCC 送呼叫给第三方
- From: 主机号码
- To:被叫号码
- 信令参考：
![](https://qcloudimg.tencent-cloud.cn/raw/83db5fb3cf23afb6df6ddfc656859659.png)
