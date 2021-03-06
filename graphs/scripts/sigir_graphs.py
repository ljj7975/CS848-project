import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math
import re
import sys
import os

root_dir = os.getcwd()
graphs_dir = os.path.join(root_dir, "graphs")

terms = ["idea", "good", "intern", "event", "start", "end"]
doc_freq = ['10%', '20%', '30%', '40%', '50%', '60%']

###

hdfs_runtime = dict()
solr_runtime = dict()
hdfs_ci = dict()
solr_ci = dict()

# 0ms
hdfs_runtime[0] = [14.10, 13.03, 12.90, 12.82, 13.09, 12.58]
solr_runtime[0] = [1.58, 3.61, 6.98, 9.30, 11.42, 14.91]

hdfs_ci[0] = [1, 1, 1, 1, 1, 1]
solr_ci[0] = [1, 1, 1, 1, 1, 1]

# 3ms
hdfs_runtime[3] = [13.85, 16.02, 25.73, 28.77, 31.91, 42.92]
solr_runtime[3] = [3.23, 6.19, 9.65, 12.01, 15.46, 19.24]

hdfs_ci[3] = [1, 1, 1, 1, 1, 1]
solr_ci[3] = [1, 1, 1, 1, 1, 1]

# 30ms
hdfs_runtime[30] = [47.06, 63.09, 108.88, 118.88, 129.67, 187.61]
solr_runtime[30] = [21.36, 41.96, 57.83, 73.32, 93.86, 116.79]

hdfs_ci[30] = [1, 1, 1, 1, 1, 1]
solr_ci[30] = [1, 1, 1, 1, 1, 1]

###

X = np.arange(len(doc_freq))

# 0ms
plt.bar(X - 0.13, hdfs_runtime[0], color='r', width=0.25, yerr=hdfs_ci[0], capsize=3)
plt.bar(X + 0.13, solr_runtime[0], color='b', width=0.25, yerr=solr_ci[0], capsize=3)

plt.xticks(X, doc_freq)
plt.xlabel('Document Frequency')
plt.ylabel('Execution Time (min)')
plt.legend(['HDFS', 'SolrRdd'], loc='upper left')

# plt.show()
plt.savefig(os.path.join(graphs_dir, "runtime_selectivity_0ms.png"))
plt.clf()

# 3ms
plt.bar(X - 0.13, hdfs_runtime[3], color='r', width=0.25, yerr=hdfs_ci[3], capsize=3)
plt.bar(X + 0.13, solr_runtime[3], color='b', width=0.25, yerr=solr_ci[3], capsize=3)

plt.xticks(X, doc_freq)
plt.xlabel('Document Frequency')
plt.ylabel('Execution Time (min)')
plt.legend(['HDFS', 'SolrRdd'], loc='upper left')

# plt.show()
plt.savefig(os.path.join(graphs_dir, "runtime_selectivity_3ms.png"))
plt.clf()

# 30ms
plt.bar(X - 0.13, hdfs_runtime[30], color='r', width=0.25, yerr=hdfs_ci[30], capsize=3)
plt.bar(X + 0.13, solr_runtime[30], color='b', width=0.25, yerr=solr_ci[30], capsize=3)

plt.xticks(X, doc_freq)
plt.xlabel('Document Frequency')
plt.ylabel('Execution Time (min)')
plt.legend(['HDFS', 'SolrRdd'], loc='upper left')

# plt.show()
plt.savefig(os.path.join(graphs_dir, "runtime_selectivity_30ms.png"))
plt.clf()

###

# plt.bar(X - 0.27, hdfs_runtime[0], color='y', width=0.25, yerr=hdfs_ci[0], capsize=3)
# plt.bar(X, hdfs_runtime[3], color='g', width=0.25, yerr=hdfs_ci[3], capsize=3)
# plt.bar(X + 0.27, hdfs_runtime[30], color='b', width=0.25, yerr=hdfs_ci[30], capsize=3)
#
# plt.xticks(X, terms)
# plt.xlabel('Search Term')
# plt.ylabel('Execution Time (m)')
# plt.legend(['0ms', '3ms', '30ms'], loc='upper left')
#
# # plt.show()
# plt.savefig(os.path.join(graphs_dir, "runtime_selectivity_hdfs.png"))
#
# plt.bar(X - 0.27, solr_runtime[0], color='y', width=0.25, yerr=solr_ci[0], capsize=3)
# plt.bar(X, solr_runtime[3], color='g', width=0.25, yerr=solr_ci[3], capsize=3)
# plt.bar(X + 0.27, solr_runtime[30], color='b', width=0.25, yerr=solr_ci[30], capsize=3)
#
# plt.xticks(X, terms)
# plt.xlabel('Search Term')
# plt.ylabel('Execution Time (m)')
# plt.legend(['0ms', '3ms', '30ms'], loc='upper left')
#
# # plt.show()
# plt.savefig(os.path.join(graphs_dir, "runtime_selectivity_solr.png"))
