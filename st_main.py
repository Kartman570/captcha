import streamlit as st

st.title('Prove you are not robot')

option = st.selectbox(
    label="Select captcha",
    options=('Noise figures', 'TODO', 'TODO'),
    index=None
)

if option == 'Noise figures':
    if "figure_answer" not in st.session_state:
        st.session_state.figure_answer = None
        st.session_state.moving = False
        st.session_state.blinking = False
        st.session_state.letter = False

    st.header('You see GIF animation with floating figure. What is that figure?')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('test.gif')
    with col2:
        st.radio(
            "What is the shape on GIF?",
            ["Circle", "Square", "Triangle", "Letter"],
            key="figure_answer",
        )
    if st.session_state.figure_answer is not None:
        with col3:
            st.checkbox("Figure moves across image", key="moving")
            st.checkbox("Figure blinks", key="blinking")
            if st.session_state.figure_answer == "Letter":
                st.session_state.letter = st.text_input("Letter")

    st.button("Submit answer") #TODO VERIFICATION
    '''
    DEBUG
    st.write(st.session_state.figure_answer)
    st.write(st.session_state.moving)
    st.write(st.session_state.blinking)
    st.write(st.session_state.letter)
    '''

elif option == 'TODO':
    st.header('header')
    st.write('write')
