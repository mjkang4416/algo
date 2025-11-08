# [level 1] 실패율 - 42889 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42889?gad_source=1&gad_campaignid=22799790467&gbraid=0AAAAAC_c4nBf6aih4kkpPyl2Pc9RDvuIo&gclid=Cj0KCQjwgpzIBhCOARIsABZm7vHSixVxGKYj3qzyTZHmVk1hzK5x2rps8Dj6Oo4i9O6o837Uno8ZZzMaAup7EALw_wcB) 

### 성능 요약

메모리: 105 MB, 시간: 29.68 ms

### 구분

코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 11월 08일 12:53:50

### 문제 설명

<h2>실패율</h2>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/bde471d8ac/48ddf1cc-c4ea-499d-b431-9727ee799191.png" title="" alt="failture_rate1.png"></p>

<p>슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.</p>

<p>이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.</p>

<ul>
<li>실패율은 다음과 같이 정의한다.

<ul>
<li>스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수</li>
</ul></li>
</ul>

<p>전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.</p>

<h5>제한사항</h5>

<ul>
<li>스테이지의 개수 N은 <code>1</code> 이상 <code>500</code> 이하의 자연수이다.</li>
<li>stages의 길이는 <code>1</code> 이상 <code>200,000</code> 이하이다.</li>
<li>stages에는 <code>1</code> 이상 <code>N + 1</code> 이하의 자연수가 담겨있다.

<ul>
<li>각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.</li>
<li>단, <code>N + 1</code> 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.</li>
</ul></li>
<li>만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.</li>
<li>스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 <code>0</code> 으로 정의한다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>N</th>
<th>stages</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>5</td>
<td>[2, 1, 2, 6, 2, 4, 3, 3]</td>
<td>[3,4,2,1,5]</td>
</tr>
<tr>
<td>4</td>
<td>[4,4,4,4,4]</td>
<td>[4,1,2,3]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
1번 스테이지에는 총 8명의 사용자가 도전했으며, 이 중 1명의 사용자가 아직 클리어하지 못했다. 따라서 1번 스테이지의 실패율은 다음과 같다.</p>

<ul>
<li>1 번 스테이지 실패율 : 1/8</li>
</ul>

<p>2번 스테이지에는 총 7명의 사용자가 도전했으며, 이 중 3명의 사용자가 아직 클리어하지 못했다. 따라서 2번 스테이지의 실패율은 다음과 같다.</p>

<ul>
<li>2 번 스테이지 실패율 : 3/7</li>
</ul>

<p>마찬가지로 나머지 스테이지의 실패율은 다음과 같다.</p>

<ul>
<li>3 번 스테이지 실패율 : 2/4</li>
<li>4번 스테이지 실패율 : 1/2</li>
<li>5번 스테이지 실패율 : 0/1</li>
</ul>

<p>각 스테이지의 번호를 실패율의 내림차순으로 정렬하면 다음과 같다.</p>

<ul>
<li>[3,4,2,1,5]</li>
</ul>

<p>입출력 예 #2</p>

<p>모든 사용자가 마지막 스테이지에 있으므로 4번 스테이지의 실패율은 1이며 나머지 스테이지의 실패율은 0이다.</p>

<ul>
<li>[4,1,2,3]</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

# 소감

저도이제 카카오 1은 푼다구요 ~ 자잘하게 실패가 나오면 놓친 조건이 없는지 확인하자 !! 이번에도 문제에서 조건

을 하나 놓쳐서 애매하게 성공이 떴었다. 나머지는 무난했다. 단계별 머물러 있는 사람 수를 binarySearch 로 구하

고 스테이지별 도전자 수를 구해 준 다음 → 스테이지 마다 실패율을 구해준다. 

- 나눌때 실수 신경쓰자.
- 확률 구할때는 실수 날아가면 안됨. 그냥 0 으로 다 날아감
- double 비교는 compare 객체로

```java
resultStage.sort((o1,o2)-> {
            if(o1.failPerc == o2.failPerc){
                return o1.stage - o2.stage; 
            }   
            return Double.compare(o2.failPerc, o1.failPerc);
        });
        
        return resultStage.stream().mapToInt(o1->o1.stage).toArray();
    }
```

- 객체 List 일 경우 해당객체.sort 로 → 람다 임으로 그냥 함수처럼 리턴 값 주면 된다.
- 일반 int[] 일 경우 Arrays.sort(arr, (a,b) →{ }) 로
- stream() 으로 값 하나씩 가져와서 객체를 matToInt() 로 int 형으로 바꿔서 .toArray() 에 담아준다.
