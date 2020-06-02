	def pixel_adition(imagen1,imagen2):
		img1 = cv2.imread(imagen1)
		img2 = cv2.imread(imagen2)
		img1 = img1.astype(int)
		img2 = img2.astype(int)

		alto1,ancho1 = img1.shape[:2]
		alto2,ancho2 = img2.shape[:2]
		
		print(alto1,' ',ancho1)
		print(alto2,' ',ancho2)
		alto = 0
		ancho = 0

		if alto1<alto2:
			alto=alto1
		else:
			alto=alto2
		if ancho1<ancho2:
			ancho=ancho1
		else:
			ancho=ancho2

		for i in range(alto):
			for j in range(ancho):
				img1[i][j][0] = img1[i][j][0]/2+img2[i][j][0]/2
				img1[i][j][1] = img1[i][j][1]/2+img2[i][j][1]/2
				img1[i][j][2] = img1[i][j][2]/2+img2[i][j][2]/2

				img1[i][j][0] = img1[i][j][0] + 20
				img1[i][j][1] = img1[i][j][1] + 20
				img1[i][j][2] = img1[i][j][2] + 20
		
		salidaImg = "static/Adition.jpg"
		cv2.imwrite(salidaImg,img1)
		return salidaImg

	def pixel_sustraction(imagen1,imagen2):
		img1 = cv2.imread(imagen1,0)
		img2 = cv2.imread(imagen2,0)
		img1 = img1.astype(int)
		img2 = img2.astype(int)
		#print(img1.dtype,' tipo')

		alto1,ancho1 = img1.shape
		alto2,ancho2 = img2.shape

		for i in range(alto1):
			for j in range(ancho1):
				img1[i][j] = abs(img2[i][j]-img1[i][j])
				img1[i][j]=img1[i][j]+105
		salidaImg1 = "static/prueba_salida.png"
		cv2.imwrite(salidaImg1,img1)
		img = cv2.imread('static/prueba_salida.png',0)
		alto,ancho = img.shape

		img_out=img

		for i in range(alto):
		    for j in range(ancho):
		        if (70<img[i][j] and img[i][j]<130):
		            img_out[i,j]=255
		        else:
		            img_out[i,j]=0
		salidaImg = "static/question_3_sol.png"
		cv2.imwrite(salidaImg, img_out)

		return salidaImg