from typing import List


class Sort012(object):
    def __init__(self) -> None:
        """Constructor.
        """
        pass

    # def main(self: object, input_list: List[int]) -> List[int]:
    #     """Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    #         Parameters
    #         ----------
    #         input_list : List[int], required
    #             List to sort.

    #         Returns
    #         ----------
    #         list
    #             Returns the sorted list.
    #     """

    #     if not input_list or len(input_list) == 0:
    #         return []
    #     if len(input_list) == 1:
    #         return input_list

    #     next_pos_0: int = 0
    #     next_pos_2: int = len(input_list) - 1

    #     front_index: int = 0

    #     while front_index <= next_pos_2:
    #         if not isinstance(input_list[front_index], int) or not isinstance(input_list[next_pos_0], int) or not isinstance(input_list[next_pos_2], int):
    #             raise TypeError("Only integers are allowed...")
    #         if not input_list[front_index] in [0, 1, 2] or not input_list[next_pos_0] in [0, 1, 2] or not input_list[next_pos_2] in [0, 1, 2]:
    #             raise ValueError("Only 0, 1, 2 are allowed...")

    #         if input_list[front_index] == 0:
    #             input_list[front_index] = input_list[next_pos_0]
    #             input_list[next_pos_0] = 0
    #             next_pos_0 += 1
    #             front_index += 1
    #         elif input_list[front_index] == 2:
    #             input_list[front_index] = input_list[next_pos_2]
    #             input_list[next_pos_2] = 2
    #             next_pos_2 -= 1
    #         else:
    #             front_index += 1

    #     return input_list

    def main(self: object, input_list: List[int]) -> List[int]:
        """Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
            More efficient approach.

            Parameters
            ----------
            input_list : List[int], required
                List to sort.

            Returns
            ----------
            list
                Returns the sorted list.
        """

        if not input_list or len(input_list) == 0:
            return []
        if not isinstance(input_list, list):
            raise TypeError("Input list must be of type list...")
        if len(input_list) == 1:
            return input_list

        input_list_lenght: int = len(input_list)
        low: int = 0
        high: int = input_list_lenght - 1
        mid: int = 0

        while mid <= high:
            if input_list[mid] == 0:
                input_list[low], input_list[mid] = input_list[mid], input_list[low]
                low = low + 1
                mid = mid + 1
            elif input_list[mid] == 1:
                mid = mid + 1
            else:
                input_list[mid], input_list[high] = input_list[high], input_list[mid]
                high = high - 1

        return input_list
