from typing import List
from tests.tests_sort_012 import TestCasesSort012
from solution.sort_012 import Sort012

if __name__ == "__main__":
    ###################################
    # Tests
    ###################################
    tests_sort_012: TestCasesSort012 = TestCasesSort012()

    tests_sort_012.input_list_is_none_return_empty_list()
    tests_sort_012.input_list_is_empty_return_empty_list()
    tests_sort_012.input_list_has_one_element_return_input_list()

    tests_sort_012.input_list_is_not_list_raise_type_error()
    #tests_sort_012.input_list_has_element_not_int_raise_type_error()
    #tests_sort_012.input_list_has_element_not_012_raise_type_error()

    tests_sort_012.input_list_unsorted_return_sorted_list()
    tests_sort_012.input_list_sorted_return_sorted_list()

    ###################################
    # Demo
    ###################################
    sort_012: Sort012 = Sort012()
    input_list: List[int] = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
    result_List: List[int] = sort_012.main(input_list)
    print(result_List) # [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]