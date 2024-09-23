import streamlit as st
import random
import datetime

st.title(':sparkles: 로또 생성기 :sparkles:')

def generate_lotto():
    lotto = set()
    while len(lotto) < 6:
        number = random.randint(1, 45)  
        lotto.add(number)
    return sorted(lotto)

if st.button('로또를 생성해 주세요!'):
    #  당첨 로또 번호 생성
    reference_lotto = generate_lotto()
    st.subheader(f'당첨 로또 번호: :blue[{reference_lotto}]')

    # 생성할 로또 번호 세트 수 입력
    num_tickets = st.number_input('생성할 로또 번호 세트 수:', min_value=1, max_value=10, value=1)
    
    for i in range(num_tickets):
        ticket = generate_lotto()
        st.subheader(f'{i + 1}. 행운의 번호: :green[{ticket}]')
    
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
