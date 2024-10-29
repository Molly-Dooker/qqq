### 컨테이너 빌드
```
docker run -d -t --name qqq -v $(pwd):/workspace --gpus all cuda_default:v1.0
```
### 컨테이너 실행
```
vscode 연결 or
docker exec -it qqq  /bin/bash
```


### venv
```
sudo apt-get upgrade -y
sudo apt-get update -y
sudo apt-get install -y python3 python3-pip
sudo apt-get install -y python3.10-venv
python3 -m venv .venv --prompt qqq
source .venv/bin/activate
pip install torch
```