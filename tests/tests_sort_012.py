import unittest
from typing import List
from solution.sort_012 import Sort012


class TestCasesSort012(unittest.TestCase):
    def input_list_is_none_return_empty_list(self: object) -> None:
        # Arrange
        sort_012: Sort012 = Sort012()
        input_list: List[int] = None

        # Act
        result_list: List[int] = sort_012.main(input_list)
        
        # Assert
        self.assertEqual(result_list, [])

    def input_list_is_empty_return_empty_list(self: object) -> None:
        # Arrange
        sort_012: Sort012 = Sort012()
        input_list: List[int] = []

        # Act
        result_list: List[int] = sort_012.main(input_list)
        
        # Assert
        self.assertEqual(result_list, [])
    
    def input_list_has_one_element_return_input_list(self: object) -> None:
        # Arrange
        sort_012: Sort012 = Sort012()
        input_list: List[int] = [1]

        # Act
        result_list: List[int] = sort_012.main(input_list)
        
        # Assert
        self.assertEqual(result_list, [1])
    
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def input_list_is_not_list_raise_type_error(self: object) -> None:
        # Arrange
        sort_012: Sort012 = Sort012()
        input_list: int = 123

        # Act & Assert
        self.assertRaises(TypeError, sort_012.main, input_list)

    def input_list_has_element_not_int_raise_type_error(self: object) -> None:
        # Arrange
        sort_012: Sort012 = Sort012()
        input_list: list = [0, 2, 1.1]

        # Act & Assert
        self.assertRaises(TypeError, sort_012.main, input_list)

    def input_list_has_element_not_012_raise_type_error(self: object) -> None:
        # Arrange
        sort_012: Sort012 = Sort012()
        input_list: list = [0, 2, 4]

        # Act & Assert
        self.assertRaises(ValueError, sort_012.main, input_list)

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def input_list_unsorted_return_sorted_list(self: object) -> None:
        # Arrange
        sort_012: Sort012 = Sort012()
        input_list: List[int] = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]

        # Act
        result_list: List[int] = sort_012.main(input_list)
        
        # Assert
        self.assertEqual(result_list, sorted(input_list))
    
    def input_list_sorted_return_sorted_list(self: object) -> None:
        # Arrange
        sort_012: Sort012 = Sort012()
        input_list: List[int] = [0, 0, 1, 1, 1, 1, 2, 2, 2]

        # Act
        result_list: List[int] = sort_012.main(input_list)
        
        # Assert
        self.assertEqual(result_list, input_list)