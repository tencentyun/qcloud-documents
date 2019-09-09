
## 漏洞名称
Fastjson < 1.2.60 远程拒绝服务漏洞
## 影响版本
Fastjson < 1.2.60 
## 漏洞详情
近日，[腾讯云安全中心](https://console.cloud.tencent.com/ssa) 监测到开源 JSON 解析库 Fastjson 1.2.60 以下版本存在字符串解析异常，攻击者可利用该漏洞发送精心构造的恶意请求包到使用到 Fastjson 的服务器，使服务器内存、CPU 等资源耗尽，导致服务不可用。目前该漏洞相关利用代码已被公开，建议尽快升级处理。

```
import java.net.URLDecoder;

public class Issue2689 extends TestCase {

    final String DEATH_STRING = "{\"a\":\"\\x";

    public void test_OOM() throws Exception {

        String line = new String("[{\\x22a\\x22:\\x22a\\xB1ph.\\xCD\\x86\\xBEI\\xBA\\xC3\\xBCiM+\\xCE\\xCE\\x1E\\xDF7\\x1E\\xD9z\\xD9Q\\x8A}\\xD4\\xB2\\xD5\\xA0y\\x98\\x08@\\xE1!\\xA8\\xEF^\\x0D\\x7F\\xECX!\\xFF\\x06IP\\xEC\\x9F[\\x85;\\x02\\x817R\\x87\\xFB\\x1Ch\\xCB\\xC7\\xC6\\x06\\x8F\\xE2Z\\xDA^J\\xEB\\xBCF\\xA6\\xE6\\xF4\\xF7\\xC1\\xE3\\xA4T\\x89\\xC6\\xB2\\x5Cx]");
        line = line.replaceAll("\\\\x", "%");
        String decodeLog = URLDecoder.decode(line, "UTF-8");
        System.out.println(decodeLog);
        try {
            Object obj = JSON.parse(decodeLog);
            obj = JSON.parse(DEATH_STRING);
        } catch (Exception e) {
            assertEquals(e.getClass(), JSONException.class);
            assertTrue(e.getMessage().contains("invalid escape character \\x"));
        }
    }
}
```


## 官方修复建议

拒绝服务安全漏洞涉及之前所有 Fastjson 版本，建议将 Fastjson 升级到最新1.2.60版本。

## 防护建议
腾讯云 Web 应用防火墙（网站管家）攻击防护规则中，已经包含该漏洞的防护规则，操作步骤如下：
1. 登录 [腾讯云 Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview) ，在左侧导航栏中，选择【Web 应用防火墙】>【防护设置】，在域名列表中，选择需要防护的域名，在右侧单击【防护配置】。
![](https://main.qcloudimg.com/raw/c6243481d9080b8bec3960a4a5c29dde.png)
2. 在基础设置页面，将 WAF 防护状态的使用模式设置为【拦截】即可防御。
![](https://main.qcloudimg.com/raw/6df57e99ad05a67e70b15cf5f7c8ce0d.png)

## 更多信息
- [【安全预警】Fastjson < 1.2.60 远程拒绝服务漏洞风险预警](https://cloud.tencent.com/announce/detail/764) 
- [Fastjson 1.2.60版本发布修复拒绝服务安全问题](https://github.com/alibaba/fastjson/releases/tag/1.2.60)
