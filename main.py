def merge_sort(list1):
    if len(list1) < 2:

        return list1

    else:  # if list has 2 elements or greater...

        left_list = list1[0:int(len(list1)/2)]
        right_list = list1[int(len(list1)/2):len(list1)]

        merge_sort(left_list)
        merge_sort(right_list)

        sorted_list_counter = 0
        left_list_counter = 0
        right_list_counter = 0
        while (len(left_list) > left_list_counter) & (len(right_list) > right_list_counter):
            if left_list[left_list_counter] < right_list[right_list_counter]:
                list1[sorted_list_counter] = left_list[left_list_counter]
                sorted_list_counter += 1
                left_list_counter += 1
            else:
                list1[sorted_list_counter] = right_list[right_list_counter]
                sorted_list_counter += 1
                right_list_counter += 1

        if len(left_list) == left_list_counter:
            for val in range(right_list_counter, len(right_list)):
                list1[sorted_list_counter] = right_list[val]
                sorted_list_counter += 1
        elif len(right_list) == right_list_counter:
            for val in range(left_list_counter, len(left_list)):
                list1[sorted_list_counter] = left_list[val]
                sorted_list_counter += 1

    return list1






















