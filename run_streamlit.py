import streamlit as st
from langchain_openai import ChatOpenAI

# from dotenv import load_dotenv
# import os
# # 환경 변수에서 API 키 로드
# load_dotenv("../../config_openaikey")
# openai_api_key = os.getenv('OPENAI_API_KEY')



# Streamlit 앱 제목
st.title("Openai 질문 답변")

# Streamlit 사이드바를 사용하여 API 키 입력 받기
openai_api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요:", type="password")


#st.session_state

# 세션 관리를 위한 코드 (질문과 답변을 session_state에 저장)
if 'query' not in st.session_state:
    #st.session_state['query'] = []
    st.session_state.query = ''
if 'formatted_response' not in st.session_state:
    #st.session_state['response'] = []
    st.session_state.formatted_response = ''


# 사용자 입력을 위한 text_input 위젯
query = st.text_area("질문을 입력하세요:", st.session_state.query)

# '질문하기' 버튼 추가
if st.button("질문하기", type="primary"):
    # LangChain ChatOpenAI 인스턴스 초기화
    llm = ChatOpenAI(openai_api_key=openai_api_key, model_name='gpt-3.5-turbo')

    # 질문이 입력되면 ChatOpenAI를 사용하여 질문에 대한 답변을 가져옴
    response = llm.invoke(query)
    
    # AIMessage 객체에서 content 속성의 값을 추출
    answer_text = response.content if hasattr(response, 'content') else '답변을 가져오는 데 문제가 발생했습니다.'

    # 포맷된 답변을 Streamlit UI에 표시
    #AIMessage 객체의 content 속성으로, Langsmith가 테스트를 지원하는 방법에 대한 상세한 설명이 포함되어 있습니다. 
    #이 response를 Streamlit UI에 출력하기 위해서는 response 객체에서 content 속성의 값을 추출하고, 이를 적절하게 포맷하여 표시해야 합니다.    
    formatted_response = '\n'.join(line.strip() for line in answer_text.split('\n'))
    
    st.session_state.query = query
    st.session_state.formatted_response = formatted_response
    #st.session_state['query'].append(query) # 이전질문 제거
    #st.session_state['response'].append(formatted_response)
    
st.write(st.session_state.formatted_response)




# 이전 질문과 답변 표시
# with st.expander("이전 질문과 답변"):
#     for q, r in zip(st.session_state.get('query', []), st.session_state.get('response', [])):
#         st.write(f"Q: {q}")
#         st.write(f"A: {r}")
#         st.write("---")



# import streamlit as st
# from dotenv import load_dotenv  ## key 가져오기
# import os

# from langchain_openai import ChatOpenAI

# # 환경 변수에서 API 키 로드
# load_dotenv("../../config_openaikey")
# openai_api_key = os.getenv('OPENAI_API_KEY')

# # LangChain ChatOpenAI 인스턴스 초기화
# llm = ChatOpenAI(openai_api_key=openai_api_key, model_name='gpt-3.5-turbo')

# # Streamlit 앱 제목
# st.title("LangChain 질문 답변 시스템")

# # 사용자 입력을 위한 text_input 위젯
# #query = st.text_input("질문을 입력하세요:")

# query = st.text_area("질문을 입력하세요:")

# # '질문하기' 버튼 추가
# if st.button("질문하기") or query:
#     # 질문이 입력되면 ChatOpenAI를 사용하여 질문에 대한 답변을 가져옴
#     response = llm.invoke(query)

#     # st.session_state를 사용하여 질문과 답변을 저장
#     if 'queries' not in st.session_state:
#         st.session_state['queries'] = []
#     if 'responses' not in st.session_state:
#         st.session_state['responses'] = []
    
#     # 질문과 답변을 session_state에 추가
#     st.session_state['queries'].append(query)
#     st.session_state['responses'].append(response)

#     # 답변 표시
#     #AIMessage 객체의 content 속성으로, Langsmith가 테스트를 지원하는 방법에 대한 상세한 설명이 포함되어 있습니다. 
#     #이 response를 Streamlit UI에 출력하기 위해서는 response 객체에서 content 속성의 값을 추출하고, 이를 적절하게 포맷하여 표시해야 합니다.
#     #st.write("--------", type(response))
#     #formatted_response = '\n'.join(line.strip() for line in response.split('\n'))
#     st.write("답변:", response)
#     st.write("content:", response.AIMessage.content)


# # 이전 질문과 답변 표시
# with st.expander("이전 질문과 답변"):
#     for q, r in zip(st.session_state.get('queries', []), st.session_state.get('responses', [])):
#         st.write(f"Q: {q}")
#         #st.write(f"A: {r.replace('\n\n', ' ').strip()}")
#         st.write(f"A: {r}")
#         st.write("---")



