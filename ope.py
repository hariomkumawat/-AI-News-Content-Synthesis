from openai import AzureOpenAI
import os
# import streamlit as st

from dotenv import load_dotenv
load_dotenv()


api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment_name = 'GPT-4-1106'
api_version = '2023-12-01-preview'  # Ensure this matches the correct version

client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}"
)

def openaifunction(prompt):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "you are a good assistent."},
            {"role": "user", "content": [
                {
                    "type": "text",
                    "text": prompt
                }
            ]}
        ],
        max_tokens=2000
    )
    response = response.choices[0].message.content
    return response
    # print(response)





# # Streamlit UI
# def main():
#     st.title("Article Synthesizer")

#     # Text input boxes for user to input articles
#     article1 = st.text_area("Enter Article 1")
#     article2 = st.text_area("Enter Article 2")
#     article3 = st.text_area("Enter Article 3")


    


#     title_prompt=f"""Input Articles:\nArticle 1: {article1}\nArticle 2: {article2}\nArticle 3: {article3}\n\nSynthesize a new article:
#             Please generate a new content article based on the provided input articles. Ensure that the synthesized article:
#             - Incorporates key information from all three input articles.
#             - Maintains a coherent and logical flow of information.
#             - Is original and does not directly copy content from the input articles.
#             - Has a length of at least [desired length] words.
#             - Article length is grater then 650"""

#     # res=openaifunction(title_prompt)

#     if st.button("Synthesize"):
#         if article1.strip() and article2.strip() and article3.strip():
#             synthesized_article = openaifunction(title_prompt)
#             st.subheader("Synthesized Article")
#             st.write(synthesized_article)
#         else:
#             st.error("Please enter all three articles.")

# if __name__ == "__main__":
#     main()
