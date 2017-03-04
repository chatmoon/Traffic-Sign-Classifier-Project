class dataExplo(object):
    def __init__(self, dataSet, csvFile='signnames.csv', sOrted=True):
        self.dataSet   = dataSet
        self.csvFile   = csvFile
        self.sOrted    = sOrted


    def showChart(self,figNb=1):
        '''Show the number of occurence per class'''
        n_classes = len(np.unique(self.dataSet))
        set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors # [2] Get "Set2" colors from ColorBrewer
        hist, bins = np.histogram(self.dataSet, np.arange(n_classes+1))
        fig = plt.figure(figsize=(16, 3))

        plt.title('fig.'+str(figNb)+': labels - number of occurence per class')
        plt.xlabel('Class id')
        plt.ylabel('Number of occurence')
        plt.xlim(0,n_classes)
        plt.ylim(0,np.amax(hist))
        ax = fig.add_subplot(111)
        ppl.bar(ax, bins[:-1], hist, grid='y', color='#616161')
     

    def showDist(self,figNb=2):
        n_classes = len(np.unique(self.dataSet))
        set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors
        axX = np.arange(len(self.dataSet))
        axY = self.dataSet
        fig = plt.figure(figsize=(16,2))

        plt.title('fig.'+str(figNb)+': labels - data distribution')
        plt.xlabel('Index')
        plt.ylabel('Class id')
        plt.ylim(0,n_classes)
        ax = fig.add_subplot(111)    
        plt.plot(axX,axY,".", color=set2[7])
        #ax.scatter(axX, axY, color=set2[7])

    def ocrLabel(self):
        n_classes = len(np.unique(self.dataSet))
        # Map class_id with Traffic-sign names: dct[classId] = Traffic-sign names
        with open(self.csvFile, newline='', encoding="utf8") as csvFile1:
            read0 = csv.reader(csvFile1)
            #dct0, dct1, dct2 = {}, {}, {}
            dct0, dct1 = {}, {}
            for i in read0:
                try:
                    dct0[int(i[0])] = i[1]
                except:
                    pass
        # Output : dct[classId] = Traffic-sign names


        # Occurence by class id: dct[classId] = occurence
        ocr, classId = np.histogram(self.dataSet, np.arange(n_classes+1))
        classId = classId[:-1].copy()
        for i,j in zip(classId,ocr):
                dct1[i] = j
        # Output : dct[classId] = occurence


        # Occurence by Traffic-sign names: dct[Traffic-sign names] = occurence
        lt = []
        for i in classId:
                lt.append([dct1[i], dct0[i]])
        # Output : lt[classId] = [occurence, Traffic-sign names] 

        return lt
    

    def showList(self,figNb=3):
        dct = { 0: '--------------------------------------------------  ---------------------------------------------------------',
                1: '%-44s|%-8s%-50s|%-5s',
                2: '%-45s%-8s%-50s|%-5s',
                3: 'Traffic sign name',
                4: 'Occu.',
                }
        if self.sOrted:
            sTr = 'sorted'
        else:
            sTr = ''
        print('fig.'+str(figNb)+': labels - {} List of occurence per Traffic sign name'.format(sTr))
        
        # Print the table header
        print(dct[0])
        print(dct[1] % (dct[3], dct[4], dct[3], dct[4]) )
        print(dct[0])

        # Print ( the Traffic sign name and the related occurence ) x 2 / line
        if self.sOrted:
            lt = sorted(self.ocrLabel(), reverse=True)
        else:
            lt = ocrLabel(self.dataSet)

        nbLine = int(len(lt)/2)
        rem    = len(lt)%2
        for i in range(nbLine):
            print(dct[1] % (lt[i][1], lt[i][0] , lt[i+nbLine][1], lt[i+nbLine][0]) )
        if rem !=0:
            print(dct[2] % ('', '', lt[-1][1], lt[-1][0]) )


    def __str__(self): # footnote [3]
        import inspect
        frame = inspect.currentframe()
        var_id = id(self.dataSet)
        for name in frame.f_back.f_locals.keys():
            try:
                if id(eval(name)) == var_id:
                    return '< dataEplo''('' ' + name + ' '')'' >'                    
            except:
                return '< dataEplo''('' ? '')'' >'
