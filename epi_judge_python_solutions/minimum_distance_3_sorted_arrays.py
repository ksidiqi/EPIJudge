from test_framework import generic_test
import sortedcontainers as sc


def find_closest_elements_in_sorted_arrays(sorted_arrays):
    container = sc.SortedDict()
    for idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)
        key = next(it, None)
        if key is not None:
            container[(key, idx)] = it
    min_distance = container.iloc[-1][0] - container.iloc[0][0]
    
    while True:
        key_idx , it = container.popitem(index=0)
        key = next(it, None)
        if key is not None:
            container[(key, key_idx[1])] = it
            min_distance = min(min_distance, container.iloc[-1][0] - container.iloc[0][0])
        else:
            break
    return min_distance

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_distance_3_sorted_arrays.py",
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
