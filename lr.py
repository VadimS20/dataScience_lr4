import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import seaborn as sns

data = pd.read_excel('data2.xlsx', sheet_name='12', names=['num','class', 'x1', 'x2','x3','x4']).drop('num', axis=1)

x_data=data[['x1','x2','x3','x4']]

#эмпирические функции распределения столбцов
ax = sns.ecdfplot(x_data)                       
ax.axes.set_yticks(np.arange(start=0, stop=1.1, step=0.1))
ax.grid()
plt.show() 

#ящики с усами и скрипичные диаграммы
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5), sharey=True)
sns.boxplot(y = 'x1', data = x_data, ax = axes[0], color = '#FE5e26')
sns.violinplot(y = 'x1', data = x_data, ax = axes[1], color = '#FE5e26')
plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5), sharey=True)
sns.boxplot(y = 'x2', data = x_data, ax = axes[0], color = '#FE5e26')
sns.violinplot(y = 'x2', data = x_data, ax = axes[1], color = '#FE5e26')
plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5), sharey=True)
sns.boxplot(y = 'x3', data = x_data, ax = axes[0], color = '#FE5e26')
sns.violinplot(y = 'x3', data = x_data, ax = axes[1], color = '#FE5e26')
plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5), sharey=True)
sns.boxplot(y = 'x4', data = x_data, ax = axes[0], color = '#FE5e26')
sns.violinplot(y = 'x4', data = x_data, ax = axes[1], color = '#FE5e26')
plt.show()

#гистограммы
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 5), sharey=True)
p3 = sns.histplot(x=data['x1'], ax = axes[0,0])
p4 = sns.histplot(x=data['x2'], ax = axes[0,1])
p3 = sns.histplot(x=data['x3'], ax = axes[1,0])
p4 = sns.histplot(x=data['x4'], ax = axes[1,1])
plt.show()

#диаграммы рассеяния с указанием класса
sns.pairplot(data,hue='class')
plt.show()

#графики двумерных плотностей распределения
sns.jointplot(x=data['x1'], y=data['x2'], cmap="coolwarm", kind = 'hex')
sns.jointplot(x=data['x1'], y=data['x3'], cmap="coolwarm", kind = 'hex')
sns.jointplot(x=data['x1'], y=data['x4'], cmap="coolwarm", kind = 'hex')
plt.show()

sns.jointplot(x=data['x2'], y=data['x1'], cmap="coolwarm", kind = 'hex')
sns.jointplot(x=data['x2'], y=data['x3'], cmap="coolwarm", kind = 'hex')
sns.jointplot(x=data['x2'], y=data['x4'], cmap="coolwarm", kind = 'hex')
plt.show()

sns.jointplot(x=data['x3'], y=data['x1'], cmap="coolwarm", kind = 'hex')
sns.jointplot(x=data['x3'], y=data['x2'], cmap="coolwarm", kind = 'hex')
sns.jointplot(x=data['x3'], y=data['x4'], cmap="coolwarm", kind = 'hex')
plt.show()

sns.jointplot(x=data['x4'], y=data['x1'], cmap="coolwarm", kind = 'hex')
sns.jointplot(x=data['x4'], y=data['x2'], cmap="coolwarm", kind = 'hex')
sns.jointplot(x=data['x4'], y=data['x3'], cmap="coolwarm", kind = 'hex')
plt.show()


#комбинированные диаграммы 
g = sns.swarmplot(y = 'x1', hue = 'class',data = data, dodge = True)
gg = sns.boxplot(y = 'x1', hue = 'class',data = data,showcaps=False,
boxprops={'facecolor':'None', 'linewidth':1.5, 'zorder':10},
showfliers=False, whiskerprops={'linewidth':1., 'zorder':10},
ax = g ,
zorder=10)
plt.show()

g = sns.swarmplot(y = 'x2', hue = 'class',data = data, dodge = True)
gg = sns.boxplot(y = 'x2', hue = 'class',data = data,showcaps=False,
boxprops={'facecolor':'None', 'linewidth':1.5, 'zorder':10},
showfliers=False, whiskerprops={'linewidth':1., 'zorder':10},
ax = g ,
zorder=10)
plt.show()

g = sns.swarmplot(y = 'x3', hue = 'class',data = data, dodge = True)
gg = sns.boxplot(y = 'x3', hue = 'class',data = data,showcaps=False,
boxprops={'facecolor':'None', 'linewidth':1.5, 'zorder':10},
showfliers=False, whiskerprops={'linewidth':1., 'zorder':10},
ax = g ,
zorder=10)
plt.show()

g = sns.swarmplot(y = 'x4', hue = 'class',data = data, dodge = True)
gg = sns.boxplot(y = 'x4', hue = 'class',data = data,showcaps=False,
boxprops={'facecolor':'None', 'linewidth':1.5, 'zorder':10},
showfliers=False, whiskerprops={'linewidth':1., 'zorder':10},
ax = g ,
zorder=10)
plt.show()