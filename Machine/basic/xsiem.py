from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import Machine.basic.learn_utils as learn_utils
from sklearn.cluster import KMeans
import learn_utils

original_timeline = [0.0, 0.0, 0.0, 1000.0, 0.0, 700.0, 0.0, 0.0, 0.0, 0.0, 0.0]
plt.plot(original_timeline)
plt.xlabel("Sample number")
plt.ylabel("Signal value")
plt.show()
segment_len = 3
slide_len = 1

timeline = original_timeline[0:len(original_timeline) - 1]

segments = []
for start_pos in range(0, len(timeline), slide_len):
    end_pos = start_pos + segment_len
    segment = np.copy(timeline[start_pos:end_pos])
    if len(segment) != segment_len:
        continue
    segments.append(segment)

learn_utils.plot_waves(segments, 1, "segments")

window_rads = np.linspace(0, np.pi, segment_len)
window = np.sin(window_rads) ** 2
learn_utils.show_wave(window)

# windowed_segments = segments
windowed_segments = []
for segment in segments:
    windowed_segment = np.copy(segment) * window
    windowed_segments.append(windowed_segment)

learn_utils.plot_waves(windowed_segments, 1, "windowed segments")

clusterer = KMeans(n_clusters=3)
clusterer.fit(windowed_segments)

learn_utils.plot_waves(clusterer.cluster_centers_, 1, "clusters")

test_segments = learn_utils.sliding_chunker(
    timeline,
    window_len=segment_len,
    slide_len=int(slide_len)
)

centroids = clusterer.cluster_centers_

segment = np.copy(test_segments[0])
# remember, the clustering was set up using the windowed data
# so to find a match, we should also window our search key
windowed_segment = segment
# predict() returns a list of centres to cope with the possibility of multiple
# samples being passed
# nearest_centroid_idx = clusterer.predict([windowed_segment])[0]
# nearest_centroid = np.copy(centroids[nearest_centroid_idx])

reconstruction = np.zeros(len(timeline))

# start = 0
# end = start + segment_len
#
# while end <= len(timeline):
#     nearest_centroid_idx = clusterer.predict([test_segments[start]])[0]
#     nearest_centroid = np.copy(centroids[nearest_centroid_idx])
#     reconstruction[start:end] += nearest_centroid
#     start += segment_len
#     end += segment_len

for segment_n, segment in enumerate(test_segments):
    # don't modify the data in segments
    segment = np.copy(segment)
    nearest_centroid_idx = clusterer.predict([segment])[0]
    centroids = clusterer.cluster_centers_
    nearest_centroid = np.copy(centroids[nearest_centroid_idx])

    # overlay our reconstructed segments with an overlap of half a segment
    pos = segment_n * slide_len
    print(reconstruction)
    print(nearest_centroid)
    print(int(pos))
    print(int(pos + segment_len))
    if len(reconstruction[int(pos):int(pos + segment_len)]) == 3:
        reconstruction[int(pos):int(pos + segment_len)] += nearest_centroid

n_plot_samples = 300

# error = reconstruction[0:n_plot_samples] - timeline[0:n_plot_samples]
# error_98th_percentile = np.percentile(error, 98)
# print("Maximum reconstruction error was %.1f" % error.max())
# print("98th percentile of reconstruction error was %.1f" % error_98th_percentile)

plt.plot(original_timeline[0:n_plot_samples], label="Original Timeline")
plt.plot(reconstruction[0:n_plot_samples], label="Reconstructed Timeline")
# plt.plot(error[0:n_plot_samples], label="Diff")
plt.legend()
plt.show()

timeline_anomalous = np.copy(timeline)
timeline_anomalous[210:215] = 0

# future = [1000.0, 0.0, 700.0]
# nearest_centroid_idx = clusterer.predict([future * window])[0]
# centroids = clusterer.cluster_centers_
# nearest_centroid = np.copy(centroids[nearest_centroid_idx])
# reconstruction[3:6] += nearest_centroid

# error = reconstruction[0:n_plot_samples] - timeline_anomalous[0:n_plot_samples]
# error_98th_percentile = np.percentile(error, 98)
# print("Maximum reconstruction error was %.1f" % error.max())
# print("98th percentile of reconstruction error was %.1f" % error_98th_percentile)

original_timeline[7] = 4000.0

segments = []
for start_pos in range(0, len(original_timeline), slide_len):
    end_pos = start_pos + segment_len
    segment = np.copy(original_timeline[start_pos:end_pos])
    if len(segment) != segment_len:
        continue
    segments.append(segment)

reconstruction = np.zeros(len(original_timeline))

for segment_n, segment in enumerate(segments):
    # don't modify the data in segments
    segment = np.copy(segment)
    nearest_centroid_idx = clusterer.predict([segment])[0]
    centroids = clusterer.cluster_centers_
    nearest_centroid = np.copy(centroids[nearest_centroid_idx])

    # overlay our reconstructed segments with an overlap of half a segment
    pos = segment_n * slide_len
    print(reconstruction)
    print(nearest_centroid)
    print(int(pos))
    print(int(pos + segment_len))
    if len(reconstruction[int(pos):int(pos + segment_len)]) == 3:
        reconstruction[int(pos):int(pos + segment_len)] += nearest_centroid

plt.plot(original_timeline[0:n_plot_samples], label="Original Timeline")
plt.plot(reconstruction[0:n_plot_samples], label="Predicted Timeline")
# plt.plot(error[0:n_plot_samples], label="Diff")
plt.legend()
plt.show()
