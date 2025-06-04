# 간단한 FastAPI 블로그 API

이 프로젝트는 FastAPI 프레임워크를 사용하여 게시글과 댓글 기능을 제공하는 간단한 백엔드 API입니다. 사용자 인증 기능을 포함하며, 데이터베이스는 SQLite를 사용합니다.

## 🚀 주요 기능

  * **사용자 관리**: 회원가입, 로그인, JWT(JSON Web Token) 기반 인증
  * **게시글 (Posts)**:
      * 게시글 생성, 조회 (단일 및 목록), 수정, 삭제
      * 인증된 사용자만 게시글 생성 및 수정/삭제 가능
  * **댓글 (Comments)**:
      * 특정 게시글에 대한 댓글 생성, 조회, 수정, 삭제
      * 인증된 사용자만 댓글 생성 및 수정/삭제 가능

-----
## 진행사항
1. 데이터베이스 모델 정의 (25.06.04~)
* 필요한 테이블
---

## 🛠️ 기술 스택

  * **백엔드**: [FastAPI](https://fastapi.tiangolo.com/)
  * **데이터베이스**: [SQLite](https://www.sqlite.org/index.html) (개발용, 추후 PostgreSQL 등으로 확장 가능)
  * **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
  * **데이터 유효성 검사**: [Pydantic](https://pydantic-docs.helpmanual.io/)
  * **인증**: [PyJWT](https://pyjwt.readthedocs.io/en/stable/) (JWT 토큰), [Passlib](https://passlib.readthedocs.io/en/stable/) (비밀번호 해싱)
  * **테스트**: [Pytest](https://docs.pytest.org/en/stable/)

-----

## 폴더 구조
```
.
├── app/
│   ├── __init__.py
│   ├── main.py                   # FastAPI 애플리케이션 인스턴스 및 라우터 포함
│   ├── core/                     # 설정, 의존성 주입 등 핵심 로직
│   │   ├── __init__.py
│   │   ├── config.py             # 환경 변수, 설정 값
│   │   ├── database.py           # DB 연결, 세션 관리
│   │   └── security.py           # 인증 관련 유틸리티 (비밀번호 해싱, JWT)
│   ├── api/                      # API 엔드포인트 정의
│   │   ├── __init__.py
│   │   ├── v1/                   # API 버전 관리 (선택 사항)
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py       # 인증 관련 엔드포인트 (회원가입, 로그인)
│   │   │   │   ├── posts.py      # 게시글 관련 엔드포인트
│   │   │   │   └── comments.py   # 댓글 관련 엔드포인트
│   │   │   └── deps.py           # 의존성 (current_user 등)
│   ├── crud/                     # 데이터베이스 CRUD 작업 (Create, Read, Update, Delete)
│   │   ├── __init__.py
│   │   ├── posts.py
│   │   └── comments.py
│   ├── models/                   # 데이터베이스 모델 정의 (SQLAlchemy 모델)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── post.py
│   │   └── comment.py
│   ├── schemas/                  # Pydantic 스키마 정의 (요청/응답 데이터 유효성 검사)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── post.py
│   │   └── comment.py
│   └── tests/                    # 테스트 코드 (pytest)
│       ├── __init__.py
│       ├── api/
│       │   ├── test_auth.py
│       │   ├── test_posts.py
│       │   └── test_comments.py
│       └── conftest.py           # 테스트 유틸리티 (DB 세팅, 클라이언트 생성 등)
├── .env                          # 환경 변수 파일 (DB URL, SECRET_KEY 등)
├── Dockerfile                    # Docker 이미지 빌드 파일 (선택 사항)
├── requirements.txt              # 프로젝트 의존성 목록
├── pyproject.toml                # poetry 또는 pip-tools 사용 시 (선택 사항)
└── README.md                     # 프로젝트 설명
```
---

## 📦 프로젝트 설정 및 실행

### 📋 사전 준비 사항

  * Python 3.9+
  * `pip` (Python 패키지 관리자)

### ⚙️ 설치

1.  **리포지토리 클론:**

    ```bash
    git clone https://github.com/your-username/fastapi-blog-api.git
    cd fastapi-blog-api
    ```

    (🚨 `your-username`을 본인의 GitHub 사용자 이름으로 변경하거나, 다른 저장소 이름을 사용하세요.)

2.  **가상 환경 생성 및 활성화:**

    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **의존성 설치:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **환경 변수 설정:**
    프로젝트 루트에 `.env` 파일을 생성하고 다음 내용을 추가합니다.

    ```env
    DATABASE_URL="sqlite:///./sql_app.db"
    SECRET_KEY="YOUR_SUPER_SECRET_KEY" # 실제 운영 환경에서는 강력하고 복잡한 키를 사용하세요!
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

    (🚨 `YOUR_SUPER_SECRET_KEY`는 반드시 본인만의 유니크하고 강력한 값으로 변경하세요.)

5.  **데이터베이스 마이그레이션 (선택 사항, 필요 시 Alembic 등 사용)**:
    이 프로젝트는 간단한 구성을 위해 애플리케이션 시작 시 DB 스키마를 자동으로 생성하거나 `uvicorn` 실행 전 수동으로 생성할 수 있습니다. 예를 들어, `app/core/database.py`에서 `Base.metadata.create_all(bind=engine)`를 호출하도록 설정할 수 있습니다.

### ▶️ 애플리케이션 실행

```bash
uvicorn app.main:app --reload
```

서버가 시작되면 `http://127.0.0.1:8000`에서 API에 접근할 수 있습니다.

-----

## 📄 API 문서 (Swagger UI)

애플리케이션이 실행 중일 때, 다음 URL에서 자동으로 생성된 API 문서를 확인할 수 있습니다:

  * **Swagger UI**: `http://127.0.0.1:8000/docs`
  * **ReDoc**: `http://127.0.0.1:8000/redoc`

이 문서를 통해 각 엔드포인트의 사용법, 요청/응답 스키마, 테스트 등을 편리하게 확인할 수 있습니다.

-----

## 🧪 테스트 실행

프로젝트에 포함된 테스트 코드를 실행하려면 `pytest`를 사용합니다.

```bash
pytest
```
