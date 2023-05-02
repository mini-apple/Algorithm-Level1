array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  if start >= end: # 원소가 1개일 경우 종료
    return
  pivot = start  # 피벗은 첫번째 원소
  left = start+1
  right = end
  # 왼쪽과 오른쪽이 엇갈릴때까지 반복
  while left <= right:
    # 왼쪽은 피벗보다 큰 데이터, 오른쪽은 피벗보다 작은 데이터 찾기
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
       right -= 1
    # 엇갈렸다면 작은 데이터와 피벗을 교체
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    # 엇갈리지 않았다면 작은데이터와 큰 데이터를 교체
    else:
      array[left], array[right] = array[right], array[left]
  # 분할 이후 재귀호출을 이용해 각각 정렬수행
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)