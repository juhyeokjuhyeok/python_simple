# 웹 크롤링(web Crawling)
# - 웹 사이트에서 원하는 데이터를 수집

# ** 웹 크롤링을 사용하는 이유?
# ㅁ어떤 데이터 필요?
# - 기업에서 제공?
# - 정부, 관공서 제공?
# - 자체적으로 보유?

#**라이브러리(다운로드 + import)
# 1. BeautifulSoup4
# 2. Request
# 3. Selenium

# ** 라이브러리 조합
# 1. 정적 페이지(Requests + BeautifulSoup4)
# 2. 동적 페이지(Selenium + BeautifulSoup4)

# ** 웹 프로그래밍 기초
# - 프론트엔드 개발자: 화면(view)단 개발
# - 백엔드 개발자: 서비스와 DB 개발
# - 풀스택 배발자: 프론트엔드 + 백엔드

# ** MVC 패턴
# 1. VIEW: 사용자 화면 구현
# 2. CONTROLLER: 컨트롤러 및 서비스 구현
# 3. MODEL: DB 구현

# **  VIEW단(웹 페이지 디자인)
# 1. HTML: 프레임(뼈대)
# 2. CSC 디자인(색상, 굵기, 크기, 회전, 등등) 구현
# 3. Javascript: 동적인 기능 구현

# ** HTML
# - <tag></tag> 구현
# - tag 종류: div, span, p, a, h4, ...

# 예시
# <div>
#       <spen class = "t2">
#               <span id="t1"></span>
#       </spen>
#       <span class = "t2">
#           <h4></h4>
#       </span>
#   </div>

# ** 선택자
# 1.자식 선택자: div > span
# 2.자손 선택자: div span
# 3.아이디 선택자: #t1(유니크 1개)
# 4.클래스 선택자: .t2(복수 개 선택가능)

# 개발환경 구축
# 1. Anaconda prompt
# > conda env list : 가상환경 목록 보기
# > conda create -n simle python=3.8   : basic 가상환경 생성(버전 3.8)
# > conda activate simple : 가상환경 접속
# pip install requests
# pip install beautifulsoup4
# pip install selenium
#pip list

import requests
import selenium
from bs4 import BeautifulSoup

#데이터 수집을 위한 URL 주소
url = "https://v.daum.net/v/20231101163231654"

# 1. URL 접속해서 전체 소스코드 가져오기
result = requests.get(url)
# status_code: 200(성공) 400번대 또는 500번대(오류)
print(result)
print(result.text)

# 2. 전체코드(requests) -> BeautifulSoup4 전달
doc = BeautifulSoup(result.text, "html.parser")

# 3. 원하는 정보 수집
# - select() -> 결과(List Type)
title = doc.select("h3.tit_view")[0].get_text()
print(f"제목: {title}")

# 태그 이름으로 셀렉트 금지
# 1. 선책지(id, class)
#2. 상위 선택자(자식, 자손)
content_list = doc.select("div.article_view p")

content = ""
for p in content_list:
    content += p.get_text()

print(f"본문: {content}")

숙제:잘짜정보
