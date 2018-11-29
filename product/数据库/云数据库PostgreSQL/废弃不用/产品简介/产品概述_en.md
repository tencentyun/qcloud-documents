## 1. Overview of PostgreSQL

PostgreSQL is one of the most powerful open-source databases in the world, which supports many popular programming languages, such as C, C++, Perl, Python, Java, Tcl, PHP, etc. It can completely implement SQL standards, and support various types of data, including JSON data, IP data and geometric data, which are not fully supported by most commercial databases. For example:

- PostgreSQL, which conforms to BSD protocol, can be used without any restrictions.
- PostgreSQL is the most similar open-source database to Oracle in terms of architecture, syntax, data types, etc.
- It is compatible with SQL standards: SQL2003, and supports the major features of SQL2011.
- In addition to the operator LIKE of traditional SQL, it also supports a new operator SIMILAR TO of SQL99 and POSIX-style regular expression:
- Various types of data: geometric, IP, XML, JSON, RANGE, array, etc.
- Complex type (custom data type) is supported.
- Complex multi-table JOIN query SQL is supported: JOIN algorithm supports has, join, merge join, etc.
- Window functions are supported, and can be changed to complex analytic functions in which they are contained.
- Function index, partial (line) index, custom index, and full-text index are supported.
- Multi-process architecture ensures high stability. Databases with massive access volume are supported for a single CVM.
- It has powerful and high-performance plug-ins, such as Postgis.

Over the past few years, PostgreSQL has been developing in a rapid way. It is now widely applied in various industries such as geospace, mobile application and data analysis, and has become the first choice of many enterprise developers and innovative companies.

## 2. Overview of Tencent Cloud CDB for PostgreSQL
CDB for PostgreSQL allows you to easily configure, work with and expand the PostgreSQL, one of the most powerful open-source databases, on the cloud. Tencent Cloud handles most complicated and time-consuming management works for you, such as installation of PostgreSQL software, storage management, high-availability replication, and data backup for disaster recovery. Therefore, you can focus on the development of business applications.

Currently, Tencent Cloud provides PostgreSQL 9.3.5 and 9.5.4 (kernel optimization) versions.
