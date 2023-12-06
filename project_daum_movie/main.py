#       3. DB에 저장된 데이터 엑셀로 다운로드
#       4. DB에 저장된 데이터 -> 텍스트 분석
#       5. DB에 저장된 데이터 -> wordcloud 시각화

from collect.collect_daum_movie_review import review_collector
from apscheduler.schedulers.blocking import BlockingScheduler

def main():
    print("="*100)
    print("== 영화리뷰수집기 ==")
    print("="*100)
    movie_code = input("영화 코드>> ")  # 169328
    print("MSG: 매일 12시간에 수집")


    scheduler = BlockingScheduler()
    scheduler.add_job(review_collector,
                      args=[movie_code],
                      trigger="cron",
                      hours="12",
                      minute="0")
    scheduler.start()


if __name__ == "__main__":
    main()