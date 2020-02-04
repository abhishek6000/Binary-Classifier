import random
import zipfile
from zipfile import ZipFile
def load_test():
	test_zip = zipfile.ZipFile('/content/drive/My Drive/dogs vs cats/test.zip', 'r')

	test_img = test_img[1:]
	test = []
	for ele in test_img:
  		pic = test_zip.extract(ele)
  		img = plt.imread(pic)
  		img = cv2.resize(img,(200,200))
  		test.append(img)

  	return test
