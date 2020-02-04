def write_submission(f_store,predec):
	import pandas as pd

	st = pd.DataFrame([f_store,predec])
	st = st.transpose()
	st.columns = ['id','label']
	print(st)
	st.to_csv("submission.csv")

	return st