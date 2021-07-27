## 操作场景

本文以 provider-demo 和 consumer-demo 两个工程为例为你介绍 TSF 应用配置 http2 的操作方法。

## 前提条件

- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [下载 TSF Demo 工程](https://github.com/tencentyun/tsf-simple-demo)（springboot 版本2.0+，tomcat 版本8.5+）

>?
>- 推荐使用 1.29.0-Finchley-RELEASE。
>- 本文 springboot-2.0.9.RELEASE 和 tomcat-8.5.56 为例。

## 操作步骤

### 步骤1. 制作 SSL 证书

通过 JDK 自带的 keytool 执行以下命令：
```
keytool -genkey -alias tomcat -keyalg RSA -keystore ./keystore.jks -storepass 123456
```

执行成功后当前目录下会生成 keystore.jks 证书文件。

![](https://main.qcloudimg.com/raw/a78ceb180f5beeeefceaf5cc8f7f145d.png)

### 步骤2. 改造 provider-demo 工程

1. 复制 jks 证书文件到 provider-demo 工程的 resources 目录下。
   ![](https://main.qcloudimg.com/raw/66eab4a26d592ac445f7811ef3180c51.png)

2. 修改 spring 配置文件，在bootstrap.yaml 文件中增加如下配置。
   ![](https://main.qcloudimg.com/raw/3388d561b13a8608f59867002d271d15.png)
   ```
   server.http2.enabled=true
   server.ssl.key-store=classpath:keystore.jks
   server.ssl.key-store-password: 123456
   ```

3. 启动 provider-demo，浏览器访问 `https://127.0.0.1:18081/echo/1`。

   Chrome 可能会提示“您的连接不是私密连接”。

   ![](https://main.qcloudimg.com/raw/d07ba3c8235b2e44b3b44f574c1dc6f2.png)

   只需单击任意空白处，键入“thisisunsafe”即可。

   ![](https://main.qcloudimg.com/raw/39f3092e0a5aca02c677d1823ac4a5a8.png)

   打开 Console，Protocol 的值为 h2 表示配置成功。

   ![](https://main.qcloudimg.com/raw/db41e627bddf59714f0a2a9b24a0cd10.png)

参考资料：

- Spring 配置 http2 文档：[howto-configure-http2](https://docs.spring.io/spring-boot/docs/2.0.9.RELEASE/reference/html/howto-embedded-web-servers.html#howto-configure-http2)
- Tomcat 版本差异文档：[whichversion](https://tomcat.apache.org/whichversion.html)


4. 开启 http 访问端口（可选）。

   由于此时只能通过 https 方式访问，可加入 Tomcat 配置开放新端口来支持 http 访问。

   1. 在启动类中增加 Bean。

      ![](https://main.qcloudimg.com/raw/fe830bb9b76e9f720f550b2deb36d537.png)
			
	<dx-codeblock>
:::  java
package com.tsf.demo.provider;
      
      import org.apache.catalina.connector.Connector;
      import org.springframework.beans.factory.annotation.Value;
      import org.springframework.boot.SpringApplication;
      import org.springframework.boot.autoconfigure.SpringBootApplication;
      import org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory;
      import org.springframework.boot.web.servlet.server.ServletWebServerFactory;
      import org.springframework.cloud.openfeign.EnableFeignClients;
      import org.springframework.context.annotation.Bean;
      import org.springframework.tsf.annotation.EnableTsf;
      
      @SpringBootApplication
      @EnableFeignClients // 使用Feign微服务调用时请启用
      @EnableTsf
      public class ProviderApplication {
      
          @Value("${http.port}")
          private Integer port;
      
          /**
           * Tomcat增加支持http访问
           **/
          @Bean
          public ServletWebServerFactory servletContainer() {
              TomcatServletWebServerFactory tomcat = new TomcatServletWebServerFactory();
              Connector connector = new Connector(TomcatServletWebServerFactory.DEFAULT_PROTOCOL);
      //        connector.setSecure(false);
      //        connector.setScheme("http");
              connector.setPort(port);
              tomcat.addAdditionalTomcatConnectors(connector);
              return tomcat;
          }
      
          public static void main(String[] args) {
              SpringApplication.run(ProviderApplication.class, args);
          }
      }
:::
</dx-codeblock>


   2. 在 Bootstrap.yml 配置文件中增加自定义配置。

      ![](https://main.qcloudimg.com/raw/2b20dc9d883f60b20d54e7a678790ffc.png)

      ```yaml
      http.port=18082
      ```

   3. 重启 provider-demo，浏览器访问 `http://127.0.0.1:18082/echo/1`。

      ![](https://main.qcloudimg.com/raw/83e3dbc87c97a7a352649bcd353bdcab.png)

      此时 provider-demo 完成支持 https 和 http（通过不同端口访问），其中 https 访问时使用 http2 协议。

      参考资料：Spring 配置 Tomcat 代码示例：[SampleTomcatTwoConnectorsApplication.java](https://github.com/spring-projects/spring-boot/blob/2.0.x/spring-boot-samples/spring-boot-sample-tomcat-multi-connectors/src/main/java/sample/tomcat/multiconnector/SampleTomcatTwoConnectorsApplication.java)。

### 步骤3. 改造 consumer-demo 工程

1. proxy 中的 @FeignClient 注解需指定 https 方式访问。

   ![](https://main.qcloudimg.com/raw/4554291f032b27e8ee24f4df9053cf3e.png)

   ```
   @FeignClient(name = "https://provider-demo")
   ```

2. RestTemplate 同理。

   ![](https://main.qcloudimg.com/raw/eaf4814c2decf8498b94c0c93639a4e2.png)

   ```
   restTemplate.getForObject("https://provider-demo/echo/" + str, String.class);
   ```

3. 通过注入不同的 bean 选择是否使用SSL证书认证（以下步骤二选一）：
<dx-tabs>
::: 使用\sSSL\s证书认证访问方式
1. 复制 jks 证书文件到 consumer-demo 工程的 resources 目录。

2. spring 配置文件中增加自定义配置。

![](https://main.qcloudimg.com/raw/2b4dc0ff2bdf0450c9b15dfda813219f.png)

```
test-ssl-config.key-store=classpath:keystore.jks
test-ssl-config.key-store-password: 123456
```

   3. 修改 bean（restTemplate、feignClient）

      ![](https://main.qcloudimg.com/raw/b0040bbe54b7d424024390cc7226e31f.png)

      ```java
      package com.tsf.demo.consumer;
      
      import feign.Client;
      import org.apache.http.conn.ssl.NoopHostnameVerifier;
      import org.apache.http.conn.ssl.SSLConnectionSocketFactory;
      import org.apache.http.conn.ssl.TrustSelfSignedStrategy;
      import org.apache.http.impl.client.CloseableHttpClient;
      import org.apache.http.impl.client.HttpClients;
      import org.apache.http.ssl.SSLContexts;
      import org.springframework.beans.factory.annotation.Value;
      import org.springframework.boot.SpringApplication;
      import org.springframework.boot.autoconfigure.SpringBootApplication;
      import org.springframework.cloud.client.loadbalancer.LoadBalanced;
      import org.springframework.cloud.netflix.ribbon.SpringClientFactory;
      import org.springframework.cloud.openfeign.EnableFeignClients;
      import org.springframework.cloud.openfeign.ribbon.CachingSpringLoadBalancerFactory;
      import org.springframework.cloud.openfeign.ribbon.LoadBalancerFeignClient;
      import org.springframework.context.annotation.Bean;
      import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
      import org.springframework.tsf.annotation.EnableTsf;
      import org.springframework.util.ResourceUtils;
      import org.springframework.web.client.AsyncRestTemplate;
      import org.springframework.web.client.RestTemplate;
      
      import javax.net.ssl.*;
      import java.io.FileInputStream;
      import java.io.IOException;
      import java.io.InputStream;
      import java.security.*;
      import java.security.cert.CertificateException;
      
      @SpringBootApplication
      @EnableFeignClients // 使用Feign微服务调用时请启用
      @EnableTsf
      public class ConsumerApplication {
      
          @Value("${test-ssl-config.key-store}")
          private String file;
          @Value("${test-ssl-config.key-store-password}")
          private String password;
      
          @LoadBalanced
          @Bean
          public RestTemplate restTemplate() {
              SSLConnectionSocketFactory csf = new SSLConnectionSocketFactory(getSSLSocket(file, password),
                      new String[]{"TLSv1"},
                      null,
                      NoopHostnameVerifier.INSTANCE);
              CloseableHttpClient httpClient = HttpClients.custom()
                      .setSSLSocketFactory(csf)
                      .build();
              HttpComponentsClientHttpRequestFactory requestFactory = new HttpComponentsClientHttpRequestFactory();
              requestFactory.setHttpClient(httpClient);
              return new RestTemplate(requestFactory);
          }
      
          @Bean
          public Client feignClient(CachingSpringLoadBalancerFactory cachingFactory, SpringClientFactory clientFactory) {
              return new LoadBalancerFeignClient(
                  new Client.Default(getSSLSocket(file, password).getSocketFactory(), (hostname, session) -> true), cachingFactory, clientFactory
              );
          }
      
          public static SSLContext getSSLSocket(String file, String password) {
              SSLContext sslContext = null;
              try {
                  KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
                  InputStream keyStoreInput = new FileInputStream(ResourceUtils.getFile(file));
                  keyStore.load(keyStoreInput, password.toCharArray());
          
                  KeyStore trustStore = KeyStore.getInstance(KeyStore.getDefaultType());
                  InputStream trustStoreInput = new FileInputStream(ResourceUtils.getFile(file));
                  trustStore.load(trustStoreInput, null);
                  sslContext = SSLContexts.custom().loadKeyMaterial(keyStore, password.toCharArray())
                          .loadTrustMaterial(trustStore, new TrustSelfSignedStrategy()).build();
              } catch (NoSuchAlgorithmException | KeyManagementException | KeyStoreException | CertificateException | IOException | UnrecoverableKeyException e) {
                  e.printStackTrace();
              }
              return sslContext;
          }
      
          @LoadBalanced
          @Bean
          public AsyncRestTemplate asyncRestTemplate() {
              return new AsyncRestTemplate();
          }
      
          public static void main(String[] args) {
              SpringApplication.run(ConsumerApplication.class, args);
          }
      }
      ```

:::
::: 忽略\sSSL\s认证方式
只需要修改 bean（restTemplate、feignClient）

![](https://main.qcloudimg.com/raw/38fea9d1e171a179c0d3970a4170bdfc.png)

![](https://main.qcloudimg.com/raw/06d8f50f8eb461e6c7795071f5a04c9e.png)



<dx-alert infotype="explain" title="">
与第一种方式的差异在 getSSLSocket() 方法。
</dx-alert>


<dx-codeblock>
:::  java
```java
package com.tsf.demo.consumer;

import feign.Client;
import org.apache.http.conn.ssl.NoopHostnameVerifier;
import org.apache.http.conn.ssl.SSLConnectionSocketFactory;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.cloud.netflix.ribbon.SpringClientFactory;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.cloud.openfeign.ribbon.CachingSpringLoadBalancerFactory;
import org.springframework.cloud.openfeign.ribbon.LoadBalancerFeignClient;
import org.springframework.context.annotation.Bean;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.tsf.annotation.EnableTsf;
import org.springframework.web.client.AsyncRestTemplate;
import org.springframework.web.client.RestTemplate;

import javax.net.ssl.*;
import java.security.*;
import java.security.cert.X509Certificate;

@SpringBootApplication
@EnableFeignClients // 使用Feign微服务调用时请启用
@EnableTsf
public class ConsumerApplication {

		@LoadBalanced
		@Bean
		public RestTemplate restTemplate() {
				SSLConnectionSocketFactory csf = new SSLConnectionSocketFactory(getSSLSocket(),
								new String[]{"TLSv1"},
								null,
								NoopHostnameVerifier.INSTANCE);
				CloseableHttpClient httpClient = HttpClients.custom()
								.setSSLSocketFactory(csf)
								.build();
				HttpComponentsClientHttpRequestFactory requestFactory = new HttpComponentsClientHttpRequestFactory();
				requestFactory.setHttpClient(httpClient);
				return new RestTemplate(requestFactory);
		}

		@Bean
		public Client feignClient(CachingSpringLoadBalancerFactory cachingFactory, SpringClientFactory clientFactory) {
				return new LoadBalancerFeignClient(
						new Client.Default(getSSLSocket().getSocketFactory(), (hostname, session) -> true), cachingFactory, clientFactory
				);
		}

		public static SSLContext getSSLSocket() {
				SSLContext sslContext = null;
				try {
						sslContext = SSLContext.getInstance("TLS");
						X509TrustManager tm = new X509TrustManager() {
								@Override
								public void checkClientTrusted(X509Certificate[] chain, String authType) {}

								@Override
								public void checkServerTrusted(X509Certificate[] chain, String authType) {}

								@Override
								public X509Certificate[] getAcceptedIssuers() {
										return null;
								}
						};
						sslContext.init(null, new TrustManager[]{tm}, null);
				} catch (NoSuchAlgorithmException | KeyManagementException e) {
						e.printStackTrace();
				}
				return sslContext;
		}

		@LoadBalanced
		@Bean
		public AsyncRestTemplate asyncRestTemplate() {
				return new AsyncRestTemplate();
		}

		public static void main(String[] args) {
				SpringApplication.run(ConsumerApplication.class, args);
		}
}
```
:::
</dx-codeblock>



:::
</dx-tabs>




4. 验证结果。

   启动 consumer-demo，浏览器访问 `http://127.0.0.1:18083/echo-feign/123`。

   ![](https://main.qcloudimg.com/raw/9d99349686a686cbb1bf1202356bc318.png)

   浏览器访问 `http://127.0.0.1:18083/echo-rest/123`。

   ![](https://main.qcloudimg.com/raw/4242479b5f87c0399e0c60ec866b67f2.png)

