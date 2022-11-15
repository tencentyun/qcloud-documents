
## Interfaces（接口）
- [BatchOption](https://cloud.tencent.com/document/product/1484/75820)
- [BatchResponse](https://cloud.tencent.com/document/product/1484/75821)
- [File](https://cloud.tencent.com/document/product/1484/75822)
- [Request](https://cloud.tencent.com/document/product/1484/75823)
- [Response](https://cloud.tencent.com/document/product/1484/75819)

## Variables（变量）


### Const default

default: { FormData: (new () => { append: *any*; body: *any*; contentType: *any* }); batch: *any*; delete: *any*; do: *any*; file: *any*; get: *any*; head: *any*; patch: *any*; post: *any*; put: *any* }


#### Type declaration

- ##### FormData: (new () => { append: *any*; body: *any*; contentType: *any* })

 - new (): { append: *any*; body: *any*; contentType: *any* }
   - 构造 form-data 类型请求体。
  ```js
 import http from 'pts/http';
      
 const data = open('./sample/tmp.js');
      
 export default function () {
 const formData = new http.FormData();
      formData.append('text', 'text');
      formData.append('file', http.file(data, 'tmp.js'));
      const resp = http.post('http://httpbin.org/post', formData.body(), {
      headers: {'Content-Type': formData.contentType()}
     });
 console.log('formData: ', resp.body);
};
```

 Returns { append: *any*; body: *any*; contentType: *any* }

- #### append:function

 - append(key: *string*, value: *string* | [File](https://cloud.tencent.com/document/product/1484/75822): *void*

 **Parameters**

 - ##### key: *string*
键

 - ##### value: *string* | [File](https://cloud.tencent.com/document/product/1484/75822)
值

 Returns *void*
 
- #### body:function
  - body(): *ArrayBuffer*
  
 Returns *ArrayBuffer*
请求体内容

- #### contentType:function
    - contentType(): *string*
 
 Returns *string*
内容类型

- #### batch:function
 - batch(requests: [Request](https://cloud.tencent.com/document/product/1484/75823)[], opt?: [BatchOption](https://cloud.tencent.com/document/product/1484/75820)): [BatchResponse](https://cloud.tencent.com/document/product/1484/75819)[]
 批量发起 http 请求。
```js
 import http from 'pts/http';
    
 export default function () {
 let responses = http.batch([
    {
         method: "GET",
         url: "http://httpbin.org/get?a=1",
         headers: {a: "1, 2, 3"},
         params: {b: 2}
            },
            {
                method: "GET",
                url: "http://httpbin.org/get?a=1",
                headers: {a: "1, 2, 3"},
                params: {b: 2}
            }
        ])
  console.log(JSON.stringify(responses))
    };
```
**Parameters**
   - ##### requests: [Request](https://cloud.tencent.com/document/product/1484/75823)[]

      请求对象数组

   - ##### Optional opt: [BatchOption](https://cloud.tencent.com/document/product/1484/75820)

   Returns [BatchResponse](https://cloud.tencent.com/document/product/1484/75821)[]
  响应对象数组

- #### delete:function

 - delete(url: *string*, request?: [Request](https://cloud.tencent.com/document/product/1484/75823)): [Response](https://cloud.tencent.com/document/product/1484/75819)
发送 DELETE 请求。
```js
 import http from 'pts/http';
    
 export default function () {
 const data = {user_id: '12345'};
   const resp = http.delete('http://httpbin.org/delete', {query: data});
  console.log(resp.json().args.user_id); // 12345
    };
```
**Parameters**
   - ##### url: *string*
 URL

- #### Optional request: [Request](https://cloud.tencent.com/document/product/1484/75823)
可选。请求对象

 Returns [Response](https://cloud.tencent.com/document/product/1484/75819)

    响应对象

- ##### do:function

  - do(request: [Request](https://cloud.tencent.com/document/product/1484/75823)): [Response](https://cloud.tencent.com/document/product/1484/75819)
  发起 http 请求。
    ```js
    import http from 'pts/http';
    
    export default function () {
        const req = {
            method: 'post',
            url: 'http://httpbin.org/post',
            headers: {'Content-Type': 'application/json'},
            body: {user_id: '12345'}
        };
        const resp = http.do(req);
        console.log(resp.json().json.user_id); // 12345
    };
    ```
 **Parameters**

    - ##### request: [Request](https://cloud.tencent.com/document/product/1484/75823)
 请求对象

   Returns [Response](https://cloud.tencent.com/document/product/1484/75819)
	响应对象

- #### file:function

  - file(data: *string* | *ArrayBuffer*, name?: *string*, contentType?: *string*): [File](https://cloud.tencent.com/document/product/1484/75822)
 构造 FormData 上传文件对象。
    ```js
    import http from 'pts/http';
    
    const data = open('./sample/tmp.js')
    
    export default function () {
        const file = http.file(data);
        console.log(file.data.length); // 231
        console.log(file.name); // 1635403323707745000
        console.log(file.contentType); // application/octet-stream
    };
```
 **Parameters**

   - ##### data: *string* | *ArrayBuffer*

      文件内容
   - ##### Optional name: *string*

      文件名，默认为纳秒级时间戳

   - ##### Optional contentType: *string*

      内容类型，默认为 application/octet-stream

    Returns [File](https://cloud.tencent.com/document/product/1484/75822)

    文件对象

- #### get:function

  - get(url: *string*, request?: [Request](https://cloud.tencent.com/document/product/1484/75823)): [Response](https://cloud.tencent.com/document/product/1484/75819)
发送 GET 请求。
    ```js
    import http from 'pts/http';
    
    export default function () {
        const data = {user_id: '12345'};
        const resp = http.get('http://httpbin.org/get', {query: data});
        console.log(resp.json().args.user_id); // 12345
    };
	```
**Parameters**

   - ##### url: *string*

      URL

    - ##### Optional request: [Request](https://cloud.tencent.com/document/product/1484/75823)

      可选。请求对象 Request

   Returns [Response](https://cloud.tencent.com/document/product/1484/75819)
 响应对象

- #### head:function

  - head(url: *string*, request?: [Request](https://cloud.tencent.com/document/product/1484/75823)): [Response](https://cloud.tencent.com/document/product/1484/75819)
 发送 HEAD 请求。
    ```js
    import http from 'pts/http';
    
    export default function () {
        const data = {user_id: '12345'};
        const resp = http.head('http://httpbin.org/get', {query: data});
        console.log(resp.statusCode); // 200
    };
    ```
**Parameters**

   - ##### url: *string*

      URL

   - ##### Optional request: [Request](https://cloud.tencent.com/document/product/1484/75823)

      可选。请求对象 Request

   Returns [Response](https://cloud.tencent.com/document/product/1484/75819)
   响应对象

- #### patch:function

  - patch(url: *string*, body: *string*, request?: [Request](https://cloud.tencent.com/document/product/1484/75823)): [Response](https://cloud.tencent.com/document/product/1484/75819)
 发送 PATCH 请求。
    ```js
    import http from 'pts/http';
    
    export default function () {
        const data = {user_id: '12345'};
        const headers = {'Content-Type': 'application/json'};
        const resp = http.patch('http://httpbin.org/patch', data, {headers: headers});
        console.log(resp.json().json.user_id); // 12345
    };
    ```
**Parameters**

    - ##### url: *string*

      URL

    - ##### body: *string*

      请求体

    - ##### Optional request: [Request](https://cloud.tencent.com/document/product/1484/75823)

      可选。请求对象

   Returns [Response](https://cloud.tencent.com/document/product/1484/75819)
  响应对象

- ##### post:function

  - post(url: *string*, body: *string* | *object* | *ArrayBuffer*, request?: [Request](https://cloud.tencent.com/document/product/1484/75823)): [Response](https://cloud.tencent.com/document/product/1484/75819)
发送 POST 请求。
 ```js
 import http from 'pts/http';
    
 export default function () {
     const data = {user_id: '12345'};
     const headers = {'Content-Type': 'application/json'};
     const resp = http.post('http://httpbin.org/post', data, {headers: headers});
     console.log(resp.json().json.user_id); // 12345
    };
	```
 **Parameters**

   - ##### url: *string*

      URL

    - ##### body: *string* | *object* | *ArrayBuffer*

      请求体

    - ##### Optional request: [Request](https://cloud.tencent.com/document/product/1484/75823)

      可选。请求对象

  Returns [Response](https://cloud.tencent.com/document/product/1484/75819)
   响应对象

- #### put:function

  - put(url: *string*, body: *string*, request?: [Request](https://cloud.tencent.com/document/product/1484/75823)): [Response](https://cloud.tencent.com/document/product/1484/75819)
发送 PUT 请求。
 ```js
    import http from 'pts/http';
    
    export default function () {
        const data = {data: 'some data'};
        const headers = {'Content-Type': 'application/json'};
        const resp = http.put('http://httpbin.org/put', data, {headers: headers});
        console.log(resp.json().json.data); // some data
    };
```
 **Parameters**

    - ##### url: *string*

      URL

    - ##### body: *string*

      请求体

    - ##### Optional request: [Request](https://cloud.tencent.com/document/product/1484/75823)

      可选。请求对象

  Returns [Response](https://cloud.tencent.com/document/product/1484/75819)
  响应对象
