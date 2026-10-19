# 김하은 취업 포트폴리오

김하은의 자기소개, 아르바이트와 학교 활동, 업무 역량, 수상 및 학력 정보를 소개하는 정적 웹사이트입니다. HTML, CSS, JavaScript만 사용하며 별도의 유료 서버나 외부 라이브러리가 필요하지 않습니다. GitHub Pages에 배포할 수 있습니다.

## 로컬에서 확인

저장소 루트의 `index.html`을 브라우저로 열면 됩니다. 또는 간단한 로컬 서버를 실행하고 `http://localhost:8000`으로 접속하세요.

```bash
python3 -m http.server 8000
```

## GitHub Pages 배포

`.github/workflows/deploy-pages.yml`은 `index.html`, `styles.css`, `script.js`, `favicon.svg`만 Pages 배포물에 넣습니다. 저장소에 포함된 Streamlit 앱이나 데이터 파일은 공개 사이트에 배포하지 않습니다.

1. 변경 사항을 저장소의 `main` 브랜치에 push합니다.
2. GitHub 저장소의 **Settings > Pages**에서 **Build and deployment > Source**를 **GitHub Actions**로 설정합니다.
3. **Actions** 탭에서 **Deploy portfolio to GitHub Pages** 워크플로가 성공적으로 끝났는지 확인합니다. 필요한 경우 **Run workflow**를 눌러 수동으로 실행할 수 있습니다.
4. 이 저장소의 Pages 주소는 `https://xyeunm.github.io/30403/`입니다. 배포가 완료된 뒤 브라우저에서 열어 실제 공개 여부를 확인하세요. GitHub 저장소의 **Settings > Pages** 및 성공한 Actions 실행의 배포 URL에서도 사이트 주소를 확인할 수 있습니다.
5. 사이트가 정상적으로 열린 것을 확인한 뒤 해당 URL로 QR 코드를 만들고 공유하세요.

## 내용 수정

- 문구, 이력, 이메일 및 페이지 구조: `index.html`
- 색상, 카드, 반응형·인쇄 레이아웃 및 애니메이션: `styles.css`
- 페이지 주소, 맨 위로 버튼 및 스크롤 등장 효과: `script.js`
- 브라우저 탭 아이콘: `favicon.svg`

학교 졸업·진학 상태는 제공된 내용에 맞춰 예정 상태로 표시했습니다. 구체적인 인스타그램 업무, FTA 대회 세부 활동명 등 확인되지 않은 정보는 임의로 추가하지 않았습니다. 연락처를 포함한 내용이 공개 저장소와 웹사이트에 노출된다는 점을 확인한 뒤 배포하세요.
