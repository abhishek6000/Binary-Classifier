import random
import zipfile
from zipfile import ZipFile
sub = pd.read_csv("/content/drive/My Drive/dogs vs cats/sample_submission.csv")
def load_training():
	i_m_t = []
	l_t = []
	train_zip = zipfile.ZipFile('/content/drive/My Drive/dogs vs cats/train.zip', 'r')

	train_img = train_zip.namelist()
	test_img = test_zip.namelist()
	train_img = train_img[1:]
	random.shuffle(train_img)

	folder = '/content/drive/My Drive/dogs vs cat/' 
	count = 0
	for ele in train_img:
  		pic = train_zip.extract(ele)
  		img = plt.imread(pic)
  		img = cv2.resize(img,(200,200))
  		img_mat_train.append(img)

  		if((ele)[6:9]=='cat'):
    		l_t.append(0)
    		count = count + 1
  		else:
			l_t.append(1)
			count = count + 1

	return(i_m_t, l_t)
	
