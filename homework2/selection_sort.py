#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sort_utils import swap


def sort(array):
    """
    Selection sort
    Complexity
        Memory
            O(n) - since all swaps "in place"
            and no addition data strictures requires
        Time
            Always O(n^2)
                Inner loop always lookup for minimum element,
                even when array is sorted

    """
    for i in range(len(array)):
        min_element = i
        for j in range(i, len(array)):
            if (array[j] < array[min_element]):
                min_element = j
        swap(array, i, min_element)
