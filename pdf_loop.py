import os
from fpdf import FPDF


def concatPic(img_path):
	# count the images file from the img_path
	cnt = 0
	for file in os.listdir(img_path):
		if file.endswith('.png'):
			cnt += 1

	for a in range(1,cnt):
		path = img_path + '/' +  str(a) + '.png'
		print('converting: ' + path + ' to PDF')
		pdf.image(path ,w=200)
		output_path = img_path + '/' + 'output.pdf'
	pdf.output(output_path,'f')
	return 0


if __name__ == '__main__':
	pdf = FPDF()
	pdf.add_page()
	img_path = 'lecture_'
	for a in range(1,24):
		img_path_1 = img_path + str(a)
		print('Working in ' + img_path_1)
		concatPic(img_path=img_path_1)