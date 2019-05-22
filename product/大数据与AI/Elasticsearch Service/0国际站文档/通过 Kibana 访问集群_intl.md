Tencent Cloud ES contains a Kibana module. You can access Kibana for a cluster over the public network to carry out various operations on data, such as visualization, query, analytics and management. You can get started with Kibana using this tutorial.

## 1. Accessing Kibana

### 1.1 Entry
You can access Kibana through the following two entry points, which can be found on Cluster List and Cluster Details pages respectively as shown below. Clicking the entry point will be redirected to the Kibana login page.
![Entry on list page](https://main.qcloudimg.com/raw/49ac415dda4184125677f3d04f84cfe3.png)
![Entry on details page](https://main.qcloudimg.com/raw/4c31ad620af4977f92ee1e28cbda48db.png)

### 1.2 Login
To access Kibana, you need to log in with the account name "elastic" and the password which was set when you created the cluster. If you forget your password, you can reset it on the cluster details page.
For security reasons, you can configure blacklist and whitelist of IPs to control the access to Kibana. For details, see [here](https://cloud.tencent.com/document/product/845/16992).
![Login](https://main.qcloudimg.com/raw/b59fc765c4d0d050f6c53d5b060f4bd2.png)

### 1.3 Access
After logging into Kibana for the first time, you will be prompted to configure an index if the cluster has not yet stored user-defined index data. Refer to the Adding and Accessing Indexes section below for details.
![Initialization page](https://main.qcloudimg.com/raw/0edfec77af83c8cbc65afe3c7a545ad0.png)

## 2. Adding and Accessing Indexes (Storing Data) 
Click **Dev Tools** on the left pane of Kibana to enter the development tools page, where you can send various operation requests to the cluster via the console. Next, we will demonstrate how to manipulate clusters and store data through the console using a data storage example of city information.

### 2.1 Adding an index

#### Define mappings for the index

Define an index name "china", a type name "city", and detailed fields and their types. "location" is type geo_point, which can represent geographic location; "level" is an object type, which contains secondary fields. For field type descriptions, see [here](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/mapping-types.html).
![Define mappings for an index](https://main.qcloudimg.com/raw/82f3de324cc82b3673f0438afe6ddcb9.png)
```
PUT china
{
  "mappings": {
    "city": {
      "properties":{
        "name":{ "type": "keyword"  }, 
        "province":{ "type": "keyword"  }, 
        "location": {"type": "geo_point"},
        "x":{ "type": "integer" },
        "level":{
            "properties":{                
                "level":{ "type": "integer" },
                "range":{ "type": "integer" },
                "name":{ "type": "keyword" }
            }
        },
        "y":{ "type": "integer" },
        "cityNo":{ "type": "integer" } 
      }
    }
  }
}
```

#### Add a single document

![Save a single piece of data](https://main.qcloudimg.com/raw/1ca53899fe58347c285665d71160289b.png)
```
PUT china/city/wuhan 
{"name":"Wuhan","province":"No. 188 Yanjiang Road, Jiang'an District, Hubei Province","location":{"lat":30.5952548577,"lon":114.2999398195},"x":6384,"level":{"level":2,"range":19,"name":"new first-tier city"},"y":4231,"cityNo":7}
```

Query a single document:
```
GET /china/city/wuhan
```

#### Add multiple documents:

```
POST _bulk
{ "index" : { "_index": "china", "_type" : "city", "_id" : "beijing" } }
{"name":"Beijing","province":"Beijing","location":{"lat":39.9031324643,"lon":116.4010433787},"x":6763,"level":{"range":4,"level":1,"name":"first-tier city"},"y":6381,"cityNo":1}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "shanghai" } }
{"name":"Shanghai","province":"Shanghai","location":{"lat":31.2319526784,"lon":121.469443249},"x":7779,"level":{"range":4,"level":1,"name":"first-tier city"},"y":4409,"cityNo":2}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "guangzhou" } }
{"name":"Guangzhou","province":"No 79, Jixiang Road, Yuexiu District, Guangdong Province","location":{"lat":23.1317146641,"lon":113.2595185241},"x":6173,"level":{"range":4,"level":1,"name":"first-tier city"},"y":2560,"cityNo":3}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "shenzhen" } }
{"name":"Shenzhen","province":"No 37, Xinyuan Road, Futian District, Guangdong Province","location":{"lat":22.5455465546,"lon":114.0527779134},"x":6336,"level":{"range":4,"level":1,"name":"first-tier city "},"y":2429,"cityNo":4}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "chengdu" } }
{"name":"Chengdu","province":"No 88-1, 4th Section of Hongxing Road, Jinjiang District, Sichuan Province","location":{"lat":30.6522796787,"lon":104.0725574128},"x":4387,"level":{"level":2,"range":19,"name":"new first-tier city"},"y":4304,"cityNo":5}
{ "index" : { "_index": "china", "_type" : "city", "_id" : "hangzhou" } }
{"name":"Hangzhou","province":"No 316, Huancheng North Road, Gongshu District, Zhejiang Province","location":{"lat":30.2753694112,"lon":120.1509063337},"x":7530,"level":{"level":2,"range":19,"name":"new first-tier city"},"y":4182,"cityNo":6}
```

Query multiple documents:
```
GET /china/city/_search
```

### 2.2 Accessing an index

#### Configure Kibana for index access

Before you can use Kibana, you need to configure at least one index that can be matched. Enter the index "china" created above and click **Create**.
![Configure index access](https://main.qcloudimg.com/raw/5210fa2ce137edaaed20bf459d8dc3f7.png)
View the fields for the index:
![View index fields](https://main.qcloudimg.com/raw/0158dab743148ead2f1abcfaf7ce507b.png)
Click **Discover** to view the documents added under the index:
![Access details](https://main.qcloudimg.com/raw/d0f8b710d44d411f8938fd56c4f08c57.png)

## 3. Visualizing Query and Analysis

Kibana can be used to visualize statistical analysis of data. Click **Visualize** on the left pane to configure various charts for data analysis.
For example, to count the different levels under the index "china" described above.
![Select a pie chart](https://main.qcloudimg.com/raw/a3a51ce39e7c659e8193b0f4f6400c01.png)
![Select an index](https://main.qcloudimg.com/raw/809c96ac06c47620d2240d75a7cba2dd.png)
Configure the metric "count" to aggregate grouped data by the field "level.level".
![Configure a statistics method](https://main.qcloudimg.com/raw/393599fb4ab811b92149e162b365e52f.png)



For more usage about Kibana, see [Kibana official documentation](https://www.elastic.co/guide/en/kibana/5.6/getting-started.html).



