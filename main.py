import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('vgsales.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Определяем Топ-жанры по глобальным продажам
# print(df.shape[0]) всего 16598 строк
# print(df.info())
# Пустые значения:
# year - 271 пустых значения
# Publisher - 58 пустых значения
# заполнить Publisher значением Unknown.
# Чтобы заполнить пропуски в столбце Year, сгруппирую значения по столбцу Platform
# далее по каждой платформе найду медиану и ей заполню пропуск
df['Publisher'] = df['Publisher'].fillna('Unknown')

median_years = df.groupby('Platform')['Year'].transform('median')
df['Year'] = df['Year'].fillna(median_years)

top_genres = df.groupby('Genre')['Global_Sales'].sum()
print(top_genres)
top_genres_df = top_genres.reset_index(name='Global_Sales').sort_values(by='Global_Sales', ascending=False)


def top_genres_bar():
	fig, ax = plt.subplots(figsize=(13, 6))
	genres = top_genres_df['Genre']
	global_sales = top_genres_df['Global_Sales']

	bars = ax.bar(genres, global_sales, width=0.5)
	for bar, gl_sales in zip(bars, global_sales):
		height = bar.get_height()
		ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{gl_sales}', va='bottom', ha='center')

	ax.set_xlabel('Жанры')
	ax.set_ylabel('Кол-во продаж по миру')
	ax.set_xticks(top_genres_df['Genre'])
	ax.set_title('Топ жанры по глобальным продажам')
	plt.show()


top_genres_bar()
