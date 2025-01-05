```mermaid
graph TD
  subgraph BigData Ecosystem
    Zookeeper["Zookeeper\n(Coordinator)"]
    Kafka["Kafka\n(Event Streaming)"]
    Namenode["Hadoop Namenode\n(HDFS Master)"]
    Datanode["Hadoop Datanode\n(HDFS Slave)"]
    DeltaSpark["Delta-Spark\n(Data Processing)"]
    Drill["Apache Drill\n(SQL Query Engine)"]
    Mongo["MongoDB\n(NoSQL Storage)"]

    Zookeeper --> Kafka
    Kafka --> DeltaSpark
    Namenode -->|Stores Metadata| Datanode
    DeltaSpark -->|Reads/Writes Data| Namenode
    DeltaSpark -->|Processes Data| Kafka
    Drill -->|Queries| Namenode
    Drill -->|Coordinates| Zookeeper
    Mongo --> DeltaSpark
  end
