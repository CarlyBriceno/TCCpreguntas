import streamlit as st

# Quiz data: questions, options, correct answers, and explanations
quiz_data = [
    {
        "question": "¿Cuál es el principio central del modelo de Albert Ellis en la Terapia Racional Emotiva Conductual (TREC)?",
        "options": [
            "Las emociones y comportamientos están determinados principalmente por factores biológicos.",
            "Los eventos activadores generan emociones directamente sin intervención de pensamientos.",
            "Las creencias irracionales sobre los eventos activadores influyen en las emociones y comportamientos."
        ],
        "correct_answer": "Las creencias irracionales sobre los eventos activadores influyen en las emociones y comportamientos.",
        "explanation": "El modelo de Ellis (TREC) se basa en que las creencias irracionales sobre los eventos activadores (A) determinan las consecuencias emocionales y conductuales (C), no los eventos en sí mismos."
    },
    {
        "question": "En el modelo ABC de Ellis, ¿qué representa la 'B'?",
        "options": [
            "Los eventos activadores (Activating events).",
            "Las creencias (Beliefs) sobre los eventos.",
            "Las consecuencias emocionales y conductuales (Consequences)."
        ],
        "correct_answer": "Las creencias (Beliefs) sobre los eventos.",
        "explanation": "En el modelo ABC, 'B' representa las creencias (Beliefs) que el individuo tiene sobre el evento activador, las cuales pueden ser racionales o irracionales."
    },
    {
        "question": "¿Según Ellis, qué tipo de creencias son las principales responsables de las emociones disfuncionales?",
        "options": [
            "Creencias racionales basadas en hechos objetivos.",
            "Creencias irracionales que incluyen pensamientos absolutistas como 'debería' o 'nunca'.",
            "Creencias basadas únicamente en experiencias pasadas sin interpretación."
        ],
        "correct_answer": "Creencias irracionales que incluyen pensamientos absolutistas como 'debería' o 'nunca'.",
        "explanation": "Ellis identificó que las creencias irracionales, como las exigencias absolutistas ('debería', 'nunca'), son las principales causas de emociones disfuncionales."
    },
    {
        "question": "¿Cuál es el objetivo principal de la TREC en el tratamiento de un paciente?",
        "options": [
            "Cambiar los eventos externos que causan malestar.",
            "Identificar y modificar creencias irracionales para promover emociones y comportamientos más saludables.",
            "Enseñar al paciente a evitar situaciones estresantes."
        ],
        "correct_answer": "Identificar y modificar creencias irracionales para promover emociones y comportamientos más saludables.",
        "explanation": "El objetivo de la TREC es ayudar al paciente a identificar y cambiar creencias irracionales para lograr emociones y comportamientos más adaptativos."
    },
    {
        "question": "En el modelo de Ellis, ¿qué técnica se utiliza comúnmente para cuestionar creencias irracionales?",
        "options": [
            "La exposición prolongada a estímulos temidos.",
            "El debate cognitivo o disputing (D).",
            "La relajación muscular progresiva."
        ],
        "correct_answer": "El debate cognitivo o disputing (D).",
        "explanation": "El debate cognitivo (D) es una técnica clave en TREC para cuestionar y modificar creencias irracionales, parte del modelo ABCDE."
    },
    {
        "question": "¿Qué tipo de pensamiento irracional se refleja en la frase 'Debo ser perfecto en todo lo que hago'?",
        "options": [
            "Catastrofización.",
            "Exigencias absolutistas.",
            "Generalización excesiva."
        ],
        "correct_answer": "Exigencias absolutistas.",
        "explanation": "La frase refleja una exigencia absolutista, un tipo de creencia irracional que usa términos como 'debo' o 'tengo que', según el modelo de Ellis."
    },
    {
        "question": "En la TREC, ¿qué papel juega la 'C' en el modelo ABC?",
        "options": [
            "Representa las creencias irracionales del paciente.",
            "Representa las consecuencias emocionales y conductuales derivadas de las creencias.",
            "Representa los eventos activadores del entorno."
        ],
        "correct_answer": "Representa las consecuencias emocionales y conductuales derivadas de las creencias.",
        "explanation": "En el modelo ABC, 'C' se refiere a las consecuencias emocionales y conductuales que resultan de las creencias (B) sobre un evento activador (A)."
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones refleja una creencia racional según el modelo de Ellis?",
        "options": [
            "Si no consigo este trabajo, será el fin del mundo.",
            "Me gustaría conseguir este trabajo, pero si no lo logro, puedo buscar otras oportunidades.",
            "Debo ser aceptado por todos, o no valgo nada."
        ],
        "correct_answer": "Me gustaría conseguir este trabajo, pero si no lo logro, puedo buscar otras oportunidades.",
        "explanation": "Una creencia racional, según Ellis, es flexible y realista, como aceptar que no lograr algo no es catastrófico y que existen otras opciones."
    },
    {
        "question": "¿Qué estrategia de la TREC ayuda al paciente a reemplazar creencias irracionales por creencias más racionales?",
        "options": [
            "La reestructuración cognitiva.",
            "La hipnosis terapéutica.",
            "La terapia de exposición sistemática."
        ],
        "correct_answer": "La reestructuración cognitiva.",
        "explanation": "La reestructuración cognitiva es la estrategia principal en TREC para reemplazar creencias irracionales por otras más racionales y funcionales."
    },
    {
        "question": "Según Ellis, ¿cómo se relacionan los eventos activadores (A) con las consecuencias (C)?",
        "options": [
            "Los eventos activadores causan directamente las consecuencias emocionales y conductuales.",
            "Los eventos activadores influyen en las consecuencias a través de las creencias (B).",
            "Los eventos activadores no tienen relación con las consecuencias."
        ],
        "correct_answer": "Los eventos activadores influyen en las consecuencias a través de las creencias (B).",
        "explanation": "En el modelo ABC de Ellis, las creencias (B) median la relación entre los eventos activadores (A) y las consecuencias emocionales y conductuales (C)."
    }
]

# Streamlit app
st.title("Cuestionario sobre el Modelo de Albert Ellis en TREC")

# Initialize session state for quiz progress
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.show_result = False
    st.session_state.selected_answer = None

# Get current question
current_question = quiz_data[st.session_state.question_index]

# Display question
st.subheader(f"Pregunta {st.session_state.question_index + 1}")
st.write(current_question["question"])

# Display answer options
selected_option = st.radio("Selecciona una opción:", current_question["options"], key=f"q{st.session_state.question_index}")

# Submit button
if st.button("Enviar respuesta"):
    st.session_state.selected_answer = selected_option
    st.session_state.show_result = True

# Show result if an answer has been submitted
if st.session_state.show_result:
    if st.session_state.selected_answer == current_question["correct_answer"]:
        st.success("¡Correcto!")
        stPrinciple: st.session_state.score += 1
    else:
        st.error("Incorrecto.")
        st.write(f"La respuesta correcta es: **{current_question['correct_answer']}**")
        st.write(f"Explicación: {current_question['explanation']}")

    # Button to continue to the next question
    if st.button("Siguiente pregunta"):
        st.session_state.question_index += 1
        st.session_state.show_result = False
        st.session_state.selected_answer = None
        if st.session_state.question_index >= len(quiz_data):
            st.write(f"¡Cuestionario completado! Tu puntaje: {st.session_state.score}/{len(quiz_data)}")
            st.session_state.question_index = 0
            st.session_state.score = 0
