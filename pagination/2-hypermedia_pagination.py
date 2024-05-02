#!/usr/bin/env python3

import csv
import math
from typing import List

"Function named index_range that takes two integer arguments"


def index_range(page, page_size):

    """
    function named index_range that takes two integer arguments
    page and page_size

    page is the page number (1-indexed)
    page_size is the number of items per page

    Returns a tuple containing the start and end indices for the given page
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:

    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:

        """
        Returns a page of the dataset

        page is the page number (1-indexed)
        page_size is the number of items per page

        Returns a list of rows representing the requested page
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()

        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:

        """
        Implement a get_hyper for returns a dictionary with key-value
        pairs about the pagination

        page is the page number (1-indexed)
        page_size is the number of items per page

        Returns a dictionary containing the following key-value pairs:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from get_page)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        dataset = self.dataset()

        total_pages = math.ceil(len(dataset) / page_size)

        data = self.get_page(page, page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
