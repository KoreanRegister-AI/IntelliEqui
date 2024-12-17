# IntelliEqui

## GitHub Action 구성 요소
### Workflow
  한개 이상의 job을 실행할 수 있는 자동화된 작업 \n
  YAML 파일로 저장되며 event에 의해 실행 됩니다.
### Event
  workflow 실행을 발동시키는 특정한 활동
  깃허브에 소스코드를 푸시하면 발생하는 push event, pull request event, issue event 등 깃허브에서 발생하는 대부분의 작업을 event로 정의할 수 있습니다.
### Jobs
  한가지 러너안에서 실행되는 여러가지 step들의 모음
  각각의 step들은 일종의 shell script 처럼 실행이 됩니다.
  Step들은 순서에 따라 실행되며 Step 끼리 데이터들을 공유할 수 있습니다.
  Job은 다른 Job에 의존관계를 가질 수 있으며, 병렬 실행도 가능합니다.
### Actions
  복잡하고 자주 반복되는 작업을 정의한 커스텀 어플리케이션
  workflow 파일 안에서 자주 반복되는 코드를 미리 정의해 코드의 양을 줄일 수 있습니다.
  깃허브 마켓플레이스를 통해 공용 Action 또는 다른 사람들이 만든 Action을 사용할 수 있습니다.

## EXAMPLE
###
