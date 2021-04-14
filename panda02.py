import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# 各空港のデータフレームを作成する。
CTS_df = pd.read_excel('sample_1.xlsx')
OKA_df = pd.read_excel('sample_2.xlsx')
FUK_df = pd.read_excel('sample_3.xlsx') 

# headメソッドで先頭5行を確認する。
CTS_df.head()

# tailメソッドで末尾5行を確認する。
OKA_df.tail()

# headメソッドに任意の行数を指定して確認する。
FUK_df.head(10)

# 日付列をindexに設定する。
CTS_df = CTS_df.set_index('日付')
OKA_df = OKA_df.set_index('日付')
FUK_df = FUK_df.set_index('日付')

# 中身を確認する。
CTS_df.head()

# 3つのデータフレームを結合する。
df = pd.concat([CTS_df, OKA_df, FUK_df], axis=0)

# 結合したデータフレームをExcelファイルに変換する。
df.to_excel('merge.xlsx')

# 日付列を昇順に並び替えする。
df.sort_values('日付', ascending=True, inplace=True)
df.head()

# 複数のExcelファイルを読み込んで1つのデータフレームを作成する方法
# パスを書いていないので結果は出ません。
from glob import glob

base_df = pd.DataFrame()

files = glob('Excelファイルまでのパス/*.xlsx')

for i in files:
    each_df = pd.read_excel(i)
    df = pd.concat([base_df, each_df])

# 折れ線グラフを描画する。
fig, ax = plt.subplots()

x = [i for i in range(1, 31)]

ax.plot(x, CTS_df.loc[:, '旅客数'], label='CTS')
ax.plot(x, OKA_df.loc[:, '旅客数'], label='OKA')
ax.plot(x, FUK_df.loc[:, '旅客数'], label='FUK')
ax.set_title('旅客数比較')
ax.legend()

plt.show()

# 棒グラフを描画する。
fig, ax = plt.subplots(figsize=(10, 5))

width = 0.3
width2 = 0.6

x = [i for i in range(1, 31)]

x2 = [i+width for i in x]
x3 = [i+width2 for i in x]

ax.bar(x, CTS_df.loc[:, '旅客数'], width=width, label='CTS', alpha=0.7)
ax.bar(x2, OKA_df.loc[:, '旅客数'], width=width, label='OKA', alpha=0.7)
ax.bar(x3, FUK_df.loc[:, '旅客数'], width=width, label='FUK', alpha=0.7)
ax.set_title('旅客数比較')
ax.set_xlabel('11-01-11/30')
ax.legend(loc='best')

plt.show()

# X軸の目盛りと、Y軸の目盛りを変更して、再度棒グラフを描画する。
fig, ax = plt.subplots(figsize=(10, 5))

width = 0.3
width2 = 0.6

x = [i for i in range(1, 31)]

x2 = [i+width for i in x]
x3 = [i+width2 for i in x]

ax.bar(x, CTS_df.loc[:, '旅客数'], width=width, label='CTS', alpha=0.7)
ax.bar(x2, OKA_df.loc[:, '旅客数'], width=width, label='OKA', alpha=0.7)
ax.bar(x3, FUK_df.loc[:, '旅客数'], width=width, label='FUK', alpha=0.7)
ax.set_title('旅客数比較')
ax.legend(loc='best')

plt.xticks(x)
plt.ylim(ymin=150) 
plt.show()

# 積み上げ棒グラフを描画する。
fig, ax = plt.subplots()

x = [i for i in range(1, 31)]

pax = CTS_df.loc[:, '旅客数']
cgo = CTS_df.loc[:, '貨物重量']
ttl = [i + j for i, j in zip(pax, cgo)]

ax.bar(x, ttl, label='旅客数')
ax.bar(x, cgo, label='貨物重量')
ax.legend()
ax.set_title('PAX + CGO')

plt.xticks(x, rotation=90)
plt.ylim(ymin=7500)
plt.show()

# Pandasのplotメソッドを使って積み上げ棒グラフを描画する。
CTS_df.plot.bar(stacked=True)
plt.show()

# 散布図を描画する。
fig, ax = plt.subplots()

x = CTS_df['旅客数']
y = CTS_df['貨物重量']

ax.scatter(x, y, marker='*')
ax.set_xlabel('旅客数')
ax.set_ylabel('貨物重量')

plt.show()

# 箱ひげ図を描画する。
fig, ax = plt.subplots()

CTS = CTS_df.loc[:, '旅客数']
OKA = OKA_df.loc[:, '旅客数']
FUK = FUK_df.loc[:, '旅客数']

label = ['CTS', 'OKA', 'FUK']
ax.boxplot((CTS, OKA, FUK), labels=label)

plt.show()

# ヒストグラムを描画する。
fig, ax = plt.subplots()

x = CTS_df.loc[:, '旅客数']

ax.hist(x)

plt.show()

# ビンの数を変更してヒストグラムを描画する。
fig, ax = plt.subplots()

x = CTS_df.loc[:, '旅客数']

ax.hist(x, bins=20)

plt.show()

# histのメソッドの返り値を利用して、度数分布表を表示する。
fig, ax = plt.subplots()

x = CTS_df.loc[:, '旅客数']

num, bin, void = ax.hist(x, bins=20)

for i, j in enumerate(num):
    print('{:.1f} {:.1f} : {}'.format(bin[i], bin[i+1], j))


# 円グラフを描画する。
fig, ax = plt.subplots()

CTS = CTS_df.loc[:, '貨物重量'].mean()
OKA = OKA_df.loc[:, '貨物重量'].mean()
FUK = FUK_df.loc[:, '貨物重量'].mean()

data = [CTS, OKA, FUK]
label = ['CTS', 'OKA', 'FUK']

ax.pie(data, labels=label)

plt.show()

# 円グラフに様々な引数を記述して視認性を高めて描画する。
fig, ax = plt.subplots()

CTS = CTS_df.loc[:, '貨物重量'].mean()
OKA = OKA_df.loc[:, '貨物重量'].mean()
FUK = FUK_df.loc[:, '貨物重量'].mean()

data = [CTS, OKA, FUK]
label = ['CTS', 'OKA', 'FUK']
explode = [0, 0.2, 0]

ax.pie(data, labels=label, explode=explode, autopct='%1.1f%%', 
       startangle=90, counterclock=False)

ax.set_title('旅客数の平均値割合')

plt.show()

# 3つのサブプロットを作成して各空港の散布図を描画する。
fig, ax = plt.subplots(figsize=(9, 3), ncols=3)

cts_pax = CTS_df.loc[:, '旅客数']
cts_cgo = CTS_df.loc[:, '貨物重量']
oka_pax = OKA_df.loc[:, '旅客数']
oka_cgo = OKA_df.loc[:, '貨物重量']
fuk_pax = FUK_df.loc[:, '旅客数']
fuk_cgo = FUK_df.loc[:, '貨物重量']

ax[0].scatter(cts_pax, cts_cgo, label='CTS', marker='*')
ax[0].set_xlabel('旅客数')
ax[0].set_ylabel('貨物重量')
ax[0].legend()
ax[1].scatter(oka_pax, oka_cgo, label='OKA', marker='s')
ax[1].set_xlabel('旅客数')
ax[1].set_ylabel('貨物重量')
ax[1].legend()
ax[2].scatter(fuk_pax, fuk_cgo, label='FUK')
ax[2].set_xlabel('旅客数')
ax[2].set_ylabel('貨物重量')
ax[2].legend()

plt.tight_layout()
plt.show()

# 1つのサブプロットに、3空港のデータを散布図で描画する。
fig, ax = plt.subplots()

cts_pax = CTS_df.loc[:, '旅客数']
cts_cgo = CTS_df.loc[:, '貨物重量']
oka_pax = OKA_df.loc[:, '旅客数']
oka_cgo = OKA_df.loc[:, '貨物重量']
fuk_pax = FUK_df.loc[:, '旅客数']
fuk_cgo = FUK_df.loc[:, '貨物重量']

ax.scatter(cts_pax, cts_cgo, label='CTS', marker='*')
ax.scatter(oka_pax, oka_cgo, label='OKA', marker='s')
ax.scatter(fuk_pax, fuk_cgo, label='FUK')
ax.set_xlabel('旅客数')
ax.set_ylabel('貨物重量')
ax.legend()

plt.tight_layout()
plt.show()

# 日単位で集計したデータを折れ線グラフで描画する。
daily_df = df.resample('D').sum()

fig, ax = plt.subplots(2)

x = [i for i in range(1, 31)]

pax = daily_df.loc[:, '旅客数']
cgo = daily_df.loc[:, '貨物重量']

ax[0].plot(x, pax)
ax[0].set_title('旅客数')
ax[1].plot(x, cgo)
ax[1].set_title('貨物重量')

plt.tight_layout()
plt.show()

# 各空港の貨物重量の合計値を棒グラフで可視化する。
fig, ax = plt.subplots()

cts = CTS_df.loc[:, '貨物重量'].sum()
oka = OKA_df.loc[:, '貨物重量'].sum()
fuk = FUK_df.loc[:, '貨物重量'].sum()

x = [1, 2, 3]
data = [cts, oka, fuk]
label = ['CTS', 'OKA', 'FUK']

ax.bar(x, data, tick_label=label)
ax.set_title('空港別貨物合計値')

plt.show()

# Pandasのgroupbyメソッドを使ってみる。（合計値と平均値）
df_sum = df.groupby(pd.Grouper(freq='W-SUN')).sum()
df_sum.head(3)

df_mean = df.groupby(pd.Grouper(freq='W-SUN')).mean()
df_mean.head(3)

# 周期的にまるめて集計（合計）した旅客数を棒グラフで可視化する。
groupby_sum_cts = CTS_df.groupby(pd.Grouper(freq='W-SUN')).sum()
sum_cts_pax = groupby_sum_cts.loc[:, '旅客数']

groupby_sum_oka = OKA_df.groupby(pd.Grouper(freq='W-SUN')).sum()
sum_oka_pax = groupby_sum_oka.loc[:, '旅客数']

groupby_sum_fuk = FUK_df.groupby(pd.Grouper(freq='W-SUN')).sum()
sum_fuk_pax = groupby_sum_fuk.loc[:, '旅客数']

fig, ax = plt.subplots(figsize=(15, 3), ncols=3)

x = sum_cts_pax.index

ax[0].bar(x, sum_cts_pax)
ax[0].set_title('CTS')
ax[0].set_xticks(x)
ax[0].set_yticks([250, 500, 750, 1000, 1250, 1500])
plot0_labels = ax[0].get_xticklabels()
plt.setp(plot0_labels, rotation=90)

ax[1].bar(x, sum_oka_pax)
ax[1].set_title('OKA')
ax[1].set_xticks(x)
ax[1].set_yticks([250, 500, 750, 1000, 1250, 1500])
plot1_labels = ax[1].get_xticklabels()
plt.setp(plot1_labels, rotation=90)

ax[2].bar(x, sum_fuk_pax)
ax[2].set_title('FUK')
ax[2].set_xticks(x)
ax[2].set_yticks([250, 500, 750, 1000, 1250, 1500])
plot2_labels = ax[2].get_xticklabels()
plt.setp(plot2_labels, rotation=90)

plt.suptitle('週単位集計（月～日）')
plt.tight_layout()
plt.show()

# 周期的にまるめて集計（平均）した旅客数を棒グラフで可視化する。
groupby_mean_cts = CTS_df.groupby(pd.Grouper(freq='W-SUN')).mean()
mean_cts_pax = groupby_mean_cts.loc[:, '旅客数']

groupby_mean_oka = OKA_df.groupby(pd.Grouper(freq='W-SUN')).mean()
mean_oka_pax = groupby_mean_oka.loc[:, '旅客数']

groupby_mean_fuk = FUK_df.groupby(pd.Grouper(freq='W-SUN')).mean()
mean_fuk_pax = groupby_mean_fuk.loc[:, '旅客数']

fig, ax = plt.subplots(figsize=(15, 3), ncols=3)

x = mean_cts_pax.index

ax[0].bar(x, mean_cts_pax)
ax[0].set_title('CTS')
ax[0].set_xticks(x)
plot0_labels = ax[0].get_xticklabels()
plt.setp(plot0_labels, rotation=90)

ax[1].bar(x, mean_oka_pax)
ax[1].set_title('OKA')
ax[1].set_xticks(x)
plot1_labels = ax[1].get_xticklabels()
plt.setp(plot1_labels, rotation=90)

ax[2].bar(x, mean_fuk_pax)
ax[2].set_title('FUK')
ax[2].set_xticks(x)
plot2_labels = ax[2].get_xticklabels()
plt.setp(plot2_labels, rotation=90)

plt.suptitle('週単位集計/平均値（月～日）')
plt.tight_layout()
plt.show()