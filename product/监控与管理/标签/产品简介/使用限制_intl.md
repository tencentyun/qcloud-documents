## Limits on Tag Keys
- A tag key starting with "qcs:" or "project" is a system reserved tag key and cannot be created.

- A tag key can only contain characters encoded in UTF-8, spaces, numbers, or special characters including `+, -, =, ., _, :, /, @`.

- A tag key should be a combination of at most 127 characters encoded in UTF-8. 

- A tag key is case sensitive.

## Limits on Tag Values
- A tag value can only contain characters encoded in UTF-8, spaces, numbers, or special characters including `+, -, =, ., _, :, /, @`.

- A tag value should be a combination of at most 255 characters encoded in UTF-8.

- A tag value is case sensitive.

## Limits on the Number of Tags
- Resource dimension: A resource has at most 50 different keys. 

- Tag dimension:
 - A user has at most 1,000 different keys.
 - A key has at most 1,000 values. 

