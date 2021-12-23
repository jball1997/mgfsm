import json
import faulthandler
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer
from pyclustering.utils.metric import distance_metric, type_metric
from pyclustering.utils import calculate_distance_matrix

def lcs(X, Y, m, n) -> int:
    '''
    a simple longest common substring calculation
    '''
    if m == 0 or n == 0:
       return 0
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1)
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

def dlcs(p1, p2) -> int:
    '''
    take the union of the events in p1 and p2 and
    takes the longest common substring length
    to do a calculation from shepard's paper
    '''
    union = set(p1) | set(p2)
    return 1 - (lcs(p1, p2, len(p1), len(p2)) / len(union))

def docc(p1,p2) -> float:
    '''
    takes the intersection of p1 and p2 and accounts
    for rarity of events
    '''
    intersection = set(p1) & set(p2)
    with open('/home/jball/CodeInquisitor/PATTERN_ANALYSIS/pattern_frequencies.json') as f:
        frequencies = f.read()
    frequencies = json.loads(frequencies)
    freq_sum = sum([v for v in frequencies.values()])
    if len(intersection) == 0:
        return 1
    else:
        ret = 0
        for e in list(intersection):
            ret += frequencies[str(e)] / freq_sum
        return ret 

def distance(p1, p2) -> float:
    '''
    # Caclulates "distance" between pattern1 and pattern2.
    # D(p1, p2) = alpha*(lcs(p1,p2)) + 1-alpha*(occ(p1,p2))
    '''
    return .25*dlcs(p1,p2) + .75*docc(p1,p2)

# investigate outputted patterns
with open('OUTPUT/translatedFS') as FS:
    readable_patterns = FS.readlines()
filtered_patterns = []
for pattern_i, pattern in enumerate(readable_patterns):
# filter out patterns with a length less than 10
    pattern = pattern.split(' ')[:-1]
    if len(pattern) > 10:
        filtered_patterns.append([int(event) for event in pattern])

filtered_patterns = filtered_patterns[:2]

# initialize medoids
print('initializing random medoids...')
init_medoids = []
for num in range(20):
    init_medoids.append(filtered_patterns[num * int(len(filtered_patterns)/20)])

# Create instance of K-Medoids algorithm.
print('setting custom distance function...')
metric = distance_metric(type_metric.USER_DEFINED, func=distance)
# distance = metric([22, 45, 22, 24, 22, 45, 22, 24, 22, 45, 9], [22, 52, 39, 22, 51, 52, 39, 22, 51, 22, 52])
# print(distance)
print('making distance matrix...')
matrix = calculate_distance_matrix(filtered_patterns, metric=distance)
print('instantiating k-medoids...')
pam = kmedoids(matrix, init_medoids, data_type='distance_matrix', ccore=False)
print('cluster analysis and obtaining results...')
faulthandler.enable()
pam.process()
clusters = pam.get_clusters()
medoids = pam.get_medoids()
print('showing results...')
visualizer = cluster_visualizer()
visualizer.append_clusters(clusters, filtered_patterns)
visualizer.append_cluster(init_medoids, filtered_patterns, markersize=12, marker='*', color='gray')
visualizer.append_cluster(medoids, filtered_patterns, markersize=14, marker='*', color='black')
visualizer.save('kmedoids_clusters.png')