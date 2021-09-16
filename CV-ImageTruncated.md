# Computer Vision - image file is truncated (4 bytes not processed)

- 원인 : 잘린 이미지  

 
 잘린 이미지를 변수에 담는 것 까지는 할 수 있다.
 이미지를 띄우거나 np.array로 변환 시 에러가 발생한다.


- 해결 : 
 ```python
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
 ```
 로 잘린 이미지도 Load 할 수 있게 하면 해결된다.

 
