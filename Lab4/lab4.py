
# coding: utf-8

# In[112]:


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import os
cwd = os.getcwd()
seed = 10
for photo in range(1,57):
    file_path = cwd + '\\images2\\mole ('+str(photo)+').jpg'
    print file_path
    im = mpimg.imread(file_path)
    
    [N1, N2, N3] = im.shape
    im_2D = im.reshape((N1*N2, N3))
    
    kmeans = KMeans(n_clusters=3, random_state=seed)
    kmeans.fit(im_2D)
    
    centroids = kmeans.cluster_centers_.astype('uint8')
    
    labels = kmeans.labels_
    
    im_3D = kmeans.predict(im_2D).reshape((N1, N2))
    
    
    # In[113]:
    
    
    s_max = 255*3
    darkest = 4
    for i in range(len(centroids)):
        if centroids[i].sum() < s_max:
            darkest = i
            s_max = centroids[i].sum()
    darkest
    
    
    # In[114]:
    
    
    new = im_3D[100:480,100:480]
    allr = []
    allc = []
    for i in range(new.shape[0]):
        for j in range(new.shape[1]):
            if new[i][j] == darkest:
                allr.append(i)
                allc.append(j)
    
    row = allr[int(len(allr)/2)]
    col = allr[int(len(allc)/2)]
    center = (row,col)
    
    
    # In[115]:
    
#    
#    fig,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(12,10))
#    ax1.imshow(im)
#    ax2.imshow(im_3D)
#    ax3.imshow(new)
#    ax3.hlines(col,0,new.shape[0]-1,colors='red')
#    ax3.vlines(row,0,new.shape[1]-1,colors='red')
#    
    
    # In[116]:
    
    
    threshold = 3
    #first row
    for i in range(center[0]):
        dark = 0
        notdark = 0
        if new[center[0]-i][center[1]] != darkest:
            for j in range(threshold):
                if new[center[0]-j-i-1][center[1]]!=darkest:
                    notdark = notdark + 1
            
            if notdark == threshold:
                break
    #print (center[0],center[0]-i)
    
    up = center[0]-i
    #last row
    for i in range(center[0]):
        dark = 0
        notdark = 0
        if new[center[0]+i][center[1]] != darkest:
            for j in range(threshold):
                if new[center[0]+j+i+1][center[1]]!=darkest:
                    notdark = notdark + 1
            
            if notdark == threshold:
                break
    #print (center[0],center[0]+i)
    
    down = center[0]+i
    
    #first column
    for i in range(center[1]):
        dark = 0
        notdark = 0
        if new[center[0]][center[1]-i] != darkest:
            for j in range(threshold):
                if new[center[0]][center[1]-j-i-1]!=darkest:
                    notdark = notdark + 1
            
            if notdark == threshold:
                break
    #print (center[1],center[1]-i)
    
    left = center[1]-i
    
    for i in range(center[1]):
        dark = 0
        notdark = 0
        if new[center[0]][center[1]+i] != darkest:
            for j in range(threshold):
                if new[center[0]][center[1]+j+i+1]!=darkest:
                    notdark = notdark + 1
            
            if notdark == threshold:
                break
    #print (center[1],center[1]+i)
    right = center[1] + i
    
    
    # In[117]:
    
    
    margin = 40
    cut = new[up-margin:down+margin,left-margin:right+margin]
    
    
    # In[118]:
    
    
    for i in range(up):
        if np.count_nonzero(new[up-i] == darkest) == 0:
            #print ('y1',up-i,up)
            up2 = up - i
            break
    for i in range(margin):
        if np.count_nonzero(new[down+i] == darkest) == 0:
            #print ('y2',down+i,down)
            down2 = down + i
            break
    for i in range(margin):
        if np.count_nonzero(new[:,right+i] == darkest) == 0:
            #print ('x2',right+i,right)
            right2 = right + i
            break
    for i in range(margin):
        if np.count_nonzero(new[:,left-i] == darkest) == 0:
            #print ('y2',left-i,left)
            left2 = left - i
            break
    cut2 = new[up2:down2,left2:right2]
    
    
    # In[119]:
    
    
    atleast = 2
    for i in range(up):
        if np.count_nonzero(new[up-i] == darkest) < atleast:
            #print ('y1',up-i,up)
            up3 = up - i
            #x1 = i
            break
    for i in range(margin):
        if np.count_nonzero(new[down+i] == darkest) < atleast:
            #print ('y2',down+i,down)
            down3 = down + i
            break
    for i in range(margin):
        if np.count_nonzero(new[:,right+i] == darkest) < atleast:
            #print ('x2',right+i,right)
            right3 = right + i
            break
    for i in range(margin):
        if np.count_nonzero(new[:,left-i] == darkest) < atleast:
            #print ('y2',left-i,left)
            left3 = left - i
            break
    cut3 = new[up3:down3,left3:right3]
    
    
    # In[120]:
    
    
    new = cut3
    contour = np.zeros((new.shape[0],new.shape[1]))
    
    border_left = []
    for x in range(new.shape[0]):
        for y in range(new.shape[1]):
            if (new[x,y] == darkest):
                contour[x,y] = 100
                break
    
    for x in range(new.shape[0]):
        for y in range(new.shape[1]):
            if (new[new.shape[0]-x-1,new.shape[1]-y-1] == darkest):
                contour[new.shape[0]-x-1,new.shape[1]-y-1] = 100
                break
    
    for y in range(new.shape[1]):
        for x in range(new.shape[0]):
            if (new[new.shape[0]-x-1,new.shape[1]-y-1] == darkest):
                contour[new.shape[0]-x-1,new.shape[1]-y-1] = 100
                break
    for y in range(new.shape[1]):
        for x in range(new.shape[0]):
            if (new[x,y] == darkest):
                contour[x,y] = 100
                break
    
    #plt.matshow(contour)
    
    
    # In[121]:
    
    
    contour2 = contour.copy()
    for i in range(cut3.shape[0]):
        for j in range(cut3.shape[1]):
            if cut3[i,j] == darkest:
                if (j-2) > 0 and (j+2)<cut3.shape[1] and ((cut3[i,j+1] != darkest and cut3[i,j+2] != darkest) or (cut3[i,j-1] != darkest and cut3[i,j-2] != darkest)) :
                    contour2[i,j] = 100 
    
    
    # In[122]:
    
    
    for j in range(cut3.shape[1]):
        for i in range(cut3.shape[0]):
            if cut3[i,j] == darkest:
                if (i-2) > 0 and (i+2)<cut3.shape[0] and ((cut3[i+1,j] != darkest and cut3[i+2,j] != darkest) or (cut3[i-1,j] != darkest and cut3[i-2,j] != darkest)):
                    contour2[i,j] = 100
                    
    
    
    # In[123]:
    
    
    for i in range(contour2.shape[0]):
        for j in range(contour2.shape[1]):
            if contour2[i][j] != 0:
                #print 'Here3'
                founded = 0
                for k in range(-2,2):
                    for l in range(-2,2):
                        #print k,l
                        if k!=0 and l!=0 and i+k<contour2.shape[0] and j+l<contour2.shape[1]:
                            #print ('Here2')
                            if contour2[i+k][j+l] != 0:
                                #print ('Here')
                                founded = 1
                                break
                    if founded == 1:
                        break
                if founded == 0:
                    contour2[i][j] = 0
    #plt.imshow(contour2)
    
    
    # In[124]:
    
    
    from collections import Counter
    perimeter = Counter(contour2.reshape(contour2.shape[0]*contour2.shape[1]))[100]
    area = Counter(cut3.reshape(cut3.shape[0]*cut3.shape[1]))[darkest]
    perimeter_circle = np.sqrt(float(area)/np.pi)*2*np.pi
    print(perimeter,perimeter_circle,float(perimeter)/perimeter_circle)
    
