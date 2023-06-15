腾讯云微搭低代码通过开放接口来满足第三方服务的定制化开发需求。

## 开放功能

| 产品功能 | 说明 | 接口文档 |
|---------|---------|---------|
| 数据模型 | 通过开放接口对数据模型进行新增、删除、更新、查询操作 | [查看](https://cloud.tencent.com/document/product/1301/70983) |

## 接口使用

### 域名
```html
https://<环境ID>.ap-shanghai.tcb-api.tencentcloudapi.com
```


<dx-alert infotype="explain" title="">
环境 ID 可前往 [资源管理](https://console.cloud.tencent.com/lowcode/resource/index) 页面获取。
</dx-alert>

### 操作步骤

1. 前往 [腾讯云控制台](https://console.cloud.tencent.com/cam/capi) 申请 SecretId + SecretKey。
2. 使用 OAuth 2.0 鉴权方式换取 Access Token。
3. 使用 Access Token 请求开放接口并在 Request Header 中加入 `Authorization: Bearer <Access Token>`。

### 请求说明
- API 的所有接口均通过 HTTPS 进行通信，均使用 UTF-8 编码。
- 支持的 HTTP 请求方法：POST、GET、PATCH、DELETE。
- Content-Type 类型：`application/json;utf-8`。

### 参数说明
接口包含三种参数类型：
- **uri：**位于请求路由，形如 `GET /weda/odata/v1/pre/data_xxxx`。
- **queryString：**位于 `?` 后，形如 `GET /weda/odata/v1/pre/data_xxxx?$filter=name eq '张三'`。
- **body：**位于 POST 请求体，以标准 `json` 传入，形如 `POST /weda/odata/v1/pre/data_xxxx { "name": "张三" }`。

### 代码示例
<dx-tabs>
:::NodeJS
```js
const Koa = require('koa');
const fetch = require('node-fetch');
const app = new Koa();

const EnvId = ''; // 环境 ID，例如 lowcode-2gay8jgh25
const SecretId = '';
const SecretKey = '';

// 域名
const domain = `https://${EnvId}.ap-shanghai.tcb-api.tencentcloudapi.com`;

app.use(async ctx => {
    // 换取 AccessToken
    const tokenResponse = await fetch(`${domain}/auth/v1/token/clientCredential`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Basic ${Buffer.from(`${SecretId}:${SecretKey}`).toString('base64')}`
        },
        body: JSON.stringify({
            grant_type: 'client_credentials',
        })
    });

    const { access_token } = await tokenResponse.json();

    // 请求某个服务端 API
    const queryResponse = await fetch(`${domain}/weda/odata/v1/prod/sys_user`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${access_token}`
        }
    });

    ctx.body = await queryResponse.json();
});

app.listen(3000);
```
:::
::: Java
```java
package com.example.odata;

import org.apache.http.HttpEntity;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpDelete;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.springframework.util.Base64Utils;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.HashMap;
import java.util.Map;

public class OpenApiClient {
    // 获取 token
    private String getToken(String envId, String secretId, String secretKey) {
        String host = "https://" + envId + ".ap-shanghai.tcb-api.tencentcloudapi.com";
        String url = host + "/auth/v1/token/clientCredential";
        HttpPost httpPost = new HttpPost(url);
        String basicKey = secretId + ":" + secretKey;
        String authorizationKey = "Basic " + Base64Utils.encodeToString(basicKey.getBytes());
        httpPost.addHeader("Authorization",authorizationKey);
        httpPost.addHeader("Content-Type","application/json");
        Map<String, String> body = new HashMap<>();
        body.put("grant_type","client_credentials");
        ObjectMapper mapper = new ObjectMapper();
        try {
            String bodyStr = mapper.writeValueAsString(body);
            StringEntity requestBody = new StringEntity(bodyStr, "UTF-8");
            httpPost.setEntity(requestBody);
        } catch (Exception e) {
            System.out.println(e.toString());
            return "";
        }
        ResponseHandler<String> responseHandler = response -> {
            int status = response.getStatusLine().getStatusCode();
            if (status >= 200 && status < 300) {
                HttpEntity entity = response.getEntity();
                return entity != null ? EntityUtils.toString(entity) : null;
            } else {
                throw new ClientProtocolException("Unexpected response status: " + status + EntityUtils.toString(response.getEntity()));
            }
        };
        try  {
            CloseableHttpClient httpClient = HttpClients.createDefault();
            String responseBody = httpClient.execute(httpPost, responseHandler);
            Map<String, Object> responseMap = mapper.readValue(responseBody, Map.class);
            /*
            {
              "token_type": "Bearer",
              "access_token": "",
              "expires_in": 111,// 过期时间,单位为 s
            }
             */
            return "Bearer " + responseMap.get("access_token").toString();
        } catch (Exception e) {
            System.out.println(e.toString());
        }
        return "";
    }

    // GET: 获取数据源记录列表
    private void GET(String token, String envId, String envType, String datasourceName) {
        String host = "https://" + envId + ".ap-shanghai.tcb-api.tencentcloudapi.com";
        String url = host + "/weda/odata/v1/" + envType + "/" + datasourceName;
        HttpGet httpGet = new HttpGet(url);
        httpGet.addHeader("Authorization", token);
        httpGet.addHeader("Content-Type", "application/json");
        ResponseHandler<String> responseHandler = response -> {
            int status = response.getStatusLine().getStatusCode();
            if (status >= 200 && status < 300) {
                HttpEntity entity = response.getEntity();
                return entity != null ? EntityUtils.toString(entity) : null;
            } else {
                throw new ClientProtocolException("Unexpected response status: " + status + EntityUtils.toString(response.getEntity()));
            }
        };
        try  {
            CloseableHttpClient httpClient = HttpClients.createDefault();
            String responseBody = httpClient.execute(httpGet, responseHandler);
            ObjectMapper mapper = new ObjectMapper();
            Map<String, Object> responseMap = mapper.readValue(responseBody, Map.class);
            // 打印 body
            System.out.println(responseMap.toString());
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }

    // GET: 获取数据源记录详情
    private void GET(String token, String envId, String envType, String datasourceName, String recordId) {
        String host = "https://" + envId + ".ap-shanghai.tcb-api.tencentcloudapi.com";
        String url = host + "/weda/odata/v1/" + envType + "/" + datasourceName + "('" + recordId + "')";
        HttpGet httpGet = new HttpGet(url);
        httpGet.addHeader("Authorization", token);
        httpGet.addHeader("Content-Type", "application/json");
        ResponseHandler<String> responseHandler = response -> {
            int status = response.getStatusLine().getStatusCode();
            if (status >= 200 && status < 300) {
                HttpEntity entity = response.getEntity();
                return entity != null ? EntityUtils.toString(entity) : null;
            } else {
                throw new ClientProtocolException("Unexpected response status: " + status + EntityUtils.toString(response.getEntity()));
            }
        };
        try  {
            CloseableHttpClient httpClient = HttpClients.createDefault();
            String responseBody = httpClient.execute(httpGet, responseHandler);
            ObjectMapper mapper = new ObjectMapper();
            Map<String, Object> responseMap = mapper.readValue(responseBody, Map.class);
            // 打印 body
            System.out.println(responseMap.toString());
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }

    // POST: 创建记录
    private void POST(String token, String envId, String envType, String datasourceName, Map<String, Object> jsonBody) {
        String host = "https://" + envId + ".ap-shanghai.tcb-api.tencentcloudapi.com";
        String url = host + "/weda/odata/v1/" + envType + "/" + datasourceName;
        HttpPost httpPost = new HttpPost(url);
        ObjectMapper mapper = new ObjectMapper();
        try {
            String bodyStr = mapper.writeValueAsString(jsonBody);
            StringEntity requestBody = new StringEntity(bodyStr, "UTF-8");
            httpPost.setEntity(requestBody);
        } catch (Exception e) {
            System.out.println(e.toString());
            return;
        }
        httpPost.addHeader("Authorization", token);
        httpPost.addHeader("Content-Type", "application/json");
        ResponseHandler<String> responseHandler = response -> {
            int status = response.getStatusLine().getStatusCode();
            if (status >= 200 && status < 300) {
                HttpEntity entity = response.getEntity();
                return entity != null ? EntityUtils.toString(entity) : null;
            } else {
                throw new ClientProtocolException("Unexpected response status: " + status + EntityUtils.toString(response.getEntity()));
            }
        };
        try  {
            CloseableHttpClient httpClient = HttpClients.createDefault();
            String responseBody = httpClient.execute(httpPost, responseHandler);
            Map<String, Object> responseMap = mapper.readValue(responseBody, Map.class);
            // 打印 body
            System.out.println("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" + responseMap.toString());
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }

    // PUT: 更新记录
    private void PUT(String token, String envId, String envType, String datasourceName, String recordId, Map<String, Object> jsonBody) {
        String host = "https://" + envId + ".ap-shanghai.tcb-api.tencentcloudapi.com";
        String url = host + "/weda/odata/v1/" + envType + "/" + datasourceName + "('" + recordId + "')";;
        HttpPost httpPost = new HttpPost(url);
        ObjectMapper mapper = new ObjectMapper();
        try {
            String bodyStr = mapper.writeValueAsString(jsonBody);
            StringEntity requestBody = new StringEntity(bodyStr, "UTF-8");
            httpPost.setEntity(requestBody);
        } catch (Exception e) {
            System.out.println(e.toString());
            return;
        }
        httpPost.addHeader("Authorization", token);
        httpPost.addHeader("Content-Type", "application/json");
        ResponseHandler<String> responseHandler = response -> {
            int status = response.getStatusLine().getStatusCode();
            if (status >= 200 && status < 300) {
                HttpEntity entity = response.getEntity();
                return entity != null ? EntityUtils.toString(entity) : null;
            } else {
                throw new ClientProtocolException("Unexpected response status: " + status + EntityUtils.toString(response.getEntity()));
            }
        };
        try  {
            CloseableHttpClient httpClient = HttpClients.createDefault();
            String responseBody = httpClient.execute(httpPost, responseHandler);
            Map<String, Object> responseMap = mapper.readValue(responseBody, Map.class);
            // 打印 body
            System.out.println(responseMap.toString());
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }

    // DELETE: 删除记录
    private void DELETE(String token, String envId, String envType, String datasourceName, String recordId) {
        String host = "https://" + envId + ".ap-shanghai.tcb-api.tencentcloudapi.com";
        String url = host + "/weda/odata/v1/" + envType + "/" + datasourceName + "('" + recordId + "')";
        HttpDelete httpDelete = new HttpDelete(url);
        httpDelete.addHeader("Authorization", token);
        httpDelete.addHeader("Content-Type", "application/json");
        ResponseHandler<String> responseHandler = response -> {
            int status = response.getStatusLine().getStatusCode();
            if (status >= 200 && status < 300) {
                HttpEntity entity = response.getEntity();
                return entity != null ? EntityUtils.toString(entity) : null;
            } else {
                throw new ClientProtocolException("Unexpected response status: " + status + EntityUtils.toString(response.getEntity()));
            }
        };
        try  {
            CloseableHttpClient httpClient = HttpClients.createDefault();
            httpClient.execute(httpDelete, responseHandler);
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }

    public static void main(String[] args) {
        OpenApiClient openApiClient = new OpenApiClient();
        // 真实环境 ID
        String envId = "";
        String secretId = "";
        String secretKey = "";
        // 数据模型标识
        String datasourceName = "";
        // 数据模型类型
        String envType = "pre";
        String token = openApiClient.getToken(envId, secretId, secretKey);

        // 创建记录
        Map<String, Object> postBody = new HashMap<>();
        postBody.put("name", "zhangsan");
        postBody.put("age", 12);

        /*
        // 创建记录
        openApiClient.POST(token, envId, envType, datasourceName, postBody);

        //删除记录
        openApiClient.DELETE(token, envId, envType, datasourceName, "");
        //查看
        openApiClient.GET(token, envId, envType, datasourceName, "");

        //查看记录
        openApiClient.GET(token, envId, envType, datasourceName);
        */
    }
}
```
:::
</dx-tabs>


## 快速体验：使用 Postman 调用开放接口
1. 打开 Postman 工具，添加一个 GET 请求。进入 **Authorization** 页面完成相应配置。
>!Access Token URL 参数设置，需要在域名后添加 `/auth/v1/token/clientCredential`。示例：`https://lowcode-8g171waac4be77f6.ap-shanghai.tcb-api.tencentcloudapi.com/auth/v1/token/clientCredential`。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/3d826dc2e851bbdb91bdc114ccc03b07.png" />
2. 进入 **headers** 页面，设置相应参数即可。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/4936c09f61d694d4ba18875705e9199d.png" />

