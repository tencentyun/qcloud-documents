
## Variables（变量）

[](id:default)
### Const default

default: { delete: *any*; get: *any*; set: *any* }


#### Type declaration

- ##### get:function

 - delete(json: *string*, path: *string*): *string*
从 json 字符串中取值。

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
    console.log(jsonpath.get(json, 'children[*]')); // Sara,Alex,Jack
    console.log(jsonpath.get(json, 'children.[0]')); // Sara
    console.log(jsonpath.get(json, 'children[1:2]')); // Alex,Jack
    console.log(jsonpath.get(json, 'friends[:].first')); // Dale,Roger,Jane
    console.log(jsonpath.get(json, 'friends[1].last')); // Craig
    console.log(jsonpath.get(json, 'friends[?(@.age > 45)].last')); // Craig,Murphy
    console.log(jsonpath.get(json, 'friends[?(@.first =~ /D.*e/)].last')); // Murphy
};
    ```
**Parameters**  
 - ##### json: *string*
      json 字符串

 - ##### path: *string | number | boolean | object*
  取值路径

