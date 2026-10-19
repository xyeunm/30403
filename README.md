# 김하은 자기소개서 & 포트폴리오

기업 인사담당자가 모바일과 PC에서 확인할 수 있는 한국어 자기소개서 및 포트폴리오입니다. 별도의 서버나 프레임워크 없이 HTML, CSS, JavaScript로 구성되어 GitHub Pages에 배포할 수 있습니다.

## 로컬에서 확인

저장소 루트에서 `index.html`을 브라우저로 열면 됩니다. 개발 서버를 사용하려면 저장소 루트에서 다음 명령을 실행하고 `http://localhost:8000`으로 접속하세요.

```bash
python3 -m http.server 8000
```

## GitHub Pages 배포

1. 변경 사항을 GitHub 저장소의 기본 브랜치에 push합니다.
2. 저장소의 **Settings > Pages**로 이동합니다.
3. **Build and deployment**의 Source에서 **Deploy from a branch**를 선택합니다.
4. 기본 브랜치(예: `main`)와 폴더 **/(root)**를 선택하고 **Save**를 누릅니다.
5. Pages 설정 화면에 표시되는 배포 상태와 URL을 확인합니다. 이 저장소의 예상 주소는 `https://xyeunm.github.io/30403/`입니다. Pages 설정을 완료하고 배포가 성공한 뒤 접속할 수 있습니다.
6. 배포된 URL을 QR 코드 생성 도구에 입력합니다. 공개 배포 전에 연락처와 공개 정보를 확인하세요.

`index.html`, `styles.css`, `script.js`는 저장소 루트에 있어야 합니다. 웹사이트 주소는 접속한 배포 위치에서 자동으로 표시됩니다. GitHub 저장소 주소는 `github.io` 주소에서 자동 추정합니다. 사용자 도메인 등 다른 호스트를 쓸 때는 `script.js`의 `repositoryUrl` 값에 저장소 URL을 입력하세요.

## 수정할 내용

- 소개와 이력: `index.html`
- 색상, 반응형 레이아웃, 인쇄 스타일: `styles.css`
- 웹사이트와 저장소 주소 표시: `script.js`
- FTA 대회의 정확한 공식 행사명: `index.html`의 **공식 행사명** 항목

수상 경력, 실습, 업무 경험은 제공된 정보만 사용했습니다. 공개 배포 전 개인정보와 연락처가 공개되어도 괜찮은지 확인하세요.
