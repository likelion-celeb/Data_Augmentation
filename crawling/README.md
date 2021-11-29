## 실행전 확인 사항
 1. 파이썬 버전은 3.8 이상으로 사용해주세요
 2. selenium, bs4가 설치되어있지 않다면 requirements.txt를 활용해 설치해주세요
 3. 자신이 사용하는 chrome의 버전을 확인하고 driver폴더를 만들어 그 폴더 안에 chrome driver를 설치해주세요
  - chrome 버전 확인 방법 : 주소창에 chrome://version/ 입력
  - [chrome driver 설치 링크 (클릭하면 넘어갑니다!)](https://chromedriver.chromium.org/downloads)


## 실행방법 (.py version)
```
# 1. move to dir in cmd or prompot
cd Crawling

# 2. run code
python main.py

# Example
(crawling) C:\>cd Crawling
(crawling) C:\Crawling>python main.py
```

## 실행방법 (.ipynb version)
```
# 1. move to dir in cmd or prompot
cd Crawling

# 2. open code
main.py

# 3. run code at IDE
```

## 입력 순서
 1. 검색하고 싶은 키워드 : (검색어 입력)
 2. 원하는 이미지 수집 개수 : (이미지 수집 숫자 (int형이라 숫자만 됩니다))
 3. 스크롤 횟수 (default=5) : (검색 페이지 스크롤 횟수를 입력하면됩니다 입력하지않으면 5로 자동 설정됩니다.) 
 
## 실행 예시
```
검색하고 싶은 키워드 : 꼬마돌
원하는 이미지 수집 개수 : 10
스크롤 횟수 (default=5) : 5

DevTools listening on ws://127.0.0.1:5964/devtools/browser/57f385f7-15f5-49f2-935c-ddb5a96cd96d
찾은 이미지 개수: 10
[29412:30060:1113/134520.542:ERROR:chrome_browser_main_extra_parts_metrics.cc(230)] crbug.com/1216328: Checking Bluetooth availability started. Please report if there is no report that this ends.
[29412:30060:1113/134520.544:ERROR:chrome_browser_main_extra_parts_metrics.cc(233)] crbug.com/1216328: Checking Bluetooth availability ended.
[29412:30060:1113/134520.547:ERROR:chrome_browser_main_extra_parts_metrics.cc(236)] crbug.com/1216328: Checking default browser status started. Please report if there is no report that this ends.
[29412:4280:1113/134520.601:ERROR:device_event_log_impl.cc(214)] [13:45:20.601] Bluetooth: bluetooth_adapter_winrt.cc:1073 Getting Default Adapter failed.
[29412:30060:1113/134520.630:ERROR:chrome_browser_main_extra_parts_metrics.cc(240)] crbug.com/1216328: Checking default browser status ended.
1/10 꼬마돌 다운로드 중....... Download time : 0.005 초
꼬마돌 ---다운로드 완료---
2/10 꼬마돌 다운로드 중....... Download time : 0.002 초
꼬마돌 ---다운로드 완료---
3/10 꼬마돌 다운로드 중....... Download time : 0.005 초
꼬마돌 ---다운로드 완료---
4/10 꼬마돌 다운로드 중....... Download time : 0.002 초
꼬마돌 ---다운로드 완료---
5/10 꼬마돌 다운로드 중....... Download time : 0.002 초
꼬마돌 ---다운로드 완료---
6/10 꼬마돌 다운로드 중....... Download time : 0.002 초
꼬마돌 ---다운로드 완료---
7/10 꼬마돌 다운로드 중....... Download time : 0.002 초
꼬마돌 ---다운로드 완료---
8/10 꼬마돌 다운로드 중....... Download time : 0.002 초
꼬마돌 ---다운로드 완료---
9/10 꼬마돌 다운로드 중....... Download time : 0.006 초
꼬마돌 ---다운로드 완료---
10/10 꼬마돌 다운로드 중....... Download time : 0.002 초
꼬마돌 ---다운로드 완료---
수집 수행시간 : 13.009초
```

## 불편한 점
사용시 오류나 불편한점은 Issues에 내용 작성 부탁드립니다
