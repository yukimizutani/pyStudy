import numpy as np
from sklearn.cluster import KMeans
import Machine.basic.ekg_data as ekg_data

segment_len = 32
slide_len = 2

if __name__ == '__main__':
    segments = []
    ekg_filename = 'a02.dat'
    ekg_data = ekg_data.read_ekg_data(ekg_filename)
    for start_pos in range(0, len(ekg_data), slide_len):
        end_pos = start_pos + segment_len
        segment = np.copy(ekg_data[start_pos:end_pos])
        # if we're at the end and we've got a truncated segment, drop it
        if len(segment) != segment_len:
            continue
        segments.append(segment)

    window_rads = np.linspace(0, np.pi, segment_len)
    window = np.sin(window_rads)**2
    windowed_segments = []
    for segment in segments:
        windowed_segment = np.copy(segment) * window
        windowed_segments.append(windowed_segment)

    clusterer = KMeans(n_clusters=150)
    clusterer.fit(windowed_segments)

    #placeholder reconstruction array

    reconstruction = np.zeros(len(ekg_data_anomalous))

    slide_len = segment_len / 2
    # slide_len = 16 as opposed to a slide_len = 2. Slide_len = 2 was used to create a lot of horizontal translations to provide K-Means with a lot of data.

    # segments were created from the ekg_data_anomalous dataset from the code above
    for segment_n, segment in enumerate(segments):
        # normalize by multiplying our window function to each segment
        segment *= window
        # sklearn uses the euclidean square distance to predict the centroid
        nearest_centroid_idx = clusterer.predict(segment.reshape(1, -1))[0]
        centroids = clusterer.cluster_centers_
        nearest_centroid = np.copy(centroids[nearest_centroid_idx])

        # reconstructed our segments with an overlap equal to the slide_len so the centroids are
        stitched
        together
        perfectly.
        pos = segment_n * slide_len
        reconstruction[int(pos):int(pos + segment_len)] += nearest_centroid