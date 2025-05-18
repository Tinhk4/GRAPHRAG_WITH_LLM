# Sơ đồ Kiến trúc GraphRAG

## 1. Tổng quan Hệ thống

```mermaid
graph TD
    A[Input Data] --> B[Data Preprocessing]
    B --> C[Graph Construction]
    C --> D[Neo4j Database]
    E[User Query] --> F[Query Processing]
    F --> G[Graph Search]
    G --> D
    D --> H[Context Retrieval]
    H --> I[LLM Processing]
    I --> J[Response Generation]
    J --> K[Final Response]
```

## 2. Chi tiết Các Thành phần

### 2.1. Data Processing Pipeline

```mermaid
graph LR
    A[Raw Text] --> B[Text Chunking]
    B --> C[Entity Extraction]
    C --> D[Relationship Detection]
    D --> E[Graph Nodes]
    D --> F[Graph Edges]
    E --> G[Neo4j Graph]
    F --> G
```

### 2.2. Query Processing Flow

```mermaid
graph TD
    A[User Query] --> B[Query Analysis]
    B --> C[Embedding Generation]
    C --> D[Graph Traversal]
    D --> E[Context Collection]
    E --> F[LLM Integration]
    F --> G[Response Generation]
    G --> H[Response to User]
```

### 2.3. System Components

```mermaid
graph TB
    subgraph "Frontend Layer"
        A[User Interface]
    end

    subgraph "Application Layer"
        B[GraphRAG Core]
        C[LLM Integration]
        D[Query Processor]
    end

    subgraph "Data Layer"
        E[Neo4j Database]
        F[Vector Store]
        G[Document Store]
    end

    A --> B
    B --> C
    B --> D
    D --> E
    D --> F
    B --> G
```

## 3. Luồng Dữ liệu

### 3.1. Data Ingestion Flow

```mermaid
sequenceDiagram
    participant U as User
    participant S as System
    participant P as Preprocessor
    participant G as Graph Builder
    participant D as Database

    U->>S: Upload Document
    S->>P: Process Document
    P->>P: Extract Entities
    P->>P: Identify Relationships
    P->>G: Create Graph Structure
    G->>D: Store Graph
    D-->>S: Confirmation
    S-->>U: Success Message
```

### 3.2. Query Processing Flow

```mermaid
sequenceDiagram
    participant U as User
    participant Q as Query Processor
    participant G as Graph Search
    participant L as LLM
    participant R as Response Generator

    U->>Q: Submit Query
    Q->>G: Search Graph
    G->>G: Traverse Nodes
    G->>L: Send Context
    L->>L: Process Context
    L->>R: Generate Response
    R-->>U: Return Answer
```

## 4. Các Module Chính

### 4.1. GraphRAG Core Module

```mermaid
graph TD
    A[GraphRAG Core] --> B[Graph Manager]
    A --> C[LLM Manager]
    A --> D[Query Manager]
    B --> E[Neo4j Interface]
    C --> F[Model Interface]
    D --> G[Search Interface]
```

### 4.2. Data Management Module

```mermaid
graph TD
    A[Data Management] --> B[Document Processor]
    A --> C[Entity Extractor]
    A --> D[Relationship Builder]
    B --> E[Text Chunker]
    C --> F[Entity Recognizer]
    D --> G[Graph Constructor]
```

## 5. Các API Endpoints

```mermaid
graph LR
    A[API Gateway] --> B[/ingest]
    A --> C[/query]
    A --> D[/graph]
    A --> E[/status]
    B --> F[Document Ingestion]
    C --> G[Query Processing]
    D --> H[Graph Operations]
    E --> I[System Status]
```

## 6. Monitoring và Logging

```mermaid
graph TD
    A[System Components] --> B[Logging Service]
    B --> C[Log Storage]
    B --> D[Monitoring Dashboard]
    D --> E[Performance Metrics]
    D --> F[Error Tracking]
    D --> G[Usage Statistics]
```

## 7. Security Layer

```mermaid
graph TD
    A[Security Layer] --> B[Authentication]
    A --> C[Authorization]
    A --> D[Data Encryption]
    B --> E[User Management]
    C --> F[Access Control]
    D --> G[Secure Storage]
```

## 8. Deployment Architecture

```mermaid
graph TD
    A[Docker Container] --> B[GraphRAG Service]
    A --> C[Neo4j Database]
    A --> D[LLM Service]
    B --> E[Load Balancer]
    C --> F[Data Volume]
    D --> G[Model Cache]
```

## 9. Error Handling

```mermaid
graph TD
    A[Error Detection] --> B[Error Classification]
    B --> C[Critical Errors]
    B --> D[Non-Critical Errors]
    C --> E[System Alert]
    D --> F[Error Log]
    E --> G[Admin Notification]
    F --> H[Error Analysis]
```

## 10. Performance Optimization

```mermaid
graph TD
    A[Performance Layer] --> B[Caching]
    A --> C[Load Balancing]
    A --> D[Query Optimization]
    B --> E[Response Cache]
    C --> F[Request Distribution]
    D --> G[Query Planner]
``` 