# [D2] [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합 - 4881 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTQh00qQs0DFAVT) 

### 성능 요약

메모리: 60,416 KB, 시간: 116 ms, 코드길이: 2,323 Bytes

### 제출 일자

2025-11-28 15:49



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
>
# 소감

dp 도 생각해보고 dfs 도 생각 해 봤는데 dfs 로 푸는게 도저히 상상이 안되서 포기했던 문제 . 결국 dfs 긴 하지만 

상하좌우를 탐색하는게 아니라 depth 를 늘려가면서 가로만 탐색하게 된다 ! 그래서 visited 도 가로개수 만큼만 

필요한것 ..    가로만 탐색하는 거도 생각했는데 그럼 세로를 어케 늘리지 ,, ? 세로로도 같은칸 방문하면 안되는데,,

를 생각하다보니 성공하지 못했었다 .. 결국 depth 랑 visited 배열을 떠올리지 못한게 문제였던 듯 싶다 !
