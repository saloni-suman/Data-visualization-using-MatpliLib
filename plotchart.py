from matplotlib import pyplot as plt
ages_x=[25,26,27,28,29,30,31,32,33,34,35]
dev_y=[11250,23456,32145,43251,49085,53213,59934,67890,76543,89065,90876]
plt.plot(ages_x,dev_y,linewidth=3,label="All Devs")

py_dev_y=[23456,29087,34215,40987,49086,54321,66543,71234,78451,89034,90876]
plt.plot(ages_x,py_dev_y,marker="o",label="Python")
plt.xlabel("ages")
plt.ylabel("median salary(USD)")
plt.title("median salary(USD) by age")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
