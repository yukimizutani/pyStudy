# # -*- coding: utf-8 -*-
# Load example data
from sklearn import datasets
digits = datasets.load_digits()
# データフォーマットの確認
for i in range(10):
    print('{} : {}'.format(digits.data[i], digits.target[i]))
# print(digits.data.shape)
n_samples = len(digits.data) # データ数
print(n_samples)

# import matplotlib.pyplot as plt
# images_and_labels = list(zip(digits.images, digits.target))
# for index, (image, label) in enumerate(images_and_labels[:10]):
#     plt.subplot(2, 5, index + 1)
#     plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
#     plt.axis('off')
#     plt.title('Training: %i' % label)
# plt.show()

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
# train SVM
clf.fit(digits.data[:n_samples * 6 / 10 ], digits.target[:n_samples * 6 / 10])

print(digits.target[-10:]) # 正解ラベル
print(clf.predict(digits.data[-10:])) # 予測ラベル

expected = digits.target[n_samples * -4 / 10:] # 正解ラベル
predicted = clf.predict(digits.data[n_samples * -4 / 10:]) # 予測ラベル
