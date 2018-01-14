import os
import cv2

def concatPic(img_path):
	# count the images file from the img_path
	cnt = 0
	for file in os.listdir(img_path):
		if file.endswith('.png'):
			cnt += 1
	print(img_path)
	base = cv2.imread('./' + img_path + '/' + str(1) + '.png')
	# resize each image and concatenate to one specific image
	for a in range(1, cnt):
		file_path = './' + img_path + '/' + str(a) + '.png'
		if os.path.isfile(file_path):
			img = cv2.imread(file_path)
			base = cv2.vconcat([base, img])
	cv2.imwrite(img_path + '/output.png', base)
	return 0


if __name__ == '__main__':
	img_path = 'lecture_'
	for a in range(1,23):
		img_path_1 = img_path + str(a)
		concatPic(img_path=img_path_1)