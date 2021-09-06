# Machine Learning : CUDA out of memory !!!

CUDA out of memory !!!  
  
RuntimeError: CUDA out of memory.  
Tried to allocate 12.50 MiB (GPU 0; 10.92 GiB total capacity; 8.57 MiB already allocated; 9.28 GiB free; 4.68 MiB cached)  

원인 :   메모리를 너무 많이 쓸 때 발생.  
        ( 본인의 경우, Jupyter에서 메모리를 많이 먹는 커널 1개에서 다른 1개로 리팩토링 중에 테스트를 해서 메모리를 많이 잡아먹게 되었음 )  
        
해결 :
1. 안 쓰는 프로세스를 Kill.  
2. batch size를 줄이기  
3. Holding python variable을 수정.  
         
