qcloudapi-sdk-java 是为了让 Java 开发者能够在自己的代码里更快捷方便的使用腾讯云的 API 而开发的 SDK 工具包。

### 快速入门
1. 申请安全凭证
在第一次使用云 API 之前，首先需要在腾讯云网站上申请安全凭证，安全凭证包括 SecretId 和 SecretKey，SecretId 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。
2. 使用 SDK
[下载 SDK](https://github.com/QcloudApi/qcloudapi-sdk-java)，放入到程序目录，使用方法请参考下面的例子。

```
import java.util.TreeMap;

import com.qcloud.QcloudApiModuleCenter;
import com.qcloud.Module.*;
import com.qcloud.Utilities.MD5;


public class Demo {
        public static void main(String[] args) {
                TreeMap<String, Object> config = new TreeMap<String, Object>();
        
                config.put("SecretId", "");
                config.put("SecretKey", "");
                config.put("RequestMethod", "POST");
                config.put("DefaultRegion", "gz");
                QcloudApiModuleCenter module = new QcloudApiModuleCenter(new Yunsou(), config);
                TreeMap<String, Object> params = new TreeMap<String, Object>();
                try{        
                        params.put("appId", "xxxx0002");
                        params.put("search_query", "qq");
                        System.out.println(module.call("DataSearch", params));
                        
//                        TreeMap<String, Object> params2 = new TreeMap<String, Object>();
//                        params2.put("appId", "xxxx0002");
//                        params2.put("op_type", "add");
//                        params2.put("contents.0.title", "test");
//                        params2.put("contents.0.contents", "qq");
//                        params2.put("contents.0.id", "12");
//                        params2.put("contents.0.score", "12");
//                        params2.put("contents.0.test", "12");
//                        
//                        System.out.println(module.call("DataManipulation", params2));
                }
                catch (Exception e) {
                        System.out.println(e.getMessage());
                }
        }
}
```
