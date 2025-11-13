# [level 3] 정수 삼각형 - 43105 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/43105) 

### 성능 요약

메모리: 63 MB, 시간: 9.41 ms

### 구분

코딩테스트 연습 > 동적계획법（Dynamic Programming）

### 채점결과

정확성: 64.3<br/>효율성: 35.7<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 11월 13일 14:30:27

### 문제 설명

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/97ec02cc39/296a0863-a418-431d-9e8c-e57f7a9722ac.png" title="" alt="스크린샷 2018-09-14 오후 5.44.19.png"></p>

<p>위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.</p>

<p>삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한사항</h5>

<ul>
<li>삼각형의 높이는 1 이상 500 이하입니다.</li>
<li>삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>triangle</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]</td>
<td>30</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges


## 소감

dp 라고 생각 안해도 풀 수 있었던 문제지만? 이전에 합친 걸 활용해서 다음 항을 구한다는 점에서 dp 라고 할 수 

있겠다.  직관적으로는 위에서 아래로 내려가면서 항을 고르는 방식이지만 더해준 항을 활용하기 위해 한칸 뒤에서

이전항을 뭐로 고를지 선택하는 방식으로 구현했다. 

```java
  answer = Math.max(answer,triangle[triangle.length-1][i]);
```

Math.max 로 가장 큰 항을 구할때 항상 두개중 택 인지를 헷갈리는데,,, 둘중 큰걸 구하는거랑 max 를 갱신하는

거랑 헷갈리지 말자 ..

근데 이게 왜 레벨3이지 .. ? 
