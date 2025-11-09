## 문제

nxm 크기의 금광이 있다. 금광은 1x1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있다. 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다. 이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하시오.

만약 다음과 같이 3x4 크기의 금광이 존재한다고 가정한다면,

![](https://blog.kakaocdn.net/dna/spuqT/btrVQpLtELX/AAAAAAAAAAAAAAAAAAAAAEVhM772rveA1OarP5oc9_CASyJJBOhdGMQckYrXb7km/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1764514799&allow_ip=&allow_referer=&signature=eUn2AqoZPVbFw3k0mL2dVTVEwqM%3D)

(2,1) -> (3,2) -> (3,3) -> (3,4)의 위치로 이동하면 총 19만큼의 금을 채굴할 수 있으며, 이때의 값이 최댓값이다.

*첫째 줄에 테스트 케이스 T가 입력된다. (1<=T<=1000)*

*매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력된다. (1<=n,m<=20)*

*둘째 줄에 nxm개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력된다. (1<=금의 개수<=100)*


## 소감

처음에 완탐인 줄 알았다가 이전항에서 세가지 조건으로 이동할 수 있다는걸 안 뒤로는 정답 테이블 하나 만들어

서 더해줘야지 생각했다. 대부분의 dp 가 이런 형식인듯 ? 그렇게 어려운 문제는 아니었다. 

- 결론적으로 3조건중 max 하나만 골라서 계속 더해나감 → 이전에 더했던걸 기반으로 다음 연산을 함으로 완탐이 아니라 dp 가 된다.

```java
for (int i = 0; i < n; i++) {
        int leftUp = (i == 0) ? 0 : AllResult[i - 1][j - 1];
        int left = AllResult[i][j - 1];
        int leftDown = (i == n - 1) ? 0 : AllResult[i + 1][j - 1];
        AllResult[i][j] += Math.max(left, Math.max(leftUp, leftDown));
    }
```

if 문을 이렇게 깔끔하게 쓸 수도 있다. 첫번째, 마지막 행인 경우 0 , 마지막 행의 숫자로 만들어 주고 아니면 1더하

기 1 빼기 와 같은 연산으로 중간행 처리를 해준다. 훨씬 깔끔한 방식 같다. 

- 없으면 기본값으로 대체 가능 한 경우 자주 쓴다고 한다.

마지막으로 나는 기본 배열을 건들지 않게 clone 해서 썼는데 ( timeout 걸리지 않을까 .. ? 생각했는데 입력값 보면

사실 그런 걱정은 안 했어도 될 것 같다. ) 더해가며 마지막 값을 구하는 것임으로 clone 은 안해도 될 듯 하다.
