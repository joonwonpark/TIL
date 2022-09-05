# Github을 통한 멀캠 - 집 활용

## 1. 준비사항

* 로컬 저장소(A - 집)

  ```bash
  $ git clone 원격저장소URL
  ```

* 로컬 저장소(B - 멀캠)

  ```bash
  $ git init
  ```

* 원격 저장소



## 2. 시나리오

> 작업 전에 pull 작업 후에 push
>
> 작업과정에서 충돌이 발생할 수 있으나 잘못한 것이 아니라 내가 수정하면 된다는 사실을 잊지말자

### 0. 집에서 pull(원격 저장소에서 받아오기)

```bash
$ git pull origin master
```

### 1. 집에서작업

```bash
$ touch a.txt
$ git add .
$ git commit -m'집 - a.txt'
```

### 2. 원격 저장소로 push

```bash
$ git push origin master
```

### 3. 멀캠에서 pull

```bash
$ git pull origin master
```

### 4. 멀캠에서 작업

```bash
$ touch b.txt
$ git add .
$ git commit -m'멀캠 - 작업'
```

### 5. 원격저장소 push

```bash
$ git push origin master
```

