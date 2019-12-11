### 상황 1. fast-foward

1. feature/test branch 생성 및 이동

   ```bash
   $ git checkout -b feature/test
   ```

   

2. 작업 완료 후 commit

   ```bash
   $ touch test.txt
   $ git add .
   $ git commit -m'test 기능 개발 완료'
   ```
   
   ```bash
   $ git log --oneline
   53ced52 (HEAD -> feature/test) text 기능 개발 완료
   e487307 (testbranch, master) testbranch -test
   243947e (origin/master) 집 - b.txt
   f30d934 멀캠 - a.txt
   4ba9639 집 - main.html
   005dfb4 멀캠 -index.html
   ```
   
   


3. master 이동

   ```bash
   $ git checkout master
   Switched to branch 'master'
   Your branch is ahead of 'origin/master' by 1 commit.
     (use "git push" to publish your local commits)
   $ git log --oneline
   e487307 (HEAD -> master, testbranch) testbranch -test
   243947e (origin/master) 집 - b.txt
   f30d934 멀캠 - a.txt
   4ba9639 집 - main.html
   005dfb4 멀캠 -index.html
   
   ```
   
   
   
   


4. master에 병합

   ```bash
   $ git merge feature/test
   Updating e487307..53ced52
   Fast-forward
    test.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 test.txt
   ```
   
   


5. 결과 -> fast-foward (단순히 HEAD를 이동)

   ```bash
   $ git log --oneline
   53ced52 (HEAD -> master, feature/test) text 기능 개발 완료
   e487307 (testbranch) testbranch -test
   243947e (origin/master) 집 - b.txt
   f30d934 멀캠 - a.txt
   4ba9639 집 - main.html
   005dfb4 멀캠 -index.html
   ```

   

6. branch 삭제

   ```bash
   $ git branch -d feature/test
   ```
   
   

---

### 상황 2. merge commit
   > feature 브랜치에서 작업하고 잇는 동안, master 브랜치에서 이력이 추가적으로 발생한 경우

1. feature/signout branch 생성 및 이동

   ```bash
   $ git checkout -b feature/signout
   ```

2. 작업 완료 후 commit

   ```bash
   $ touch signout.txt
   $ git add .
   $ git commit -m'complete signout'
   ```

   

3. master 이동

   ```bash
   $ git checkout master
   Switched to branch 'master'
   Your branch is ahead of 'origin/master' by 2 commits.
     (use "git push" to publish your local commits)
   
   ```

   

4. *master에 추가 commit 이 발생시키기!!*

   * **다른 파일을 수정 혹은 생성하세요!**

     ```bash
     $ touch master.txt
     $ git add .
     $ git commit -m'update master'
     ```

     

5. master에 병합

   ```bash
   $ git merge feature/sigout
   Merge made by the 'recursive' strategy.
    signout.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 sigout.txt
    [esc] 누르고 :wq
   ```

   

6. 결과 -> 자동으로 *merge commit 발생*

   ```bash
   $ git log --oneline
   944ca8a (HEAD -> master) Merge branch 'feature/signout'
   87cfef2 update master
   cafd00b (feature/signout) complete signout
   53ced52 text 기능 개발 완료
   e487307 testbranch -test
   243947e (origin/master) 집 - b.txt
   f30d934 멀캠 - a.txt
   4ba9639 집 - main.html
   005dfb4 멀캠 -index.html
   
   ```

   

7. 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   *   944ca8a (HEAD -> master) Merge branch 'feature/signout'
   |\
   | * cafd00b (feature/sigout) complete signout
   * | 87cfef2 update master
   |/
   * 53ced52 test 기능 개발 완료
   * e487307 testbranch -test
   * 243947e (origin/master) 집 - b.txt
   * f30d934 멀캠 - a.txt
   * 4ba9639 집 - main.html
   * 005dfb4 멀캠 -index.html
   ```

   

8. branch 삭제

   

---

### 상황 3. merge commit 충돌

1. feature/board branch 생성 및 이동

   ```bash
   $ git checkout -b hotfix/test
   ```

   

2. 작업 완료 후 commit

   ```bash
   # hotfix/test 의 test.txt 수정
   $ git add .
   $ git commit -m'hotfix test'
   $ git log --oneline
   944ca8a (HEAD -> hotfix/test, master) Merge branch 'feature/signout'
   87cfef2 update master
   cafd00b (feature/signout) complete signout
   53ced52 text 기능 개발 완료
   e487307 testbranch -test
   243947e (origin/master) 집 - b.txt
   f30d934 멀캠 - a.txt
   4ba9639 집 - main.html
   005dfb4 멀캠 -index.html
   ```
   
   


3. master 이동

   ```bash
   $ git checkout master
   Switched to branch 'master'
   Your branch is ahead of 'origin/master' by 5 commits.
     (use "git push" to publish your local commits)
   ```
   
   


4. *master에 추가 commit 이 발생시키기!!*

   * **동일 파일을 수정 혹은 생성하세요!**

   ```bash
   # master의 test.txt 수정
   $ git add .
   $ git commit -m'master test'
   ```

   

5. master에 병합

   ```bash
   $ git merge hotfix/test
   Auto-merging test.txt
   CONFLICT (content): Merge conflict in test.txt
   Automatic merge failed; fix conflicts and then commit the result.
   
   ```
   
   


6. 결과 -> *merge conflict발생*

   ```bash
   Auto-merging test.txt
   CONFLICT (content): Merge conflict in test.txt
   Automatic merge failed; fix conflicts and then commit the result.
   ```
   
   


7. 충돌 확인 및 해결

   ``` bash
   [visual studio code]
   master 수정 파일과 hotfix/test 수정 파일 중 선택
   <<<<<<< HEAD
   마스터 test 긴급 수정!!
   성공했다!!
   =======
   hotfix 브랜치에서 수정
   우아아아!
   >>>>>>> hotfix/test
   ```
   
   
   
   ```bash
   $ git status
   On branch master
   Your branch is ahead of 'origin/master' by 6 commits.
     (use "git push" to publish your local commits)
   
   You have unmerged paths.
     (fix conflicts and run "git commit")
     (use "git merge --abort" to abort the merge)
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
           both modified:   test.txt
   
   no changes added to commit (use "git add" and/or "git commit -a")
   ```
   
   


8. merge commit 진행

    ```bash
    $ git commit
    [esc]
:wq
   $ git log --oneline
   05ae5f5 (HEAD -> master) Merge branch 'hotfix/test'
   5e31160 master test
   6806157 (hotfix/test) hotfix test
   944ca8a Merge branch 'feature/sigout'
   87cfef2 update master
   cafd00b (feature/sigout) complete sigout
   53ced52 text 기능 개발 완료
   e487307 testbranch -test
   243947e (origin/master) 집 - b.txt
   f30d934 멀캠 - a.txt
   4ba9639 집 - main.html
   005dfb4 멀캠 -index.html
   ```
   
   * vim 편집기 화면이 나타납니다.
   
   * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
      * `w` : write
      * `q` : quit
      
   * 커밋이  확인 해봅시다.
   
9. 그래프 확인하기

    


10. branch 삭제

    