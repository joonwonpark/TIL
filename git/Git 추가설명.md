# Git 추가설명

## 1. commit

> commit을 통해 이력을 확정하면 hash값이 부여되며, 이 값을 통해 동일한 커밋인지 확인한다.

```bash
#WD 변화 없고, staging area 비어있을 때
$ git commit
nothing to commit, working tree clean
# WD 변화 O, staging area 비어있을 때
$git commit
Untracked files:
		lee.txt
nothing added to commit but untracked files present
```



### commit 메시지 작성하기

> 부제: vim 활용

```bash
$ git commit 
```

* 편집모드 (i)
  * 문서 편집가능
* 명령모드(esc)
  * dd: 해당 줄 삭제
  * :wq : 저장 및 종료
    * w: write(저장)
    * q:quit(종료)
  * :q!:강제종료
    * q:quit
    * !:강제

###  log 활용하기

```bash
$ git log
$ git log --oneline
$ git log -1
$ git log -1 --oneline 
$ git log --oneline --graph
```

* HEAD: 현재 작업하고 있는 커밋 이력 및 브랜치에 대한 포인터 

```bash
1d1a9a7 (HEAD -> master)
#나는 현재 master 브랜치에 있고, 1d1a9a7 커밋의 상태에 있다.
```

* 예시)

 ```bash
$ git log --oneline
  1d1a9a7 (HEAD -> master) Add lee.txt
  b6dbe65 (feature/signout) Complete signout
  9372d4d (origin/master)집  - main.html
  
 ```

 ```bash
  #나는 master 브랜치에서 1d1a9a7 커밋을 했고,
  #feature/signout 브랜치는 b6dbe65 이력이고,
  #원격저장소(origin/master)는 9372d4d 이력이다.
 ```

## 직전 커밋 메시지 수정

> 아래의 명령어는 커밋 이력을 변경하기 때문에  조심해야 한다.
>
> 공개된 저장소에(원격 저장소)  이미 push 된 이력이라면 절대 해서는 안된다.

```bash
$ git commit --amend
```

### 커밋시 특정 파일을 빠뜨렸을 때

> 만약  staging area에 특정 파일(omit_file.txt)을 올리지 않아서 커밋이 되지 않았을 때! 

```bash
$ git add omit_file.txt
$ git commit --amend
```

## 2.staging area

* 커밋 이력이 있는 파일 수정한 경우 

  ```bash
  $ git status
  On branch master #마스터 브랜치에 있다
  
  Changes not staged for commit: # staged가 안된 변경사항들
  		#staged 로 바꾸려면 
  	(use "git add <file>..." to update what will be commited)
  		#WD에 있는 변화를 버리려면 
  		#커밋이후에 변경된 사항을 없애버림 
  	(use "git restore <file>..." to discard changes in working directory)
  		modified: 2.txt
  #커밋 staginga area 가 비어있습니다.
  #커밋에 추가될 변화가 없다.
  no changes added to commit (use "git add" and/or "git commit -a")   #git commit -a= git add . + git commit 합친 명령어   // git commit -am 'add t.txt' 해도됨
  ```

```bash
$ git add 2.txt
$ git status
On branch master 
#커밋이 될 변화
#커밋 명령어 했을 때, 아래의 내용이 이력에 남는다. 
Changes to be committed:
	#unstage하기 위해서 
	(use "git restore <file>..."to unstage)
		modified: 2.txt

```



* 커밋 이력이 없는 파일인 경우

  ```bash
  $ git status
  On branch master
  #tracking 되고 있지 않는 파일 -> commit(이력)에 한번도 관리된적 없다.
  Untracked files:
  (use "git add <file>..." to include in what will be commited)
  	a.txt
  	"\335\230\201\354\234\254.txt"
  #커밋할 것 도 없고(staging area가 비어 있고),
  #트래킹 되고 있지 않는 파일도 있다.
  	
  	
  nothing added to commit but untracked files present (use "git add" to track)
  
  ```

  

### add 취소하기

```bash
$ git restore --staged <file>
```

* 구버전 git 에서는 아래의 명령어를 사용해야한다.

  ```bash
  $ git reset HEAD <file>
  ```

  

### Working directory 변화 삭제하기

> git에서는 모든 commit된 내용은 되돌릴 수 있다. 
>
> 다만, 아래의  WD 내용을 삭제하는 것은 되돌릴 수 없다. 

```bash
 $ git  restore <file>
```

* 구버전 git에서는 아래의 명령어를 사용해야 한다.

  ```bash
  $ git checkout -- <file>
  ```

## Stash

> Stash는 변경사항을 임시로 저장 해놓는 공간이다.

### 예시 상황

```bash
1. feature branch 에서 a.txt를 변경후 커밋
2. master branch 에서 a.txt 를 수정(add/commit x)
3. merge
```

```bash
$ git merge test
#현재 merge명령어로 인해 아래의 파일이 덮어쓰여질 수 있다.
error: Your local changes to the following files would be overwritten by merge
	a.txt
#commit을 하거나  ->이력 확정을 해서 merge서 충돌 나는 상황으로 
#stash 해라 ->working directory 를 잠시 비워놓음


Please commit your changes or stash them before you merge
Aborting
Updating 4d56f57..b8f2357
```

### 명령어

```bash
$ git stash #stash 공간에 저장
Saved working directory and index stage WIP on master: 4d56f57 a.txt
$ git stash list  # stash 공간 내용확인
stash{0}: WIP on master : 4d56f57 a.txt
$ git stash pop # stash 공간에서 적용하고 삭제하기 
On branch master
Changes not staged for commit:
	(use "git add <file>..." to update what will be committed)

	(use "git restore <file>..." to discard changes in working directory)
		modified: a.txt
no changes added to commit (use "git add" and/or"git commit -a")
Dropped refs/stash{0}
```

### 예시 상황 해결

```bash
$ git stash
$ git merge test
$ git stash pop
# c충돌 해결 후 작업 이어나가기
```

```bash
첫번쨰 내용
<<<<<<< Updated upstream
브랜치 내용
=======
마스터 내용
>>>>>>> Stashed changes
```

### reset vs revert

> commit 이력을 되돌리는 작업을 한다.

