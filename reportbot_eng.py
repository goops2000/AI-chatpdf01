from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import streamlit as st


from streamlit_extras.buy_me_a_coffee import button

button(username="inMyUniverse", floating=True, width=221)

with st.sidebar:
    st.markdown("---")
    st.markdown("# 💡 About ")
    st.markdown(
    "Report Master is an innovative tool that helps anyone easily write professional reports."
)

    st.markdown(
    "It creates customized report drafts based on the age, topic, language, desired length, and specific aspects the user wants to emphasize."
)

    st.markdown("Utilize artificial intelligence to quickly compose reports containing accurate and logical content.")

    st.markdown("---")
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
   
    


# Streamlit UI 설정
st.title("📝 Report Master")


# 레포트 초안 생성 함수
def generate_report_draft(age, topic, length, emphasis, language):
    # LLM 모델 인스턴스화
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key, streaming=True)

        # PromptTemplate를 사용한 대화 형식의 프롬프트 설정
        report_prompt_template = PromptTemplate(
            input_variables=["age", "topic", "length", "emphasis", "language"],
            template="""
            I need to create a report for an audience of age {age}. The topic is '{topic}'. The report should be A4, {length} pages long, according to the user's request: {emphasis}. It should be written in {language}. Can you help me draft it? The report should include:
            - An Introduction: Brief mention of the topic, including definitions and explanations. And describe what will be discussed in the main body.
            - A Main Body: Detailed explanations based on research and data, including statistics and factual evidence. Discuss the current situation, issues, implications, and expert opinions related to the topic.  Include statistics and factual evidence. When referencing external sources, provide a brief explanation along with the source. Discuss the current situation, issues, implications, and expert opinions related to the topic.
            - A Conclusion: Summarizing the main points and implications, suggesting attitudes or actions for the reader, and presenting various opinions on the topic.
            Please avoid vague language and abstract expressions. Please create a natural context for good readability. And if age audience is more than 15, since it's for a submission, please write in a weighty tone. Conclude with a creative idea.
            """
        )

        # PromptTemplate을 사용하여 프롬프트 포맷팅
        prompt_query = report_prompt_template.format(age=age, topic=topic, length=length, emphasis=emphasis, language=language)
    
        response = llm.predict(prompt_query)
        st.info(response)
# 사용자 입력 폼 설정
with st.form("report_form"):
   age_input = st.number_input("Please enter your age range", min_value=10, max_value=100)
   topic_input = st.text_input("Please enter the topic", "")
   length_input = st.select_slider("Please select the length", options=['1', '2', '3'], value='3')
   emphasis_input = st.text_area("Please let me know if there are any points you would like to emphasize or specific requests. The more detailed your input, the more accurate the report will be.")
   language_input = st.selectbox("Please select the language to use", ["English", "Spanish", "French", "German", "Chinese", "Other"])
   if language_input == "Other":
    custom_language_input = st.text_input("Please enter your language")
    # Update language_input with the custom language if provided
    if custom_language_input:
        language_input = custom_language_input
        
   submitted = st.form_submit_button("Start")
   

   if submitted:
    if not openai_api_key:
        st.info("Please enter the OpenAI API key in the bottom left")
    else:
        if not topic_input:
            st.warning("Please enter a topic.")
        elif age_input < 10 or age_input > 100:
            st.warning("Please enter a valid age range.")
        elif language_input == "Other" and not custom_language_input:
            st.warning("Please enter your language.")
        else:
            with st.spinner('Please wait...🫨'):
                generate_report_draft(age_input, topic_input, length_input, emphasis_input, language_input)


