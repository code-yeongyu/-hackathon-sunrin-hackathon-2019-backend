# api urls

인증방식으로는 Basic Auth 를 사용합니다.

- profiles/
  - / : 본인 프로필
    - get으로 요청시 프로필의 내용을, patch로 요청시 입력받은 패러미터의 값을 수정합니다.
    - 학생의 경우 다음과 같은 형식의 내용을 받을것입니다.
    ```json
    {
      "is_high": true
    }
    ```
  - signup/ : 회원가입
    - 회원가입시에는 POST요청을 사용해야 하며 username, email, password1, password2가 각각 body에 있어야 합니다.
      - username: 사용자명, 인증시에 사용됩니다.
      - email: 이메일
      - password1: 비밀번호
      - password2: 비밀번호 확인
    - 올바르지 않은 요청시에는 HTTP 상태코드 406을 반환하며, 만약 아무런 값도 body에 넣지 않았을경우 다음과 같은 내용이 반환될 것입니다.
    ```json
    {
      "username": ["이 필드는 필수 항목입니다."],
      "email": ["이 필드는 필수 항목입니다."],
      "password1": ["이 필드는 필수 항목입니다."],
      "password2": ["이 필드는 필수 항목입니다."]
    }
    ```
    - 올바른 요청에는 HTTP 상태코드 201을 반환합니다.
- posts/
  - / : GET요청시에는 자신이 작성한 게시글을 리턴합니다. 다음은 예시입니다:
  ```json
  [[
    {
        "id": 1,
        "created_at": "2019-07-19T13:13:58.553761Z",
        "writer_id": 2,
        "content": "hi",
        "tags": ""
    },
    {
        "id": 2,
        "created_at": "2019-07-19T13:21:19.330051Z",
        "writer_id": 2,
        "content": "개발은 너무 재미이따!",
        "tags": ""
    }
  ]
  ```
  - 또한 POST 요청시에는 body의 content 필드에 값을 넣어주기만하면 됩니다.
  - <ID>/ : GET요청만 받으며, 해당 <ID>의 글을 조회합니다. 자신의 글이라면 HTTP 상태코드 200과 함께 다음과 같은 내용이 반환될 것입니다.
  ```json
  {
    "id": 1,
    "created_at": "2019-07-19T22:13:58.553761+09:00",
    "writer": "exlock",
    "content": "hi",
    "tags": ""
  }
  ```
  - 자신의 글이 아니라면, HTTP 상태코드 403을 반환 할 것입니다.
