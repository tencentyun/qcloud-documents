在 PostgreSQL 老版本中可通过继承支持表分区功能，如按时间，每月创建一个表分区，数据记录到对应分区中。在 PostgreSQL 10版本后，同样也支持了声明式分区了。本文将介绍如何提前创建分区或者根据写入数据实时创建分区。

下面将是常见的几种 PostgreSQL 自动创建分区表的方案。

## 场景
分区表在实际使用中，一般以时间字段作为分区键。如分区字段类型为 timestamp，分区方式为 List of values。
表结构如下：
```
CREATE TABLE tab
(
    id   bigint GENERATED ALWAYS AS IDENTITY,
    ts   timestamp NOT NULL,
    data text
) PARTITION BY LIST ((ts::date));
CREATE TABLE tab_def PARTITION OF tab DEFAULT;
```

**分区的创建一般分以下两种场景：**
### 一、定时提前创建分区
定时提前创建分区只需一个定时任务调度工具即可实现，常见的定时任务调度工具和创建分区方法如下：

#### 使用系统调度器，如 Crontab (Linux, Unix, etc.) 和 Task Scheduler (Windows)
以 Linux 操作系统为例，每天下午14点创建次日的分区表：
```
cat > /tmp/create_part.sh <<EOF
dateStr=\$(date -d '+1 days' +%Y%m%d); 
psql -c "CREATE TABLE tab_\$dateStr (LIKE tab INCLUDING INDEXES); ALTER TABLE tab ATTACH PARTITION tab_\$dateStr FOR VALUES IN ('\$dateStr')";
EOF
(crontab -l 2>/dev/null; echo "0 14 * * * bash /tmp/create_part.sh ") | crontab -
```

#### 使用数据库内置调度器，如 pg_cron、pg_timetable
以 pg_cron 为例，每天下午14点创建次日的分区表：
```
CREATE OR REPLACE FUNCTION create_tab_part() RETURNS integer
    LANGUAGE plpgsql AS
$$
DECLARE
    dateStr varchar;
BEGIN
    SELECT to_char(DATE 'tomorrow', 'YYYYMMDD') INTO dateStr;
    EXECUTE
        format('CREATE TABLE tab_%s (LIKE tab INCLUDING INDEXES)', dateStr);
    EXECUTE
        format('ALTER TABLE tab ATTACH PARTITION tab_%s FOR VALUES IN (%L)', dateStr, dateStr);
    RETURN 1;
END;
$$;

CREATE EXTENSION pg_cron;

SELECT cron.schedule('0 14 * * *', $$SELECT create_tab_part();$$);
```

#### 使用专门的分区管理插件，如 pg_partman
以 pg_partman 为例，每天提前创建次日的分区表；
```
CREATE EXTENSION pg_partman;

SELECT partman.create_parent(p_parent_table => 'public.tab',
                             p_control => 'ts',
                             p_type => 'native',
                             p_interval=> 'daily',
                             p_premake => 1);
```

### 二、按需实时创建分区
如需按数据插入的需要来创建分区，可根据分区是否存在来判断该时间区间内有无数据的存在，一般采用触发器来实现。

**需注意此方法存在以下两个问题**：
- PostgreSQL 13及以上的版本才提供针对分区表的 BEFORE/FOR EACH ROW 触发器。
```
ERROR:  "tab" is a partitioned table
DETAIL:  Partitioned tables cannot have BEFORE / FOR EACH ROW triggers.
```
- 插入数据时，因为锁表的原因，无法修改分区表定义，即无法 ATTACH 子表， 因此必须有另一个连接来做 ATTACH 的操作，此处可以用 LISTEN/NOTIFY 机制来通知另一个连接进行分区定义的修改。
```
ERROR:  cannot CREATE TABLE .. PARTITION OF "tab"
        because it is being used by active queries in this session
或
ERROR:  cannot ALTER TABLE "tab"
        because it is being used by active queries in this session
```

**触发器（实施子表创建和 NOTIFY）**
```
CREATE FUNCTION part_trig() RETURNS trigger
    LANGUAGE plpgsql AS
$$
BEGIN
    BEGIN
        /* try to create a table for the new partition */
        EXECUTE
            format('CREATE TABLE %I (LIKE tab INCLUDING INDEXES)', 'tab_' || to_char(NEW.ts, 'YYYYMMDD'));

        /*
         * tell listener to attach the partition
         * (only if a new table was created)
         */
        EXECUTE
            format('NOTIFY tab, %L', to_char(NEW.ts, 'YYYYMMDD'));
    EXCEPTION
        WHEN duplicate_table THEN
            NULL; -- ignore
    END;

    /* insert into the new partition */
    EXECUTE
        format('INSERT INTO %I VALUES ($1.*)', 'tab_' || to_char(NEW.ts, 'YYYYMMDD'))
        USING NEW;

    /* skip insert into the partitioned table */
    RETURN NULL;
END;
$$;

CREATE TRIGGER part_trig
    BEFORE INSERT
    ON TAB
    FOR EACH ROW
    WHEN (pg_trigger_depth() < 1)
EXECUTE FUNCTION part_trig();
代码(实施 LISTEN 和子表 ATTACH )
#!/usr/bin/env python3.9
# encoding:utf8
import asyncio

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect('application_name=listener')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()
cursor.execute(f'LISTEN tab;')


def attach_partition(table, date):
    with conn.cursor() as cs:
        cs.execute('ALTER TABLE "%s" ATTACH PARTITION "%s_%s" FOR VALUES IN (\'%s\')' % (table, table, date, date))


def handle_notify():
    conn.poll()
    for notify in conn.notifies:
        print(notify.payload)
        attach_partition(notify.channel, notify.payload)
    conn.notifies.clear()

loop = asyncio.get_event_loop()
loop.add_reader(conn, handle_notify)
loop.run_forever()
```

## 总结
本文向您介绍了两种自动创建分区的方案，以下为每种方案的总结分析：
- **定时提前创建分区**场景下的几种解决方案简单易懂，但会依赖系统或插件的定时管理机制，在运维、迁移时具有额外管理成本。
- **按需实时创建分区**场景下，能按实际数据规律减少不必要的分区数量，但也需要较高版本(≥13)及额外连接来完成，复杂度比较高。

您可根据业务情况，选择合适的自动创建分区方式。

| 场景 | 版本 | 实现难易度 | 是否需要系统调度器或插件工具 | 是否需要额外连接机制 | 成本 |
|---------|---------|---------|---------|---------|---------|
| 定时提前创建分区 | PostgreSQL 10 | 较简单 | 是 | 否 | 相对较高 |
| 按需实时创建分区 | 大于等于 PostgreSQL 13 | 较复杂 | 否 | 是 | 相对较低 |

