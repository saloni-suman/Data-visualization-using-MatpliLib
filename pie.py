from matplotlib import pyplot as plt

#plt.style.use("")
slices=[53451,12345,47653,36443,35917]
labels=["javascript","Html/css","python","sql","java"]
explode=[0,0,0.1,0,0]
plt.pie(slices,labels=labels,explode=explode,shadow=True,autopct="%1.1f%%",wedgeprops={'edgecolor':'black'},startangle=0)
plt.title("prog. language statistic")
plt.legend(loc=(0.00,0.00))
plt.show()
