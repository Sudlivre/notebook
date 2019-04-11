# 字符串消除
def get_max_remove_number(s, ss):
    tt_list = [ss[0:index] + s + ss[index:] for index in range(len(ss))]
    tt_list.append(ss + s)
    tt_list = list(set(tt_list))
    max_number = 0
    for tt in tt_list:
        remove_count = remove_number(tt)
        if remove_count > max_number:
            max_number = remove_count
    return max_number

def remove_number(tt):
    remove_count = 0

    return remove_count

get_max_remove_number('A', 'ABCC')