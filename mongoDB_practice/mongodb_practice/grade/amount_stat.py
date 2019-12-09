# amount_list: a list including all amount of a category 
# target: amount that should equal
# skip: number that this category should skip
def amount_pathfinding(amount_list: list, target: int, skip: int=0) -> list:
    path_list = {}
    for amount in amount_list:

        if amount <= target:
            origin_index = target-amount
            if origin_index not in path_list:
                path_list[origin_index] = set([1])
            else:
                path_list[origin_index].add(1)

            path_index_list = list(path_list)
            path_index_list.sort()
            for path_index in path_index_list :


                if amount<=path_index:
                    index = path_index-amount

                    for step_num in path_list[path_index]:
                        if origin_index == path_index and step_num==1:
                            continue
                        if index not in path_list:
                            path_list[index] = set([])
                        path_list[index].add(step_num+1)
    if not 0 in path_list:
        return []
    else:
        rst = path_list[0]
        if skip in rst:
            rst.remove(skip)
        return list(rst)