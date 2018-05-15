### 获取 SDK

[Java SDK](https://github.com/QcloudApi/qcloudapi-sdk-java)

### 获取临时密钥

```
import com.qcloud.Utilities.Json.JSONObject;

public class Demo {
    public static void main(String[] args) {
    
        TreeMap<String, Object> config = new TreeMap<String, Object>();
        
        config.put("SecretId", "你的SecretId");
        config.put("SecretKey", "你的SecretKey");

        config.put("RequestMethod", "GET");

        QcloudApiModuleCenter module = new QcloudApiModuleCenter(new Sts(),
                config);

        TreeMap<String, Object> params = new TreeMap<String, Object>();
        
        params.put("name", "你的昵称");
        
        String policy = "{\"statement\": [{\"action\": [\"name/cos:*\"],\"effect\": \"allow\",\"resource\":\"*\"}],\"version\": \"2.0\"}";
        params.put("policy", policy);

        String result = null;
        try {
            /* call 方法正式向指定的接口名发送请求，并把请求参数 params 传入，返回即是接口的请求结果。 */
            result = module.call("GetFederationToken", params);
            JSONObject json_result = new JSONObject(result);
            System.out.println(json_result);
        } catch (Exception e) {
            System.out.println("error..." + e.getMessage());
        }
    }
}
```

成功的话，可以拿到包含密钥的 JSON 文本：

```
{"code":0,"message":"","codeDesc":"Success","data":{"credentials":{"sessionToken":"2a0c0ead3e6b8eed9608899eb74f2458812208ab30001","tmpSecretId":"AKIDBSrMaeFD0ZAECKuBzohnjAhJ53XNCE2F","tmpSecretKey":"UC7YjMrIlcuFgoWGwnrHwsMBrQrpUwYI"},"expiredTime":1526288317}}
```


