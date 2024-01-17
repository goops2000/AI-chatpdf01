# 📝 ReportMaster 

ReportMaster는 AI 기반의 레포트 작성 도구로, 사용자가 빠르고 효율적으로 레포트를 작성할 수 있도록 지원합니다.


ReportMaster는 과제를 제출하기 위해 Chat GPT를 활용하는 과정에서 반복적인 수정과 질문의 번거로움을 해소하기 위해 개발되었습니다. 


LangChain과 Chat GPT를 결합하여 사용자가 보고서 틀을 쉽게 생성하고, 사용자의 요구에 맞춘 보고서 초안과 정확한 프롬프트를 제공함으로써, 보고서 작성 과정을 간소화하고 향상시키도록 설계되었습니다. 

<br>

## 배포 링크
실제 작동중인 사이트를 보고싶다면 [여기를 클릭하세요](https://reportmaster1.streamlit.app/)

<br>

## 사용한 기술과 라이브러리

- Python
- Streamlit
- LangChain
- OpenAI GPT-3.5-turbo

<br>

## 프로젝트의 기능

- **📝 맞춤형 프롬프트 입력**: 사용자의 연령대, 주제, 분량, 강조할 내용 및 언어 선택을 통한 맞춤형 프롬프트 생성.
- **🔍 보고서 자동 생성**: LangChain 및 OpenAI GPT-3.5-turbo를 활용한 보고서 자동 작성.
- **💬 실시간 AI 응답 처리:**: Streamlit과 연동된 ChatOpenAI 모델을 사용하여 사용자의 질문에 실시간으로 응답.

<br>


## 프로젝트 설치 및 실행 방법

1. 저장소 클론:
```
git clone https://github.com/goops2000/ReportMaster.git
```

2. 의존성 설치:
```
cd ReportMaster
pip install -r requirements.txt
```

3. 애플리케이션 실행:
```
streamlit run reportbot.py
```


 이제 `localhost:8501`에서 ReportMaster 애플리케이션에 접근할 수 있습니다.

