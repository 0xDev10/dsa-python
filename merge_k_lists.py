def merge_k_lists(lists):
    merge_sorted = []
    min_heap = []
    for i_list in lists:
        curr = i_list
        print(curr)
        while curr:
            print(curr.val)
            heappush(min_heap, curr.val)
            curr = curr.next
    print(min_heap)
    
    while min_heap:
        merge_sorted.append(heappop(min_heap))
        
    return merge_sorted

lists = [[1,4,5],[1,3,4],[2,6]]
print(merge_k_lists(lists))