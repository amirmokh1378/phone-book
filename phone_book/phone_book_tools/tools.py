def search(lis, platform):
    if platform in lis:
        return True
    else:
        return False


def get_equal_items_list_one_in_list_tow(list1, list2):
    list_equal_item = []
    list_not_equal_item = []
    for first_list_item in list1:
        if search(list2, first_list_item):
            list_equal_item.append(first_list_item)
        else:
            list_not_equal_item.append(first_list_item)
    return list_equal_item, list_not_equal_item
