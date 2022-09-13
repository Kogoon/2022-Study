## Git 정리 

### git init 

### git config 

### git status

### git add

### git commit 

### git push 

### git pull

### git clone

### git remote
`-v`

* origin 이 아닌 다른 곳으로
~~~
$ git remote add github https://github.com/Company_Name/repository_name.git

# push master to github
$ git push github master

# Push my-branch to github and set it to track github/my-branch
$ git push -u github my-branch

# Make some existing branch track github instead of origin
$ git branch --set-upstream other-branch github/other-branch
~~~

### git branch
`-r`
### git checkout 

### git log
`--oneline`

### git diff

### git reflog

### git merge

### git rebase

### git reset

### git stash

### git tag

* * *
[Git merge, rebase 이해하기](https://cyberx.tistory.com/96?category=195631)  
[rebase로 병합하기](https://backlog.com/git-tutorial/kr/stepup/stepup2_8.html)  
[자주 쓰는 git 명령어 정리](https://velog.io/@eeeun/%EC%9E%90%EC%A3%BC-%EC%93%B0%EB%8A%94-Git-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%A0%95%EB%A6%AC)
