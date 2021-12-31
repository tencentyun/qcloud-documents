|操作|	语法	| 描述 |
|--|--|--|
|cat	| cat "path"	|将 Alluxio 中的一个文件内容打印在控制台中。
|checkConsistency|	checkConsistency "path"	|检查 Alluxio 与底层存储系统的元数据一致性。
|checksum |	checksum "path"	| 计算一个文件的 md5 校验码。
|chgrp	|chgrp "group" "path"	|修改 Alluxio 中的文件或文件夹的所属组。
|chmod	| chmod "permission" "path" |	修改 Alluxio 中文件或文件夹的访问权限。
|chown	| chown "owner" "path"	| 修改 Alluxio 中文件或文件夹的所有者。
|copyFromLocal	| copyFromLocal "source path""remote path" | "remote path" 将 "source path" 指定的本地文件系统中的文件拷贝到 Alluxio 中 "remote path" 指定的路径，如果 "remote path" 已经存在该命令会失败。
|copyToLocal|	copyToLocal "remote path" "local path" |	将 "remote path" 指定的 Alluxio 中的文件复制到本地文件系统中。
|count |	count "path"	|输出 "path" 中所有名称匹配一个给定前缀的文件及文件夹的总数。
|cp	| cp "src" "dst"|	在 Alluxio 文件系统中复制一个文件或目录。
|du	| du "path" |	输出一个指定的文件或文件夹的大小。
|fileInfo|	fileInfo "path" |	输出指定的文件的数据块信息。
|free	| free "path"|	将 Alluxio 中的文件或文件夹移除，如果该文件或文件夹存在于底层存储中，那么仍然可以在那访问。
|getCapacityBytes	|getCapacityBytes	|获取 Alluxio 文件系统的容量。
|getUsedBytes	|getUsedBytes|	获取 Alluxio 文件系统已使用的字节数。
|help	|help "cmd"	| 打印给定命令的帮助信息，如果没有给定命令，打印所有支持的命令的帮助信息。
|leader	| leader |	打印当前 Alluxio leader master 节点名。
|load	|load "path"	|将底层文件系统的文件或者目录加载到 Alluxio 中。
|loadMetadata	|loadMetadata "path"	| 将底层文件系统的文件或者目录的元数据加载到 Alluxio 中。
|location	|location "path" |	输出包含某个文件数据的节点。
|ls	| ls "path" |	列出给定路径下的所有直接文件和目录的信息，例如大小。
|masterInfo	| masterInfo	|打印 Alluxio master 容错相关的信息，例如，leader 的地址、所有 master 的地址列表以及配置的 Zookeeper 地址。
|mkdir	| mkdir "path1" ... "pathn" |	在给定路径下创建文件夹，以及需要的父文件夹，多个路径用空格或者 tab 分隔，如果其中的任何一个路径已经存在，该命令失败。
|mount	| mount "path" "uri"	| 将底层文件系统的 "uri" 路径挂载到 Alluxio 命名空间中的 "path" 路径下，"path" 路径事先不能存在并由该命令生成。没有任何数据或者元数据从底层文件系统加载。当挂载完成后，对该挂载路径下的操作会同时作用于底层文件系统的挂载点。
|mv	| mv "source" "destination"	| 将 "source" 指定的文件或文件夹移动到 "destination" 指定的新路径，如果 "destination" 已经存在该命令失败。
|persist |	persist "path1" ... "pathn" |	将仅存在于 Alluxio 中的文件或文件夹持久化到底层文件系统中。
|pin	| pin "path"	| 将给定文件锁定到内容中以防止剔除。如果是目录，递归作用于其子文件以及里面新创建的文件。
|report	| report "path"	| 向 master 报告一个文件已经丢失。
|rm	| rm "path"	| 删除一个文件，如果输入路径是一个目录该命令失败。
|setTtl	| setTtl "path" "time"	| 设置一个文件的 TTL 时间，单位毫秒。
|stat	| stat "path"	| 显示文件和目录指定路径的信息。
|tail	| tail "path"	| 将指定文件的最后1KB内容输出到控制台。
|test	| test "path"	| 测试路径的属性，如果属性正确，返回0，否则返回1。
|touch	| touch "path"	| 在指定路径创建一个空文件。
|unmount |	unmount "path"	| 卸载挂载在 Alluxio 中 "path" 指定路径上的底层文件路径，Alluxio 中该挂载点的所有对象都会被删除，但底层文件系统会将其保留。
|unpin	| unpin "path"	| 将一个文件解除锁定从而可以对其剔除，如果是目录则递归作用。
|unsetTtl	|unsetTtl "path"	| 删除文件的 ttl 值。

## cat
#### 背景
cat 命令将 Alluxio 中的一个文件内容全部打印在控制台中，这在用户确认一个文件的内容是否和预想的一致时非常有用。如果您想将文件拷贝到本地文件系统中，使用 copyToLocal 命令。

#### 操作示例 
例如，当测试一个新的计算任务时，cat 命令可以用来快速确认其输出结果。
```
$ ./bin/alluxio fs cat /output/part-00000
```

## checkConsistency
#### 背景
checkConsistency 命令会对比一给定路径下 Alluxio 以及底层存储系统的元数据，如果该路径是一个目录，那么其所有子内容都会被对比。该命令返回包含所有不一致的文件和目录的列表，系统管理员决定是否对这些不一致数据进行调整。为了防止 Alluxio 与底层存储系统的元数据不一致，应将您的系统设置为通过 Alluxio 来修改文件和目录，而不是直接访问底层存储系统进行修改。

如果使用了 -r 选项，那么 checkConsistency 命令会去修复不一致的文件或目录，对于只存在底层存储的文件或者文件夹会从 Alluxio 中删除，对于在底层文件系统中，但是，文件内容发生变化的文件，该文件的元数据会重新 load 到 Alluxio。

>!该命令需要请求将要被检查的目录子树的读锁，这意味着在该命令完成之前无法对该目录子树的文件或者目录进行写操作或者更新操作。

#### 操作示例
例如，checkConsistency 命令可以用来周期性地检查命名空间的完整性。

列出不一致的文件或者目录：
```
$ ./bin/alluxio fs checkConsistency /
```
修复不一致的文件或者目录：
```
$ ./bin/alluxio fs checkConsistency -r /
```

## checksum
#### 背景
checksum 命令输出某个 Alluxio 文件的 md5 值。

#### 操作示例
例如，checksum 可以用来验证 Alluxio 中的文件内容与存储在底层文件系统或者本地文件系统中的文件内容是否匹配。
```
$ ./bin/alluxio fs checksum /LICENSE
```

## chgrp
#### 背景
chgrp 命令可以改变 Alluxio 中的文件或文件夹的所属组，Alluxio 支持 POSIX 标准的文件权限，组在 POSIX 文件权限模型中是一个授权实体，文件所有者或者超级用户可以执行这条命令从而改变一个文件或文件夹的所属组。

加上 -R 选项可以递归的改变文件夹中子文件和子文件夹的所属组。

#### 操作示例
使用 chgrp 命令能够快速修改一个文件的所属组。
```
$ ./bin/alluxio fs chgrp alluxio-group-new /input/file1
```

## chmod
#### 背景
chmod 命令修改 Alluxio 中文件或文件夹的访问权限，目前可支持八进制模式：三位八进制的数字分别对应于文件所有者、所属组以及其他用户的权限。以下是数字与权限的对应表：

|Number	|Permission	| rwx |
|--|--|--|
|7	|read, write and execute	| rwx
|6	|read and write	| rw-
|5	|read and execute	|r-x
|4	|read only	|r--
|3	|write and execute	|-wx
|2	|write only	|-w-
|1	|execute only	|--x
|0	|none	|---

加上 -R 选项可以递归的改变文件夹中子文件和子文件夹的权限。

#### 操作示例
使用 chmod 命令可以快速修改一个文件的权限。
```
$ ./bin/alluxio fs chmod 755 /input/file1
```

## chown
#### 背景
chown 命令用于修改 Alluxio 中文件或文件夹的所有者，出于安全方面的考虑，只有超级用户能够更改一个文件的所有者。

加上 -R 选项可以递归的改变文件夹中子文件和子文件夹的所有者。

#### 使用示例
使用 chown 命令可以快速修改一个文件的所有者。
```
$ ./bin/alluxio fs chown alluxio-user /input/file1
```

## copyFromLocal
#### 背景
copyFromLocal 命令将本地文件系统中的文件拷贝到 Alluxio 中，如果您运行该命令的机器上有 Alluxio worker，那么数据便会存放在这个 worker 上，否则，数据将会随机地复制到一个运行 Alluxio worker 的远程节点上。如果该命令指定的目标是一个文件夹，那么这个文件夹及其所有内容都会被递归复制到 Alluxio 中。

#### 操作示例
使用 copyFromLocal 命令可以快速将数据复制到 alluxio 系统中以便后续处理。
```
$ ./bin/alluxio fs copyFromLocal /local/data /input
```

## copyToLocal
#### 背景
copyToLocal 命令将 Alluxio 中的文件复制到本地文件系统中，如果该命令指定的目标是一个文件夹，那么该文件夹及其所有内容都会被递归地复制。

#### 操作示例
使用 copyToLocal 命令可以快速将输出数据下载下来从而进行后续研究或调试。
```
$ ./bin/alluxio fs copyToLocal /output/part-00000 part-00000
```

## count
#### 背景
count 命令输出 Alluxio 中所有名称匹配一个给定前缀的文件及文件夹的总数，以及它们总的大小，该命令对文件夹中的内容递归处理。当用户对文件有预定义命名习惯时，count 命令很有用。

#### 操作示例
若文件是以它们的创建日期命名，使用 count 命令可以获取任何日期、月份以及年份的所有文件的数目以及它们的总大小。
```
$ ./bin/alluxio fs count /data/2014
```

## cp
#### 背景
cp 命令拷贝 Alluxio 文件系统中的一个文件或者目录，也可以在本地文件系统和 Alluxio 文件系统之间相互拷贝。filescheme 表示本地文件系统，alluxioscheme 或不写 scheme 表示 Alluxio 文件系统。如果使用了 -R 选项，并且源路径是一个目录，cp 将源路径下的整个子树拷贝到目标路径。

#### 操作示例
例如，cp 可以在底层文件系统之间拷贝文件。
```
$ ./bin/alluxio fs cp /hdfs/file1 /s3/
```

## du
#### 背景
du 命令输出一个文件的大小，如果指定的目标为文件夹，该命令输出该文件夹下所有子文件及子文件夹中内容的大小总和。

#### 操作示例
如果 Alluxio 空间被过分使用，使用 du 命令可以检测到哪些文件夹占用了大部分空间。
```
$ ./bin/alluxio fs du /\\*
```

## fileInfo
#### 背景
fileInfo 命令从1.5开始不再支持，请使用 stat 命令。fileInfo 命令将一个文件的主要信息输出到控制台，这主要是为了让用户调试他们的系统。一般来说，在 Web UI 上查看文件信息要容易理解得多。

#### 操作示例
使用 fileInfo 命令能够获取到一个文件的数据块的位置，这在获取计算任务中的数据局部性时非常有用。
```
$ ./bin/alluxio fs fileInfo /data/2015/logs-1.txt
```

## free
#### 背景
free 命令请求 Alluxio master 将一个文件的所有数据块从 Alluxio worker 中剔除，如果命令参数为一个文件夹，那么会递归作用于其子文件和子文件夹。该请求不保证会立即产生效果，因为该文件的数据块可能正在被读取。free 命令在被 master 接收后会立即返回。注意该命令不会删除底层文件系统中的任何数据，而只会影响存储在 Alluxio 中的数据。另外，该操作也不会影响元数据，这意味着如果运行 ls 命令，该文件仍然会被显示。

#### 操作示例
使用 free 命令可以手动管理 Alluxio 的数据缓存。
```
$ ./bin/alluxio fs free /unused/data
```

## getCapacityBytes
#### 背景
getCapacityBytes 命令返回 Alluxio 被配置的最大字节数容量。

#### 操作示例
使用 getCapacityBytes 命令能够确认您的系统是否正确启动。
```
$ ./bin/alluxio fs getCapacityBytes
```

## getUsedBytes
#### 背景
getUsedBytes 命令返回 Alluxio 中以及使用的空间字节数。

#### 操作示例
使用 getUsedBytes 命令能够监控集群健康状态。
```
$ ./bin/alluxio fs getUsedBytes
```

## leader
#### 背景
leader 命令打印当前 Alluxio 的 leader master 节点名。

#### 操作示例
```
$ ./bin/alluxio fs leader
```

## load
#### 背景
load 命令将底层文件系统中的数据载入到 Alluxio 中。如果运行该命令的机器上正在运行一个 Alluxio worker，那么数据将移动到该 worker 上，否则，数据会被随机移动到一个 worker 上。如果该文件已经存在在 Alluxio 中，该命令不进行任何操作。如果该命令的目标是一个文件夹，那么其子文件和子文件夹会被递归载入。

#### 操作示例
使用 load 命令能够获取用于数据分析作用的数据。
```
$ ./bin/alluxio fs load /data/today
```

## loadMetadata
#### 背景
loadMetadata 命令查询本地文件系统中匹配给定路径名的所有文件和文件夹，并在 Alluxio 中创建这些文件的镜像。该命令只创建元数据，例如文件名及文件大小，而不会传输数据。

#### 操作示例
当其他系统将数据输出到底层文件系统中（不经过 Alluxio），而在 Alluxio 上运行的某个应用又需要使用这些输出数据时，就可以使用 loadMetadata 命令。
```
$ ./bin/alluxio fs loadMetadata /hdfs/data/2015/logs-1.txt
```

## location
#### 背景
location 命令返回包含一个给定文件包含的数据块的所有 Alluxio worker 的地址。

#### 操作示例
当使用某个计算框架进行作业时，使用 location 命令可以调试数据局部性。
```
$ ./bin/alluxio fs location /data/2015/logs-1.txt
```

## ls
#### 背景
ls 命令列出一个文件夹下的所有子文件和子文件夹及文件大小、上次修改时间以及文件的内存状态。对一个文件使用 ls 命令仅仅会显示该文件的信息。ls 命令也将任意文件或者目录下的子目录的元数据从底层存储系统加载到 Alluxio 命名空间，如果 Alluxio 还没有这部分元数据的话。ls 命令查询底层文件系统中匹配给定路径的文件或者目录，然后会在 Alluxio 中创建一个该文件的镜像文件。只有元数据，例如文件名和大小，会以这种方式加载而不发生数据传输。

选项：
- -d 选项将目录作为普通文件列出。例如，`ls -d /`显示根目录的属性。
- -f 选项强制加载目录中的子目录的元数据。默认方式下，只有当目录首次被列出时，才会加载元数据。
- -h 选项以可读方式显示文件大小。
- -p 选项列出所有固定的文件。
- -R 选项可以递归的列出输入路径下的所有子文件和子文件夹，并列出从输入路径开始的所有子树。

#### 操作示例
使用 ls 命令可以浏览文件系统。
```
$ ./bin/alluxio fs mount /cos/data cosn://data-bucket/
```
验证：
```
$ ./bin/alluxio fs ls /s3/data/
```

## masterInfo
#### 背景
masterInfo 命令打印与 Alluxio master 容错相关的信息，例如 leader 的地址、所有 master 的地址列表以及配置的 Zookeeper 地址。如果 Alluxio 运行在单 master 模式下，masterInfo 命令会打印出该 master 的地址；如果 Alluxio 运行在多 master 容错模式下，masterInfo 命令会打印出当前的 leader 地址、所有 master 的地址列表以及 Zookeeper 的地址。

#### 操作示例
使用 masterInfo 命令可以打印与 Alluxio master 容错相关的信息。

```
$ ./bin/alluxio fs masterInfo
```

## mkdir
#### 背景
mkdir 命令在 Alluxio 中创建一个新的文件夹。该命令可以递归创建不存在的父目录。注意在该文件夹中的某个文件被持久化到底层文件系统之前，该文件夹不会在底层文件系统中被创建。对一个无效的或者已存在的路径使用 mkdir 命令会失败。

#### 操作示例
管理员使用 mkdir 命令可以创建一个基本文件夹结构。
```
$ ./bin/alluxio fs mkdir /users
$ ./bin/alluxio fs mkdir /users/Alice
$ ./bin/alluxio fs mkdir /users/Bob
```

## mount
#### 背景
mount 命令将一个底层存储中的路径链接到 Alluxio 路径，并且在 Alluxio 中该路径下创建的文件和文件夹会在对应的底层文件系统路径进行备份。访问统一命名空间获取更多相关信息。

选项：
--readonly 选项在 Alluxio 中设置挂载点为只读。
--option `<key>=<val>` 选项传递一个属性到这个挂载点（如 S3 credential）。

#### 操作示例
使用 mount 命令可以让其他存储系统中的数据在 Alluxio 中也能获取。
```
$ ./bin/alluxio fs mount /mnt/hdfs hdfs://host1:9000/data/
```

## mv
#### 背景
mv 命令将 Alluxio 中的文件或文件夹移动到其他路径。目标路径一定不能事先存在或者是一个目录。如果是一个目录，那么该文件或文件夹会成为该目录的子文件或子文件夹。mv 命令仅仅对元数据进行操作，不会影响该文件的数据块。mv 命令不能在不同底层存储系统的挂载点之间操作。

#### 操作示例
使用 mv 命令可以将过时数据移动到非工作目录。
```
$ ./bin/alluxio fs mv /data/2014 /data/archives/2014
```

## persist
#### 背景
persist 命令将 Alluxio 中的数据持久化到底层文件系统中。该命令是对数据的操作，因而其执行时间取决于该文件的大小。在持久化结束后，该文件即在底层文件系统中有了备份，因而该文件在 Alluxio 中的数据块被剔除甚至丢失的情况下，仍能够访问。

#### 操作示例
在从一系列临时文件中过滤出包含有用数据的文件后，便可以使用 persist 命令对其进行持久化。
```
$ ./bin/alluxio fs persist /tmp/experimental-logs-2.txt
```

## pin
#### 背景
pin 命令对 Alluxio 中的文件或文件夹进行标记。该命令只针对元数据进行操作，不会导致任何数据被加载到 Alluxio 中。如果一个文件在 Alluxio 中被标记了，该文件的任何数据块都不会从 Alluxio worker 中被剔除。如果存在过多的被锁定的文件，Alluxio worker 将会剩余少量存储空间，从而导致无法对其他文件进行缓存。

#### 操作示例
如果管理员对作业运行流程十分清楚，那么可以使用 pin 命令手动提高性能。
```
$ ./bin/alluxio fs pin /data/today
```

## report
#### 背景
report 命令向 Alluxio master 标记一个文件为丢失状态。该命令应当只对使用 Lineage API 创建的文件使用。将一个文件标记为丢失状态将导致 master 调度重计算作业从而重新生成该文件。

#### 操作示例
使用 report 命令可以强制重新计算生成一个文件。
```
$ ./bin/alluxio fs report /tmp/lineage-file
```

## rm
#### 背景
rm 命令将一个文件从 Alluxio 以及底层文件系统中删除。该命令返回后该文件便立即不可获取，但实际的数据要过一段时间才被真正删除。

加上 -R 选项可以递归的删除文件夹中所有内容后再删除文件夹自身。加上 -U 选项将会在尝试删除持久化目录之前不会检查将要删除的 UFS 内容是否与 Alluxio 一致。

#### 操作示例
使用 rm 命令可以删除掉不再需要的临时文件。
```
$ ./bin/alluxio fs rm /tmp/unused-file
```

## setTtl
#### 背景
setTtl 命令设置一个文件或者文件夹的 ttl 时间，单位为毫秒。如果当前时间大于该文件的创建时间与 ttl 时间之和时，行动参数将指示要执行的操作。delete 操作（默认）将同时删除 Alluxio 和底层文件系统中的文件，而 free 操作将仅仅删除 Alluxio 中的文件。

#### 操作示例
管理员在知道某些文件经过一段时间后便没用时，可使用带有 delete 操作的 setTtl 命令来清理文件；如果仅希望为 Alluxio 释放更多的空间，可使用带有 free 操作的 setTtl 命令来清理 Alluxio 中的文件内容。
```
$ ./bin/alluxio fs setTtl -action free /data/good-for-one-day 86400000
```

## stat
#### 背景
stat 命令将一个文件或者文件夹的主要信息输出到控制台，这主要是为了让用户调试他们的系统。一般来说，在 Web UI 上查看文件信息要容易理解得多。

可以指定 -f 来按指定格式显示信息：
- “%N”：文件名。
- “%z”：文件大小（bytes）。
- “%u”：文件拥有者。
- “%g”：拥有者所在组名。
- “%y” or “%Y”：编辑时间，`%y shows ‘yyyy-MM-dd HH:mm:ss’ (the UTC date), %Y`为自从 January 1, 1970 UTC 以来的毫秒数。
- “%b”：为文件分配的数据块数。

#### 操作示例
例如，使用 stat 命令能够获取到一个文件的数据块的位置，这在获取计算任务中的数据局部性时非常有用。
```
$ ./bin/alluxio fs stat /data/2015/logs-1.txt
$ ./bin/alluxio fs stat /data/2015
$ ./bin/alluxio fs stat -f %z /data/2015/logs-1.txt
```

## tail
#### 背景
tail 命令将一个文件的最后1kb内容输出到控制台。

#### 操作示例
使用 tail 命令可以确认一个作业的输出是否符合格式或者包含期望的值。
```
$ ./bin/alluxio fs tail /output/part-00000
```

## test
#### 背景
test 命令测试路径的属性，如果属性为真，返回0，否则返回1。

选项：
-d 选项测试路径是否是目录。
-e 选项测试路径是否存在。
-f 选项测试路径是否是文件。
-s 选项测试路径是否为空。
-z 选项测试文件长度是否为0。

#### 操作示例
```
$ ./bin/alluxio fs test -d /someDir
```

## touch
#### 背景
touch 命令创建一个空文件。由该命令创建的文件不能被覆写，大多数情况是用作标记。

#### 操作示例
使用 touch 命令可以创建一个空文件用于标记一个文件夹的分析任务完成了。
```
$ ./bin/alluxio fs touch /data/yesterday/_DONE_
```

## unmount
#### 背景
unmount 将一个 Alluxio 路径和一个底层文件系统中的目录的链接断开。该挂载点的所有元数据和文件数据都会被删除，但底层文件系统会将其保留。访问 Unified Namespace 获取更多信息。

#### 操作示例
当不再需要一个底层存储系统中的数据时，使用 unmont 命令可以移除该底层存储系统。
```
$ ./bin/alluxio fs unmount /s3/data
```

## unpin
#### 背景
unpin 命令将 Alluxio 中的文件或文件夹解除标记。该命令仅作用于元数据，不会剔除或者删除任何数据块。一旦文件被解除锁定，Alluxio worker 可以剔除该文件的数据块。

#### 操作示例
当管理员知道数据访问模式发生改变时，可以使用 unpin 命令。
```
$ ./bin/alluxio fs unpin /data/yesterday/join-table
```

## unsetTtl
#### 背景
unsetTtl 命令删除 Alluxio 中一个文件的 TTL。该命令仅作用于元数据，不会剔除或者删除 Alluxio 中的数据块。该文件的 TTL 值可以由 setTtl 命令重新设定。

#### 操作示例
在一些特殊情况下，当一个原本自动管理的文件需要手动管理时，可使用 unsetTtl 命令。
```
$ ./bin/alluxio fs unsetTtl /data/yesterday/data-not-yet-analyzed
```
