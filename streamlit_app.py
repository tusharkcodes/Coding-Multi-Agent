# app.py
import streamlit as st
import asyncio
from orchestrator import stream_round_robin, stream_selector

st.set_page_config(page_title="AutoGen Multi-Agent", layout="wide")
st.title("🤖 AutoGen Multi-Agent Framework")

task = st.text_area("Enter software requirement")

mode = st.selectbox("Execution Mode", ["Selector (Iterative)", "Round Robin"])

run_btn = st.button("Run")

if run_btn and task.strip():

    st.subheader("Agent Execution Logs")

    output_container = st.container()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def run():
        if mode == "Selector (Iterative)":
            async for event in stream_selector(task):
                with output_container:
                    st.markdown(f"### 🧠 {event.source}")
                    st.code(event.content)
        else:
            async for event in stream_round_robin(task):
                with output_container:
                    st.markdown(f"### 🧠 {event.source}")
                    st.code(event.content)

    loop.run_until_complete(run())

    st.success("Execution completed ✅")
