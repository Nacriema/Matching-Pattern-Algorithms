# Pattern Matching
## Brute-Fort Algorithm

## The Rabin Karp Algorithm

## The Knuth-Morris-Pratt Algorithm

Link tìm hiểu thêm về giải thuật tại đây [**GeeksForGeeks**](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/)
và link từ [**Youtube**](https://www.youtube.com/watch?v=V5-7GzOfADQ) 

Tóm tắt nội dung, KMP được phát triển để giảm thiểu chi phí so sánh trong quá trình tìm kiếm chuỗi con trong một trường 
văn bản rộng lớn. Ta có thể thấy rằng so với Naive approach thì KMP có độ phức tạp trong trường hợp xấu nhất nhỏ hơn 
nhiều, chỉ là O(n) với n là chiều dài của đoạn **text** (Xảy ra khi tất cả các ký tự trong **pattern** là không trùng lắp
nhau trong hàm prefix)

Thuật toán KMP bao gồm 2 pha 
* Phase 1: Pha xử lý, tính toán prefix function. Nó có độ phức tạp là O(m) với m là chiều dài của 
pattern cần tìm. Chú ý rằng cái prefix function cho phép cái prefix cũng như là suffix overlap lên nhau.

Ví dụ: Tìm cái prefix function cho chuỗi acacac

Ta có được chuỗi prefix như sau: 0, 0, 1, 2, 3, 4

Giải thích: a -> 0, ac-> 0, aca -> 1, acac -> 2, acaca -> 3, acacac -> 4

Giải thuật được trình bày bằng đoạn code python:
```python
def prefix_function(pattern):
    n = len(pattern)
    prefix_func = [0] * n
    k = 0
    for i in range(1, n):
        while k > 0 and pattern[k] != pattern[i]:
            k = prefix_func[k - 1]
        if pattern[k] == pattern[i]:
            k += 1
            prefix_func[i] = k
    return prefix_func
```

* Phase 2: Pha tìm kiếm (searching phase), thuật toán KMP có độ phức tạp là O(n) với n là chiều dài của đoạn text cần 
đầu vào.

Phần này được trình bày bằng đoạn code sau, các bạn tham khảo thêm cách giải thích trong phần link mô tả của bài viết nha:
```python
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
```

* Test:
```python
    KMP_Matcher('adcasfcassa', 'cas')
    KMP_Matcher('abcsesg', 'mkn')
```

* Result: 
```python 
    Pattern occours at index 2
    Pattern occours at index 6
    
    No match found
```

## Boyer-Moore Algorithm




