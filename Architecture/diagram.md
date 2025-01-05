```mermaid
graph TD
  subgraph BigData Ecosystem
    Zookeeper["<img src='https://cdn-icons-png.flaticon.com/512/1077/1077970.png' width=30 height=30><br>Zookeeper"]
    Kafka["<img src='https://cdn-icons-png.flaticon.com/512/2281/2281186.png' width=30 height=30><br>Kafka"]
    Namenode["<img src='https://cdn-icons-png.flaticon.com/512/744/744458.png' width=30 height=30><br>Hadoop Namenode"]
    Datanode["<img src='https://cdn-icons-png.flaticon.com/512/2933/2933997.png' width=30 height=30><br>Hadoop Datanode"]
    DeltaSpark["<img src='https://cdn-icons-png.flaticon.com/512/919/919825.png' width=30 height=30><br>Delta-Spark"]
    Drill["<img src='https://cdn-icons-png.flaticon.com/512/917/917707.png' width=30 height=30><br>Apache Drill"]
    Mongo["<img src='https://cdn-icons-png.flaticon.com/512/2523/2523644.png' width=30 height=30><br>MongoDB"]

    Zookeeper --> Kafka
    Kafka --> DeltaSpark
    Namenode -->|Stores Metadata| Datanode
    DeltaSpark -->|Reads/Writes Data| Namenode
    DeltaSpark -->|Processes Data| Kafka
    Drill -->|Queries| Namenode
    Drill -->|Coordinates| Zookeeper
    Mongo --> DeltaSpark
  end
