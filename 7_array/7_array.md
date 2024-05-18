# 7장. 배열

- 자료구조
    - 메모리 공간 기반의 연속 방식 👉 배열
    - 포인터 기반의 연결 방식

- 과거 16비트 이전에, `int`는 2바이트였다.
    - 오늘날 32비트 이상의 시스템에서는 `int`를 4바이트로 사용한다.
    
    → 가리키는 주소는 1바이트마다 1씩 증가한다.(`int`형 배열)
    
- 배열은 어느 위치나 O(1)에 조회가 가능하다.

## 동적 배열

---

- 배열: 고정된 크기만큼의 연속된 메모리 할당
- 동적 배열: 크기를 지정하지 않고 자동으로 리사이징하는 배열
    - 자바: `ArrayList`, C++: `std::vector`, 파이썬이나 루비 같은 동적 프로그래밍 언어: 정적 배열 자체가 없다.
    - 더블링이 필요할 만큼 공간이 차면, 새로운 메모리 공간에 더 큰 크기의 배열을 할당하고 기존 데이터를 복사하는 작업이 필요하므로 O(n) 비용이 발생한다.
    - 최악의 경우 삽입 시 O(n)이 되지만 자주 일어나는 일은 아님

# 7. 두 수의 합

---

- [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)
- 덧셈하여 타깃을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
- 나의 풀이
    
    ```python
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            dic = {}
            
            for idx, n in enumerate(nums):
                if (target - n) in dic:
                    return [dic[target - n], idx]
                dic[n] = idx
    ```
    

## 풀이1. 브루트 포스로 계산

---

- 브루트 포스: 무차별 대입 방식. 마지막 엘리먼트까지 모두 차례대로 비교해가며 정답을 찾을 때까지 계속 진행한다.

- 전체 코드
    
    ```java
    public int[] towSum(int[] nums, int target) {
        // 입력값 배열을 처음부터 순회
        for (int i = 0; i < nums.length; i++) {
            // 입력값 배열을 그다음부터 순회
            for (int j = 0; j < nums.length; j++) {
                // 두 값의 합을 비교해 target과 일치하는 경우 정답으로 리턴
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        // 항상 정답이 존재하므로 널이 리턴되는 경우는 없음
        return null;
    }
    
    ```
    
    - 시간 복잡도: O(n^2)
        - 정확히는 1/2 * n^2

## 풀이2. 첫 번째 수를 뺀 결과 키 조회

---

- 전체 코드
    
    ```java
    public int[] towSum(int[] nums, int target) {
        Map<Integer, Integer> numsMap = new HashMap<>();
        // 키와 값을 바꿔서 맵으로 저장
        for (int i = 0; i < nums.length; i++) {
            numsMap.put(nums[i], i);
        }
        // target에서 첫 번째 수를 뺀 결과를 키로 조회하고 현재 인덱스가 아닌 경우 정답으로 리턴
        for (int i = 0; i < nums.length; i++) {
            if (numsMap.containsKey(target - nums[i]) && i != numsMap.get(target - nums[i])) {
                return new int[]{i, numsMap.get(target - nums[i])};
            }
        }
        // 항상 정답이 존재하므로 널이 리턴되는 경우는 없음
        return null;
    }
    ```
    
    - 자바에서 `HashMap`은 내부적으로 해시 테이블로 구현되어 있다.
        - 조회는 평균적으로 O(1)에 가능하다.
            - 최악의 경우에는 O(n)이 될 수 있지만 말 그대로 최악의 경우이고 드문 경우이므로, 분할 상환 분석에 따른 시간 복잡도는 O(1)
    - 전체는 O(n)이 된다.

## 풀이3. 조회 구조 개선

---

- 맵 저장과 조회를 2개의 `for` 문으로 각각 처리했던 방식을 좀 더 개선해 이번에는 하나의 `for`로 합쳐서 처리해보자.
- 동일한 O(n)에서 약간의 차이만 있을 뿐이라 성능상 큰 이점은 없겠다.

- 전체 코드
    
    ```java
    public int[] towSum(int[] nums, int target) {
        Map<Integer, Integer> numsMap = new HashMap<>();
        // 하나의 for 반복으로 통합
        for (int i = 0; i < nums.length; i++) {
            // target에서 num을 뺀 값이 있으면 정답으로 리턴 
            if (numsMap.containsKey(target - nums[i])) {
                return new int[]{numsMap.get(target - nums[i]), i};
            }
            // 정답이 아니므로 다음번 비교를 위해 인덱스를 맵에 저장
            numsMap.put(nums[i], i);
        }
        // 항상 정답이 존재하므로 널이 리턴되는 경우는 없음
        return null;
    }
    ```
    

## 풀이4. 투 포인터 이용

---

- 투 포인터: 왼쪽 포인터와 오른쪽 포인터의 합이 타깃보다 크다면 오른쪽 포인터를 왼쪽으로, 작다면 왼쪽 포인터를 오른쪽으로 옮기면서 값을 조정하는 방식
    - 그러나 이 문제는 투 포인터로 풀 수 없다.
    - 왜냐하면 투 포인터는 주로 정렬된 입력값을 대상으로 하며, nums는 정렬된 상태가 아니기 때문이다.

## 풀이5. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    fun towSum(nums: IntArray, target: Int): IntArray {
        val numsMap: MutableMap<Int, Int> = mutableMapOf()
        // 하나의 for 반복으로 통합
        for ((i, num) in nums.withIndex()) {
            // target에서 num을 뺀 값이 있으면 정답으로 리턴 
            if (numsMap.containsKey(target - num)) {
                return intArrayOf(numsMap[target - num] ?: 0, i)
            }
            // 정답이 아니므로 다음번 비교를 위해 인덱스를 맵에 저장
            numsMap[num] = i
        }
        // 항상 정답이 존재하므로 이 값이 리턴되는 경우는 없음
        return intArrayOf(0, 0)
    }
    ```
    
    - 코틀린은 마치 파이썬의 `enumerate()`처럼 `withIndex()`를 부여하면 인덱스와 값을 동시에 추출할 수 있다.
    - 엘비스 연산자를 활용해 기본값을 0으로 설정했다.
        - 사실 이 값은 반드시 존재하기 때문에 널이 될 수 없지만 행여나 발생할지 모를 NPE를 방지하기 위해 기본값을 0으로 선언했다.

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 브루트 포스로 계산 | 90밀리초 |
| 2 | 첫 번째 수를 뺀 결과 키 조회 | 11밀리초 |
| 3 | 조회 구조 개선 | 6밀리초 |
| 4 | 투 포인터 이용 | 풀이 불가 |
| 5 | 코틀린 풀이 | 측정하지 않음 |

# 8. 빗물 트래핑

---

- [https://leetcode.com/problems/trapping-rain-water/](https://leetcode.com/problems/trapping-rain-water/)
- 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
- 나의 풀이
    
    ```python
    def trap(self, height: List[int]) -> int:
        volume = 0
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
    
        while left < right:
            leftMax = max(height[left], leftMax)
            rightMax = max(height[right], rightMax)
    
            if leftMax < rightMax:
                volume += leftMax - height[left]
                left += 1
            else:
                volume += rightMax - height[right]
                right -= 1
    
        return volume
    ```
    

## 풀이1. 투 포인터를 최대로 이동

---

- 이 문제는 높이와 너비 모든 공간을 차례대로 모두 살펴보면 O(n^2)에 풀이가 가능하다. 그러나 시간 복잡도가 너무 높기 때문에 좀 더 효율적인 풀이를 찾아야 한다.
- 막대는 높고 낮음에 무관하게, 전체 부피에 영향을 끼치지 않으면서 그저 왼쪽과 오른쪽을 가르는 장벽 역할을 한다.
    
    ```java
    volume += leftMax - height[left]
    ...
    volume += rightMax - height[right]
    ```
    
- 이처럼 최대 높이의 막대까지 각각 좌우 막대 최대 높이 leftMax, rightMax가 현재 높이와의 차이만큼 물 높이 volume을 더해나간다.
    
    ```java
    if (leftMax <= rightMax) {
        volume += leftMax - height[left];
        left += 1;
    } else {
        volume += rightMax - height[right];
        right -= 1;
    }
    ```
    
- 이렇게 하면 가장 높이가 높은 막대, 즉 '최대' 지점에서 좌우 포인터가 서로 만나게 되며 O(n)에 풀이가 가능하다.

- 전체 코드
    
    ```java
    public int trap(int[] height) {
        int volume = 0;
        int left = 0;
        int right = height.length - 1;
        int leftMax = height[left];
        int rightMax = height[right];
    
        // 투 포인터가 서로 겹칠 때까지 반복
        while (left < right) {
            leftMax = Math.max(height[left], leftMax);
            rightMax = Math.max(height[right], rightMax);
    
            // 더 높은 쪽을 향해 투 포인터 이동
            if (leftMax < rightMax) {
                // 왼쪽 막대 최대 높이와의 차이를 더하고 왼쪽 포인터 이동
                volume += leftMax - height[left];
                left += 1;
            } else {
                // 오른쪽 막대 최대 높이와의 차이를 더하고 오른쪽 포인터 이동
                volume += rightMax - height[right];
                right -= 1;
            }
        }
        return volume;
    }
    ```
    

## 풀이2. 스택 쌓기

---

- 스택에 쌓아나가면서 현재 높이가 이전 높이보다 높을 때, 즉 꺾이는 부분 변곡점을 기준으로 격차만큼 물이 쌓이는 양을 채운다.
    - 이전 높이는 고정된 형태가 아니라 들쑥날쑥하기 때문에, 계속 스택으로 채워나가다가 변곡점을 만날 때마다 스택에서 하나씩 꺼내면서 이전과의 차이만큼 물이 쌓이는 양을 채워나간다.
- 스택으로 이전 항목들을 되돌아보며 체크하기는 하지만, 기본적으로 한 번만 살펴보기 때문에 마찬가지로 O(n)에 풀이가 가능하다.

- 전체 코드
    
    ```java
    public int trap(int[] height) {
        Deque<Integer> stack = new ArrayDeque<>();
        int volume = 0;
    
        for (int i = 0; i < height.length; i++) {
            // 변곡점을 만나는 경우
            while (!stack.isEmpty() && height[i] > height[stack.peek()]) {
                // 스택에서 꺼낸다.
                Integer top = stack.pop();
    
                if (stack.isEmpty())
                    break;
    
                // 스택의 마지막 위치까지를 거리로 계산
                int distance = i - stack.peek() - 1;
                // 현재 높이 또는 스택의 마지막 위치 높이 중 낮은 값에 방금 꺼낸 높이의 차이를 물 높이로 지정
                int waters = Math.min(height[i], height[stack.peek()]) - height[top];
    
                // 물이 쌓이는 양은 거리와 물 높이의 곱
                volume += distance * waters;
            }
    
            // 진행하면서 현재 위치를 스택에 삽입
            stack.push(i);
        }
        return volume;
    }
    ```
    

## 풀이3. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    fun trap(height: IntArray): Int {
        var volume = 0
        var left = 0
        var right = height.size - 1
        var leftMax = height[left]
        var rightMax = height[right]
    
        // 투 포인터가 서로 겹칠 때까지 반복
        while (left < right) {
            leftMax = height[left].coerceAtLeast(leftMax)
            rightMax = height[right].coerceAtLeast(rightMax)
    
            // 더 높은 쪽을 향해 투 포인터 이동
            if (leftMax < rightMax) {
                // 왼쪽 막대 최대 높이와의 차이를 더하고 왼쪽 포인터 이동
                volume += leftMax - height[left]
                left += 1
            } else {
                // 오른쪽 막대 최대 높이와의 차이를 더하고 오른쪽 포인터 이동
                volume += rightMax - height[right]
                right -= 1
            }
        }
        return volume
    }
    ```
    
    - 기존에 자바에서는 `Math.max()`로 처리했던 부분을 코틀린에서는 `coerceAtLeast()`라는 함수로 처리했다.
        - 파라미터보다 값이 커야 함을 뜻한다.
            - 파라미터의 값이 더 크다면 그 값이 리턴됨
            - 결국 두 값 중 큰 값을 취하는 `Math.max()`와 사실상 같은 역할을 한다.

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 투 포인터를 최대로 이동 | 0밀리초 |
| 2 | 스택 쌓기 | 8밀리초 |
| 3 | 코틀린 풀이 | 측정하지 않음 |

# 9. 세 수의 합

---

- [https://leetcode.com/problems/3sum/](https://leetcode.com/problems/3sum/)
- 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
- 나의 풀이
    
    ```python
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
    
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
    
            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                # 합이 0보다 작다면 왼쪽 포인터 이동
                if sum < 0:
                    left += 1
                # 합이 0보다 크다면 오른쪽 포인터 이동
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
    
                    # 중복된 값 건너뛰기, 이 처리를 하지 않으면 같은 정답이 두 번 나올 수 있다.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 정답이 나왔으므로 투 포인터 모두 한 칸씩 이동.
                    left += 1
                    right -= 1
    
        return results
    ```
    

## 풀이1. 브루트 포스로 계산

---

- 언뜻 보면 숫자 3개를 매번 반복하면 O(n^3) 정도에 풀이가 가능해 보인다.
    - 그러나 이 경우 타임아웃이 발생해 풀리지 않을 것도 같다.
    - 이 문제는 시간 복잡도를 O(n^2) 이내로 줄이기를 요구할 것이다.
- 앞뒤로 같은 값이 있을 경우, 이를 쉽게 처리하기 위해 먼저 다음과 같이 `sort()` 함수를 사용해 정렬부터 한다.
    
    ```java
    Arrays.sort(nums);
    ```
    
    - 정렬의 시간 복잡도: O(n * log n)
- i, j, k 각각의 포인터가 계속 이동하면서 i + j + k = 0을 찾아낸다.
    - 이 브루트 포스 풀이에는 중복된 값이 있을 수 있으므로 이 경우 다음과 같이 `continue`로 건너뛰도록 처리한다.
        - 이 처리를 하지 않으면 같은 값이 두 번 중복해서 나올 수 있다.
            
            ```java
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            ```
            

- 전체 코드
    
    ```java
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> results = new LinkedList<>();
        Arrays.sort(nums);
    
        // 브루트 포스 n^3 반복
        for (int i = 0; i < nums.length - 2; i++) {
            // 중복된 값 건너뛰기, 이 처리를 하지 않으면 같은 값이 두 번 나올 수 있다.
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
    
            for (int j = i + 1; j < nums.length - 1; j++) {
                // 중복된 값 건너뛰기, 사유 동일
                if (j > i + 1 && nums[j] == nums[j - 1])
                    continue;
                for (int k = j + 1; k < nums.length; k++) {
                    // 중복된 값 건너뛰기, 사유 동일
                    if (k > j + 1 && nums[k] == nums[k - 1])
                        continue;
                    if (nums[i] + nums[j] + nums[k] == 0)
                        results.add(Arrays.asList(nums[i], nums[j], nums[k]));
                }
            }
        }
        return results;
    }
    ```
    
    - 예상대로 이 방식으로는 문제가 풀리지 않는다. 타임아웃으로 풀이에 실패한다.

## 풀이2. 투 포인터로 합 계산

---

- 정렬한 다음에 i를 축으로 하고, 중복된 값을 건너뛰게 한 부분은 다음과 같이 풀이 #1과 동일하다.
    
    ```java
    if (i > 0 && nums[i] == nums[i - 1])
        continue;
    ```
    
- 풀이 #1과 다른 곳은 i의 다음 지점과 마지막 지점을 left, right로 설정하고 간격을 좁혀가며 sum을 계산하는 부분이다.
    
    ```java
    left = i + 1;
    right = nums.length - 1;
    while (left < right) {
        sum = nums[i] + nums[left] + nums[right];
        ...
    ```
    
    - 두 포인터가 간격을 좁혀나가며 합 sum을 계산한다.
    - 합 sum이 0보다 작다면 값을 더 키워야 하므로 left를 우측으로 이동하고, 0보다 크다면 값을 더 작게 하기 위해 right를 좌측으로 이동한다.
- sum이 0이면 정답이므로, 이 경우 결과를 리스트 변수 results에 추가한다.
    - 추가한 다음에는 left, right 양 옆으로 동일한 값이 있을 수 있으므로 같은 정답이 두 번 나오지 않도록 left += 1, right -= 1을 반복해서 스킵하도록 처리한다.
        
        ```java
        left += 1;
        right -= 1;
        ```
        
        - 마지막으로 left를 한 칸 우측으로, right를 한 칸 좌측으로 더 이동하고 다음으로 넘긴다.

- 전체 코드
    
    ```java
    public List<List<Integer>> threeSum(int[] nums) {
        int left, right, sum;
        List<List<Integer>> results = new LinkedList<>();
        Arrays.sort(nums);
    
        for (int i = 0; i < nums.length - 2; i++) {
            // 중복된 값 건너뛰기
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
    
            // 간격을 좁혀가며 합 sum 계산
            left = i + 1;
            right = nums.length - 1;
            while (left < right) {
                sum = nums[i] + nums[left] + nums[right];
                // 합이 0보다 작다면 왼쪽 포인터 이동
                if (sum < 0)
                    left += 1;
                    // 합이 0보다 크다면 오른쪽 포인터 이동
                else if (sum > 0)
                    right -= 1;
                else {
                    // 합이 0인 경우이므로 정답 처리
                    results.add(Arrays.asList(nums[i], nums[left], nums[right]));
    
                    // 중복된 값 건너뛰기, 이 처리를 하지 않으면 같은 정답이 두 번 나올 수 있다.
                    while (left < right && nums[left] == nums[left + 1])
                        left += 1;
                    while (left < right && nums[right] == nums[right - 1])
                        right -= 1;
                    // 정답이 나왔으므로 투 포인터 모두 한 칸씩 이동.
                    // 합이 0인 상황이므로 양쪽 모두 이동해야 한다.
                    left += 1;
                    right -= 1;
                }
            }
        }
        return results;
    }
    ```
    
    - 시간 복잡도: O(n^2)

## 풀이3. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    fun threeSum(nums: IntArray): List<List<Int>> {
        var left: Int
        var right: Int
        var sum: Int
        val results: MutableList<List<Int>> = mutableListOf()
        Arrays.sort(nums)
    
        for (i in 0 until nums.size - 2) {
            // 중복된 값 건너뛰기
            if (i > 0 && nums[i] == nums[i - 1])
                continue
    
            // 간격을 좁혀가며 합 sum 계산
            left = i + 1
            right = nums.size - 1
            while (left < right) {
                sum = nums[i] + nums[left] + nums[right]
                // 합이 0보다 작다면 왼쪽 포인터 이동
                if (sum < 0)
                    left += 1
                else if (sum > 0)
                    right -= 1
                else {
                    // 합이 0인 경우이므로 정답 처리
                    results.add(listOf(nums[i], nums[left], nums[right]))
    
                    // 중복된 값 건너뛰기, 이 처리를 하지 않으면 같은 정답이 두 번 나올 수 있다.
                    while (left < right && nums[left] == nums[left + 1])
                        left += 1
                    while (left < right && nums[right] == nums[right - 1])
                        right -= 1
                    // 정답이 나왔으므로 투 포인터 모두 한 칸씩 이동.
                    // 합이 0인 상황이므로 양쪽 모두 이동해야 한다.
                    left += 1
                    right -= 1
                }
            }
        }
        return results
    }
    ```
    
    - `MutableList`는 `List`를 상속받기 때문에 리턴 타입이 `List`일 때 `MutableList`를 리턴하는 게 가능하다. 하지만 반대는 불가능하다.

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 브루트 포스로 계산 | 타임아웃 |
| 2 | 투 포인터로 합 계산 | 28밀리초 |
| 3 | 코틀린 풀이 | 측정하지 않음 |

# 10. 배열 파티션 1

---

- [https://leetcode.com/problems/array-partition/](https://leetcode.com/problems/array-partition/)
- n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
- 나의 풀이
    
    ```python
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        
        for i in range(0, len(nums), 2):
            result += nums[i]
        
        return result
    ```
    

## 풀이1. 오름차순 풀이

---

- 페어의 `min()`을 합산했을 때 최대가 되려면 결국 각각의 `min()`이 가급적 커야 한다는 뜻이고, 뒤에서부터 내림차순으로 집어넣으면 항상 최대 `min()` 페어를 유지할 수 있다.
    - 배열 입력값의 길이는 항상 2n개이므로 앞에서부터 오름차순으로 집어넣어도 결과는 같을 것이다.

- 전체 코드
    
    ```java
    public int arrayPairSum(int[] nums) {
        int sum = 0;
        List<Integer> pair = new ArrayList<>();
        Arrays.sort(nums);
    
        // 앞에서부터 오름차순으로 반복
        for (int n : nums) {
            pair.add(n);
            // 페어 변수에 값이 2개 채워지면 min()을 합산하고 변수 초기화
            if (pair.size() == 2) {
                sum += Collections.min(pair);
                pair.clear();
            }
        }
        return sum;
    }
    ```
    

## 풀이2. 짝수 번째 값 계산

---

- 이렇게 페어에 대해 일일이 `min()` 값을 구하지 않아도 짝수 번째 인덱스의 값을 더하면 될 것 같다.
    - 정렬된 상태에서는 짝수 번째에 항상 작은 값이 위치하기 때문이다.
    - 불필요한 `min()` 계산이 생략되어 실행 속도도 더 빠를 것이다.

- 전체 코드
    
    ```java
    public int arrayPairSum(int[] nums) {
        int sum = 0;
        Arrays.sort(nums);
    
        // 앞에서부터 오름차순으로 인덱스 반복
        for (int i = 0; i < nums.length; i++) {
            // 짝수 번째일 때 값의 합 계산
            if (i % 2 == 0)
                sum += nums[i];
        }
        return sum;
    }
    ```
    

## 풀이3. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    fun arrayPairSum(nums: IntArray): Int {
        var sum = 0
        nums.sort()
    
        // 앞에서부터 오름차순으로 인덱스 반복
        for ((i, n) in nums.withIndex()) {
            // 짝수 번째일 때 값의 합 계산
            if (i % 2 == 0)
                sum += n
        }
        return sum
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 오름차순 풀이 | 41밀리초 |
| 2 | 짝수 번째 값 계산 | 11밀리초 |
| 3 | 코틀린 풀이 | 측정하지 않음 |

# 11. 자신을 제외한 배열의 곱

---

- [https://leetcode.com/problems/product-of-array-except-self/](https://leetcode.com/problems/product-of-array-except-self/)
- 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 엘리먼트의 곱셈 결과가 되도록 출력하라.
- 나의 풀이
    
    ```python
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        multiply = 1
        for i in range(len(nums)):
            result[i] = multiply
            multiply *= nums[i]
        
        multiply = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= multiply
            multiply *= nums[i]
        
        return result
    ```
    

## 풀이1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱하기

---

- 이 문제에는 중요한 제약 사항이 있다: 나눗셈을 하지 않고 O(n)에 풀이하라
- 가능한 풀이 방법은 한 가지뿐이다: 자기 자신을 제외하고 왼쪽의 곱셈 결과와 오른쪽의 곱셈 결과를 곱하는 방법
    - 공간 복잡도: O(n)
        - 별도의 리스트 변수를 만들고 그 변수에 우측 곱셈 결과를 넣으면
    - 공간 복잡도: O(1)
        - 기존 result 변수를 재활용한다면

- 전체 코드
    
    ```java
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        // 왼쪽 곱셈
        int p = 1;
        for (int i = 0; i < nums.length; i++) {
            result[i] = p;
            // 왼쪽 곱셈 결과
            p *= nums[i];
        }
        // 오른쪽 곱셈, 왼쪽 곱셈 결과에 차례대로 곱하기
        p = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            result[i] *= p;
            // 오른쪽 곱셈 결과
            p *= nums[i];
        }
        return result;
    }
    ```
    

## 풀이2. 코틀린 풀이

---

- 2가지 차이점이 있다.
    - 자바 풀이의 결과 변수는 원시형으로 지정했으나 코틀린은 원시형을 지원하지 않기 때문에 `IntArray`로 선언했다.
    - 인덱스를 순회할 때 자바는 앞에서 한 번, 뒤에서 한 번 순회했다. 사실 가독성이 좋진 않다.
        - 코틀린은 매우 직관적으로 표현이 가능하다.

- 전체 코드
    
    ```kotlin
    fun productExceptSelf(nums: IntArray): IntArray {
        val result = IntArray(nums.size)
        // 왼쪽 곱셈
        var p = 1
        for (i in nums.indices) {
            result[i] = p
            // 왼쪽 곱셈 결과
            p *= nums[i]
        }
        // 오른쪽 곱셈, 왼쪽 곱셈 결과에 차례대로 곱하기
        p = 1
        for (i in nums.indices.reversed()) {
            // 왼쪽 곱셈 결과에 차례대로 곱한 최종 결과
            result[i] *= p
            // 오른쪽 곱셈 결과
            p *= nums[i]
        }
        return result
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱하기 | 2밀리초 |
| 2 | 코틀린 풀이 | 측정하지 않음 |

# 12. 주식을 사고팔기 가장 좋은 시점

---

- [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
- 나의 풀이
    
    ```python
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buyIdx, sellIdx, minIdx, answer = 0, 1, 0, 0
    
        while sellIdx < len(prices):
            if prices[buyIdx] > prices[minIdx]:
                buyIdx = minIdx
            answer = max(answer, prices[sellIdx] - prices[buyIdx])
                
            if prices[sellIdx] < prices[minIdx]:
                minIdx = sellIdx
            sellIdx += 1
    
        return answer
    ```
    

## 풀이1. 브루트 포스로 계산

---

- 처음부터 O(n^2)으로 사고팔고를 반복하면, 마지막에 최대 이익을 산출할 수 있을 것 같다.

- 전체 코드
    
    ```java
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        // 구매 시점 순회, 처음부터 끝까지 차례대로 반복한다.
        for (int i = 0; i < prices.length; i++) {
            // 판매 시점 순회, 구매 다음부터 끝까지 차례대로 반복한다.
            for (int j = i + 1; j < prices.length; j++) {
                // 판매 시점 가격에서 구매 시점 가격을 뺄 때 가장 높은 금액 찾기
                maxProfit = Math.max(maxProfit, prices[j] - prices[i]);
            }
        }
        return maxProfit;
    }
    ```
    
    - 하지만 안타깝게도 이 풀이는 타임아웃으로 풀리지 않는다.

## 풀이2. 저점과 현재 값과의 차이 계산

---

- 현재 값을 가리키는 포인터가 우측으로 이동하면서 이전 상태의 저점을 기준으로 가격 차이를 계산하고, 만약 가격이 클 경우 최댓값을 계속 교체해 나가는 형태로 O(n) 풀이가 가능할 것 같다.

- 전체 코드
    
    ```java
    public int maxProfit(int[] prices) {
        // 최대 이익은 0, 저점은 임시로 첫 번째 값으로 지정
        int maxProfit = 0, minPrice = prices[0];
        // 현재 값을 우측으로 차례대로 이동하면서 계산
        for (int price : prices) {
            // 지금까지 저점 계산
            minPrice = Math.min(minPrice, price);
            // 현재 값과 저점의 차이가 최대 이익인 경우 교체
            maxProfit = Math.max(maxProfit, price - minPrice);
        }
        return maxProfit;
    }
    ```
    

## 풀이3. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    fun maxProfit(prices: IntArray): Int {
        var maxProfit = 0
        // 임시로 첫 번째 값을 저점으로 지정
        var minPrice = prices[0]
        // 현재 값을 우측으로 차례대로 이동하면서 계산
        for (price in prices) {
            // 지금까지 저점 계산
            minPrice = minPrice.coerceAtMost(price)
            // 현재 값과 저점의 차이가 최대 이익인 경우 교체
            maxProfit = maxProfit.coerceAtLeast(price - minPrice)
        }
        return maxProfit
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 브루트 포스로 계산 | 타임아웃 |
| 2 | 저점과 현재 값의 차이 계산 | 2밀리초 |
| 3 | 코틀린 풀이 | 측정하지 않음 |