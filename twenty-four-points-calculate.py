'''
通过该函数递归实现24点计算
'''
def recursion(array, process=[]):
    tmp_pro = process
    if len(array) == 1:
        if array[0] == 24:
            print_process(process)
            exit(0)
    else:
        for i in range(len(array) - 1):
            for j in range(i + 1, len(array)):
                if j is not i:
                    new_array = []
                    for k in range(len(array)):
                        if k is not i and k is not j:
                            new_array.append(array[k])
                    #加法
                    new_process = str(array[i]) + '+' + str(array[j]) + '=' + str(array[i]+array[j])
                    recursion(new_array+[array[i]+array[j]], process+[new_process])
                    #减法
                    if array[i] is not array[j]:
                        new_process = str(max(array[i], array[j])) + '-' + str(min(array[i], array[j])) + '=' + str(abs(array[i] - array[j]))
                        recursion(new_array + [abs(array[i] - array[j])], process + [new_process])
                    else:
                        new_process = str(array[i]) + '-' + str(array[j]) + '=' + str(0)
                        recursion(new_array + [array[i] - array[k]], process + [new_process])
                    #乘法
                    new_process = str(array[i]) + '*' + str(array[j]) + '=' + str(array[i] * array[j])
                    recursion(new_array + [array[i] * array[j]], process + [new_process])
                    #除法
                    if array[i] is not 0 or array[j] is not 0:
                        if array[i] is 0 or array[j] is 0:
                            new_process = ''
                            if array[i] is 0:
                                new_process = new_process + '0/' + array[j]
                            else:
                                new_process = new_process + '0/' + str(array[i])
                            new_process += '=0'
                            recursion(new_array + [0], process + [new_process])
                        else:
                            if max(array[i], array[j]) % min(array[i], array[j]) is 0:
                                new_process = str(max(array[i], array[j])) + '/' + str(min(array[i], array[j])) + '=' + str(max(array[i], array[j])/min(array[i], array[j]))
                                recursion(new_array + [max(array[i], array[j])/min(array[i], array[j])], process + [new_process])

'''
该函数用于打印运算过程
'''
def print_process(process):
    for i in range(3):
        print('第' + str(i+1) + '步：' + process[i])


input_array = input()
input_array = [int(x) for x in input_array.split()]
recursion(input_array)
