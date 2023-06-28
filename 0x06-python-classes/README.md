# Python Code Examples

This repository contains a collection of Python code examples that demonstrate various concepts and features of the Python programming language.

## Table of Contents

1. [Singly Linked List](#singly-linked-list)
2. [Print Square Instance](#print-square-instance)
3. [Compare 2 Squares](#compare-2-squares)
4. [MagicClass](#magicclass)

## Singly Linked List

### Description

The `singly_linked_list.py` file contains the implementation of a singly linked list. It defines a `Node` class that represents a node in the linked list, and a `SinglyLinkedList` class that represents the linked list itself. The `SinglyLinkedList` class provides methods for inserting nodes into the list in a sorted order.

### Usage

To use the singly linked list, you can create an instance of the `SinglyLinkedList` class and call the `sorted_insert()` method to insert nodes into the list. The list can then be printed using the `print()` function.

Example:

```python
sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
print(sll)
