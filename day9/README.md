# DAy 9

## Draw & Interpret (ER Diagrams)

### Common Diagram Components

- Entities: Squares or rectangles that represent objects or concepts (e.g., Student, Course).
- Attributes: Ovals connected to entities that describe properties (e.g., Student Name, Course
- Relationships: Diamonds that show how entities are related (e.g., Enrolls, Teaches).
- Cardinality: Numbers or symbols near relationships indicating how many instances of one entity relate to another
  - One-to-One (1:1)
  - One-to-Many (1:N)
  - Many-to-Many (M:N)

### Cardinality and Modality

## Use Primary & foreign Keys

### Entities

## Normalization

### 1NF (First Normal Form)

- Eliminate repeating groups; ensure each field contains only atomic values.
- Establish a primary key for each table.

### 2NF (Second Normal Form)

- Meet all 1NF requirements; remove partial dependencies (i.e., no non-key attribute    depends on part of a composite key).

### 3NF (Third Normal Form)

- Meet all 2NF requirements; remove transitive dependencies (i.e., non-key attributes depend only on the primary key).
