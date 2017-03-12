class dataPPro():
    def __init__(self, dataImg, dataLabel, path=''):
        self.dataImg   = dataImg
        self.dataLabel = dataLabel
        self.path      = path


    # Preprocess the data: RGB > grayscale
    def proGray(self):
        outImg = np.empty_like(self.dataImg)
        outImg = np.array([cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in self.dataImg ])
        outImg = outImg[..., newaxis]
        outLabel = self.dataLabel.copy()
        return outImg, outLabel


    # Preprocess the data: input{RGB,GRAY} > sharpen
    def proShp(self):
        kernel = np.array([[-1,-1,-1], [-1,10,-1], [-1,-1,-1]])
        outImg = np.array([cv2.filter2D(img, -1, kernel) for img in self.dataImg])
        #outImg = outImg[..., newaxis]
        outLabel = self.dataLabel.copy()
        return outImg, outLabel
    
    
    # Preprocess the data: sharpen > equalized histogram
    def proHst(self):
        outImg = np.array([cv2.equalizeHist(img) for img in self.dataImg ])
        #outImg = outImg[..., newaxis]
        outLabel = self.dataLabel.copy()
        return outImg, outLabel
    

    # Preprocess the data: equalized histogram > CLAHE
    def proClahe(self):
        '''CLAHE - Equalize (adaptively with limited contrast) the histogram of a globaly equalize image'''
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        outImg = np.array([clahe.apply(img) for img in self.dataImg ])
        #outImg = outImg[..., newaxis]
        outLabel = self.dataLabel.copy()
        return outImg, outLabel

    
    # Preprocess the data: CLAHE > center & normilize images
    def proCtrNrm(self):
        '''Source: SDCNP, Lesson 8, lecture 23-Normalized Inputs and Initial Weights'''
        outImg = (self.dataImg - np.mean(self.dataImg))/np.std(self.dataImg) # zero-center&normalize
        outLabel = self.dataLabel.copy()
        return outImg, outLabel

    
    def __str__(self):
        return '< dataPPro >'  
    

if tRace1:print(msg1)