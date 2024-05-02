#!/usr/bin/env python3

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
