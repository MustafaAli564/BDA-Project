```mermaid
flowchart LR
    subgraph MongoDB
        M[MongoDB<br>(NoSQL Storage)]
    end
    subgraph Kafka
        K[Kafka<br>(Event Streaming)]
    end
    subgraph DeltaSpark
        DS[Delta-Spark<br>(Data Processing)]
    end
    subgraph Zookeeper
        Z[Zookeeper<br>(Coordination)]
    end
    subgraph Hadoop
        HN[Hadoop Namenode]
        HD[Hadoop Datanode<br>(Data Storage)]
    end
    subgraph ApacheDrill
        AD[Apache Drill<br>(SQL Queries)]
    end
    
    M --> Z
    K --> HN
    DS --> HN
    Z --> HN
    HN --> HD
    AD --> HD

