# split

## Cachs chạy docker:
* sudo docker pull pytorch/pytorch:1.4-cuda10.1-cudnn7-devel
* sudo docker run -it -d --name sang -v /home/sang/Documents/car-license-plate-recognition-master:/home --gpus device=0 pytorch/pytorch:1.4-cuda10.1-cudnn7-devel bash
