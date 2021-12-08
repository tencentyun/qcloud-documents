
接入腾讯云 ECDN，将静态边缘缓存与动态回源路径优化相融合，通过腾讯在全球部署的节点优势，为您解决跨运营商、跨国、网络不稳定等因素导致的响应慢、丢包、服务不稳定等问题。
配置 ECDN 您需要注册腾讯云账号、开通 ECDN、接入域名和配置 CNAME，本文将依次为您介绍。


若您是第一次使用全站加速网络，请参考 [CDN 产品文档](https://cloud.tencent.com/document/product/228/3149) 进行入门配置。

## 步骤一：注册腾讯云账号
如果您已在腾讯云注册，可忽略此步骤。
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.3149.btn1">点此注册腾讯云账号</a></div>

## 步骤二：开通 ECDN
#### 1. 完成实名认证
未进行实名认证的用户，需要先完成实名认证，您可以通过 CDN 控制台或账户中心进行实名认证。 详细认证流程请参见 [实名认证指引](https://cloud.tencent.com/doc/product/378/3629) 。

<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;;"><a href="https://console.cloud.tencent.com/developer" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.3149.btn2">点此进入帐号中心</a></div><br>

![](https://main.qcloudimg.com/raw/aea08d1a99a05ffe35e2d777b1b35368.png)

#### 2. 开通 ECDN 服务
完成实名认证后，进入 [ECDN 控制台](https://console.cloud.tencent.com/ecdn)，即可开始开通 ECDN 服务。
![](https://main.qcloudimg.com/raw/8ce4391600356cf97e5986f61411f79c.png)

## 步骤三：接入域名
ECDN 通过加速域名把源站上的静态资源缓存到 ECDN 加速节点，动态内容通过智能路由优化、协议优化等动态加速技术快速回源获取，实现资源访问加速。详情请参见 <a href="https://cloud.tencent.com/document/product/570/10361" hotrep="document.guide.3149.linkdomain">接入域名</a>。

## 步骤四：配置 CNAME
您的域名接入 ECDN 后，还需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受 ECDN 加速服务。详情请参见 <a href="https://cloud.tencent.com/document/product/570/11134" hotrep="document.guide.3149.linkcname">配置 CNAME</a>。
