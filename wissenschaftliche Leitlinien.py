#Wissenschaftliche Notationen:
ax.ticklabel__format(style='sci', axis='x',scilimits=(0,0))
ax.ticklabel__format(style='sci', axis='y',scilimits=(0,0))

#hohe Kontraste verwenden wie colorblind, deep, viridis, magma

#Lesbare Beschriftungen:
plt.xlabel("X-Achse",fontsize=12)
plt.ylabel("Y-Achse",fontsize=12)
plt.legend(title="Kategorien",fontsize=10)

#Betitelung
plt.title("Title des Projekts", fontsize=14)

#Gitterlinien
plt.grid(True, linestyle='--',linewidth=0.5)

#Einheitlicher Stil im gesamten Projekt
sns.set_theme(style="whitegrid")

#Speicherung
plt.savefig("name.png", dpi=300, bbox_inches="tight")

#Quellenangaben:
plt.text(
    x=1.0,
    y=0.1,
    s="Quelle: Name der Quelle (Jahr)",
    fontsize=9,
    ha='right',
    transform=plt.gca().transAxes
)


