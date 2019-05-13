### Cluster and nodes
A running Elasticsearch instance is a node. In a network, one or more nodes that have the same cluster name and can communicate with each other form an Elasticsearch cluster. Nodes in the cluster work together to store data and process query requests. When new nodes are added into the cluster or some nodes are removed from the cluster, the cluster will re-distribute the data evenly. Each node knows where a document is located. Any node that receives a query request forwards it directly to the nodes where the document is stored, then collects data from these nodes, and finally returns the result to the client. All the above processes are transparent.

### Document
Elasticsearch is document-oriented, which stores the entire object or document, and indexes the content of each document so that it can be searched. Elasticsearch serializes documents to JSON, making them simple, concise and easy to read. JSON serialization is supported by most programming languages and has become a standard format in NoSQL area. In Elasticsearch, you can index, search, sort and filter the entire document instead of searching data from rows and columns. This is a completely different way of thinking about data, and also the reason why Elasticsearch can support complex full-text search.

### Index
#### Common concept
Just like a traditional relational database, an index is a place where relational documents are stored. The plural of index is indices or indexes.

Indexing a document is to store a document in an index, so that is can be searched and queried. An existing document will be replaced with the new version, which is similar to the keyword INSERT in SQL statements.

#### Inverted index
The relational database accelerates data search speed by adding an index, such as a B-tree index, to the specified column. Elasticsearch and Lucene use a structure called inverted index to achieve the same purpose. By default, each attribute in a document is indexed (with an inverted index) and searchable. An attribute without an inverted index cannot be searched.

### Shard
A shard is a data container where documents are stored. A shard is an underlying work unit, which only stores part of the data. Shards are assigned to each node of a cluster. When you scale your cluster up or down, Elasticsearch will automatically migrate shards between nodes to distribute data evenly in the cluster.

A shard can be a primary shard or a replica. Any document in an index belongs to a primary shard, so the number of primary shards determines the maximum volume of data that can be stored in the index. Technically, a primary shard can hold up to Integer.MAX_VALUE - 128 documents.

A replica is a copy of a primary shard. Replicas are used as redundant backups to avoid data loss in case of hardware failure, and provide services for read operations such as searching and returning documents. When an index is created, the number of primary shards is set, but the number of replicas can be modified at any time.


