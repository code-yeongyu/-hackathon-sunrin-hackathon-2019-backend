# api urls

인증방식으로는 Basic Auth 를 사용합니다.

- profiles/
  - / : 본인 프로필
    - get으로 요청시 프로필의 내용을, patch로 요청시 입력받은 패러미터의 값을 수정합니다.
    - 학생의 경우 다음과 같은 형식의 내용을 받을것입니다.
    ```json
    {
      "is_student": true,
      "school": "선린인터넷고등학교",
      "location": "서울시 용산구",
      "school_type": "특성화고"
    }
    ```
    - 선생의 경우 다음과 같은 형식의 내용을 받을것입니다.
    ```json
    {
      "is_student": false,
      "is_certified": True,
      "work_at": "선린인터넷고등학교",
      "location": null,
      "career": "한양대학교 국어교육과"
    }
    ```
  - /signup/ : 회원가입
    - 회원가입시에는 POST요청을 사용해야 하며 username, email, password1, password2가 각각 body에 있어야 합니다.
      - username: 사용자명, 인증시에 사용됩니다.
      - email: 이메일
      - password1: 비밀번호
      - password2: 비밀번호 확인
    - 올바르지 않은 요청시에는 HTTP 상태코드 406을 반환하며, 만약 아무런 값도 body에 넣지 않았을경우 다음과 같은 내용이 출력될 것입니다.
    ```
    {
        "username": [
            "이 필드는 필수 항목입니다."
        ],
        "email": [
            "이 필드는 필수 항목입니다."
        ],
        "password1": [
            "이 필드는 필수 항목입니다."
        ],
        "password2": [
            "이 필드는 필수 항목입니다."
        ]
    }
    ```
    - 올바른 요청에는 HTTP 상태코드 201을 반환합니다.
  - /[사용자이름]/ : 특정 user의 프로필 접근
    - 학생은 선생의 프로필만, 선생은 학생의 프로필만이 접근이 가능합니다.
    - 요청이 유효하다면 / 에 요청했을때 처럼 상대방의 정보를 받아 올 수 있습니다.
