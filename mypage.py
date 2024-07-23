import streamlit as st

import user_db as db

from streamlit_cookies_controller import CookieController

# db 임시 생성
# db.add_user('1234', '1234', 'example@gmail.com', '1234')
# db.add_ingredient('1234', '감자')
# db.add_ingredient('1234', '물')
# db.add_likes('1234', '케이크')
# db.add_dislikes('1234', '땅콩')

def naviagation_button():
    cols = st.columns([3, 1, 1]) 
    with cols[1]:
        if st.button("홈으로 돌아가기"):
            st.session_state.page = 'main'
            st.rerun()
    with cols[2]:
        if st.button('로그아웃'):
            cookies.set('logged_in', 'False')
            cookies.set('user_id', '')
            cookies.set('user_pw', '')
            cookies.set('user_email', '')
            cookies.set('user_name', '')
            st.success('로그아웃 되었습니다.')
            st.session_state.page = 'login'
            time.sleep(1)
            st.rerun()


def display_mypage():
    cookies = CookieController()
    
    st.write(f'안녕하세요 {cookies.get('user_name')}님')
    
    user_id = cookies.get('user_id')
    user_pw = cookies.get('user_pw')
    user_email = cookies.get('user_email')
    user_name = cookies.get('user_name')
    
    st.header(f"{user_id} 님의 마이페이지")
    
    naviagation_button()
    
    # 냉장고
    st.markdown("### 내 냉장고")
    
    items_list = db.get_ingredient(user_id)
    st.markdown(items_list)
    
    cols = st.columns([1, 1]) 
    with cols[0]:
        with st.form("add_ingredient"):
            st.markdown("**재료 추가하기**")
            subcols = st.columns([3, 1]) 
            with subcols[0]:
                add_ingredient_input = st.text_input("추가할 재료를 입력하세요. 예시) 사과", value="")
            with subcols[1]:
                submitted_add_ingredient = st.form_submit_button('추가')
        if submitted_add_ingredient:
            db.add_ingredient(user_id, add_ingredient_input)
            print("add_ingredient 성공")
            st.rerun()
    with cols[1]:
        with st.form("delete_ingredient"):
            st.markdown("**재료 삭제하기**")
            delete_ingredient_input = st.text_input("삭제할 재료를 입력하세요. 예시) 사과", value="")
            submitted_delete_ingredient = st.form_submit_button('삭제')
        if submitted_delete_ingredient:
            db.delete_ingredient(user_id, delete_ingredient_input)
            print("add_ingredient 성공")
            st.rerun()
    
    st.divider()
    
    cols = st.columns([1, 1]) 
    # 호
    with cols[0]:
        st.markdown("### 호")
        items_list = db.get_likes(user_id)
        st.markdown(items_list)
        with st.form("likes"):
            st.markdown("**좋아하는 음식 추가하기**")
            add_likes_input = st.text_input("추가할 음식 입력하세요. 예시) 사과", value="")
            submitted_add_likes = st.form_submit_button('추가')
            
            st.markdown("**좋아하는 음식 삭제하기**")
            delete_likes_input = st.text_input("삭제할 음식 입력하세요. 예시) 사과", value="")
            submitted_delete_likes = st.form_submit_button('삭제')
            
        if submitted_add_likes:
            db.add_likes(user_id, add_likes_input)
            print("add_likes 성공")
            st.rerun()
        if submitted_delete_likes:
            db.delete_likes(user_id, delete_likes_input)
            print("delete_likes 성공")
            st.rerun()
    # 불호
    with cols[1]:
        st.markdown("### 불호")
        items_list = db.get_dislikes(user_id)
        st.markdown(items_list)
        with st.form("dislikes"):
            st.markdown("**불호 음식 추가하기**")
            add_dislikes_input = st.text_input("추가할 음식 입력하세요. 예시) 사과", value="")
            submitted_add_dislikes = st.form_submit_button('추가')
            
            st.markdown("**불호 음식 삭제하기**")
            delete_dislikes_input = st.text_input("삭제할 음식 입력하세요. 예시) 사과", value="")
            submitted_delete_dislikes = st.form_submit_button('삭제')
            
        if submitted_add_dislikes:
            db.add_dislikes(user_id, add_dislikes_input)
            print("add_dislikes 성공")
            st.rerun()
        if submitted_delete_dislikes:
            db.delete_dislikes(user_id, delete_dislikes_input)
            print("delete_dislikes 성공")
            st.rerun()
    
    st.divider()
    
    # 회원정보수정
    st.markdown("### 회원정보")
    with st.form("edit_user_info"):
        # st.markdown("**정보 수정하기**")
        st.text_input("ID (수정 불가)", value=user_id)
        new_pw = st.text_input("Password", value=user_pw)
        new_email = st.text_input("Email", value=user_email) 
        submitted_add_ingredient = st.form_submit_button('수정하기')

    if submitted_add_ingredient:
        db.edit_information(user_id, new_pw, new_email)
        print("edit_user_info 성공")
        st.rerun()
    
    st.markdown("### 히스토리")