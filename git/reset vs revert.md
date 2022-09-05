# reset vs revert

> commit 이력을 되돌리는 작업을 한다.

* reset : 이력을 삭제한다.

  * -- mixed  : 기본 옵션 해당 커밋 이후 변경사항 staging area에 보관
  * -- hard : 해당 커밋 이후 변경사항 모두 삭제 (주의!!)
  * -- soft : 해당 커밋 이후 변경사항 및 working directory 내용까지 모두 보관

  ```bash
  $ git log --online
  
  ```

* revert : 되돌렸다는 이력을 남긴다.

  ```bash
  $ git log --online
  ```

  