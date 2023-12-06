#  DB에 저장되어있는 수집 데이터를 EXCEL로 저장
# Python(Dice, List 컬렉션)
# ‡
#Pandas의 DataFrame(표)
#
#File(CSV, EXCEL)


import pandas as pd
from db.movie_dao import get_reviews
reviews = get_reviews()

for item in reviews:
    print(item)

df_save = pd.DataFrame(reviews)
print(df_save)

now = datetime.now().strftime("%Y%m%d")
df_save.to_excel(f"./review_{now}.xlsx", index=False)