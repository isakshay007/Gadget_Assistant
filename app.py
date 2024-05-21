import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
from lyzr_automata.tasks.task_literals import InputType, OutputType
import os

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Gadget Recommendation Assistant🤖")
st.markdown("Welcome to the Gadget Recommendation Assistant!  Using Lyzr Automata, this app offers tailored gadget recommendations to perfectly match your needs.")
input = st.text_input("Please enter your requirements for recommendation:",placeholder=f"""Type here""")

open_ai_text_completion_model = OpenAIModel(
    api_key=st.secrets["apikey"],
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)


def generation(input):
    generator_agent = Agent(
        role="Expert GADGET RECOMMENDATION ASSISTANT",
        prompt_persona=f"Your task is to meticulously ANALYZE and IDENTIFY the 3-5 TOP gadgets that perfectly ALIGN with the specific INPUT CRITERIA provided by the user: CATEGORY, BUDGET, KEY FEATURES, and USAGE.")
    prompt = f"""
You are an Expert GADGET RECOMMENDATION ASSISTANT. Your task is to meticulously ANALYZE and IDENTIFY the 3-5 TOP gadgets that perfectly ALIGN with the specific INPUT CRITERIA provided by the user: CATEGORY, BUDGET, KEY FEATURES, and USAGE.

Here are your GUIDED STEPS to deliver spot-on recommendations:

1. START by compiling an EXTENSIVE list of gadgets within the given CATEGORY.

2. PROCEED to FILTER this list to include only those gadgets that fall within the specified BUDGET range.

3. NEXT, REFINE your selection by ensuring each gadget matches the desired KEY FEATURES.

4. THEN, EVALUATE how each gadget meets the USAGE criteria to guarantee it suits the user's needs impeccably.

5. PRESENT a well-curated list of 3-5 PREMIER gadgets, complete with DETAILED SPECIFICATIONS for each recommendation.

You MUST execute these steps with precision to provide VALUE and SATISFACTION to the user.
 """

    generator_agent_task = Task(
        name="Generation",
        model=open_ai_text_completion_model,
        agent=generator_agent,
        instructions=prompt,
        default_input=input,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
    ).execute()

    return generator_agent_task 
   
if st.button("Recommend"):
    solution = generation(input)
    st.markdown(solution)

with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Automata Agent . For any inquiries or issues, please contact Lyzr.

    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width=True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width=True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width=True)
    st.link_button("Slack",
                   url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw',
                   use_container_width=True)