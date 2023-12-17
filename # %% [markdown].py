# %% [markdown]
# импортируем библеотку pabdas 
# создаем переменную и читаем нашу таблицу(переменная будет хранит эту таблицу)
# и выводим нашу переременную 

# %%
import pandas as pd
import numpy as np
artists = pd.read_csv("EDA - Spotify Top10 2010 - 2019.csv")

artists

# %% [markdown]
# выводим количество строк и столбцов
# первый элемент количество строк 
# второй количество столбцов 

# %%
artists.shape

# %% [markdown]
# выводим информацию о DataFrame 
# количество непустых значений в каждом столбце
# тип данных каждого столбца
# общее количество столбцов 
# количество использованной памяти

# %%
artists.info()

# %% [markdown]
# выводим первые 800 колонок

# %%
artists.head(800)

# %% [markdown]
# выводим 400 последних колонок 

# %%
artists.tail(400)

# %% [markdown]
# выводим подсчет уникальных значений в столбце или в DataFrame

# %%
artists.nunique()

# %% [markdown]
# выводим основные статистические показатели для каждого числового столбца, 
# такие как количество, 
# среднее значение, 
# стандартное отклонение, 
# минимальное и максимальное значения, 
# медиана и квартили.

# %%
artists.describe()

# %% [markdown]
# выводим первую колонку и всю её информацию

# %%
artists.loc[0]

# %% [markdown]
# выводим первые три колонки artist и top genre, year

# %%
subset = artists.loc[[0,1,2], ["artist", 'top genre', 'year']]

subset

# %% [markdown]
# 

# %% [markdown]
# удаляем колонки year и bpm все

# %%
artists[["year", "bpm"]] = artists[["year", "bpm"]].fillna(0)

artists

# %% [markdown]
# удаляем дубликаты

# %%
artists.drop_duplicates()

# %% [markdown]
# выводим все колонки

# %%
artists.columns

# %% [markdown]
# заменяем все пустые значения(

# %%
artists = artists.replace({"year": np.nan}, "Unknown")

artists

# %%
artists.to_csv("new_dataset.csv", index=False)


