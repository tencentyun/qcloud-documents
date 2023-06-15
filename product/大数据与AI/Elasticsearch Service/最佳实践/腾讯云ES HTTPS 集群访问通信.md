Elasticsearch 提供了多种数据访问安全的方式，如用户名密码校验、api_key 等。但是依然无法保障数据传输过程中的安全性问题。而 HTTPS 协议，则是一种以安全为目的的 HTTP 通道，在 HTTP 的基础上通过传输加密和身份认证等机制来保障数据传输过程中的安全性。本文将基于腾讯云 ES 集群环境，演示 Beats、Logstash、Kibana 和 Java Client 等客户端访问连接开启了 HTTPS 协议的 ES 集群。
## HTTPS 集群环境准备
### 创建 HTTPS 协议集群
首先我们在腾讯云 ES 控制台创建出一个 HTTPS 集群，在购买页这里勾选上 HTTPS 协议。目前该特性目前是通过白名单支持，可提 [工单](https://console.cloud.tencent.com/workorder/category) 申请开放。
![](https://qcloudimg.tencent-cloud.cn/raw/e5990ecfed55152d21e4bee5bba1d64c.png)
其中，ES 集群是通过在 elasticsearch.yml 配置文件中设置如下参数来开启 HTTPS 协议的：
```
xpack.security.http.ssl.enabled: true
xpack.security.http.ssl.keystore.path: certs/ces-certificates.p12
xpack.security.http.ssl.truststore.path: certs/ces-certificates.p12
```

### 获取 pem 证书文件
集群创建成功后，可在 [ES 控制台](https://console.cloud.tencent.com/es) 访问控制页面，进行相关证书导出。此时腾讯云 ES 侧会提供如下两个证书文件：

|文件名称|用途|
|:-------------- |:-------------|
|client-certificates.pem |用于 Beats Logstash、Java Client 连接 ES 集群
|server-certificates.pem	|用于 Kibana 连接 ES 集群

下面将详细介绍 Beats、Logstash、Kibana 和 Java 等客户端连接 HTTPS 集群的配置方式。

## Beats 输出到 HTTPS 集群
### CVM Metriceat 输出到 ES
我们首先在腾讯云 [CVM 控制台](https://console.cloud.tencent.com/cvm/overview) 创建一个和 ES 集群同 VPC 下的 CVM，创建好后，将得到的 pem 鉴权文件上传到该 CVM 上，这里的存放路径为：/usr/local/service/https-certs。随后到腾讯云 [ES 控制台](https://console.cloud.tencent.com/es) 的 Beats 管理页，创建一个 Metricbeat：
![](https://qcloudimg.tencent-cloud.cn/raw/c39bb651b68b7a4cede8f47d3f43f1c9.png)
其中，最核心的步骤是在 metricbeat.yml 配置文件中进行如下配置。
```
output.elasticsearch: 
    hosts: ["https://ES-VIP:9200"]
    username: "elastic"
    password: "changeme"
    ssl.certificate_authorities: ["/usr/local/service/https-certs/client-certificates.pem"]
    ssl.verification_mode: certificate
```
配置信息说明：

|配置项|说明|
|:-------------- |:-------------|
|hosts | ES 集群的 VIP，如 `https://10.0.X.29:9200`，以 https 开头|
| username/password | ES 集群的用户名密码
| ssl.certificate_authorities	| 连接 HTTPS 集群所需的 pem 鉴权证书文件路径
| ssl.verification_mode | 服务器证书认证模式，有四种模式，分别是 full，strict，certificate 和 none。我们这里以 certificate 模式进行认证，即只认证 CA 证书，不认证主机名信息。详情可参考官方文档。|

配置完成后，即可在 ES 集群中看到自动创建了一个 metricbeat-7.14.20-*开头的索引，到此 CVM 中 Metricbeat 连接 HTTPS 的 ES 集群配置完成。
![](https://qcloudimg.tencent-cloud.cn/raw/61033f2fd59562e5df8c926b79a49f3f.png)

### TKE Filebeat 日志采集器输出到 ES
TKE Filebeat 日志采集器输出到 HTTPS 的 ES 集群流程和 CVM的metricBeat 输出一样，首先我们将 pem 文件上传到创建 TKE 集群时自动创建的 Worker 所在的 CVM 节点上，如/var/log/https-certs目录下。 
![](https://qcloudimg.tencent-cloud.cn/raw/1389090a5675dd61723346464fdd6891.png)
client-certificates.pem 文件存放位置：
![](https://qcloudimg.tencent-cloud.cn/raw/f8f5526a6e269e92b0b5ba4f6969e6f3.png)
随后我们在腾讯云 ES 控制台新建 Fliebeat 采集器，这里选择 TKE 日志采集：
![](https://qcloudimg.tencent-cloud.cn/raw/6cb4c508be66db71a42fec061d98579b.png)
下面进行 Filebeat 采集器的基本信息配置，如版本号选择，采集器输出 ES 集群选择，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9f086204188a196627a68efc5f4710a2.png)
![](https://qcloudimg.tencent-cloud.cn/raw/428768d6b92e54c48566225067570097.png)
创建好 Filebeat TKE 容器日志采集器后，随后我们在 TKE 集群的详情页，找到配置管理中的 ConfigMap，然后找到对应 beats的config 文件：
![](https://qcloudimg.tencent-cloud.cn/raw/5d0152f2865826f0e1ce3273ef41d127.png)
单击**编辑 yaml**后对 output.elasticsearch 配置项进行修改，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8b998aad769650725282896ae72d9dd6.png)
具体配置信息如下：
```
output.elasticsearch:
      hosts: ['https://ES-VIP:9200']
      username: "elastic"
      ssl.certificate_authorities: ["/var/log/https-certs/client-certificates.pem"]
      ssl.verification_mode: "certificate"
      password: "changeme"
      indices:
        - index: "filebeat-tke-%{+yyyy.MM.dd}"
          when.equals:
            tke_collector_target_name: "logs_to_https_es"
```
然后在 TKE 集群中的工作负载中，找到 DaemonSet，然后再到对应 beats 的 DaemonSet，点击进去，对它的 pod 进行销毁重建。
![](https://qcloudimg.tencent-cloud.cn/raw/a70f21cd43b8b2fef11f75b6d896a51a.png)
进入到 Pod 管理页，选择对应的 Pod 销毁重建。
![](https://qcloudimg.tencent-cloud.cn/raw/4cb2373b4196c83b189651ba38e82fac.png)
销毁重建后，Pod 的运行状态变成 Running，如下图所示。  
>! 如果多次对 pod 进行销毁重建，仍是红色 Running，有可能是 beats 的 yml 配置出现问题，可以在日志里面查看具体问题，或者重新检查一下 yml 配置是否错误。
>
![](https://qcloudimg.tencent-cloud.cn/raw/71396727cf1565cc4668dbec85b87f93.png)
随后我们到 ES 集群中，可以看到自动创建了以 filebeat-tke-*开头的索引。表明 TKE 日志顺利输出到 HTTPS 集群中了。
![](https://qcloudimg.tencent-cloud.cn/raw/66fa51122925ba51b9d348f0cf8065e2.png)

## Logstash 输出到 HTTPS 集群
腾讯云 Logstash 是一款全托管的产品，因此我们首先需要在腾讯云 Logstash 控制台将 pem 文件以扩展文件方式进行上传，如下图所示。
![](https://qcloudimg.tencent-cloud.cn/raw/2210de98487927d222e9da576d8afb79.png)
随后我们新建一个管道，在管道的 Config 配置编辑框里配置上 ES 的连接信息和证书路径。
![](https://qcloudimg.tencent-cloud.cn/raw/44b8b8be84b1516d6216b1738e142587.png)
管道详细配置文本信息如下：
```
output {
    elasticsearch {
        hosts => ["https://ES-VIP:9200"]
        user => "elastic"
        password => "changeme"
        ssl => true
        cacert => "/usr/local/service/logstash/extended-files/client-certificates.pem"
        ssl_certificate_verification => false
    }
}
```
其中 cacert 即可我们上一步上传的扩展文件 pem 的路径，固定路径为：`/usr/local/service/logstash/extended-files/client-certificates.pem`。
点击保存并部署管道后，就会在管道列表里可以看到我们刚刚新建出来的管道信息了，此时状态为运行中。
![](https://qcloudimg.tencent-cloud.cn/raw/209b0a43d8738c4ad511cd9f54300bed.png)
这时候我们再到 HTTPS 集群中就可以看到有数据从 input 的集群中写入进来了。

## Kibana 连接 HTTPS 集群
腾讯云 ES 集群默认自带 Kibana 访问能力，因此一般情况下，客户是不需要对 Kibana 进行任何配置的。这里介绍自建 Kibana 连接 HTTPS 集群的配置方式。和 Beats、Logstash 等使用的客户端鉴权证书不一样，Kibana 使用的是 server-certificates.pem，腾讯云 ES 侧生成证书命令如下：
```
openssl pkcs12 -in ces-certificates.p12 -password pass:xxxxxx -nokeys -cacerts -out server-certificates.pem
```
由于前面我们已经拿到了 pem 证书文件。因此，我们将 server-certificates.pem 文件拷贝到 Kibana 所在节点的如下路径：`/usr/local/service/https-certs`。然后修改 kibana.yml 配置文件如下：
```
elasticsearch.hosts: ["https://ES-VIP:9200"]
elasticsearch.username: "elastic"
elasticsearch.password: "changeme"
elasticsearch.ssl.verificationMode: certificate
elasticsearch.ssl.certificateAuthorities: ["/usr/local/service/https-certs/server-certificates.pem"]
xpack.encryptedSavedObjects.encryptionKey: "dfed624ca4014135f61804440536xxxx"
xpack.fleet.registryUrl: "https://epr.elastic.co"
```
配置项说明：
- elasticsearch.ssl.certificateAuthorities： pem 文件的存放路径。
- elasticsearch.ssl.verificationMode： 证书鉴权模式，certificate 采用只鉴权 CA 证书，不鉴权主机名称的模式。
- xpack.fleet.registryUrl： （非必选配置）Fleet 集成模块需要访问的公网仓库，这里需要 Kibana 节点具备公网访问能力。
- xpack.encryptedSavedObjects.encryptionKey： value 可以通过 `bin/kibana-encryption-keys generate` 命令获得。
![](https://qcloudimg.tencent-cloud.cn/raw/0280e59cea613ea4a41fbe38e8c1ace1.png)
重新启动 Kibana 后即可正常访问 HTTPS 的 ES 集群了。

## Java Client 连接 HTTPS 集群
本文档演示在 Spring 项目中访问 HTTPS 集群的配置方式，首先需要添加如下 maven 依赖：
```
        <dependency>
			<groupId>org.elasticsearch.client</groupId>
			<artifactId>elasticsearch-rest-client</artifactId>
			<version>7.10.1</version>
		</dependency>
		<dependency>
			<groupId>org.elasticsearch.client</groupId>
			<artifactId>elasticsearch-rest-high-level-client</artifactId>
			<version>7.10.1</version>
		</dependency>
		<dependency>
			<groupId>org.elasticsearch</groupId>
			<artifactId>elasticsearch</artifactId>
			<version>7.10.1</version>
		</dependency>
```
随后我们在ElasticsearchConfig自定义类中实现对Elasticsearch连接的配置。
```
@Configuration
public class ElasticsearchConfig {
    @Value("${es.username}")
    private String userName;
    @Value("${es.password}")
    private String password;
    @Value("${es.scheme}")
    private String scheme;
    @Value("${es.domain}")
    private String domain;
    @Value("${es.https.cert}")
    private String certFile;
    @Value("${es.port}")
    private int port;
    private RestHighLevelClient client;
    @Bean
    public RestHighLevelClient EsConnectInit() throws CertificateException, IOException, KeyStoreException, NoSuchAlgorithmException, KeyManagementException {
        final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
        credentialsProvider.setCredentials(AuthScope.ANY,new UsernamePasswordCredentials(userName,password));
        RestClientBuilder builder;
        if (scheme.equals("https")) {
            Path caCertificatePath = Paths.get(certFile);
            System.out.println(certFile);
            CertificateFactory factory = CertificateFactory.getInstance("X.509");
            Certificate trustedCa;
            try(InputStream is = Files.newInputStream(caCertificatePath)) {
                trustedCa = factory.generateCertificate(is);
            }
            KeyStore trustStore = KeyStore.getInstance("pkcs12");
            trustStore.load(null,null);
            trustStore.setCertificateEntry("ca",trustedCa);
            SSLContextBuilder sslContextBuilder = SSLContexts.custom().loadTrustMaterial(trustStore, new TrustStrategy() {
                @Override
                public boolean isTrusted(X509Certificate[] x509Certificates, String s) throws CertificateException {
                    return true;
                }
            });
            final SSLContext sslContext = sslContextBuilder.build();
            final HostnameVerifier hostnameVerifier = new HostnameVerifier() {
                public boolean verify(String hostname, SSLSession session) {
                    return true;
                }
            };
            builder = RestClient.builder(new HttpHost(domain, port, scheme)).setRequestConfigCallback(new RestClientBuilder.RequestConfigCallback() {
                @Override
                public RequestConfig.Builder customizeRequestConfig(RequestConfig.Builder requestConfigBuilder) {
                    requestConfigBuilder.setConnectTimeout(-1);
                    requestConfigBuilder.setSocketTimeout(-1);
                    requestConfigBuilder.setConnectionRequestTimeout(-1);
                    return requestConfigBuilder;
                }
            }).setHttpClientConfigCallback(new RestClientBuilder.HttpClientConfigCallback() {
                @Override
                public HttpAsyncClientBuilder customizeHttpClient(HttpAsyncClientBuilder httpClientBuilder) {
                    httpClientBuilder.disableAuthCaching();
                    httpClientBuilder.setSSLHostnameVerifier(hostnameVerifier);
                    return httpClientBuilder.setSSLContext(sslContext)
                            .setDefaultCredentialsProvider(credentialsProvider);

                }
            });
        } else {
             builder = RestClient.builder(new HttpHost(domain, port, scheme))
                    .setRequestConfigCallback(new RestClientBuilder.RequestConfigCallback() {
                        @Override
                        public RequestConfig.Builder customizeRequestConfig(RequestConfig.Builder requestConfigBuilder) {
                        requestConfigBuilder.setConnectTimeout(-1);
                            requestConfigBuilder.setSocketTimeout(-1);
                            requestConfigBuilder.setConnectionRequestTimeout(-1);
                            return requestConfigBuilder;
                        }
                    }).setHttpClientConfigCallback(new RestClientBuilder.HttpClientConfigCallback() {
                        @Override
                        public HttpAsyncClientBuilder customizeHttpClient(HttpAsyncClientBuilder httpClientBuilder) {                            httpClientBuilder.disableAuthCaching();
                            return httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider);
                        }
                    });
        }
        client = new RestHighLevelClient(builder);
        return client;
    }
}
```
其中 Elasticsearch 的配置信息如下：
```
es.scheme=https
es.port=9200
es.domain=9.10.1.X  #es vip
es.username=elastic
es.password=changeme
es.https.cert=/usr/local/services/certs/client-certificates.pem
```
通过如上配置后，即可在 Spring 项目中成功连接上开启了 HTTPS 协议的 ES 集群了。
