# Git_version_control (git 에서 커밋 다루기 )

# commit history 보기 

명령어 : $ git log

# history 깔끔하게 보기 

명령어 : $ git log --pretty=oneline

#명령어 별명 붙이기 

명령어 : $ git config alias.history 'log --pretty=oneline'

# commit 수정하기 

명령어 : $ git commit --amend    

# 이전 commit으로 git reset 하기 

명령어 : $ git reset --hard, --mixed, --soft + commit ID

              working dir   staging area   repository       

1. hard ==>     reset          reset         reset

2. mixed ==>    no reset       reset         reset

3. soft  ==>	no reset       no reset      reset

# 가장 최근 commit으로 reset

명령어 : $ git reset --hard HEAD^

# commit tag 달기 

명령어 : $ git tag + [별명] + [commit ID]

# hard의 위험성 

hard reset을 실행 하면

reset 한 commit 이후로 한 작업이 모두 사라진다

본인은 hard의 위험성에 대해 안일하게 생각하여 함부로 사용하여 

error: failed to push some refs to 를 경험함 

=== 해결 방법 ===

1. remote repo 에서 $ git pull 하면 복구 이후 push 작업 

항상 당황하지말고 remote repo를 잘 활용하자 ! 

2. 작업내용이 많아서 곤란할때 강제로 push 하는 방법

명령어 : $ git push -f origin 사용 

2번은 최후의 수단으로 사용하는게 좋을듯 1번 방법을 우선시하자!