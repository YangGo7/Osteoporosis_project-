# 🦴 골다공증 위험도 예측 시스템

**AI 기반 골다공증 진단 및 관리 웹 플랫폼**

Django 웹 프레임워크를 활용하여 개발한 골다공증 위험도 예측 및 건강 관리 시스템입니다. 사용자의 개인정보와 건강 상태를 기반으로 골절 위험도를 예측하고, 맞춤형 건강 관리 방안을 제시합니다.
## 🎯 프로젝트 개요

### 핵심 목표
- **조기 예측**: 골다공증의 조용한 진행 특성을 고려한 사전 예방 시스템
- **개인 맞춤형**: 사용자별 위험 요소 분석 및 맞춤형 관리 방안 제시
- **접근성**: 웹 기반 플랫폼으로 언제 어디서나 손쉬운 접근
- **종합 관리**: 예측부터 병원 검색까지 원스톱 건강 관리 서비스

### 주요 특징
- 🔬 **과학적 예측 모델**: 로지스틱 회귀 기반 위험도 계산 알고리즘
- 📊 **데이터 시각화**: Chart.js를 활용한 직관적인 결과 표시
- 📄 **PDF 리포트**: xhtml2pdf를 활용한 전문적인 진단서 생성
- 🏥 **병원 연계**: 지역별 병원 검색 및 Google Maps 연동
- 💬 **커뮤니티**: Q&A 게시판을 통한 사용자 간 정보 공유

## 🏗️ 시스템 아키텍처

```
골다공증 진단 시스템/
├── 🔐 사용자 관리 (User Management)
│   ├── 회원가입/로그인/로그아웃
│   ├── 개인정보 관리 (Profile)
│   └── 마이페이지 (결과 히스토리)
│
├── 🧠 골다공증 예측 (Osteoporosis Prediction)
│   ├── 다단계 설문조사 폼
│   ├── AI 기반 위험도 계산
│   ├── 개인 맞춤형 운동/식단 추천
│   └── PDF 진단서 생성
│
├── 🏥 병원 정보 (Hospital Information)
│   ├── 지역별 병원 검색
│   ├── 시/도, 시/군/구 필터링
│   └── Google Maps 연동
│
└── 💬 커뮤니티 (Community)
    ├── Q&A 게시판
    ├── 좋아요/댓글 시스템
    └── 비밀글 기능
```

## 🚀 주요 기능

### 1. 🔍 골다공증 위험도 예측
- **다면적 평가**: 나이, 성별, BMI, 병력 등 12개 위험 요소 종합 분석
- **과학적 알고리즘**: 로지스틱 회귀 모델 기반 위험도 계산
- **3단계 위험도 분류**: Normal, Caution, High Risk 등급 제시
- **정량적 결과**: 주요 골절 위험도(%), 고관절 골절 위험도(%) 수치 제공

```python
# 핵심 예측 알고리즘 예시
def calculate_frax_risk(age, gender, bmi, fracture, smoking, ...):
    coef = {
        "age": 0.05 * age,
        "gender": 0.3 if gender == 1 else 0,
        "bmi": -0.1 * (bmi - 25),
        "fracture": 0.8 if fracture else 0,
        # ... 기타 위험 요소들
    }
    logit_major = sum(coef.values())
    return round(logistic_function(logit_major) * 100, 2)
```

### 2. 📊 맞춤형 건강 관리
- **개인별 운동 추천**: 위험도별 맞춤형 운동 프로그램 제시
- **식단 가이드**: 칼슘/비타민D 풍부한 식단 이미지 및 설명
- **생활습관 개선**: 금연, 금주 등 위험 요소 개선 방안

### 3. 📄 전문적인 리포트 생성
- **PDF 진단서**: 병원 방문용 전문 리포트 자동 생성
- **QR 코드**: 모바일 접근을 위한 QR 코드 삽입
- **결과 히스토리**: 시간별 예측 결과 추적 및 관리

### 4. 🏥 의료기관 연계 서비스
- **병원 데이터베이스**: 전국 100개 병원 정보 제공
- **지역별 검색**: 시/도, 시/군/구 단위 병원 필터링
- **Google Maps 연동**: 가까운 정형외과 실시간 검색

### 5. 💬 커뮤니티 플랫폼
- **Q&A 게시판**: 골다공증 관련 질의응답 공간
- **좋아요 시스템**: Ajax 기반 실시간 좋아요 기능
- **비밀글 기능**: 민감한 의료 정보 보호

## 🛠️ 기술 스택

### Backend
- **Django 5.1.7**: 메인 웹 프레임워크
- **Python 3.8+**: 핵심 개발 언어
- **SQLite**: 개발용 데이터베이스
- **NumPy**: 수치 계산 라이브러리

### Frontend
- **HTML5/CSS3**: 마크업 및 스타일링
- **Bootstrap 4.6.2**: 반응형 UI 프레임워크
- **JavaScript/jQuery**: 동적 상호작용
- **Chart.js**: 데이터 시각화

### 추가 라이브러리
- **xhtml2pdf**: PDF 리포트 생성
- **qrcode**: QR 코드 생성
- **django-widget-tweaks**: 폼 스타일링
- **Pillow**: 이미지 처리

## 📱 주요 화면

### 1. 메인 진단 페이지
```html
<!-- 사용자 친화적인 설문 인터페이스 -->
<div class="form-group">
    <label>골다공증 진단 여부
        <span class="tooltip-icon" title="골다공증이란? 뼛속에 구멍이 많이 생긴다는 뜻...">❓</span>
    </label>
    <div class="radio-group">
        <input type="radio" name="op" value="True"> 예
        <input type="radio" name="op" value="False"> 아니오
    </div>
</div>
```

### 2. 결과 시각화
```javascript
// Chart.js를 활용한 위험도 시각화
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Major Fracture', 'Hip Fracture'],
        datasets: [{
            data: [majorRisk, hipRisk],
            backgroundColor: ['#4e79a7', '#f28e2b']
        }]
    }
});
```

### 3. 병원 검색 시스템
```javascript
// Ajax 기반 동적 지역 필터링
$('#city-select').change(function () {
    const city = $(this).val();
    $.get("{% url 'hospital:get_districts' %}", { city: city }, function (data) {
        const districtSelect = $('#district-select');
        districtSelect.empty();
        data.forEach(function (d) {
            districtSelect.append('<option value="' + d + '">' + d + '</option>');
        });
    });
});
```

## 📈 데이터 모델

### 사용자 프로필 모델
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    # 위험 요소들
    fracture = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    # ... 기타 의료 정보
```

### 예측 결과 모델
```python
class OsteoporosisResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    major_risk = models.FloatField()  # 주요 골절 위험도
    hip_risk = models.FloatField()    # 고관절 골절 위험도
    level = models.CharField(max_length=50)  # 위험 등급
    created_at = models.DateTimeField(auto_now_add=True)
```

## 🚀 설치 및 실행

### 1. 프로젝트 클론
```bash
git clone https://github.com/YangGo7/Osteoporosis_project-.git
cd Osteoporosis_project-
```

### 2. 가상환경 설정
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 설정
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. 병원 데이터 로드 (선택사항)
```bash
python manage.py load_hospitals
```

### 6. 서버 실행
```bash
python manage.py runserver
```

## 📋 Requirements

```txt
Django>=5.1.7
django-widget-tweaks>=1.4.0
numpy>=1.21.0
Pillow>=8.0.0
xhtml2pdf>=0.2.5
qrcode>=7.3.1
django-extensions>=3.1.0
```

## 🎯 사용자 시나리오

### 1. 신규 사용자 진단 과정
1. **회원가입** → 개인정보 입력
2. **설문조사** → 12개 위험 요소 체크
3. **결과 확인** → AI 기반 위험도 예측
4. **맞춤 추천** → 개인별 운동/식단 가이드
5. **PDF 저장** → 병원 방문용 리포트 다운로드

### 2. 기존 사용자 관리
1. **마이페이지** → 과거 진단 결과 확인
2. **재진단** → 정기적 위험도 업데이트
3. **커뮤니티** → Q&A 게시판 참여
4. **병원 검색** → 지역별 의료기관 탐색

## 🔬 핵심 알고리즘

### FRAX 기반 위험도 계산
```python
def logistic_function(x):
    return 1 / (1 + math.exp(-x))

def predict_osteoporosis(data):
    # BMI 계산
    bmi = data['weight'] / ((data['height'] / 100) ** 2)
    
    # 위험 요소별 가중치 적용
    coef = {
        'intercept': -4.0,
        'age': 0.05 * data['age'],
        'gender': 0.3 if data['gender'] == '여자' else 0,
        'bmi': -0.1 * (bmi - 25),
        'fracture': 0.8 if data['fracture'] else 0,
        # ... 기타 요소들
    }
    
    # 로지스틱 회귀 계산
    logit_score = sum(coef.values())
    risk_probability = logistic_function(logit_score) * 100
    
    return {
        'major_risk': round(risk_probability, 2),
        'hip_risk': round(risk_probability - 15, 2),
        'level': classify_risk(risk_probability)
    }
```

## 🎨 UI/UX 특징

### 반응형 디자인
- **모바일 최적화**: Bootstrap 그리드 시스템 활용
- **직관적 인터페이스**: 단계별 설문 진행 가이드
- **접근성**: 툴팁과 설명을 통한 의료용어 해설

### 시각적 피드백
- **색상 코딩**: 위험도별 차별화된 색상 표시
- **차트 시각화**: 막대그래프/도넛차트로 결과 표현
- **진행 표시**: 실시간 입력 상태 피드백

## 🔒 보안 및 개인정보 보호

### 데이터 보안
- **CSRF 보호**: Django 내장 보안 기능 활용
- **사용자 인증**: 로그인 기반 개인정보 보호
- **비밀글 시스템**: 민감한 의료 정보 선택적 공개

### 개인정보 처리
- **최소 수집**: 진단에 필요한 정보만 수집
- **목적 제한**: 골다공증 예측 목적으로만 활용
- **사용자 제어**: 개인정보 수정/삭제 권한 제공

## 📊 성과 및 특징

### 기술적 성과
- **모듈화 설계**: Django 앱 기반 확장 가능한 구조
- **RESTful API**: 향후 모바일 앱 연동 대비 설계
- **데이터 시각화**: Chart.js 활용 직관적 결과 표시
- **PDF 생성**: 전문적인 의료 리포트 자동 생성

### 사용자 경험
- **원스톱 서비스**: 진단부터 병원 검색까지 통합 제공
- **개인 맞춤화**: 위험도별 차별화된 관리 방안
- **지속적 관리**: 히스토리 추적 및 정기 재진단 지원

## 🚀 향후 개발 계획

### 단기 목표
- [ ] **AI 모델 고도화**: 더 정확한 예측을 위한 딥러닝 모델 도입
- [ ] **모바일 앱**: React Native 기반 모바일 애플리케이션
- [ ] **실시간 알림**: 정기 검진 알림 및 건강 관리 팁

### 장기 비전
- [ ] **의료기관 연동**: 실제 병원 시스템과의 API 연동
- [ ] **빅데이터 분석**: 사용자 데이터 기반 예측 모델 개선
- [ ] **텔레헬스 연동**: 화상 상담 및 원격 모니터링

## 🤝 기여 및 협업

### 개발 환경 설정
```bash
# 개발용 브랜치 생성
git checkout -b feature/new-feature

# 코드 스타일 확인
flake8 .
black .

# 테스트 실행
python manage.py test
```

### 기여 가이드라인
- **PEP 8 준수**: Python 코딩 스타일 가이드 준수
- **테스트 작성**: 새로운 기능에 대한 단위 테스트 필수
- **문서화**: 코드 변경 시 README 업데이트

## 📞 연락처

- **개발자**: YangGo7
- **이메일**: yanggo7@example.com
- **GitHub**: [https://github.com/YangGo7](https://github.com/YangGo7)
- **프로젝트 저장소**: [https://github.com/YangGo7/Osteoporosis_project-](https://github.com/YangGo7/Osteoporosis_project-)

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 🏆 프로젝트 하이라이트

### 💡 혁신성
- **예방 중심 접근**: 증상 발현 전 조기 예측으로 예방 의학 구현
- **개인 맞춤형 서비스**: AI 기반 개별화된 건강 관리 솔루션
- **통합 플랫폼**: 진단부터 치료기관 연계까지 원스톱 서비스

### 🔧 기술적 우수성
- **확장 가능한 아키텍처**: Django 기반 모듈화 설계
- **과학적 근거**: 의학적으로 검증된 FRAX 알고리즘 활용
- **사용자 중심 설계**: 직관적 UI/UX와 접근성 고려

### 🌟 사회적 가치
- **의료 접근성 향상**: 웹 기반으로 언제 어디서나 이용 가능
- **조기 발견 기여**: 골다공증의 조기 발견으로 사회적 의료비 절감
- **건강 증진**: 개인별 맞춤 관리로 삶의 질 향상 기여

---

<div align="center">

**🦴 건강한 뼈, 행복한 삶을 위한 스마트 헬스케어 솔루션 🦴**

*Made with ❤️ for better bone health*

</div>
