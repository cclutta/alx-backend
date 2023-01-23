#!/usr/bin/env python3
"""
Simple pagination module

Contains the function get_page
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return a tuple of size two containing a start index and an end index.

    Args:
        page: the number of the page
        page_size: the size of the page
    """
    return (page_size * (page - 1), page_size * page)


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
        """ That takes two integer arguments page with default value 1
        and page_size with default value 10.
        """
        assert type(page) is int and type(
            page_size) is int and page > 0 and page_size > 0

        return self.dataset()[slice(*index_range(page, page_size))]

    def get_hyper(self,
                  page: int = 1,
                  page_size: int = 10) -> \
            Dict[str, Union[int, List[List], None]]:
        """
        returns a dictionary containing the following key-value pairs:
        """
        assert type(page) is int and type(
            page_size) is int and page > 0 and page_size > 0

        page_data: List[List] = self.get_page(page, page_size)

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page+1 if self.get_page(page+1, page_size) else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": math.ceil(len(self.dataset()) / page_size)
        }
