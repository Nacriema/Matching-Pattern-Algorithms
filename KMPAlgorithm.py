def prefix_function(pattern):
    n = len(pattern)
    prefix_fun = [0] * n
    k = 0
    for i in range(1, n):
        while k > 0 and pattern[k] != pattern[i]:
            k = prefix_fun[k-1]
        if pattern[k] == pattern[i]:
            k += 1
            prefix_fun[i] = k
    return prefix_fun


def KMP_Matcher(text, pattern):
    m = len(text)
    n = len(pattern)
    flag = False

    prefix_func = prefix_function(pattern)
    q = 0
    for i in range(0, m):
        while q > 0 and pattern[q] != text[i]:
            q = prefix_func[q-1]
        if pattern[q] == text[i]:
            q += 1
            if q == n:
                print(f'Pattern occours at index {i - n + 1}')
                flag = True
                q = prefix_func[q-1]
    if not flag:
        print('No match found')


if __name__ == '__main__':
    print(prefix_function('acacac'))
    KMP_Matcher('adcasfcassa', 'cas')
    KMP_Matcher('abcsesg', 'mkn')