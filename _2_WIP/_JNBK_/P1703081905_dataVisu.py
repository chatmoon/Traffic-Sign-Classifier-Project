class dataVisu(object):
    def __init__(self, dataImg, dataLabel, path, cmap=None, imgFileFormat='png'):
        self.dataImg   = dataImg
        self.dataLabel = dataLabel
        self.path      = path
        self.cmap      = cmap
        self.png       = imgFileFormat
        self.pathNmeImg= None
        self.sprImg    = None


    def showMosaic(dataImg, dataLabel, nbr=43, cmap=None):
        # Get list = [ TS Name, [indexMin , indexMax] ]
        #lt0 = locateTS(dataLabel)
        
        # Get dictionary[idClass] = tuple( index(idClass))
        lt, dct = [], {} 
        lt  = ocrLabel(dataLabel)
        dct = indexClass()
        
        # Compute the width and the height of the sprite image
        dIm = nbr**0.5
        dIm = int(dIm) + (dIm - int(dIm) > 0)
        master_width, master_height = dIm*3, dIm*3
        gs1 = gridspec.GridSpec(master_width, master_height)
        gs1.update(left=0, right=0.5, hspace=0.05, wspace=0.05)
        
        # Create and save the sprite image
        count = 0
        for y0 in range(dIm):
            y = y0*3
            for x0 in range(dIm):
                x = x0*3
                lt1 = [ [0+x,y+0], [0+x,y+2], [1+x,y+2], [2+x,y+2], [2+x,y+1], [2+x,y+0] ]
                flag = True
                
                if count+1 <= nbr:
                    for i in lt1:
                        if flag:
                            ax = plt.subplot(gs1[0+x:x+2,0+y:y+2])            
                            flag = False
                        else:
                            ax = plt.subplot(gs1[i[0],i[1]])
                        index = random.randint(dct[count][0], dct[count][-1]) 
                        image = dataImg[index]
                        ax.imshow(image, cmap=cmap)
                        ax.set_xticks([]); ax.set_yticks([])
                else:
                    ax = plt.subplot(gs1[x,y])
                    ax.set_xticks([]); ax.set_yticks([])
                    ax.axis('off')            
                #title = lt[count][1][:17]+'.'
                #ax.set_title(title, fontsize=8) 
                    
                count += 1

