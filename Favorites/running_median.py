import heapq

def get_median(min_heap, max_heap):
  if len(min_heap) > len(max_heap):
    return min_heap[0]
  elif len(min_heap) < len(max_heap):
    return -max_heap[0]
  else:
    min_root = min_heap[0]
    max_root = -max_heap[0]
    return (min_root + max_root) / 2.0

def add(num, min_heap, max_heap):
  if len(min_heap) + len(max_heap) <= 1:
    heapq.heappush(max_heap, -num)
    return
  median = get_median(min_heap, max_heap)
  if num > median:
    heapq.heappush(min_heap, num)
  else:
    heapq.heappush(max_heap, -num)

def rebalance(min_heap, max_heap):
  if len(min_heap) > len(max_heap) + 1:
    root = heapq.heappop(min_heap)
    heapq.heappush(max_heap, -root)
  elif len(max_heap) > len(min_heap) + 1:
    root = -heapq.heappop(max_heap)
    heapq.heappush(min_heap, root)


def running_median(stream):
  min_heap = []
  max_heap = []

  for num in stream:
    add(num, min_heap, max_heap)
    rebalance(min_heap, max_heap)
    print_median(min_heap, max_heap)

running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2 
        

print(running_median([2, 1, 4, 7, 2, 0, 5]))