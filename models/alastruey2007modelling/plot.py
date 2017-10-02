import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a_name = "alastruey2007modelling_results/23-L-MCA_"

sns.set_style("ticks")
fig1 = plt.figure(1)
fig1.clf()
ax1 = fig1.add_subplot(211)
ax2 = fig1.add_subplot(212)
sns.despine()

fig2 = plt.figure(2)
fig2.clf()
ax3 = fig2.add_subplot(211)
ax4 = fig2.add_subplot(212)
sns.despine()

titles = ["Cardiac cycle - Right middle cerebral artery",
            "Convergence history - Right middle cerebral artery"]
for axs, ext, title in zip([[ax1, ax2], [ax3, ax4]], [".last", ".out"], titles):
    for q, ax, m, lbl in zip(["P", "Q"], axs, [133.332, 1e-6], ["$P$ (mmHg)",
                            "$Q$ (ml$\cdot$s$^{-1}$)"]):

        w = np.loadtxt("{0}{1}{2}".format(a_name, q, ext))

        if "Cardiac cycle" in title:
            w[:,0] -= w[0,0]

        ax.plot(w[:,0], w[:,3]/m)
        ax.set_ylabel(lbl)

        if q == "Q":
            ax.set_xlabel("time (t)")
        else:
            ax.set_title(title)

plt.draw()
plt.show()

fig1.savefig("imgs/{}.png".format(titles[0].split("-")[0].replace(" ","")))
fig2.savefig("imgs/{}.png".format(titles[1].split("-")[0].replace(" ","")))
