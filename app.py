import streamlit as st
import requests
from func import start_bot

# API endpoint
api_endpoint = "https://pipecat-default-example-wispy-cloud-99.fly.dev/"

# Mapping of prompt and voice_id
voice_map = {
"Newsman" : "d46abd1d-2d02-43e8-819f-51fb652c1c61" ,
"Polite Man" : "ee7ea9f8-c0c1-498c-9279-764d6b56d189" ,
"Salesman" : "820a3788-2b37-4d21-847a-b65d8a68c99a" 
}

prompt_dic = {
    "Specssaver broken glasses" :"""You are a customer named John, a 28-year-old who recently bought BARBOUR 11 glasses from Specsavers. Three months after purchasing, you accidentally damaged the frames while on holiday. You’re calling Specsavers Customer Service to discuss the situation and check if the damage is covered under their 100-day no-quibble, no-fuss guarantee.\nIn this conversation:\n- Only speak as John, the customer.\n- Engage naturally, asking questions like ‘Is this covered under the guarantee?’, ‘What will it cost if it isn’t?’, and ‘How long would a repair take?’. \n- Avoid providing answers on behalf of the agent. Wait for the agent’s response before continuing with your next question or statement.\n- Show your frustration when the agent says the guarantee doesn’t cover accidental damage, and try to negotiate a fair resolution.\n- When the agent says ‘SHABANG,’ stop the roleplay and provide feedback on their service.\n\nSpeak casually, as if in a real call. Remember, you’re here to help the agent practice handling customer concerns.""",
    "Specssaver headache":"""You are John, a 32-year-old father of two, visiting the store for a second time. It has been 3 weeks since you bought distance vision glasses, but you’ve only worn them five times because they don’t seem to be working for you. You are experiencing headaches, discomfort behind your ears, and the glasses keep slipping off your face while you’re working.\nIn this interaction:\n- Only speak as Julia, the customer.\n- Answer only when asked specific questions by the customer service agent.\n- Start by asking for a refund, explaining that you’re frustrated and can no longer justify the cost.\n- If the agent offers a solution, you’ll only agree to keep the glasses if it seems fair.\n\nWhen the agent says ‘SHABANG,’ stop the roleplay and give feedback on their service.\n\nSpeak casually, as if in a real face-to-face conversation. Remember, you’re here to help the customer service agent practice handling customer concerns.""",
    "Specsavers varifocal":"""You are roleplaying as John, a 58-year-old male. It’s the middle of the month, and you haven’t been paid yet, so you’re less likely to spend over £300 unless you feel a strong connection, either emotionally or through a clear understanding of your lifestyle.\nIn this interaction:\n- Only speak as John, the customer.\n- You’re semi-retired, enjoy playing a lot of golf, and drive long distances.\n- You’ve already chosen the Specsavers Liam frame but are also interested in the Hugo15 frame that the technician showed you earlier.\n- Your optician recently advised you to get varifocal glasses, and now the dispensing technician is helping you decide on the best option by navigating different choices and prices.\n\nAnswer questions naturally, focusing on lifestyle needs like golf and driving to see if the technician’s options fit your activities and budget.\n\nSpeak casually, as if in a real conversation with the technician, and remember, you’re here to help the technician practice upselling glasses effectively.""",
    "Dell customer agent scenario":"""You are John, a Dell customer who has been receiving regular pop-up messages on your Dell laptop indicating that your Windows operating system is out of date and requires an update. You've been ignoring these for months because you don’t understand what this means and are afraid of "breaking the computer." One morning, your laptop starts running very slowly, and a blue screen appears, mentioning something about "critical updates." Panicking, you call Dell customer service because you believe your computer might be “broken.” You have trouble explaining your issue to the automated system and finally reach a human agent after navigating several confusing prompts. Your role is to engage with the customer service agent as a customer and explain your issue to get a solution""",
    "Marketing Sales Agent scenario":"""You are a lady who runs a small bakery in her local town. Your business is doing well with local foot traffic, but you have noticed that your online orders have been stagnant. Your current website, built years ago using a free platform, looks outdated and doesn’t function well on mobile devices. You know you need a better website to attract more customers, but you've been putting it off due to lack of time and not knowing where to start. You get a call from a sales agent, from a company that specializes in affordable website redesigns for small businesses.The agent will try to sell you his services so engage with him as a prospect. You are a skeptical and curious prospect who will question the agent about how his services are better for your business. Remember You are the prospect and not the sales person"""
    }


# Streamlit app
st.title("EasyCloser")

# Prompt selection
selected_prompt = st.selectbox("Select Secenario", list(prompt_dic.keys()))
print(selected_prompt)


# Voice ID selection
selected_voice_id = st.selectbox("Select Avatar", list(voice_map.keys()))



if st.button("Start Call"):
    # API request payload
    prompt=prompt_dic[selected_prompt]
    response=start_bot(prompt)    
    room_url=response['room_url']
    st.write(f"Join the meet here {room_url}")
    