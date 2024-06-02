# 9장. 스택, 큐

### 스택

---

- 가장 나중에 삽입된 엘리먼트가 가장 먼저 처리되는 후입선출(LIFO)로 처리되는 추상 자료형이다.
    - 콜 스택(Call Stack)이라 하여 컴퓨터 프로그램의 서브루틴에 대한 정보를 저장하는 자료구조에도 널리 활용된다.
    - 컴파일러가 출력하는 에러도 스택처럼 맨 마지막 에러가 가장 먼저 출력되는 순서를 보인다.
- 메모리 영역에서 LIFO 형태로 할당하고 접근하는 구조인 아키텍처 레벨의 하드웨어 스택의 이름으로도 널리 사용된다.
- 꽉 찬 스택에 엘리먼트를 삽입하고자 할 때 스택에 엘리먼트가 넘쳐서 에러가 발생하는 것을 스택 버퍼 오버플로라고 부른다.

### 큐

---

- 가장 먼저 삽입된 엘리먼트가 가장 먼저 처리되는 선입선출(FIFO) 순으로 처리되는 추상 자료형이다.
- 큐는 상대적으로 스택에 비해서는 쓰임새가 적다.
    - 그러나 이후에 살펴보게 될 데크(Deque)나 우선순위 큐(Priority Queue) 같은 큐의 변형들은 여러 분야에서 매우 유용하게 쓰인다.
    - 너비 우선 탐색(Breadth-First Search(BFS))이나 캐시 등을 구현할 때도 널리 사용된다.

### 자바에서 활용하기

---

- 자바의 큐 선언
    - 이 책에서도 특별한 이유가 없는 한 큐 선언은 이와 같이 `LinkedList`를 구현체로 한 `Queue` 인터페이스를 사용하겠다.
        
        ```java
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        queue.offer(2);
        queue.poll(); // 1
        ```
        
- 자바의 스택 선언
    - `Stack` 클래스는 자바 1.2가 채 등장하기 전, 아직 CPU 코어가 하나밖에 없던 시절에 나온 자료형으로, 모든 작업에 잠금(Lock)이 수행되는 `Vector`라는 자료형을 기반으로 한다.
        - 읽기 작업도 동시에 한 번밖에 수행할 수 없음
    - 자바는 하위 호환성을 매우 중요하게 여기는 언어다.
        - 개선
            - `Vector` → `ArrayList`
            - `Stack` → `Deque`
    - 이 책에서도 스택이 필요할 때 `ArrayDeque`를 구현체로 한 `Deque` 인터페이스를 사용할 것이며, 이는 자바 공식 문서에서 권고하고 있는 내용이기도 하다.
        
        ```java
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(1);
        stack.push(2);
        stack.pop(); // 2
        ```
        
- 스레드 안전이 필요한 경우
    - 새로운 자료형을 사용하라고 했지만 성능이 좋은 대신 한 가지 문제가 있다.
        
        → 스레드 안전(Thread-Safe)하지 않다는 점
        
    - `LinkedBlockingDeque` 또는 `ConcurrentLinkedDeque`를 사용하면 된다.
    - 스레드 안전이 필요한 해시 테이블(`Hashtable`)의 경우 `ConcurrentHashMap` 같은 자료형을 사용하면 된다.

# 20. 유효한 괄호

---

- [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)
- 대중소 세 종류 괄호로 된 입력값이 유효한지 판별하라.
- 나의 풀이
    
    ```python
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "{": "}", "[": "]"}
        nextArr = []
        
        if len(s) % 2 != 0:
            return False
    
        for c in s:
            if c not in dic:
                if len(nextArr) == 0 or c != nextArr.pop():
                    return False
            else:
                nextArr.append(dic[c])
    
        return len(nextArr) == 0
    ```
    

## 풀이1. 스택 일치 여부 판별

---

- 열림 괄호인 `[`, `{`, `(`는 스택에 푸시하고, 닫힘 괄호인 `)`, `}`, `]`를 만날 때 스택에서 팝(Pop)한 결과가 매핑 테이블 결과와 매칭되는지 확인하면 된다.

- 전체 코드
    
    ```java
    public boolean isValid(String s) {
        // 유효성 검증을 위한 스택 선언
        Deque<Character> stack = new ArrayDeque<>();
        // 유효성 검증을 위한 매핑 테이블
        Map<Character, Character> table = new HashMap<>() {{
            put(')', '(');
            put('}', '{');
            put(']', '[');
        }};
    
        // 문자열을 문자 단위로 반복
        for (int i = 0; i < s.length(); i++) {
            // 닫힘 괄호가 아닌 경우 스택에 푸시
            if (!table.containsKey(s.charAt(i))) {
                stack.push(s.charAt(i));
                // 중간에 스택이 비거나 팝 결과가 열림 괄호가 아닌 경우 유효하지 않음
            } else if (stack.isEmpty() || table.get(s.charAt(i)) != stack.pop()) {
                return false;
            }
        }
        // 유효한 입력이 되려면 반복 완료 후 스택이 비어야 한다.
        return stack.size() == 0;
    }
    ```
    

## 풀이2. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    fun isValid(s: String): Boolean {
        // 유효성 검증을 위한 스택 선언
        val stack: Deque<Char> = ArrayDeque()
        // 유효성 검증을 위한 매핑 테이블
        val table: Map<Char, Char> = mapOf(
            ')' to '(',
            '}' to '{',
            ']' to '['
        )
    
        // 문자열을 문자 단위로 반복
        for (i in s.indices) {
            // 닫힘 괄호가 아닌 경우 스택에 푸시
            if (!table.containsKey(s[i])) {
                stack.push(s[i])
                // 중간에 스택이 비거나 팝 결과가 열림 괄호가 아닌 경우 유효하지 않음
            } else if (stack.isEmpty() || table[s[i]] !== stack.pop()) {
                return false
            }
        }
        // 유효한 입력이 되려면 반복 완료 후 스택이 비어야 한다.
        return stack.size == 0
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 스택 일치 여부 판별 | 2밀리초 |
| 2 | 코틀린 풀이 | 측정하지 않음 |

# 21. 중복 문자 제거

---

- [https://leetcode.com/problems/remove-duplicate-letters/](https://leetcode.com/problems/remove-duplicate-letters/)
- 중복된 문자를 제외하고 사전식 순서(Lexicographical Order)로 나열하라.
- 나의 풀이
    
    ```python
    def removeDuplicateLetters(self, s: str) -> str:
        counter = {}
        seen = set()
        stack = []
    
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
    
        for c in s:
            counter[c] -= 1
    
            if c in seen:
                continue
    
            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
    
            stack.append(c)
            seen.add(c)
    
        return ''.join(stack)
    ```
    

## 풀이1. 재귀를 이용한 분리

---

- ex> "cbacdcbc" 기준
    - 중복 문자를 제외한 알파벳순으로 문자열 입력값을 모두 정렬한 다음 가장 빠른 a부터 접미사 suffix를 분리해 확인한다.
        - a는 가장 빠른 알파벳일 뿐만 아니라 문자열에서 b, c, d도 뒤에 있기 때문에 가장 먼저 정답으로 추출할 수 있다.
    - 이제 a가 빠지고 cdcbc가 남은 상태에서 다음 알파벳 순서는 b이지만 b를 추출하면 그 뒤에 남은 문자가 c밖에 없기 때문에 추출할 수 없다.
    - 분리 가능 여부는 다음 코드와 같이 전체 집합과 접미사 집합이 일치하는지 여부로 판별할 수 있다.
        
        ```java
        if (toSortedSet(s).equals(toSortedSet(suffix))) {
        ...
        ```
        
- 이후에 이어지는 모든 c를 `replace()`로 제거한다. 이렇게 하면 일종의 분할 정복과 비슷한 형태로 접미사 suffix의 크기는 점점 줄어들고 더 이상 남지 않을 때 백트래킹되면서 결과가 조합된다.

- 전체 코드
    
    ```java
    public Set<Character> toSortedSet(String s) {
        // 문자열을 문자 단위 집합으로 저장할 변수 선언
        Set<Character> set = new TreeSet<>(new Comparator<Character>() {
            // 비교 메소드 재정의
            @Override
            public int compare(Character o1, Character o2) {
                // 동일한 문자이면 무시
                if (o1 == o2) {
                    return 0;
                    // 새로운 문자(o1)가 기본 문자(o2)보다 크면 뒤에 위치
                } else if (o1 > o2) {
                    return 1;
                } else {
                    return -1;
                }
            }
        });
    
        // 문자열을 문자 단위로 집합에 저장, 정렬된 상태로 저장된다.
        for (int i = 0; i < s.length(); i++) {
            set.add(s.charAt(i));
        }
        return set;
    }
    
    public String removeDuplicateLetters(String s) {
        // 정렬된 문자열 집합 순회
        for (char c : toSortedSet(s)) {
            // 해당 문자가 포함된 위치부터 접미사로 지정
            String suffix = s.substring(s.indexOf(c));
            // 전체 집합과 접미사 집합이 일치하면 해당 문자 정답에 추가하고 재귀 호출 진행
            if (toSortedSet(s).equals(toSortedSet(suffix))) {
                return c + removeDuplicateLetters(suffix.replace(String.valueOf(c), ""));
            }
        }
        return "";
    }
    ```
    

## 풀이2. 스택을 이용한 문자 제거

---

- 입력 문자열을 문자 단위로 처리하면서 스택 변수 stack에는 다음과 같이 앞에서부터 문자를 차례대로 쌓아나가고, seen 변수에는 처리한 걸로 선언하면서 반복한다.
    
    ```java
    Map<Character, Integer> counter = new HashMap<>();
    Map<Character, Boolean> seen = new HashMap<>();
    Deque<Character> stack = new ArrayDeque<>();
    
    stack.push(c);
    seen.put(c, true);
    ```
    
- 만약 스택에 있는 문자가 현재 문자보다 더 뒤에 붙여야 할 문자이고 아직 처리해야 할 문자가 남아 있다면(카운터가 0 이상이라면), 다음과 같이 스택에 쌓아둔 걸 꺼내서 없앤다.
    
    ```java
    while (!stack.isEmpty() && stack.peek() > c && counter.get(stack.peek()) > 0)
        seen.put(stack.pop(), false);
    ```
    
- 카운터가 0 이상인 d와 b는 뒤에 다시 붙일 문자가 남아 있기 때문에 이처럼 스택에서 제거가 가능하다. 또한 이미 처리한 문자는 아무런 처리도 하지 않고 다음과 같이 바로 건너뛴다.
    
    ```java
    if (seen.get(c) != null && seen.get(c) == true)
        continue;
    ```
    

- 전체 코드
    
    ```java
    public String removeDuplicateLetters(String s) {
        // 문자 개수를 계산해서 담아둘 변수 선언
        Map<Character, Integer> counter = new HashMap<>();
        // 이미 처리한 문자 여부를 확인하기 위한 변수 선언
        Map<Character, Boolean> seen = new HashMap<>();
        // 문제 풀이에 사용할 스택 선언
        Deque<Character> stack = new ArrayDeque<>();
    
        // 문자별 개수 계산
        for (char c : s.toCharArray()) {
            counter.put(c, counter.get(c) == null ? 1 : counter.get(c) + 1);
        }
    
        for (char c : s.toCharArray()) {
            // 현재 처리하는 문자는 카운터에서 -1 처리
            counter.put(c, counter.get(c) - 1);
            // 이미 처리한 문자는 건너뛴다.
            if (seen.get(c) != null && seen.get(c) == true) {
                continue;
            }
            // 스택에 있는 문자가 현재 문자보다 더 뒤에 붙여야 할 문자라면 스택에서 제거하고 처리하지 않은걸로 표시
            while (!stack.isEmpty() && stack.peek() > c && counter.get(stack.peek()) > 0) {
                seen.put(stack.pop(), false);
            }
            // 현재 문자를 스택에 삽입
            stack.push(c);
            // 현재 문자를 처리한 걸로 선언
            seen.put(c, true);
        }
    
        // 스택에 있는 문자를 큐 순서대로 추출하여 리턴
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pollLast());
        }
        return sb.toString();
    }
    ```
    
    - `peek()`: 전통적인 스택 추상 자료형에는 정의되지 않은, 다음에 추출될 엘리먼트를 조회하는 연산

## 풀이3. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    fun removeDuplicateLetters(s: String): String {
        // 문자 개수를 계산해서 담아둘 변수 선언
        val counter: MutableMap<Char, Int> = HashMap()
        // 이미 처리한 문자 여부를 확인하기 위한 변수 선언
        val seen: MutableMap<Char, Boolean> = HashMap()
        // 문제 풀이에 사용할 스택 선언
        val stack: Deque<Char> = ArrayDeque()
    
        // 문자별 개수 계산
        for (c in s) {
            counter[c] = counter.getOrDefault(c, 0) + 1
        }
    
        for (c in s) {
            // 현재 처리하는 문자는 카운터에서 -1 처리
            counter[c] = counter[c]!! - 1
            // 이미 처리한 문자는 건너뛴다.
            if (seen[c] == true) {
                continue
            }
    
            // 스택에 있는 문자가 현재 문자보다 더 뒤에 붙여야 할 문자라면 스택에서 제거하고 처리하지 않은걸로 표시
            while (!stack.isEmpty() && stack.peek() > c && counter[stack.peek()]!! > 0) {
                seen[stack.pop()] = false
            }
            // 현재 문자를 스택에 삽입
            stack.push(c)
            // 현재 문자를 처리한 걸로 선언
            seen[c] = true
        }
    
        // 스택에 있는 문자를 큐 순서대로 추출하여 리턴
        val sb = StringBuilder()
        while (!stack.isEmpty()) {
            sb.append(stack.pollLast())
        }
        return sb.toString()
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 재귀를 이용한 분리 | 151밀리초 |
| 2 | 스택을 이용한 문자 제거 | 8밀리초 |
| 3 | 코틀린 풀이 | 측정하지 않음 |

# 22. 일일 온도

---

- [https://leetcode.com/problems/daily-temperatures/](https://leetcode.com/problems/daily-temperatures/)
- 매일의 온도 리스트를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.
- 나의 풀이
    
    ```python
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
    
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last = stack.pop()
                result[last] = i - last
            stack.append(i)
    
        return result
    ```
    

## 풀이1. 스택 값 비교

---

- 7장에서 풀어본 8번 ‘빗물 트래핑’ 문제와 유사한 방법으로 풀이할 수 있다.
    - 현재의 인덱스를 계속 스택에 쌓아두다가, 이전보다 상승하는 지점에서 현재 온도와 스택에 쌓아둔 인덱스 지점의 온도 차이를 비교해서, 더 높다면 다음과 같이 스택의 값을 pop()으로 꺼내고 현재 인덱스와 스택에 쌓아둔 인덱스의 차이를 정답으로 업데이트 한다. 그리고 현재 인덱스를 다시 스택에 삽입한다.
        
        ```java
        while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
            int last = stack.pop();
            result[last] = i - last;
        }
        stack.push(i);
        ```
        

- 전체 코드
    
    ```java
    public int[] dailyTemperatures(int[] temperatures) {
        // 결과를 담을 정수형 배열 선언
        int[] result = new int[temperatures.length];
        // 결과 처리를 위한 스택 선언
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < temperatures.length; i++) {
            //현재 온도가 스택에 있는 온도보다 높다면 꺼내서 결과를 업데이트한다.
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int last = stack.pop();
                // 결과 업데이트
                result[last] = i - last;
            }
            stack.push(i);
        }
        return result;
    }
    ```
    

## 풀이2. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        // 결과를 담을 정수형 배열 선언
        val result = IntArray(temperatures.size)
        // 결과 처리를 위한 스택 선언
        val stack: Deque<Int> = ArrayDeque()
        for (i in temperatures.indices) {
            //현재 온도가 스택에 있는 온도보다 높다면 꺼내서 결과를 업데이트한다.
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                val last = stack.pop()
                // 결과 업데이트
                result[last] = i - last
            }
            stack.push(i)
        }
        return result
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 스택 값 비교 | 185밀리초 |
| 2 | 코틀린 풀이 | 측정하지 않음 |

# 23. 큐를 이용한 스택 구현

---

- [https://leetcode.com/problems/implement-stack-using-queues/](https://leetcode.com/problems/implement-stack-using-queues/)
- 큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
    - push(x): 엘리먼트 x를 스택에 삽입한다.
    - pop(): 스택의 첫 번째 엘리먼트를 삭제한다.
    - top(): 스택의 첫 번째 엘리먼트를 가져온다.
    - empty(): 스택이 비어 있는지 여부를 리턴한다.
- 나의 풀이
    
    ```python
    class MyStack:
        def __init__(self):
            self.queue = []
    
        def push(self, x: int) -> None:
            self.queue.append(x)
    
        def pop(self) -> int:
            return self.queue.pop()
    
        def top(self) -> int:
            return self.queue[-1]
    
        def empty(self) -> bool:
            return len(self.queue) == 0
    ```
    

## 풀이1. push() 할 때 큐를 이용해 재정렬

---

- 대개 스택은 연결 리스트로 구현하고 큐는 배열로 구현하지만, 이처럼 반대로 큐를 연결 리스트로 구현하는 것도 얼마든지 가능하다.
- 가장 복잡한 부분은 아마 push()가 될 것이다.
    - 엘리먼트를 삽입한 후에 방금 삽입한 엘리먼트를 맨 앞에 두는 상태로 전체를 재정렬하면 나머지는 기본적인 큐 연산으로 쉽게 구현이 가능할 것이다. → 시간 복잡도: O(n)
        
        ```java
        queue.add(x);
        for (int i = 1; i < queue.size(); i++) {
            queue.add(queue.remove());
        }
        ```
        
- 전체 코드
    
    ```java
    class MyStack {
        // 큐 변수, 구현체는 LinkedList로 선언
        Queue<Integer> queue = new LinkedList<>();
    
        public void push(int x) {
            // 엘리먼트 삽입
            queue.add(x);
            // 맨 앞에 두는 상태로 전체 재정렬
            for (int i = 1; i < queue.size(); i++) {
                queue.add(queue.remove());
            }
        }
    
        public int pop() {
            // 재정렬한 상태이므로 큐 연산으로 추출
            return queue.remove();
        }
    
        public int top() {
            // 재정렬한 상태이므로 큐 연산으로 조회
            return queue.peek();
        }
    
        public boolean empty() {
            // 크기를 비교해 비어 있는지 확인
            return queue.size() == 0;
        }
    }
    ```
    

## 풀이2. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    class MyStack {
        // 큐 변수, 구현체는 LinkedList로 선언
        val queue: Queue<Int> = LinkedList()
    
        fun push(x: Int) {
            // 엘리먼트 삽입
            queue.add(x)
            // 맨 앞에 두는 상태로 전체 재정렬
            for (i in 1 until queue.size) {
                queue.add(queue.remove())
            }
        }
    
        fun pop(): Int {
            // 재정렬한 상태이므로 큐 연산으로 추출
            return queue.remove()
        }
    
        fun top(): Int {
            // 재정렬한 상태이므로 큐 연산으로 조회
            return queue.peek()
        }
    
        fun empty(): Boolean {
            // 크기를 비교해 비어 있는지 확인
            return queue.size == 0
        }
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | push() 할 때 큐를 이용해 재정렬 | 0밀리초 |
| 2 | 코틀린 풀이 | 측정하지 않음 |

# 24. 스택을 이용한 큐 구현

---

- [https://leetcode.com/problems/implement-queue-using-stacks/](https://leetcode.com/problems/implement-queue-using-stacks/)
- 스택을 이용해 다음 연산을 지원하는 큐를 구현하라.
    - push(x): 엘리먼트 x를 큐 마지막에 삽입한다.
    - pop(): 큐 처음에 있는 엘리먼트를 제거한다.
    - peek(): 큐 처음에 있는 엘리먼트를 조회한다.
    - empty(): 큐가 비어 있는지 여부를 리턴한다.
- 나의 풀이
    
    ```python
    class MyQueue:
        def __init__(self):
            self.queue = []
    
        def push(self, x: int) -> None:
            self.queue.append(x)
    
        def pop(self) -> int:
            target = self.queue[0]
            self.queue = self.queue[1:]
            return target
    
        def peek(self) -> int:
            return self.queue[0]
    
        def empty(self) -> bool:
            return len(self.queue) == 0
    ```
    

## 풀이1. 스택 2개 사용

---

- 지난 풀이에서는 큐에 엘리먼트를 삽입한 후 전체를 재정렬해서 맨 앞의 엘리먼트부터 끄집어냈다. 그렇게 원래의 큐에 추출 결과를 덧붙여 나가는 형태로, 추가 공간 없이 풀이했다.
- 이번에는 앞서와는 다른 중요한 차이점이 있다. 가장 먼저 삽입된 아이템을 끄집어내야 하는데, 스택은 아무리 추가, 삭제를 반복해도 가장 마지막에 삽입된 아이템만 넣고 빼기를 반복한다는 점이다.
    - 이 문제를 풀기 위해서는 2개의 스택이 필요하다. 특히 추출 시 pop()과 조회 시 peek()는 결국 같은 데이터를 끄집어낸다는 점에 착안해, 이번에는 pop()을 할 때 peek()을 호출해 한 번에 처리하는 형태로 다음과 같이 구현했다. → 시간 복잡도: O(1)
        
        ```java
        if (output.isEmpty()) {
            while (!input.isEmpty()) {
                output.push(input.pop());
            }
        }
        ```
        

- 전체 코드
    
    ```java
    class MyQueue {
        // 삽입할 때 사용하는 스택 선언
        Deque<Integer> input = new ArrayDeque<>();
        // 추출할 때 사용하는 스택 선언
        Deque<Integer> output = new ArrayDeque<>();
    
        public void push(int x) {
            // 삽입은 삽입 스택에 단순 추가
            input.push(x);
        }
    
        public int pop() {
            // 추출 스택 조회하면서 비어 있다면 처리 진행
            peek();
            // 추출 스택에 있는 마지막 값 추출
            return output.pop();
        }
    
        public int peek() {
            // 추출 스택에 저장된 게 없다면 진행
            if (output.isEmpty()) {
                // 삽입 스택이 비워질 때까지 진행
                while (!input.isEmpty()) {
                    // 삽입 스택에서 추출한 결과를 추출 스택에 삽입(역순으로 저장된다)
                    output.push(input.pop());
                }
            }
            // 가장 나중에 삽입된 결과 조회
            return output.peek();
        }
    
        public boolean empty() {
            // 두 스택이 모두 비어야 비어 있는 것으로 처리
            return input.isEmpty() && output.isEmpty();
        }
    }
    ```
    

## 풀이2. 코틀린 풀이

---

- 전체 코드
    
    ```java
    class MyQueue {
        // 삽입할 때 사용하는 스택 선언
        var input: Deque<Int> = ArrayDeque()
        // 추출할 때 사용하는 스택 선언
        var output: Deque<Int> = ArrayDeque()
    
        fun push(x: Int) {
            // 삽입은 삽입 스택에 단순 추가
            input.push(x)
        }
    
        fun pop(): Int {
            // 추출 스택 조회하면서 비어 있다면 처리 진행
            peek()
            // 추출 스택에 있는 마지막 값 추출
            return output.pop()
        }
    
        fun peek(): Int {
            // 추출 스택에 저장된 게 없다면 진행
            if (output.isEmpty()) {
                // 삽입 스택이 비워질 때까지 진행
                while (!input.isEmpty()) {
                    // 삽입 스택에서 추출한 결과를 추출 스택에 삽입(역순으로 저장된다)
                    output.push(input.pop())
                }
            }
            // 가장 나중에 삽입된 결과 조회
            return output.peek()
        }
    
        fun empty(): Boolean {
            // 두 스택이 모두 비어야 비어 있는 것으로 처리
            return input.isEmpty() && output.isEmpty()
        }
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 스택 2개 사용 | 1밀리초 |
| 2 | 코틀린 풀이 | 측정하지 않음 |

# 25. 원형 큐 디자인

---

- [https://leetcode.com/problems/design-circular-queue/](https://leetcode.com/problems/design-circular-queue/)
- 원형 큐를 디자인하라. 큐가 비어 있다면 -1을 리턴하며, 해당 원형 큐의 사용 예는 다음과 같다.
- 나의 풀이
    
    ```java
    
    ```
    

## 풀이1. 배열을 이용한 풀이

---

- 원형 큐: FIFO 구조를 지닌다는 점에서 기존의 큐와 동일하다. 그러나 마지막 위치가 시작 위치와 연결되는 원형 구조를 띠기 때문에, 링 버퍼라고도 부른다.
    - 장점: 앞쪽에 공간이 남아 있다면 앞쪽으로 추가할 수 있도록 재활용이 가능하다.
    - 동작 원리: 투 포인터와도 비슷하다. 마지막 위치와 시작 위치를 연결하는 원형 구조를 만들고, 엘리먼트의 시작점과 끝점을 따라 투 포인터가 움직인다.

- 전체 코드
    
    ```java
    class MyCircularQueue {
        int[] q;
        int front = 0, rear = -1, len = 0;
    
        public MyCircularQueue(int k) {
            // k 크기의 원형 큐로 사용할 배열 선언
            this.q = new int[k];
        }
    
        public boolean enQueue(int value) {
            // 꽉 차 있지 않다면 삽입 진행
            if (!this.isFull()) {
                // rear 포인터 한 칸 앞으로 이동, 최대 크기를 초과하면 나머지 위치로 이동
                this.rear = (this.rear + 1) % this.q.length;
                // rear 위치에 값 삽입
                this.q[rear] = value;
                // 현재 큐의 크기 계산
                this.len++;
                return true;
            } else {
                return false;
            }
        }
    
        public boolean deQueue() {
            // 텅 비어 있지 않다면 삭제 진행
            if (!this.isEmpty()) {
                // front 포인터 한 칸 앞으로 이동, 최대 크기를 초과하면 나머지 위치로 이동
                this.front = (this.front + 1) % this.q.length;
                // 현재 큐의 크기 계산
                this.len--;
                return true;
            } else {
                return false;
            }
        }
    
        public int Front() {
            // 맨 앞의 값을 가져온다.
            return (this.isEmpty()) ? -1 : this.q[this.front];
        }
    
        public int Rear() {
            // 맨 뒤의 값을 가져온다.
            return (this.isEmpty()) ? -1 : this.q[this.rear];
        }
    
        public boolean isEmpty() {
            // 현재 큐의 크기가 0이면 비어 있음
            return this.len == 0;
        }
    
        public boolean isFull() {
            // 현재 큐의 크기가 전체 큐의 크기와 일치하면 꽉 차 있음
            return this.len == this.q.length;
        }
    }
    
    ```
    

## 풀이2. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    class MyCircularQueue(k: Int) {
        // k 크기의 원형 큐로 사용할 배열 선언
        var q = IntArray(k)
        var front = 0
        var rear = -1
        var len = 0
    
        fun enQueue(value: Int): Boolean {
            // 꽉 차 있지 않다면 삽입 진행
            return if (!isFull()) {
                // rear 포인터 한 칸 앞으로 이동, 최대 크기를 초과하면 나머지 위치로 이동
                this.rear = (this.rear + 1) % this.q.size
                // rear 위치에 값 삽입
                this.q[rear] = value
                // 현재 큐의 크기 계산
                this.len++
                true
            } else {
                false
            }
        }
    
        fun deQueue(): Boolean {
            // 텅 비어 있지 않다면 삭제 진행
            return if (!this.isEmpty()) {
                // front 포인터 한 칸 앞으로 이동, 최대 크기를 초과하면 나머지 위치로 이동
                this.front = (this.front + 1) % this.q.size
                // 현재 큐의 크기 계산
                this.len--
                true
            } else {
                false
            }
        }
    
        fun Front(): Int {
            // 맨 앞의 값을 가져온다.
            return if (this.isEmpty()) -1 else q[front]
        }
    
        fun Rear(): Int {
            // 맨 뒤의 값을 가져온다.
            return if (this.isEmpty()) -1 else q[rear]
        }
    
        fun isEmpty(): Boolean {
            // 현재 큐의 크기가 0이면 비어 있음
            return this.len == 0
        }
    
        fun isFull(): Boolean {
            // 현재 큐의 크기가 전체 큐의 크기와 일치하면 꽉 차 있음
            return this.len == this.q.size
        }
    }
    ```