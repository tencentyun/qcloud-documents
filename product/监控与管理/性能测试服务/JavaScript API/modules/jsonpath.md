## 目录

### Variables（变量）
- [default](#default)

## Variables（变量）

[](id:default)
### Const default

default: { delete: *any*; get: *any*; set: *any* }

```
Defined in typings/jsonpath.d.ts:5
```


#### Type declaration

- ##### delete:function

- delete(json: *string*, path: *string*): *string*

```
Defined in typings/jsonpath.d.ts:120
```

从 json 字符串中删除值。

 ```js
  import jsonpath from 'pts/jsonpath';
    
  export default function () {
    // Delete a value:
   console.log(jsonpath.delete(`{"name":{"first":"Sara","last":"Anderson"}}`, 'name.first'));
   // {"name":{"last":"Anderson"}}
    
   // Delete an array value:
   console.log(jsonpath.delete(`{"friends":["Andy","Carol"]}`, 'friends.1'));
   // {"friends":["Andy"]}
    
   // Delete the last array value:
   console.log(jsonpath.delete(`{"friends":["Andy","Carol"]}`, 'friends.-1'));
   // {"friends":["Andy"]}
    };
    ```

#### Parameters

    
 - ##### json: *string*

      json 字符串

 - ##### path: *string*

      取值路径

#### Returns *string*

 Json 字符串

- ##### get:function

  - get(json: *string*, path: *string*): *string* | *number* | *boolean* | *object*


```
 Defined in typings/jsonpath.d.ts:49
```

 从 Json 字符串中取值。
    ```js
    import jsonpath from 'pts/jsonpath';
    
    export default function () {
        const json = JSON.stringify({
            "name": {"first": "Tom", "last": "Anderson"},
            "age": 37,
            "children": ["Sara", "Alex", "Jack"],
            "fav.movie": "Deer Hunter",
            "friends": [
                {"first": "Dale", "last": "Murphy", "age": 44, "nets": ["ig", "fb", "tw"]},
                {"first": "Roger", "last": "Craig", "age": 68, "nets": ["fb", "tw"]},
                {"first": "Jane", "last": "Murphy", "age": 47, "nets": ["ig", "tw"]}
            ]
        });
    
        console.log(jsonpath.get(json, 'name.last')); // Anderson
        console.log(jsonpath.get(json, 'age')); // 37
        console.log(jsonpath.get(json, 'children')); // Sara,Alex,Jack
        console.log(jsonpath.get(json, 'children.#')); // 3
        console.log(jsonpath.get(json, 'children.1')); // Alex
        console.log(jsonpath.get(json, 'child*.2')); // Jack
        console.log(jsonpath.get(json, 'c?ildren.0')); // Sara
        console.log(jsonpath.get(json, 'fav\\.movie')); // Deer Hunter
        console.log(jsonpath.get(json, 'friends.#.first')); // Dale,Roger,Jane
        console.log(jsonpath.get(json, 'friends.1.last')); // Craig
    
        console.log(jsonpath.get(json, 'friends.#(last=="Murphy").first')); // Dale
        console.log(jsonpath.get(json, 'friends.#(last=="Murphy")#.first')); // Dale,Jane
        console.log(jsonpath.get(json, 'friends.#(age>45)#.last')); // Craig,Murphy
        console.log(jsonpath.get(json, 'friends.#(first%"D*").last')); // Murphy
        console.log(jsonpath.get(json, 'friends.#(first!%"D*").last')); // Craig
        console.log(jsonpath.get(json, 'friends.#(nets.#(=="fb"))#.first')); // Dale,Roger
    };
    ```

#### Parameters

  - ##### json: *string*

      json 字符串

  - ##### path: *string*

      取值路径

#### Returns *string* | *number* | *boolean* | *object*

 取值数据

- ##### set:function

- set(json: *string*, path: *string*, value: *string* | *number* | *boolean* | *object*): *string*

```
Defined in typings/jsonpath.d.ts:93
```

修改 Json 字符串。

   ```
    import jsonpath from 'pts/jsonpath';
    
    export default function () {
        // Set a value from empty document:
        console.log(jsonpath.set('', 'name', 'Tom'));
        // {"name":"Tom"}
    
        // Set a nested value from empty document:
        console.log(jsonpath.set('', 'name.last', 'Anderson'));
        // {"name":{"last":"Anderson"}}
    
        // Set a new value:
        console.log(jsonpath.set(`{"name":{"last":"Anderson"}}`, 'name.first', 'Sara'));
        // {"name":{"last":"Anderson","first":"Sara"}}
    
        // Update an existing value:
        console.log(jsonpath.set(`{"name":{"last":"Anderson"}}`, 'name.last', 'Smith'));
        // {"name":{"last":"Smith"}}
    
        // Set a new array value:
        console.log(jsonpath.set(`{"friends":["Andy","Carol"]}`, 'friends.2', 'Sara'));
        // {"friends":["Andy","Carol","Sara"]}
    
        // Append an array value by using the -1 key in a path:
        console.log(jsonpath.set(`{"friends":["Andy","Carol"]}`, 'friends.-1', 'Sara'));
        // {"friends":["Andy","Carol","Sara"]}
    
        // Append an array value that is past the end:
        console.log(jsonpath.set(`{"friends":["Andy","Carol"]}`, 'friends.4', 'Sara'));
        // {"friends":["Andy","Carol",null,null,"Sara"]}
    };
    ```

#### Parameters

- ##### json: *string*

  Json 字符串

 - ##### path: *string*

      修改路径

 - ##### value: *string* | *number* | *boolean* | *object*

      修改值

#### Returns *string*

  Json 字符串

