class dataPPro():
    def __init__(self, dataImg, dataLabel, path=''):
        self.dataImg   = dataImg
        self.dataLabel = dataLabel
        self.path      = path

        
    def getImg(self):
        return self.dataImg
        
    def setImg(self, newImg):
        self.dataImg = newImg
        
    def getLabel(self):
        return self.dataImg
        
    def setLabel(self, newLabel):
        self.dataLabel = newLabel
        
       
    # Preprocess the data: RGB > grayscale
    def proGray(self, newImg = self.dataImg, newLabel = self.dataLabel):
        outImg = np.empty_like(newImg)
        outImg = np.array([cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in newImg ])
        outImg = outImg[..., newaxis]
        outLabel = newLabel.copy()
        return outImg, outLabel


    # Preprocess the data: input{RGB,GRAY} > sharpen
    def proShp(self, newImg = self.dataImg, newLabel = self.dataLabel):
        kernel = np.array([[-1,-1,-1], [-1,10,-1], [-1,-1,-1]])
        outImg = np.array([cv2.filter2D(img, -1, kernel) for img in newImg])
        #outImg = outImg[..., newaxis]
        outLabel = newLabel.copy()
        return outImg, outLabel
    
    
    # Preprocess the data: sharpen > equalized histogram
    def proHst(self, newImg = self.dataImg, newLabel = self.dataLabel):
        outImg = np.array([cv2.equalizeHist(img) for img in newImg ])
        #outImg = outImg[..., newaxis]
        outLabel = newLabel.copy()
        return outImg, outLabel
    

    # Preprocess the data: equalized histogram > CLAHE
    def proClahe(self, newImg = self.dataImg, newLabel = self.dataLabel):
        '''CLAHE - Equalize (adaptively with limited contrast) the histogram of a globaly equalize image'''
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        outImg = np.array([clahe.apply(img) for img in newImg ])
        #outImg = outImg[..., newaxis]
        outLabel = newLabel.copy()
        return outImg, outLabel

    
    # Preprocess the data: CLAHE > center & normilize images
    def proCtrNrm(self, newImg = self.dataImg, newLabel = self.dataLabel):
        '''Source: SDCNP, Lesson 8, lecture 23-Normalized Inputs and Initial Weights'''
        outImg = (newImg - np.mean(newImg))/np.std(newImg) # zero-center&normalize
        outLabel = newLabel.copy()
        return outImg, outLabel

    
    def __str__(self):
        return '< dataPPro >'  
    