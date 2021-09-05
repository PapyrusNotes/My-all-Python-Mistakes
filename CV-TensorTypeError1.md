# Computer vision : TensorType

TypeError    Traceback (most recent call last)  
/tmp/ipykernel_140/851497589.py in <module>  
  ```python
----> 1 test(sample_images)
  ```

/tmp/ipykernel_140/3607641383.py in test(sample_images)  
    
  ```python
     17         # Save mask img  
     18         original_img = imread(f"./sample_img/"+i)  
---> 19         mask_array = output['instances'].pred_masks.numpy()  
     20         mask_array = np.moveaxis(mask_array, 0, -1)  
     21         mask_array = np.repeat(mask_array, 3, axis=2)  
  ```
  
TypeError: can't convert cuda:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.
    
    
 원인 : cuda를 사용하는 그래픽카드 저장 공간에서의 tensor 타입을 numpy로 변환할 수 없는 경우 발생한다.  
 해결 : Tensor.cpu()를 이용하여 tensor값을 호스트 메모리에 복사 한 뒤 사용해야한다. 
