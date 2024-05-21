# 8장. 연결 리스트

### 연결리스트

---

- 순서대로 저장되는 배열과의 가장 큰 차이점: 데이터 엘리먼트의 선형 집합이지만 데이터의 순서가 메모리에 물리적인 순서대로 저장되지는 않는다.
- 동적으로 새로운 노드를 삽입하거나 삭제하기가 간편하며, 연결 구조를 통해 물리 메모리를 연속적으로 사용하지 않아도 되기 때문에 관리도 쉽다.
- 탐색: O(n)
- 추가, 삭제, 추출: O(1)
- 자바에서 연결 리스트를 구현한 자료형: `LinkedList`
    - 이중 연결 리스트(Doubly Linked List)이기 때문에 삽입과 추출이 양방향 모두 가능하다.

# 13. 팰린드롬 연결 리스트

---

- [https://leetcode.com/problems/palindrome-linked-list/](https://leetcode.com/problems/palindrome-linked-list/)
- 연결 리스트가 팰린드롬 구조인지 판별하라.
- 나의 풀이
    
    ```python
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
    
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
    
        if fast:
            slow = slow.next
    
        rev = None
        while slow:
            next = slow.next
            slow.next = rev
            rev = slow
            slow = next
    
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
    
        return True
    ```
    

## 풀이1. 스택을 이용한 풀이

---

- 팰린드롬 여부를 판별하기 위해서는 앞뒤로 모두 추출할 수 있는 자료구조가 필요하다.
    - 그러나 일반적인 스택 자료형은 마지막 엘리먼트만 추출할 수 있다.
- 연결 리스트를 먼저 스택에 복사해 넣은 다음, 다시 연결 리스트를 앞에서부터 이동하면서 값을 조회하고, 스택은 `pop()`으로 추출하면서 뒤에서부터 값을 끄집어내어 함께 비교해본다.

- 전체 코드
    
    ```java
    public class ListNode {
        int val;
        ListNode next;
    
        ListNode() {
        }
    
        ListNode(int val) {
            this.val = val;
        }
    
        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }
    
    public boolean isPalindrome(ListNode head) {
        // 주의: 스택을 이렇게 선언하면 안 됨
        Stack<Integer> stack = new Stack<>();
        // 연결 리스트를 스택에 삽입
        ListNode node = head;
        while (node != null) {
            stack.add(node.val);
            node = node.next;
        }
    
        // 연결 리스트가 모두 빌 때까지 비교
        while (head != null) {
            // 연결 리스트와 스택에서 추출한 값을 비교해 팰린드롬 판별
            if (head.val != stack.pop()) {
                return false;
            }
            head = head.next;
        }
        return true;
    }
    ```
    
    - 여기서는 스택 선언을 `new Stack<>()`으로 했지만 사실 이 자료형은 더 이상 사용해선 안 된다.

## 풀이2. 데크를 이용한 풀이

---

- 데크(Deque): 이중 연결 리스트 구조로 양쪽 방향 모두 추출하는 데 시간 복잡도 O(1)이 걸린다.
    - 자바에서 데크는 다음과 같이 선언한다.
        
        ```java
        Deque<Integer> deque = new LinkedList<>();
        ```
        
- 데크 변수에 담은 이후에는 양 끝을 추출해 팰린드롬 여부를 확인한다.

- 전체 코드
    
    ```java
    public boolean isPalindrome(ListNode head) {
        Deque<Integer> deque = new LinkedList<>();
        // 연결 리스트를 스택에 삽입
        ListNode node = head;
        while (node != null) {
            deque.add(node.val);
            node = node.next;
        }
    
        // 연결 리스트가 모두 빌 때까지 비교
        while (!deque.isEmpty() && deque.size() > 1) {
            // 데크의 양 끝을 추출해 팰린드롬 여부 확인
            if (deque.pollFirst() != deque.pollLast()) {
                return false;
            }
        }
        return true;
    }
    ```
    
    - 데크 풀이가 앞서의 풀이에 비해 실행 속도도 더 빠르다.

## 풀이3. 러너를 이용한 우아한 풀이

---

- 빠른 러너와 느린 러너를 각각 출발시키면, 빠른 러너가 끝에 다다를 때 느린 러너는 정확히 중간 지점에 도달하게 될 것이다.
    - 느린 러너가 중간까지 이동한 후에는 나머지 경로를 역순으로 하여 연결 리스트 rev를 만들어나간다.
    - 빠른 러너인 fast는 두 칸씩, 느린 러너인 slow는 한 칸씩 이동하며 끝까지 이동할 것이다.
- 입력값이 홀수일 때와 짝수일 때 처리가 다른데, 홀수일 때는 느린 러너가 한칸 더 앞으로 이동해 중앙의 값을 빗겨나가야 한다.

- 전체 코드
    
    ```java
    public boolean isPalindrome(ListNode head) {
        ListNode fast = head, slow = head;
        // 빠른 러너가 끝까지 갈 때까지 느린 러너와 함께 진행
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        // 홀수 개일 때 느린 러너가 한 칸 더 앞으로 가도록 처리
        if (fast != null) {
            slow = slow.next;
        }
    
        // 중간에 도달한 느린 러너를 기준으로 하여 역순 연결 리스트를 만든다.
        ListNode rev = null;
        while (slow != null) {
            // 느린 러너로 역순 연결 리스트 rev를 만들어나간다.
            ListNode next = slow.next;
            slow.next = rev;
            rev = slow;
            slow = next;
        }
    
        // rev 연결 리스트를 끝까지 이동하며 비교
        while (rev != null) {
            // 역순 연결 리스트 rev와 기존 연결 리스트 head를 차례대로 비교
            if (rev.val != head.val) {
                return false;
            }
            rev = rev.next;
            head = head.next;
        }
        return true;
    }
    ```
    
    - 아무런 자료형을 사용하지 않고 단순히 러너 기법만 활용해서 그런지 매우 빠르게 실행된다.
    - 연결 리스트를 다른 자료형으로 변환하거나 편법을 사용하지 않고 그 자리에서 바로 풀이함으로써 좀 더 연결 리스트답게 우아한 방식으로 풀 수 있다.

## 풀이4. 코틀린 풀이

---

- 풀이 #3이 가장 빠르고 우아한 풀이이지만, 단순히 러너 기법을 활용한 것 외에는 코틀린으로 변환한다고 해서 특별히 달라질 만한 부분이 없다.
    
    → 그러므로 여기서는 풀이 #2를 코틀린으로 변환
    

- 전체 코드
    
    ```kotlin
    class ListNode(val `val`: Int, var next: ListNode? = null)
    
    fun isPalindrome(head: ListNode?): Boolean {
        val deque: Deque<Int> = LinkedList()
        // 연결 리스트를 스택에 삽입
        var node = head
        while (node != null) {
            deque.add(node.`val`)
            node = node.next
        }
    
        // 데크가 모두 비거나(짝수 개일 때) 1개 이하(홀수 개일 때)가 될 때까지 비교
        while (!deque.isEmpty() && deque.size > 1) {
            // 데크의 양 끝을 추출해 팰린드롬 여부 확인
            if (deque.pollFirst() !== deque.pollLast()) {
                return false
            }
        }
        return true
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 스택을 이용한 풀이 | 43밀리초 |
| 2 | 데크를 이용한 풀이 | 28밀리초 |
| 3 | 러너를 이용한 우아한 풀이 | 4밀리초 |
| 4 | 코틀린 풀이 | 측정하지 않음 |

<aside>
💡 러너 기법

- 러너(Runner): 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법. 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다.
- 대개 빠른 러너는 두 칸씩 건너뛰고 느린 러너는 한 칸씩 이동하게 한다. 빠른 러너가 연결 리스트의 끝에 도달하면, 느린 러너는 정확히 연결 리스트의 중간 지점을 가리키게 된다.
    - 중간 위치를 찾아내면 전체 길이를 알아낼 수 있고, 여기서부터 값을 비교하거나 뒤집기를 시도하는 등 여러모로 활용할 수 있어 연결 리스트 문제에서는 반드시 쓰이는 기법이기도 하다.
</aside>

# 14. 두 정렬 리스트의 병합

---

- [https://leetcode.com/problems/merge-two-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/)
- 정렬되어 있는 두 연결 리스트를 합쳐라.
- 나의 풀이
    
    ```python
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        cur = answer
        
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
    
        cur.next = list1 or list2
        
        return answer.next
    ```
    

## 풀이1. 재귀 구조로 연결

---

- 전체 코드
    
    ```java
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // 두 노드 중 한쪽이 널이면 널이 아닌 노드를 리턴
        if (list1 == null) return list2;
        if (list2 == null) return list1;
    
        // l2가 더 크면 l1에 재귀 호출 결과를 엮고 l1을 리턴
        if (list1.val < list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
            // l1이 더 크거나 같으면 l2에 재귀 호출 결과를 엮고 l2를 리턴
        } else {
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }
    ```
    

### 참고: **같은 뎁스 때, 연결 리스트 끝까지 탐색**

---

- `while` 문을 사용한 탐색
    - 장점
        - 메모리 효율성: `while` 반복문은 추가적인 스택 프레임을 생성하지 않기 때문에, 재귀 호출에 비해 메모리 사용이 효율적입니다. 연결 리스트를 끝까지 탐색하는 과정에서 메모리 사용량이 중요한 요소라면, `while` 문이 더 나은 선택일 수 있습니다.
        - 이해하기 쉬움: 반복문은 일반적으로 재귀보다 이해하기 쉬울 수 있으며, 디버깅하기도 더 간단합니다.
    - 단점
        - 유연성 부족: 특정 상황에서 재귀 함수가 제공할 수 있는 유연성이나 간결함을 반복문으로는 달성하기 어려울 수 있습니다.
- 재귀 호출을 사용한 탐색
    - 장점
        - 코드 간결성: 재귀 함수는 경우에 따라 코드를 더 간결하고 명확하게 만들 수 있습니다. 특히, 복잡한 데이터 구조를 다룰 때 코드의 가독성을 높일 수 있습니다.
        - 유연성: 재귀 호출은 복잡한 문제를 해결하거나, 동적인 데이터 구조를 다룰 때 더 유연한 접근 방식을 제공할 수 있습니다.
    - 단점
        - 메모리 사용: 재귀 호출은 각 호출마다 스택 프레임을 추가로 사용하기 때문에, 메모리 사용량이 늘어날 수 있습니다. 이는 연결 리스트가 매우 길 경우 스택 오버플로우를 일으킬 위험이 있습니다.
        - 성능 이슈: 재귀 호출은 함수 호출에 따른 오버헤드가 있기 때문에, 특히 깊이가 깊은 경우 성능 저하가 발생할 수 있습니다.
- 결론
    - 연결 리스트를 끝까지 탐색하는 경우, 같은 뎁스라는 조건 하에서는 `while` 문을 사용하는 것이 일반적으로 더 효율적입니다. `while` 문은 메모리 사용량이 적고, 연결 리스트와 같은 선형 데이터 구조를 탐색하는 데 있어서 직관적이고 간단한 접근 방식을 제공합니다. 반면, 재귀 호출은 코드의 간결성과 유연성을 제공할 수 있지만, 연결 리스트 탐색과 같이 간단한 작업에는 오버킬일 수 있습니다. 따라서, 대부분의 경우 `while` 문을 사용하는 것이 좋습니다.
        - 오버킬: 어떤 상황이나 문제를 해결하기 위해 필요 이상으로 과도하게 대응하는 것

## 풀이2. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        // 두 노드 중 한쪽이 널이면 널이 아닌 노드를 리턴
        if (list1 == null) return list2
        if (list2 == null) return list1
    
        // l2가 더 크면 l1에 재귀 호출 결과를 엮고 l1을 리턴
        return if (list1.`val` < list2.`val`) {
            list1.next = mergeTwoLists(list1.next, list2)
            list1
            // l1이 더 크거나 같으면 l2에 재귀 호출 결과를 엮고 l2를 리턴
        } else {
            list2.next = mergeTwoLists(list1, list2.next)
            list2
        }
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 재귀 구조로 연결 | 1밀리초 |
| 2 | 코틀린 풀이 | 측정하지 않음 |

# 15. 역순 연결 리스트

---

- [https://leetcode.com/problems/reverse-linked-list/](https://leetcode.com/problems/reverse-linked-list/)
- 연결 리스트를 뒤집어라.
- 나의 풀이
    
    ```python
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
    
        while head:
            next = head.next
            head.next = rev
            rev = head
            head = next
    
        return rev
    ```
    

## 풀이1. 재귀 구조로 뒤집기

---

- 연결 리스트를 뒤집는 문제는 매우 일반적이면서도 활용도가 높은 문제로, 실무에서도 빈번하게 쓰인다.
    - 재귀 구조와 반복 구조, 2가지 방식으로 모두 풀이해 보자.

- 전체 코드
    
    ```java
    public ListNode reverse(ListNode node, ListNode prev) {
        // 현재 노드인 node가 널이면 리턴
        if (node == null)
            return prev;
        // 현재 노드의 다음 노드 미리 지정
        ListNode next = node.next;
        // 현재 노드의 다음으로 이전 노드 지정
        node.next = prev;
        // 다음 노드와 현재 노드를 파라미터로 하여 재귀 호출
        return reverse(next, node);
    }
    
    public ListNode reverseList(ListNode head) {
        return reverse(head, null);
    }
    ```
    

## 풀이2. 반복 구조로 뒤집기

---

- 전체 코드
    
    ```java
    public ListNode reverseList(ListNode head) {
        ListNode prev = null, node = head;
        // 노드 끝으로 이동할 때까지 순회
        while (node != null) {
            // 현재 노드의 다음 노드 미리 지정
            ListNode next = node.next;
            // 현재 노드의 다음으로 이전 노드 지정
            node.next = prev;
            // 이전 노드는 현재 노드로 지정
            prev = node;
            // 미리 지정했던 다음 노드를 현재 노드로 변경
            node = next;
        }
        // prev는 뒤집힌 연결 리스트의 첫 번째 노드
        return prev;
    }
    ```
    

## 풀이3. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    fun reverseList(head: ListNode?): ListNode? {
        var prev: ListNode? = null
        var node = head
        // 노드 끝으로 이동할 때까지 순회
        while (node != null) {
            // 현재 노드의 다음 노드 미리 지정
            val next = node.next
            // 현재 노드의 다음으로 이전 노드 지정
            node.next = prev
            // 이전 노드는 현재 노드로 지정
            prev = node
            // 미리 지정했던 다음 노드를 현재 노드로 변경
            node = next
        }
        // prev는 뒤집힌 연결 리스트의 첫 번째 노드
        return prev
    }
    ```
    

- 일반적으로 반복 구조가 재귀 구조에 비해 메모리를 더 적게 차지하고 실행 속도도 더 빠른 편이다.
    - 반복 구조: 코드를 이해하기가 쉽지만 코드가 더 길다.
    - 재귀 구조: 코드가 더 짧으며 훨씬 더 우아한 풀이라는 느낌을 준다.

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 재귀 구조로 뒤집기 | 0밀리초 |
| 2 | 반복 구조로 뒤집기 | 0밀리초 |
| 3 | 코틀린 풀이 | 측정하지 않음 |

# 16. 두 수의 덧셈

---

- [https://leetcode.com/problems/add-two-numbers/](https://leetcode.com/problems/add-two-numbers/)
- 역순으로 저장된 연결 리스트의 숫자를 더하라.
- 나의 풀이
    
    ```python
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        temp = answer
    
        while l1 or l2:
            sum = 0
            if l1:
                sum = l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += temp.val
    
            temp.val = sum if sum < 10 else sum - 10
            temp.next = ListNode(1 if sum > 9 else 0)
            
            if not (l1 or l2) and temp.next.val == 0:
                temp.next = None
            else:
                temp = temp.next
    
        temp.next = l1 or l2
    
        return answer
    ```
    

## 풀이1. 자료형 변환

---

- 연결 리스트를 문자열로 이어 붙인 다음에 숫자로 변환하고, 이를 모두 계싼한 후 다시 연결 리스트로 바꾸면 쉽게 풀이할 수 있을 것 같다.
    - 역순으로 뒤집어야 해서 수행 시간이 제법 소요될 것으로 예상된다.

- 전체 코드
    
    ```java
    public ListNode reverseList(ListNode head) {
        ListNode prev = null, node = head;
        // 노드 끝으로 이동할 때까지 순회
        while (node != null) {
            // 현재 노드의 다음 노드 미리 지정
            ListNode next = node.next;
            // 현재 노드의 다음으로 이전 노드 지정
            node.next = prev;
            // 이전 노드는 현재 노드로 지정
            prev = node;
            // 미리 지정했던 다음 노드를 현재 노드로 변경
            node = next;
        }
        // prev는 뒤집힌 연결 리스트의 첫 번째 노드
        return prev;
    }
    
    // 연결 리스트를 임의 정밀도 정수형으로 변환
    public BigInteger toBigInt(ListNode node) {
        String val = "";
        // 연결 리스트를 순회하며 한 글자씩 조합
        while (node != null) {
            val += node.val;
            node = node.next;
        }
        // 조합한 글자를 임의 정밀도 정수형으로 변환
        return new BigInteger(val);
    }
    
    // 임의 정밀도 정수형을 연결 리스트로 변환
    public ListNode toReversedLinkedList(BigInteger val) {
        ListNode prev = null, node = null;
        // 정수형을 문자로 바꾼 다음 문자 배열로 전환하여 한 글자씩 순회
        for (char c : String.valueOf(val).toCharArray()) {
            // 한 글자씩 숫자로 변환하여 노드 지정
            node = new ListNode(Character.getNumericValue(c));
            // 최종 결과는 뒤집어야 하므로 현재 노드의 다음으로 이전 노드 지정
            node.next = prev;
            // 이전 노드는 현재 노드로 지정
            prev = node;
        }
        return node;
    }
    
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // 2개의 연결 리스트를 뒤집는다.
        ListNode l1Reversed = reverseList(l1);
        ListNode l2Reversed = reverseList(l2);
    
        // 임의 정밀도 정수형으로 변환하여 더하기 연산 진행
        BigInteger result = toBigInt(l1Reversed).add(toBigInt(l2Reversed));
        // 결과를 다시 역순 연결 리스트로 변환
        return toReversedLinkedList(result);
    }
    ```
    
    - 코드가 다소 길고 산만하지만 풀이 자체는 전혀 어렵지 않다. 빠르게 실행되며 수행 속도에도 아무런 문제가 없다.
        - 그러나 애초에 이 문제가 요구한 풀이는 이런 방식이 아닐 것이다.

## 풀이2. 전가산기 구현

---

- 이진법이 아니라 십진법이란 차이만 있을 뿐, 자리올림수(Carry)를 구하는 것까지 가산기의 원리와 거의 동일하다.
- 여기서는 덧셈 결과에 나머지를 취하고 몫은 자리올림수 형태로 올리는 전가산기의 전체적인 구조만 참고해 풀이해 본다.

- 전체 코드
    
    ```java
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // 값을 계산할 임시 노드 선언
        ListNode node = new ListNode(0);
        // 임시 노드를 첫 번째 노드로 선언
        ListNode root = node;
    
        // 자릿수의 합(sum), 자리올림수(carry), 나머지(remainder)를 저장할 변수 선언
        int sum, carry = 0, remainder;
        // 모든 연결 리스트를 끝까지 순회하고, 자리올림수도 0이 될 때까지 진행
        while (l1 != null || l2 != null || carry != 0) {
            sum = 0;
            // 첫 번째 연결 리스트 합산 및 진행
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            // 두 번째 연결 리스트 합산 및 진행
            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
    
            // 노드의 값으로 사용할 나머지 계산
            remainder = (sum + carry) % 10;
            // 10으로 나누었을 때 몫은 자릿수가 증가했다는 의미이므로 자리올림수로 사용
            carry = (sum + carry) / 10;
            // 나머지는 다음 노드의 값으로 지정
            node.next = new ListNode(remainder);
            // 계산할 노드를 다음으로 이동
            node = node.next;
        }
        // 첫 번째 노드는 임시 노드이므로 그다음부터 결과로 리턴
        return root.next;
    }
    ```
    

## 풀이3. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    class ListNode(val `val`: Int, var next: ListNode? = null)
    
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        // 파라미터는 수정할 수 없으므로 var 별도 선언
        var l1var = l1
        var l2var = l2
    
        // 값을 계산할 임시 노드 선언
        var node = ListNode(0)
        val root = node
    
        // 자릿수의 합(sum), 자리올림수(carry), 나머지(remainder)를 저장할 변수 선언
        var sum: Int
        var carry = 0
        var remainder: Int
        // 모든 연결 리스트를 끝까지 순회하고, 자리올림수도 0이 될 때까지 진행
        while (l1var != null || l2var != null || carry != 0) {
            sum = 0
            // 첫 번째 연결 리스트 합산 및 진행
            if (l1var != null) {
                sum += l1var.`val`
                l1var = l1var.next
            }
            // 두 번째 연결 리스트 합산 및 진행
            if (l2var != null) {
                sum += l2var.`val`
                l2var = l2var.next
            }
    
            // 노드의 값으로 사용할 나머지 계산
            remainder = (sum + carry) % 10
            // 10으로 나누었을 때 몫은 자릿수가 증가했다는 의미이므로 자리올림수로 사용
            carry = (sum + carry) / 10
            // 나머지는 다음 노드의 값으로 지정
            node.next = ListNode(remainder)
            // 계산할 노드를 다음으로 이동
            node = node.next!!
        }
        // 첫 번째 노드는 임시 노드이므로 그다음부터 결과로 리턴
        return root.next
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 자료형 변환 | 37밀리초 |
| 2 | 전가산기 구현 | 1밀리초 |
| 3 | 코틀린 풀이 | 측정하지 않음 |

# 17. 페어의 노드 스왑

---

- [https://leetcode.com/problems/swap-nodes-in-pairs/](https://leetcode.com/problems/swap-nodes-in-pairs/)
- 연결 리스트를 입력 받아 페어(Pair) 단위로 스왑하라.
- 나의 풀이
    
    ```python
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = head
    
        while answer and answer.next:
            curr_val = answer.val
            answer.val = answer.next.val
            answer.next.val = curr_val
    
            answer = answer.next.next
    
        return head
    ```
    

## 풀이1. 값만 교환

---

- 연결 리스트의 노드를 변경하는 게 아닌, 노드 구조는 그대로 유지하되 값만 변경하는 방법이다.

- 전체 코드
    
    ```java
    public ListNode swapPairs(ListNode head) {
        // 스왑을 진행할 노드 선언
        ListNode node = head;
    
        // 현재 노드와 다음 노드가 존재하면 계속 진행
        while (node != null && node.next != null) {
            // 임시 변수를 이용해 값만 교환
            int tmp;
            tmp = node.val;
            node.val = node.next.val;
            node.next.val = tmp;
            // 두 칸 앞으로 이동
            node = node.next.next;
        }
        // 첫 번째 노드를 정답으로 리턴
        return head;
    }
    ```
    
    - 온라인 코딩 테스트 시에는 이런 풀이가 나쁘지 않다. 무엇보다, 빨리 풀 수 있고 타임아웃도 발생하지 않을 것이다.
        - 그러나 변칙적인 풀이 방법이므로, 만약 코딩 테스트 이후 코드 리뷰를 진행하다 좋지 않은 피드백을 받을 가능성도 있다.
        - 안 좋은 피드백을 받게 된다면, 빨리 풀기 위해 시도한 방법이라는 사실을 충분히 어필하고 다른 풀이법, 예를 들어 바로 다음 풀이인 #2 반복 풀이에 대해 충분히 설명할 수 있어야 한다.

## 풀이2. 반복 구조로 스왑

---

- 연결 리스트 자체를 바꾸는 일은 생각보다 다소 복잡한 문제다.
    - 이렇게 위치를 변경한 이후에는 두 칸씩 앞으로 이동하며 다시 다음번 교환을 진행하면 된다.

- 전체 코드
    
    ```java
    public ListNode swapPairs(ListNode head) {
        // 값을 계산할 임시 노드 선언
        ListNode node = new ListNode(0);
        // 임시 노드를 첫 번째 노드로 선언
        ListNode root = node;
        // 다음 노드는 첫 번째 노드로 지정
        node.next = head;
        // 다음 노드와 다음 다음 노드가 있으면 반복
        while (node.next != null && node.next.next != null) {
            // a는 다음 노드
            ListNode a = node.next;
            // b는 다음 다음 노드
            ListNode b = node.next.next;
            // 위치 변경
            a.next = b.next;
            node.next = b;
            node.next.next = a;
            // 두 칸 앞으로 이동
            node = node.next.next;
        }
        // 첫 번째 노드는 임시 노드이므로 그다음부터 결과로 리턴
        return root.next;
    }
    ```
    

## 풀이3. 재귀 구조로 스왑

---

- 전체 코드
    
    ```java
    public ListNode swapPairs(ListNode head) {
        // 현재 노드와 다음 노드가 있으면 반복
        if (head != null && head.next != null) {
            // 다음 노드 선언
            ListNode p = head.next;
            // 다음 다음 노드를 파라미터로 전달하고 스왑된 값을 리턴받음
            head.next = swapPairs(head.next.next);
            // 다음 다음 노드는 현재 노드로 지정
            p.next = head;
            // 다음 노드 리턴
            return p;
        }
        return head;
    }
    ```
    
    - 반복 풀이와 달리 포인터 역할을 하는 p 변수는 하나만 있어도 충분하며, 더미 노드를 만들 필요도 없이 head를 바로 리턴할 수 있어 공간 복잡도가 낮다.
        - 매우 우아한 풀이라는 느낌이 든다.

## 풀이4. 코틀린 풀이

---

- 코틀린에서는 널(Nullable) 타입 여부는 `?`로 바로 판별할 수 있다.
    
    ```java
    // 자바
    if (head != null && head.next != null)
    // 코틀린
    if (head?.next != null)
    ```
    

- 전체 코드
    
    ```kotlin
    fun swapPairs(head: ListNode?): ListNode? {
        // 현재 노드와 다음 노드가 있으면 반복
        if (head?.next != null) {
            // 다음 노드 선언
            val p = head.next!!
            // 다음 다음 노드를 파라미터로 전달하고 스왑된 값을 리턴받음
            head.next = swapPairs(head.next!!.next)
            // 다음 다음 노드는 현재 노드로 지정
            p.next = head
            // 다음 노드 리턴
            return p
        }
        return head
    }
    
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 값만 교환 | 0밀리초 |
| 2 | 반복 구조로 스왑 | 0밀리초 |
| 3 | 재귀 구조로 스왑 | 0밀리초 |
| 4 | 코틀린 풀이 | 측정하지 않음 |

# 18. 홀짝 연결 리스트

---

- [https://leetcode.com/problems/odd-even-linked-list/](https://leetcode.com/problems/odd-even-linked-list/)
- 연결 리스트를 홀수 번째 노드 다음에 짝수 번째 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라
- 나의 풀이
    
    ```python
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
    
        odd = head
        even = head.next
        tail = even
    
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
    
        odd.next = tail
        return head
    ```
    

## 풀이1. 반복 구조로 홀짝 노드 처리

---

- 이런 문제는 제약이 없을 경우 연결 리스트를 리스트로 바꾸고 리스트의 메소드를 이용하면 좀 더 쉽고 직관적으로 풀이할 수 있다.
    - 그러나 이러한 풀이가 문제에서 요구한 풀이 방식은 아닐 것이며 우아하지도 않다.
- 홀수 노드 다음에 짝수 노드가 오게 재구성하라고 했으니 홀, 짝 각 노드를 구성한 다음 홀수 노드의 마지막을 짝수 노드의 처음과 이어주면 될 것 같다.
    - 짝수 노드가 존재한다면 계속 반복하면서 홀수 노드는 홀수끼리, 짝수 노드는 짝수끼리 이어나가며 한 칸씩 진행한다.

- 전체 코드
    
    ```java
    public ListNode oddEvenList(ListNode head) {
        // 예외 처리
        if (head == null) {
            return null;
        }
        // 홀수 노드
        ListNode odd = head;
        // 짝수 노드
        ListNode even = head.next;
        // 짝수 첫 번째 노드
        ListNode evenHead = even;
    
        // 반복하면서 홀짝 노드 처리
        while (even != null && even.next != null) {
            // 홀짝 노드의 다음 노드로 다음 다음 노드 지정
            odd.next = odd.next.next;
            even.next = even.next.next;
            // 홀짝 한 칸씩 진행
            odd = odd.next;
            even = even.next;
        }
        // 홀수 노드 마지막을 짝수 첫 번째와 연결
        odd.next = evenHead;
        // 첫 번째 노드 리턴
        return head;
    }
    ```
    
    - 이렇게 풀이하면 시간 복잡도 O(n)에 풀이가 가능하며, ❓공간 복잡도 또한 odd, even, evenHead 등의 변수들이 n의 크기에 관계없이 항상 일정하게 사용되기 때문에 O(1)로, 문제의 제약 조건을 만족한다.

## 풀이2. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    fun oddEvenList(head: ListNode?): ListNode? {
        // 예외 처리
        if (head == null) {
            return null
        }
        // 홀수 노드
        var odd = head
        // 짝수 노드
        var even = head.next
        // 짝수 첫 번째 노드
        val evenHead = even
    
        // 반복하면서 홀짝 노드 처리
        while (even?.next != null) {
            // 홀짝 노드의 다음 노드로 다음 다음 노드 지정
            odd!!.next = odd.next!!.next
            even.next = even.next!!.next
            // 홀짝 한 칸씩 진행
            odd = odd.next
            even = even.next
        }
        // 홀수 노드 마지막을 짝수 첫 번째와 연결
        odd!!.next = evenHead
        // 첫 번째 노드 리턴
        return head
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 반복 구조로 홀짝 노드 처리 | 0밀리초 |
| 2 | 코틀린 풀이 | 측정하지 않음 |

# 19. 역순 연결 리스트 ii

---

- [https://leetcode.com/problems/reverse-linked-list-ii/](https://leetcode.com/problems/reverse-linked-list-ii/)
- 위치 left에서 right까지를 역순으로 만들어라. 위치는 1부터 시작한다.
- 나의 풀이
    
    ```python
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = ListNode(0)
        root.next = head
        start = root
        count = 0
        rev = None
    
        while head:
            count += 1
            if count < left:
                start = start.next
                head = head.next
            elif left <= count <= right:
                next = head.next
                head.next = rev
                rev = head
                head = next
            else:
                break
    
        start.next = rev
        while start.next:
            start = start.next
        start.next = head
    
        return root.next
    ```
    

## 풀이1. 반복 구조로 노드 뒤집기

---

- ex> 1 → 2 → 3 → 4 → 5 → 6, left = 2, right = 5
    - 1 → 5 → 4 → 3 → 2 → 6
- 우선 변경이 필요한 위치의 바로 앞까지 다음과 같이 이동한다.
    
    ```java
    ListNode root = new ListNode(0);
    root.next = head;
    ListNode start = root;
    for (int i = 0; i < left - 1; i++)
        start = start.next;
    ListNode end = start.next;
    ```
    
    - start: 변경이 필요한 2의 바로 앞 지점
    - end: start.next인 2를 가리킨다.

- 전체 코드
    
    ```java
    public ListNode reverseBetween(ListNode head, int left, int right) {
        // 예외 처리
        if (head == null) {
            return null;
        }
        // 임시 노드 선언
        ListNode root = new ListNode(0);
        // 임시 노드 다음으로 노드 시작
        root.next = head;
        // 임시 노드부터 시작해 변경 필요한 위치 앞으로 이동
        ListNode start = root;
        for (int i = 0; i < left - 1; i++) {
            start = start.next;
        }
        // 변경이 필요한 마지막 위치 선언
        ListNode end = start.next;
        // right - left만큼 위치 변경 진행
        for (int i = 0; i < right - left; i++) {
            ListNode tmp = start.next;
            start.next = end.next;
            end.next = end.next.next;
            start.next.next = tmp;
        }
        // 첫 번째 노드는 임시 노드이므로 그다음부터 결과로 리턴
        return root.next;
    }
    ```
    

## 풀이2. 코틀린 풀이

---

- 전체 코드
    
    ```kotlin
    fun reverseBetween(head: ListNode?, left: Int, right: Int): ListNode? {
        // 예외 처리
        if (head == null) {
            return null
        }
        // 임시 노드 선언
        val root = ListNode(0)
        // 임시 노드 다음으로 노드 시작
        root.next = head
        // 임시 노드부터 시작해 변경 필요한 위치 앞으로 이동
        var start = root
        for (i in 0 until left - 1) {
            start = start.next!!
        }
        // 변경이 필요한 마지막 위치 선언
        val end = start.next
        // right - left만큼 위치 변경 진행
        for (i in 0 until right - left) {
            val tmp = start.next
            start.next = end!!.next
            end.next = end.next!!.next
            start.next!!.next = tmp
        }
        // 첫 번째 노드는 임시 노드이므로 그다음부터 결과로 리턴
        return root.next
    }
    ```
    

| 풀이 | 방식 | 실행 시간 |
| --- | --- | --- |
| 1 | 반복 구조로 노드 뒤집기 | 0밀리초 |
| 2 | 코틀린 풀이 | 측정하지 않음 |