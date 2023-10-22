# Datastore Indexes Documentation

Welcome to the Datastore Indexes repository. This documentation outlines the indexes for Google Cloud Datastore, providing essential information on how to enhance query performance for specific entities and properties.

## Table of Contents

1. [Introduction](#introduction)
2. [Indexes](#indexes)
    - [Cat Kind Indexes](#cat-kind-indexes)
    - [Store Kind Indexes](#store-kind-indexes)
3. [How to Use](#how-to-use)
4. [Contributing](#contributing)
5. [License](#license)

---

## Introduction

Harness the power of Google Cloud Datastore, a NoSQL database service, to build applications with optimized query performance. The key to this efficiency lies in the well-defined indexes provided in this repository.

## Indexes

### Cat Kind Indexes

#### Index 1 - Cat

- **Kind:** Cat
- **Ancestor:** No ancestor is associated.
- **Properties:** 
    - `name` - Sorted in ascending order.
    - `age` - Sorted in descending order.

#### Index 2 - Cat

- **Kind:** Cat
- **Ancestor:** No ancestor is associated.
- **Properties:** 
    - `name` - Sorted in ascending order.
    - `whiskers` - Sorted in descending order.

### Store Kind Indexes

#### Index 1 - Store

- **Kind:** Store
- **Ancestor:** Ancestor is associated.
- **Properties:** 
    - `business` - Sorted in ascending order.
    - `owner` - Sorted in ascending order.

## How to Use

Enhance the performance of your Google Cloud Datastore application by following these action-oriented steps:

1. **Configure Your Datastore:** Make sure to include these index definitions in your Datastore configuration.

2. **Deployment:** Deploy your application with these index definitions within the Google Cloud Platform environment.

3. **Query Optimization:** The Datastore service will actively utilize these indexes to optimize queries for the specified entity kinds and properties.

## Contributing

We actively encourage you to contribute to this repository. If you have ideas for improvements or wish to add new index definitions that benefit the community, take the following actions:

1. **Fork the Repository:** Begin by forking this repository.

2. **Create a New Branch:** Establish a new branch dedicated to your changes.

3. **Implement Improvements:** Make impactful improvements or introduce new index definitions.

4. **Pull Request:** Submit a pull request, initiating the review process for your contributions.

## License

This project operates under the [MIT License](LICENSE). You have the freedom to use, modify, and distribute the code as you see fit.

---

Thank you for engaging with and contributing to this repository. We aspire to assist you in optimizing your Google Cloud Datastore queries efficiently. Should you have any questions or concerns, please don't hesitate to reach out to us.
