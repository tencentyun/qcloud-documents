## 基本结构

生命周期配置使用 XML 描述方法，其可以配置一条或多条生命周期规则，基本结构如下：

```xml
<LifecycleConfiguration>
	<Rule>
		<ID>**your lifecycle name**</ID>
        <Status>Enabled</Status>
        <Filter>
            <And>
            	<Prefix>projectA/</Prefix>
                <Tag>
                	<Key>key1</Key>
                    <Value>value1</Value>
                </Tag>
            </And>
        </Filter>
        **transition/expiration actions**
	</Rule>
	<Rule>
		...
	</Rule>
</LifecycleConfiguration>
```

其中每一条规则包含如下内容：

- ID（可选）：可自定义的描述规则的内容。
- Status：可选择规则启用 Enabled 或禁用 Disabled 的状态。
- Filter：用于指定需要操作的对象的筛选条件。
- 操作：需要对符合以上描述的对象执行的操作。
- 时间：支持根据最后修改时间指定天数 Days，或指定某个具体的日期 Date 前修改的对象。

## 规则描述

### Filter 元素

#### 针对存储桶中的所有对象

指定空的筛选条件，将会应用于存储桶中的所有对象。

```xml
<LifecycleConfiguration>
    <Rule>
        <Filter>
        </Filter>
        <Status>Enabled</Status>
        **transition/expiration actions**
    </Rule>
</LifecycleConfiguration>
```

#### 针对指定的对象键前缀

指定对象前缀，可以对一部分符合前缀描述的对象组执行操作，例如设置以 logs/ 为前缀的所有对象。

```xml
<LifecycleConfiguration>
    <Rule>
        <Filter>
           <Prefix>logs/</Prefix>
        </Filter>
        <Status>Enabled</Status>
        **transition/expiration actions**
    </Rule>
</LifecycleConfiguration>
```

#### 针对指定的对象标签

指定某些符合对象标签的 key 和 value 为筛选条件，对特定标签的对象执行操作，例如设置标签的 key=type 和 value=image 为筛选条件的对象：
```xml
<LifecycleConfiguration>
    <Rule>
        <Filter>
           <Tag>
              <Key>type</Key>
              <Value>image</Value>
           </Tag>
        </Filter>
        <Status>Enabled</Status>
        **transition/expiration actions**
    </Rule>
</LifecycleConfiguration>
```

#### 合并使用多个筛选条件

腾讯云对象存储（Cloud Object Storage，COS）支持通过 AND 的逻辑来合并使用多个筛选条件，例如设置以 logs/ 为前缀，同时对象标签的 key=type 和 value=image 为筛选条件的对象：
```xml
<LifecycleConfiguration>
    <Rule>
        <Filter>
            <And>
            	<Prefix>logs/</Prefix>
                <Tag>
              		<Key>type</Key>
              		<Value>image</Value>
           	 </Tag>
            </And>
        </Filter>
        <Status>Enabled</Status>
        **transition/expiration actions**
    </Rule>
</LifecycleConfiguration>
```

### 操作元素

在生命周期规则中，可以对符合条件的一组对象执行一个或多个操作。

#### 转换操作

指定 Transition 操作可以使对象从一个存储类型转换到另一个存储类型，如果存储桶开启了版本控制，其只对当前版本执行操作。最短的 Transition 设置时间为0天。例如，设置30天后沉降至归档存储：

```xml
<Transition>
	<StorageClass>ARCHIVE</StorageClass>
    <Days>30</Days>
</Transition>
```

#### 过期删除

指定 Expiration 操作可以使符合规则的对象执行过期删除操作，如果存储桶从未启用过版本控制，则将永久删除对象。如果存储桶启用过版本控制，则将为过期的对象**添加一个 DeleteMarker 标记**，并将其设置为当前版本。例如，设置30天后删除对象：
```xml
<Expiration>
	<Days>30</Days>
</Expiration>
```

#### 未完成的分块上传


>! 不支持在同一条生命周期规则内同时设置指定对象标签和清理未完成上传的文件碎片。
>

指定 AbortIncompleteMultipartUpload 操作可以允许分块上传的指定 UploadId 任务在保持一段时间后删除，其不再提供续传或可被检索的特性。例如，设置7天后清除未完成的分块上传任务：
```xml
<AbortIncompleteMultipartUpload>
   <DaysAfterInitiation>7</DaysAfterInitiation>
</AbortIncompleteMultipartUpload>
```

#### 非当前版本的对象

在启用过版本控制的存储桶中，转换只会对最新版本执行，过期操作只会添加删除标记，因此 COS 对非当前版本的对象提供了如下操作：

指定 NoncurrentVersionTransition 可以将非当前版的对象在指定时间转换到另一个存储类型。例如，设置历史版本在30天后沉降至归档存储：

```xml
<NoncurrentVersionTransition>
	<StorageClass>ARCHIVE</StorageClass>
    <Days>30</Days>
</NoncurrentVersionTransition>
```

指定 NoncurrentVersionExpiration 可以将非当前版本的对象在指定时间内过期删除。例如，设置历史版本在30天后删除：
```xml
<NoncurrentVersionExpiration>
	<Days>30</Days>
</NoncurrentVersionExpiration>
```

指定 ExpiredObjectDeleteMarker 用于清理剩余的删除标记，可填入的值为 true 或 false，此选项的生效由清理过期的历史版本的动作（NoncurrentVersionExpiration）触发。开启了这一功能后，当生命周期删除对象的最后一个历史版本时，将自动清理剩余的多个删除标记。

具体情况如下，当清理过期的历史版本这个动作（NoncurrentVersionExpiration）生效时：
- 若剩余删除标记只有一个，无论是否开启 ExpiredObjectDeleteMarker，都会自动清理最后一个删除标记。
- 若剩余删除标记有多个，COS 会检查是否开启了 ExpiredObjectDeleteMarker。如果是 true，会自动清理剩余的多个删除标记；如果是 false，剩余的多个删除标记不会被清理。


```xml
<ExpiredObjectDeleteMarker>
	<Days>true|false</Days>
</ExpiredObjectDeleteMarker>
```

### 时间元素

#### 按天数计算

使用 Days 指定天数，是按照对象的最后修改时间来计算的。
- 例如，设置一个对象在0天后转换为归档存储类型，对象于2018-01-01 23:55:00 GMT+8上传，则其将于2018-01-02 00:00:00 GMT+8起进入转换存储类型的处理队列，最晚于2018-01-02 23:59:59 GMT+8前完成转换。
- 例如，设置一个对象在1天后过期删除，对象于2018-01-01 23:55:00 GMT+8上传，则其将于2018-01-03 00:00:00 GMT+8起进入过期删除的处理队列，最晚于2018-01-03 23:59:59 GMT+8前完成删除。

#### 按指定日期

使用 Date 指定日期，将会在到达特定日期时，对符合筛选条件的所有对象执行该操作。目前仅支持指定 GMT+8 时区，设置为0时的 ISO8601 格式的时间。
例如，2018年01月01日，描述为：2018-01-01T00:00:00+08:00。


