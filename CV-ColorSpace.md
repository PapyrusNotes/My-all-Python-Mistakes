Computer vision : Read, Converting Color space

문제 : CV2를 이용해서 원본 이미지를 읽을 때, 색상을 온전히 읽지 못하는 상태.


```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread("tiger.jpg",3)
img2 = cv2.imread("tiger.jpg",0)

plt.subplot(121),plt.imshow(img1),plt.title('TIGER_COLOR')
plt.subplot(122),plt.imshow(img2),plt.title('TIGER_BW')

plt.show()
```




원인 : OpenCV는 RGB 공간이 아니라, BGR 공간을 사용한다. 

      
       
해결 :  원본처럼 출력되게 하려면 Red 채널과 Blue 채널을 swap 해주어야 한다.


```python
img1 = cv2.imread("tiger.jpg", 3)

b,g,r = cv2.split(img1)           # get b, g, r
rgb_img1 = cv2.merge([r,g,b])     # switch it to r, g, b

plt.subplot(121),plt.imshow(rgb_img1),plt.title('TIGER_COLOR')
```
