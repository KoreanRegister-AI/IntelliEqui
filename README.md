# IntelliEqui
## GitHub Action 구성 요소

### Workflow
  한개 이상의 job을 실행할 수 있는 자동화된 작업  
  * YAML 파일로 저장되며 event에 의해 실행 됩니다.
### Event
  workflow 실행을 발동시키는 특정한 활동  
  * 깃허브에 소스코드를 푸시하면 발생하는 push event, pull request event, issue event 등 깃허브에서 발생하는 대부분의 작업을 event로 정의-
### Jobs
  한가지 러너안에서 실행되는 여러가지 step들의 모음  
  * 각각의 step들은 일종의 shell script 처럼 실행
  * Step들은 순서에 따라 실행되며 Step 끼리 데이터들을 공유 가능
  * Job은 다른 Job에 의존관계를 가질 수 있으며, 병렬 실행도 가능
### Actions
  복잡하고 자주 반복되는 작업을 정의한 커스텀 어플리케이션  
  * workflow 파일 안에서 자주 반복되는 코드를 미리 정의해 코드의 양을 줄일 수 있습니다.
  * 깃허브 마켓플레이스를 통해 공용 Action 또는 다른 사람들이 만든 Action을 사용할 수 있습니다.

## EXAMPLE

```yaml
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
```
> name : workflow의 name을 정의
* 선택사항이며 깃허브 저장소의 깃허브 액션 탭에서 workflow의 이름
> on : 해당 workflow를 실행시키는 이벤트를 정의  
* push이벤트가 발생 시, workflow 실행되도록 정의
> jobs : check-bats-version--> job의 이름을 정의
* runs-on : 어떤 호스트에서 실행될지 정의 - ex) ubuntu 가상 머신에서 실행되도록 정의
> steps
* uses: actions/checkout@v2 - 해당 레포지토리를 pull 받고 이동하는 action 대부분의 workflow에서 사용
* uses: actions/setup-node@v2 - 노드를 설치하는 action으로 가상머신안에는 대부분의 프로그래밍 언어가 설치되어 있지 않기 때문에 프로젝트 실행에 필요한 언어들을 action을 통해 다운
* run: npm install -g bats - run 키워드를 통해 러너가 실행되는 서버에서 명령어를 실행

```yaml
name: Gradle Build & K8S Deploy
# V를 앞글자로 가지는 태그가 push 될 때 해당 workflow 실행 - ex) V2, V3
on:
  push:
    tags: V*
# Workflow의 이름을 Gradle Build & K8S Deploy로 정의
# V를 앞글자로 가지는 태그가 푸시될 때 해당 workflow 실행
jobs:
  build:
# build 시작
    runs-on: ubuntu-latest

    steps:
    
    - uses: actions/checkout@v2
    
    - name: Set up JDK 11
      uses: actions/setup-java@v2
      with:
        java-version: '11'
        distribution: 'temurin'
        
    - name: Login to Docker Hub
      uses: docker/login-action@v1
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_PASSWORD }}
    
    - name: Grant execute permission for gradlew
      run : chmod +x gradlew
      
    - name: Build with jib
      run: |
        ./gradlew jib \
        -Djib.to.image="zxcvb5434/devopstest:${GITHUB_REF##*/}"
# checkout Action을 통해 레포지토리를 다운받은 폴더로 이동
# setup-java Action을 통해 java 11 설치
# Docker Hub로 이미지를 푸시하기 위해 docker login action을 통해 자격정보 획득
# ${{ secrets.DOCKERHUB_USERNAME }}를 통해 시크릿 환경 변수 사용
# run 명령어를 통해 ubuntu에서 특정 명령 실행
# chmod +x gradlew 명령어를 통해 권한을 조정한 후 gradlw jib 명령을 통해 이미지 빌드 후 컨테이너 레지스리로 업로드
# 깃허브 액션은 workflow가 실행될때 기본 환경 변수가 제공 됨 - 커밋 sha, tag name 등
# ${GITHUB_REF##*/} - 를 통해 TAG 이름을 사용

  deploy:
    
    needs: build
    runs-on: ubuntu-latest
    
    steps:
    
    - uses: actions/checkout@v2
    
    - name: update yaml file
      run: |
        sed -i s/latest/${GITHUB_REF##*/}/ ./k8s/deployment.yaml
        cat ./k8s/deployment.yaml
    
    - name: Kubectl apply
      uses: steebchen/kubectl@v2.0.0
      with: 
        config: ${{ secrets.KUBECONFIG }}
        command: apply -f ./k8s/deployment.yaml
# needs 문법을 통해 build job이 성공적으로 완료될 때만 수행 --> 직렬로만 수행 가능
# sed 명령어를 통해 Repositroy에 Deployment yaml 파일의 tag 수정
# latest 태그를 깃허브 태그 이름으로 수정
# kubectl action을 통해 kubectl apply 명령 실행
```
