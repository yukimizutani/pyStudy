from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import Machine.basic.learn_utils as learn_utils
from sklearn.cluster import KMeans
import learn_utils

timeline = [1000.0, 1500.0, 2000.0, 2300.0, 2500.0, 2600.0, 2500.0, 2300.0, 2000.0, 1500.0, 1000.0]
plt.plot(timeline)
plt.xlabel("Sample number")
plt.ylabel("Signal value")
plt.show()
segment_len = 3
slide_len = 1

segments = []
for start_pos in range(0, len(timeline), slide_len):
    end_pos = start_pos + segment_len
    segment = np.copy(timeline[start_pos:end_pos])
    if len(segment) != segment_len:
        continue
    segments.append(segment)

window_rads = np.linspace(0, np.pi, segment_len)
window = np.sin(window_rads) ** 2
print(window)

windowed_segments = segments
# for segment in segments:
#     windowed_segment = np.copy(segment) * window
#     windowed_segments.append(windowed_segment)

# learn_utils.show_every_wave(windowed_segments)

clusterer = KMeans(n_clusters=5)
clusterer.fit(windowed_segments)

# learn_utils.show_every_wave(clusterer.cluster_centers_)

slide_len = segment_len / 2
test_segments = learn_utils.sliding_chunker(
    timeline,
    window_len=segment_len,
    slide_len=int(slide_len)
)

centroids = clusterer.cluster_centers_

segment = np.copy(test_segments[0])
# remember, the clustering was set up using the windowed data
# so to find a match, we should also window our search key
windowed_segment = segment * window
# predict() returns a list of centres to cope with the possibility of multiple
# samples being passed
nearest_centroid_idx = clusterer.predict([windowed_segment])[0]
nearest_centroid = np.copy(centroids[nearest_centroid_idx])

reconstruction = np.zeros(len(timeline))
slide_len = segment_len / 2

for segment_n, segment in enumerate(test_segments):
    # don't modify the data in segments
    segment = np.copy(segment)
    segment *= window
    nearest_centroid_idx = clusterer.predict([segment])[0]
    centroids = clusterer.cluster_centers_
    nearest_centroid = np.copy(centroids[nearest_centroid_idx])

    # overlay our reconstructed segments with an overlap of half a segment
    pos = segment_n * slide_len
    print(reconstruction)
    print(nearest_centroid)
    print(int(pos))
    print(int(pos + segment_len))
    reconstruction[int(pos):int(pos + segment_len)] += nearest_centroid

n_plot_samples = 300

error = reconstruction[0:n_plot_samples] - timeline[0:n_plot_samples]
error_98th_percentile = np.percentile(error, 98)
print("Maximum reconstruction error was %.1f" % error.max())
print("98th percentile of reconstruction error was %.1f" % error_98th_percentile)

plt.plot(timeline[0:n_plot_samples], label="Original Timeline")
plt.plot(reconstruction[0:n_plot_samples], label="Predicted Timeline")
plt.plot(error[0:n_plot_samples], label="Diff")
plt.legend()
plt.show()

timeline_anomalous = np.copy(timeline)
timeline_anomalous[210:215] = 0

reconstruction = learn_utils.reconstruct(timeline_anomalous, window, clusterer)

error = reconstruction[0:n_plot_samples] - timeline_anomalous[0:n_plot_samples]
error_98th_percentile = np.percentile(error, 98)
print("Maximum reconstruction error was %.1f" % error.max())
print("98th percentile of reconstruction error was %.1f" % error_98th_percentile)

plt.plot(timeline_anomalous[0:n_plot_samples], label="Original Timeline")
plt.plot(reconstruction[0:n_plot_samples], label="Predicted Timeline")
plt.plot(error[0:n_plot_samples], label="Diff")
plt.legend()
plt.show()
