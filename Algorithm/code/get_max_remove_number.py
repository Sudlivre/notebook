def get_max_remove_number(s, ss):
    if not all([s, ss]):
        return 0
    if not (isinstance(s, str) or isinstance(ss, str)):
        return 0
    tt_list = [ss[0:index] + s + ss[index:] for index in range(len(ss))]
    tt_list.append(ss + s)
    tt_list = list(set(tt_list))
    max_number = 0
    for tt in tt_list:
        tt_len = len(tt)
        tt = list(tt)
        count = remove_number(tt)
        if count == tt_len:
            return count
        if count > max_number:
            max_number = count
    return max_number


def remove_number(tt, count=0):
    index, start, end = 0, 0, 0
    rm_list = []
    while index < len(tt) - 1:
        if tt[index] == tt[index + 1]:
            start = index
            tt.append('$$')
            for i in range(start, len(tt)):
                if tt[start] != tt[i]:
                    end = i - 1
                    rm_list.append((start, end))
                    break
            tt.pop()
            index += end - start
        index += 1
    if not rm_list:
        return count
    len_tt = len(tt)
    re_rm_list = reversed(rm_list)
    for item in re_rm_list:
        del tt[item[0]:item[1]+1]
    new_count = count + len_tt - len(tt)
    return remove_number(tt, count=new_count)


res = get_max_remove_number('A', 'ABCC')
print(res)
