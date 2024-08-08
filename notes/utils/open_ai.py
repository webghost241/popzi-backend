import openai
from django.conf import settings
import logging

logger = logging.getLogger(__name__)
# Assuming Django settings are used and OPENAI_KEY is set in your settings.py file
openai.api_key = settings.OPKEY

def query_openai(prompt):
    try:
        print(prompt)
        response = openai.chat.completions.create(
            model="gpt-4-turbo-preview",
            temperature=0.7,
            max_tokens=4096,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            messages=[
                {"role": "system", "content": "You are an helpful assistant."},
                {"role": "user", "content": f"""You are tasked with generating AI multiple-choice questions from educational content, leveraging your expertise in natural language processing and education technology. Your objective is to create questions that are clear, concise, and directly related to the key concepts presented in the notes provided.

Project Specifications for 'Poppy':

Generate five multiple-choice questions, each with 3-5 options, derived from the students' selected notes. Following the selection of an answer, provide a succinct explanation that justifies its correctness or identifies its inaccuracies. Reward users with points for correct answers, which can be exchanged for gift cards to encourage consistent study habits.

Content for Question Generation:

Notes Title: __
Notes Content: f{prompt}

Guidelines for Effective Question Generation:

Ensure each question directly relates to and covers the main ideas within the content provided.
Employ straightforward and understandable language to avoid confusion.
Craft the correct answer to be challenging yet distinguishable from incorrect options without ambiguity.
Offer clear explanations for the correct answer.
Provide individualized feedback for each incorrect option, avoiding the combination of similar incorrect choices.
Aim to make questions engaging and educational, enhancing the learning experience.
Structure the output as follows for each question, adhering to the specific format and markers:

QUESTIONSTART
...(Question Text)...
A) Option 1
B) Option 2
C) Option 3
D) Option 4 (if applicable)
E) Option 5 (if applicable)
QUESTIONEND

CORRECTANSWERSTART
...(Correct option, e.g., A) Option 1)...
CORRECTANSWEREND

EXPLANATIONSTART
...(A detailed explanation for why the correct answer is right)...
EXPLANATIONEND

WHYWRONGSTART
Explanation for why each option is incorrect, corresponding with their letters but not including an explanation for the correct choice here.
WHYWRONGEND

Remember, each section should be clearly marked and separated to maintain consistency across all generated questions. No additional explanations or content should be included outside the specified sections."""},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Error querying OpenAI: {e}")
        raise e