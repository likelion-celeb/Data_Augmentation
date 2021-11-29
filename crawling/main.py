import time, os
import urllib.request

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# 폴더 확인해보고 없으면 생성
def makedirs(path): 
   try: 
        os.makedirs(path) 
   except OSError: 
       if not os.path.isdir(path): 
           raise

def search_selenium(search_name, search_limit, scroll_limit=5):
    root = os.path.join(os.getcwd())
    
    driver = webdriver.Chrome(root + '/driver/chromedriver.exe') # 여기에 크롬드라이브 다운로드 받은 경로를 입력한다.
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")      # google 이미지 카테고리 링크
    elem = driver.find_element_by_name("q")                      # q라는 엘리멘트를 찾는다
    elem.send_keys(search_name)                                  # 검색하고 싶은 검색어로 검색
    elem.send_keys(Keys.RETURN)

    # Scroll 제어 파라미터 선언
    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_count = 1

    while True:
        # scroll limit가 넘어가면 scroll 종료
        if scroll_count > scroll_limit:
            break

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        time.sleep(SCROLL_PAUSE_TIME)
    
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                # 만약에 더보기 버튼 생기면 클릭
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

        scroll_count += 1

    images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
    
    save_dir = root + "/download_imgs/" + search_name
    makedirs(save_dir)

    links = []

    # 이미지 다운로드 경로 받아오는 영역    
    for image in images[:search_limit]: 
        if image.get_attribute('src') != None: 
            links.append(image.get_attribute('src'))

    print('찾은 이미지 개수:', len(links)) 
    time.sleep(2)

    # 다운로드 경로를 통해 이미지 받는 영역
    for idx, link in enumerate(links): 
        url = link
        download_start = time.time()

        # 이미지 다운로드 받는 method (이미지 다운로드 링크, 이미지 저장 경로 & 이미지 이름)
        urllib.request.urlretrieve(url, save_dir + "/" + str(idx) + ".jpg")
        print(str(idx+1) + '/' + str(len(links)) + ' '+ search_name + ' 다운로드 중....... Download time : ' + str(time.time() - download_start)[:5] + ' 초') 
        print(search_name+' ---다운로드 완료---')

    driver.close()



if __name__ == "__main__":
    search_names = list(map(str, input("검색하고 싶은 키워드(한칸씩 띄워서 여러개 입력 가능) : ").split()))
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    try:
        scroll_limit = int(input("스크롤 횟수 (default=5) : "))
    except:
        scroll_limit = 5
    start = time.time()
    for search_name in search_names:
        search_selenium(search_name, search_limit, scroll_limit)
    print("수집 수행시간 : {}초".format(round(time.time() - start, 3)))