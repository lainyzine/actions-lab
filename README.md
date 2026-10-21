# actions-lab

LainyZine의 GitHub Actions 연재에서 쓰는 실습 저장소입니다. 글과 저장소를 서로 링크해 두었으니, 글을 따라 하다 막히면 여기 파일과 실행 기록을 보면 됩니다.

## 연재 글

- [GitHub Actions 시작하기: 첫 워크플로 만들고 실행 로그 읽기](https://www.lainyzine.com/ko/article/github-actions-getting-started-first-workflow/)
- [GitHub Actions 실행 조건: push부터 수동 실행까지](https://www.lainyzine.com/ko/article/github-actions-workflow-triggers/)
- [GitHub Actions 파이썬 테스트: pytest 실행과 실패 로그 읽기](https://www.lainyzine.com/ko/article/github-actions-python-tests-pytest/)
- [GitHub Actions 실패 원인 찾기: 빨간 단계와 종료 코드 읽기](https://www.lainyzine.com/ko/article/github-actions-failed-run-find-cause/)
- [GitHub Actions 의존성 잠그기: actions.lock 만들고 갱신하기](https://www.lainyzine.com/ko/article/github-actions-lock-dependencies-actions-lock/)

## 워크플로 파일

| 파일 | 내용 |
|---|---|
| `.github/workflows/hello.yml` | 체크아웃 후 문자열을 출력하는 가장 작은 워크플로 |
| `.github/workflows/triggers.yml` | `push`·`pull_request`·`schedule`·`workflow_dispatch` 트리거 예제 |

## 실행 기록 보기

저장소 상단의 **Actions** 탭에서 실행 로그를 그대로 볼 수 있습니다. 글에서 설명한 로그 위치와 같은 화면입니다.
