# Install TensorFlow with pip

시스템 환경 설정
- pip 19.0 or later
- Ubuntu 16.04 or later
- MacOS 10.12.6 (Sierra) or later
- Windows 7 or later

## 1. Install the Python Development environment on your system

시스템 환경에 이미 Python이 설치되었는지 확인합니다.

```
$ python3 --version
$ pip3 --version
$ virtualenv --version

```

Package들이 이미 설치되었으면, 다음 단계로 넘어가도 됩니다. 

```
$ sudo apt update
$ sudo apt install python3-dev python3-pip
$ sudo pip3 install -U virtualenv  # system-wide install
```

## 2. Create a Virtual Environment (recommended)

(venv)이름을 가진 새로운 가상 환경을 구축합니다.
```
$ virtualenv --system-site-packages -p python3 ./(venv)
```

Shell에 맞게 가상환경을 활성화합니다
```
$ source ./(venv)/bin/activate
```

pip업데이트를 한 후, 가상환경에 설치된 package리스트를 확인합니다.
```
(venv) $ pip install --upgrade pip
(venv) $ pip list
```

추후에 가상환경을 나가기 위하여
```
(venv) $ deactivate
```

## 3. Install the TensorFlow pip package

```
(venv) $ pip install --upgrade tensorflow
```