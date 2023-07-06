
import unittest

import numpy as np
from common.np_helper import npRemoveLastRow, npSelectlastRow, npSelectlastRowColN
import numpy.testing as np_testing
# commenting these as not sharing the reader now.
# from readers.experiment_reader import clean_end_of_iteration, clean_start_of_iteration, cut_np_first_and_last_n

# # chatgbt
# class TestCleanStartOfIteration(unittest.TestCase):
#     def test_clean_start_of_iteration(self):
#         # Create a test case
#         power_col_index = 0
#         iterationMonitorings = np.array([[1, 3, 3], [4, 6, 6],[4, 6, 6],[4, 6, 6],[4, 6, 6],[4, 6, 6],[4, 6, 6],[4, 6, 6],[4, 6, 6],[4, 6, 6],[4, 6, 6],[4, 6, 6],[4, 6, 6],[4, 6, 6],[4, 6, 6],[4, 6, 6], [7, 9, 9],[4, 6, 6]])
#         nb_measruements_potential_spikes_area=5# each time checks 5, but array is getting smaller, eacht time keep 5 window
#         # Call the function
#         cleaned_monitorings, count_removed_rows = clean_start_of_iteration(iterationMonitorings, power_col_index,nb_measruements_potential_spikes_area)
        
#         # Assertions
#         self.assertEqual(cleaned_monitorings.shape[0], 17)  # Check if the first row is removed
#         self.assertEqual(count_removed_rows, 1)  # Check the count of removed rows


# def test_clean_end_of_iteration():
#     # Create a sample input array
#     iterationMonitorings = np.array([[1, 2, 3],
#                                      [4, 5, 6],
#                                      [7, 8, 9],
#                                      [10, 11, 12]])

#     # Define parameters
#     power_col_index = 2
#     nb_measruements_potential_cleaning_area = 2

#     # Expected output
#     expected_array = np.array([[1, 2, 3],
#                                [4, 5, 6]])
#     expected_count = 2

#     # Call the function
#     result_array, result_count = clean_end_of_iteration(iterationMonitorings, power_col_index, nb_measruements_potential_cleaning_area)

#     # Perform the tests
#     assert np.array_equal(result_array, expected_array)
#     assert result_count == expected_count

#     print("Unit test passed.")



# # chatgbt
# class TestGetPowerMeasurements(unittest.TestCase):
#     def test_cut_np_first_and_last_n(self):
#         # Create a test case
#         iterationMonitorings_np = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
#         nCut = 1
#         pColIndex = 1
        
#         # Call the function
#         result = cut_np_first_and_last_n(iterationMonitorings_np, nCut, pColIndex)
#         #iterationMonitorings_np[nCut:-nCut or None ,pColIndex]
#         # Define the expected output
#         expected_output = np.array([5, 8, 11])
        
#         # Assertions
#         self.assertTrue(np.array_equal(result, expected_output))  # Check if the result matches the expected output

# Unit test
def test_npRemoveLastRow():
    # Create a sample array
    arr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

    # Expected result
    expected_result = np.array([[1, 2, 3],
                                [4, 5, 6]])

    # Remove the last row using the function
    result = npRemoveLastRow(arr)

    # Perform the test
    np_testing.assert_array_equal(result, expected_result)
    print("Unit test passed.")

def test_npSelectlastRow():
    # Create a sample array
    arr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

    # Expected result
    expected_result = np.array([7, 8, 9])

    # Select the last row using the function
    result = npSelectlastRow(arr)

    # Perform the test
    np_testing.assert_array_equal(result, expected_result)
    print("Unit test passed.")
def test_npSelectlastRowColN():
    # Create a sample array
    arr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

    # Define the column index to select
    col_index = 1

    # Expected result
    expected_result = 8

    # Select the specific column from the last row using the function
    result = npSelectlastRowColN(arr, col_index)

    # Perform the test
    np_testing.assert_equal(result, expected_result)
    print("Unit test passed.")

# Run the unit test
# test_clean_end_of_iteration()

# Run the unit test
test_npSelectlastRowColN()
# Run the unit test
test_npSelectlastRow()
test_npRemoveLastRow()

if __name__ == '__main__':
    unittest.main()
    test_npRemoveLastRow()

    