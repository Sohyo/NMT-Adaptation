from nmt_adaptation.util import arr2txt, rm_dupl_from_list, text2arr
from os.path import join
import numpy as np
import matplotlib.pyplot as plt


def get_length_sentences_from_file(path_data: dir) -> list:
    length_sentences = []
    with open(join(path_data, "train.de")) as text:
        for sentence in text:
            words = sentence.split()
            length_sentences.append(len(words))

    return length_sentences


root_dir = "../data/custom_data"
list_of_data = ['EMEA', 'GNOME', 'JRC']
leng_dataset = []
for data in list_of_data:
    leng_dataset.append(get_length_sentences_from_file(join(root_dir, data)))

kwargs = dict(histtype='stepfilled', alpha=0.4, bins=50)
# plt.axis([0, 140, 0, 200])
plt.hist(leng_dataset[0], **kwargs)
plt.hist(leng_dataset[1], **kwargs)
plt.hist(leng_dataset[2], **kwargs)

plt.ylabel('Counts')
plt.xlabel('Length of sentence')
plt.legend()
plt.show()


##### bar plot : overlapping phrases

labels = ['1','2', '3~4','5~7', '8~12', '13~20']
EMEA = [0.415, 0.16781017724413952, 0.050, 0.021835951998020537, 0.011, 0.008]
GNOME = [0.43381642512077295,0.17996955197912134, 0.04686204710586629, 0.017749140214254656, 0.010800807537012113, 0.008272165909355703]
JRC = [0.6628092577813248, 0.3251381215469613, 0.11767664068393262, 0.021847070506454815, 0.00733783387144115, 0.007077856420626896]
x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x+0.0, EMEA, width, label='EMEA', color='tab:blue')
rects2 = ax.bar(x+0.2, GNOME, width, label='GNOME', color='salmon')
rects3 = ax.bar(x+0.40, JRC, width, label='JRC', color='olivedrab')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Proportion of overlapping phrases',fontweight='bold')
ax.set_xlabel('Length of phrases',fontweight='bold')
ax.set_xticks(x + width)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width()/2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
fig.tight_layout()

plt.show()


# multiple line plots
plt.plot(labels, EMEA, marker='.',  color='tab:blue', label="EMEA")
plt.plot(labels, GNOME, marker='v', color='salmon', linewidth=2, label="GNOME")
plt.plot(labels, JRC, marker='s', color='olive', linewidth=2, label="JRC")
# show legend

plt.ylabel('Proportion of overlapping phrases',fontweight='bold')
plt.xlabel('Length of phrases', fontweight='bold')
plt.legend()
# show graph
plt.show()
