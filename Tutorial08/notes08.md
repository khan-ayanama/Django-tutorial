# Notes - 08

## Introduction

ORM is an acronym for the object-relational mapper. The ORM’s main goal is to transmit data between a relational database and application model. The ORM automates this transmission, such that the developer need not write any SQL.  

An ORM will automatically create and store your object data in the database. You don’t have to write any SQL for the same.  

## Query Set

A QuerySet is a collection of data from a database, A QuerySet is built up as a list of objects.  

Django QuerySet represents and executes a SQL query to load a collection of model instances from the database  

### There are some methods to get data from a model into a queryset

1. all()

    ```python
    >>> Students.objects.all().values()
    ```

2. values_list()

   - The values_list() returns only the column that is specified inside the syntax. The source code for the same is given below:

        ```python
        >>> Students.objects.values_list('Subjects')
        ```

3. Create Objects

   - for creating an object, use the following code

        ```python
        >>>Students.objects.create(id=06,name='Victor', subject='Ecology')
        ```

4. Filter

    ```python
    >>>Students.objects.filter(name='Robert')
    ```

5. AND

    ```python
    >>>Students.objects.filter(name='Jerry', id=2).values()
    ```

6. OR

    ```python
    >>>Students.objects.filter(name='Jacob').values()| Students.objects.filter(name='Robert').values()
    ```

7. Field Lookups

   - Field lookups are keywords that represent specific SQL keywords. Say we want to get a query set with the records where the field name starts with the alphabet "J".

        ```python
        >>>Students.objects.filter(name__startswith='J').values()
        ```

        ![More fields](./static/Screenshot%20(98).png)

## Django ORM

### One to One Relationship

1. A one-to-one relationship exists between two tables. For each row in table1, there shall be a row/ entity in table2.

   - Let’s understand it with an example

        ![one to one relationship](./static/one-to-one-relationship%20(1).jpg)

### One to Many

A one to many relationships is where one object from table1 can have multiple relations with entities in table2. Although, table2 objects will have only one relation to the object of table1.

### Many to Many Relationships

We can also implement many to many relations in the database. In this case, we are taking examples of multiple drivers
