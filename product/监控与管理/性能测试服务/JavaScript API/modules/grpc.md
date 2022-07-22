## 目录

### Interfaces（接口）
- [DialOption](https://cloud.tencent.com/document/product/1484/75816)
- [Info](https://cloud.tencent.com/document/product/1484/75817)
- [InvokeOption](https://cloud.tencent.com/document/product/1484/75818)
- [Response](https://cloud.tencent.com/document/product/1484/75819)

### Variables（变量）
- [default](#default)

## Variables（变量）

[](id:default)
## 目录

### Interfaces（接口）
- [Item](https://cloud.tencent.com/document/product/1484/75805)

### Variables（变量）
- [default](#default)

## Variables（变量）
[](id:default)
### default
**default**:  { add: any; forEach: any; get: any; random: any }
```
Defined in typings/dataset.d.ts:17
```


#### Type declaration

- ##### add:function

  - add(filename: *string*, values: *Record*<*string*, *any*>[]): *void*

```
Defined in typings/dataset.d.ts:54
```

增加一行参数文件。

    ```
    import dataset from 'pts/dataset';
    
    export function setup () {
        dataset.add("user", [
                {"id": 1, "name": "zhangsan", "age": 1},
                {"id": 2, "name": "lisi", "age": 2}
            ]
        )
    };
    ```

#### Parameters

  - ##### filename: *string*

      文件名。

   - ##### values: *Record*<*string*, *any*>[]

      文件数据。

    #### Returns *void*

- ##### forEach:function

  - forEach(fileName: *string*, callback: ((item: [Item](https://cloud.tencent.com/document/product/1484/75805), i?: *number*) => *void*)): *void*

  - Defined in typings/dataset.d.ts:95

    遍历 csv 文件，支持修改和删除。

    ```js
    import dataset from 'pts/dataset';
    
    export function setup() {
        dataset.forEach("test.csv", (item) => {
            item.data.key5 = "555";
            if (item.data.key1 === "1") {
                item.delete();
            }
            console.log(JSON.stringify(item.data));
        });
    }
    ```

    #### Parameters

    - ##### fileName: *string*

      文件名

    - ##### callback: ((item: [Item](https://cloud.tencent.com/document/product/1484/75805), i?: *number*) => *void*)

      回调函数

      - - (item: [Item](https://cloud.tencent.com/document/product/1484/75805), i?: *number*): *void*

        - #### Parameters

          - ##### item: [Item](https://cloud.tencent.com/document/product/1484/75805)

          - ##### Optional i: *number*

          #### Returns *void*

    #### Returns *void*

- ##### get:function

  - get(key: *string*): *string*

  - Defined in typings/dataset.d.ts:73

    获取 csv 文件的列数据。

    ```
    import http from 'pts/http';
    import dataset from 'pts/dataset';
    
    export default function () {
        const value = dataset.get('key1');
        console.log('key1 => '+value)
        const postResponse = http.post('http://httpbin.org/post', JSON.stringify({data:value}));
    };
    ```

#### Parameters

 - ##### key: *string*

   列名

#### Returns *string*

  数据

- ##### random:function

  - random(filename: *string*): *Record*<*string*, *any*>

  - Defined in typings/dataset.d.ts:34

    随机获取参数文件一行。

    ```js
    import dataset from 'pts/dataset';
    
    export default function () {
        const record = dataset.random('test.csv');
        console.log(JSON.stringify(record)); // {"key1":"1","key2":"2","key3":"3","key4":"4"}
        console.log(record.key1); // 1 
    };
    ```

#### Parameters

 - ##### filename: *string*

      文件名。

#### Returns *Record*<*string*, *any*>

  一行数据。
