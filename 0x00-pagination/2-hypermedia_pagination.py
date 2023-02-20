#!/usr/bin/env python3
"""
Defines index_range function and Server class
"""
import csv
import math
from typing import List, Mapping, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple[int, int]: Tuple containing the start and end indexes
    """

    start = (page - 1) * page_size
    return (start, start + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Reads CSV

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): page size. Defaults to 10.

        Returns:
            List[List]: result
        """

        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        start, end = start + 1, end + 1
        result = []

        with open("Popular_Baby_Names.csv", "r") as f:
            file = csv.reader(f)

            for line in file:
                result.append(line)

        return result[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Mapping:
        """Reads CSV

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): page size. Defaults to 10.

        Returns:
            Mapping: result
        """

        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        start, end = start + 1, end + 1
        result = self.get_page(page, page_size)
        count = 0

        with open("Popular_Baby_Names.csv", "r") as f:
            file = csv.reader(f)

            for line in file:
                count += 1

        if (end + page_size) > count - 1:
            next_page = None
        else:
            next_page = page + 1

        if page == 0:
            prev_page = None
        else:
            prev_page = page - 1

        total_pages = (count - 1) // page_size
        if (count - 1) % page_size != 0:
            total_pages += 1

        if page_size > len(result):
            page_size = len(result)

        return {
            "page_size": page_size,
            "page": page,
            "data": result,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
