# **LCA란? (Lowest Common Ancestor)**

- 트리 내에서 공통 부모인 LCA를 찾아주는 알고리즘
- 두 점 사이의 거리를 구할 때 사용한다. ( 두 노드의 공통된 조상 중에서 가장 가까운 조상 찾기 )

예를들어 다음과 같은 트리가 있다 생각해보자.

[https://t1.daumcdn.net/cfile/tistory/2733765058C8325902](https://t1.daumcdn.net/cfile/tistory/2733765058C8325902)

여기서 a,b의 공통 조상을 LCA(a,b)라고 하자.

**LCA(14, 7)은 무엇일까?**

[https://t1.daumcdn.net/cfile/tistory/2136754858C832C90F](https://t1.daumcdn.net/cfile/tistory/2136754858C832C90F)

위의 그림으로 우리는 LCA(14, 7) = 1임을 파악할 수 있다.

# LCA 알고리즘 순서

![https://images.velog.io/images/shiningcastle/post/e6cfc65e-b220-442d-ad36-b385ab82bb16/image.png](https://images.velog.io/images/shiningcastle/post/e6cfc65e-b220-442d-ad36-b385ab82bb16/image.png)

1. 모든 노드에 대한 깊이를 계산합니다.
2. 최소 공통 조상을 찾을 두 노드를 확인합니다.
3. 먼저 두 노드의 깊이가 동일하도록 거슬러 올라갑니다.
4. 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라갑니다.
5. 모든 LCA(a, b) 연산에 대하여 3~4번의 과정을 반복합니다.

[python-for-coding-test/5.py at master · ndb796/python-for-coding-test](https://github.com/ndb796/python-for-coding-test/blob/master/21/5.py)