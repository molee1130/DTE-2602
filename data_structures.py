# Imports
from __future__ import annotations  # Needed for typing Node class

from ast import Index
from tkinter import NO
import warnings
from typing import Any

import binarytree
import heapdict


# Node class (do not change)
class Node:
    def __init__(self, data: Any = None, next: None | Node = None):
        self.data = data
        self.next = next


# Add your implementations below


class Stack:
    def __init__(self):
        """Initialize stack object, with head attribute"""
        self.head = None 

    def push(self, data: Any) -> None:
        """Add new node with data to stack"""
        if self.head is None: 
            self.head = Node(data)
        else:
            self.head = Node(data, self.head)

    def peek(self) -> Node | None: #type hint should be "Any" not "Node"? 
        """Return data from node on top of stack, without changing stack"""
        if self.head:
            return self.head.data
        return None

    def pop(self) -> Node: #type hint should be "Any" not "Node"?
        """Remove last added node and return its data"""
        if self.head is None:
            raise IndexError("Stack is empty")
        pop_data = self.head.data
        self.head = self.head.next
        return pop_data


class Queue:
    def __init__(self):
        """Initialize queue object with head and tail"""
        self.head = None  
        self.tail = None

    def enqueue(self, data: Any) -> None:
        """Add node with data to queue"""
        if self.head is None: 
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data) #add new node to linked list
            self.tail = self.tail.next  #setting new tail 

    def peek(self) -> Any | None:
        """Return data from head of queue without changing the queue"""
        return self.head.data

    def dequeue(self) -> Any:
        """Remove node from head of queue and return its data"""
        if self.head is None:
            raise IndexError("Queue is empty")
        data = self.head.data
        self.head = self.head.next
        return data 


class EmergencyRoomQueue:
    def __init__(self):
        """Initialize emergency room queue, use heapdict as property 'queue'""" 
        #you mean priority not property? 
        self.queue = heapdict.heapdict()

    def add_patient_with_priority(self, patient_name: str, priority: int) -> None:
        """Add patient name and priority to queue

        # Arguments:
        patient_name:   String with patient name
        priority:       Integer. Higher priority corresponds to lower-value number.
        """
        # Do not ensure correct priority if patients is assigned
        # same priority value. 
        self.queue[patient_name] = priority

    def update_patient_priority(self, patient_name: str, new_priority: int) -> None:
        """Update the priority of a patient which is already in the queue

        # Arguments:
        patient_name:   String, name of patient in queue
        new_priority:   Integer, updated priority for patient

        """
        del self.queue[patient_name]
        self.queue[patient_name] = new_priority

    def get_next_patient2(self) -> str:
        """Remove highest-priority patient from queue and return patient name

        # Returns:
        patient_name    String, name of patient with highest priority
        """
        patient_name, _ = self.queue.popitem()
        return patient_name 
    
    def get_next_patient(self) -> str:
        """Remove highest-priority patient from queue and return patient name

        # Returns:
        patient_name    String, name of patient with highest priority
        """
        
        return self.queue.popitem()[0]


class BinarySearchTree:
    def __init__(self, root: binarytree.Node | None = None):
        """Initialize binary search tree

        # Inputs:
        root:    (optional) An instance of binarytree.Node which is the root of the tree

        # Notes:
        If a root is supplied, validate that the tree meets the requirements
        of a binary search tree (see property binarytree.Node.is_bst ). If not, raise
        ValueError.
        """
        pass

    def insert(self, value: float | int) -> None:
        """Insert a new node into the tree (binarytree.Node object)

        # Inputs:
        value:    Value of new node

        # Notes:
        The method should issue a warning if the value already exists in the tree.
        See https://docs.python.org/3/library/warnings.html#warnings.warn
        In the case of duplicate values, leave the tree unchanged.
        """
        pass

    def __str__(self) -> str | None:
        """Return string representation of tree (helper function for debugging)"""
        if self.root is not None:
            return str(self.root)
