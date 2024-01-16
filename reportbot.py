from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import streamlit as st


from streamlit_extras.buy_me_a_coffee import button

button(username="inMyUniverse", floating=True, width=221)

with st.sidebar:
    st.markdown("---")
    st.markdown("# 💡 About ")
    st.markdown(
       "Report Master는 누구나 쉽게 전문적인 레포트를 작성할 수 있도록 도와주는 혁신적인 도구입니다. "
       
            )
    st.markdown(
      "사용자가 제공한 연령대, 주제, 언어, 원하는 분량, 그리고 강조하고 싶은 특정 부분을 기반으로 맞춤형 레포트 초안을 생성합니다."
            )
    st.markdown("인공지능을 활용하여 정확하고 논리적인 내용을 담은 레포트를 빠르게 작성할 수 있습니다.")
    st.markdown("---")
    
    openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
   
    


# Streamlit UI 설정
st.title("📝 Report Master")


# 레포트 초안 생성 함수
def generate_report_draft(age, topic, length, emphasis, language):
    # LLM 모델 인스턴스화
    llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
    
    # 프롬프트 템플릿 설정
    template = """
    [Language: {language}]
    As an assistant, create a report draft considering an audience of age {age}. The topic is: {topic}.
    Length: A4 {length} pages.
    Emphasize on: {emphasis}.
    Structure:
        - Introduction: Brief mention of the topic. Include definition and explanation. Describe what will be discussed in the main body.
        - Main Body: Detailed definition and explanation based on research and data. Discuss the current situation, issues, implications, and expert opinions related to the topic.  Include statistics and factual evidence. When referencing external sources, provide a brief explanation along with the source. Discuss the current situation, issues, implications, and expert opinions related to the topic
        - Conclusion: Summarize main points and implications. Suggest attitudes or actions for the reader, and present various opinions on the topic.
    Avoid vague language and abstract expressions.
    End with a summary of the content and one creative idea.
    """
    prompt = PromptTemplate(input_variables=["age", "topic", "length", "emphasis", "language"], template=template)
    prompt_query = prompt.format(age=age, topic=topic, length=length, emphasis=emphasis, language=language)
    
    # LLM 모델 실행
    response = llm(prompt_query)
    # 결과 출력
    return st.info(response)

# 사용자 입력 폼 설정
with st.form("report_form"):
    age_input = st.number_input("연령대를 입력해주세요", min_value=10, max_value=100)
    topic_input = st.text_input("주제를 입력해주세요", "")
    length_input = st.select_slider("분량을 선택해주세요", options=['1', '2', '3'], value='3')
    emphasis_input = st.text_area("강조하고 싶은 부분을 알려주세요")
    language_input = st.selectbox("사용할 언어를 선택해주세요", [ "Korean", "English", "Japanese", "Chinese", "Other"])
    submitted = st.form_submit_button("시작하기")
    if language_input == "Other":
     custom_language_input = st.text_input("사용할 언어를 적어주세요")
    # Update language_input with the custom language if provided
     if custom_language_input:
        language_input = custom_language_input
    
    if not openai_api_key:
        st.info("왼쪽 하단의 OpenAI API key 를 입력해주세요")  
    
    elif submitted:
        if not topic_input:
            st.warning("주제를 작성해주세요!")
        if age_input < 10 or age_input > 100:
            st.warning("10-100 사이 연령을 입력해주세요")
        if language_input == "Other" and not custom_language_input:
            st.warning("사용한 언어를 직접 적어주세요")   
        generate_report_draft(age_input, topic_input, length_input, emphasis_input, language_input)




