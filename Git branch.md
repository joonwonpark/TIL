# Git branch

> Git 개발 흐름에서 branch는 매우 중요하다.
>
> 독립적인 개발환경을 제공하여 동시에 다양한 작업을 진행할 수 있도록 만들어준다.
>
> 일반적으로 브랜치의 이름은 해당 작업을 나타낸다.

## 1. 기초명령어

```bash
$ git branch # branch 목록 확인
$ git branch (브랜치이름) # (브랜치이름) 생성
$ git checkout (브랜치이름) # (브랜치이름)으로 이동
$ git branch -d (브랜치이름) # (브랜치이름) 삭제

$ git check out -b (브랜치이름) # (브랜치이름) 생성 및 이동
```

* branch 병합

  ```bash
  (master) $ git merge feature
  # master 브랜치로 feature 브랜치 이력 가져오기 (병합)
  ```

  

