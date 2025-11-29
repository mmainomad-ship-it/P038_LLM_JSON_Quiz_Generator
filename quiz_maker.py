# STEP 1: Imports & Configuration
import json  # Import the built-in JSON library for parsing LLM output
import ollama  # Import the ollama client for connecting to the local LLM

# STEP 2: Data/Input Preparation
# Prompt the user to enter a topic for the quiz
topic = input("Enter a topic for the quiz (e.g., 'The French Revolution'): ")
print(f"Generating quiz for topic: '{topic}'... Please wait.")


# STEP 3: Function Definition (Header only)
def generate_quiz(topic):
    # This function will communicate with Ollama and return a JSON object
    pass

    # STEP 4: Core Logic/API Call (Body)
    # Define strict JSON instructions
    system_prompt = "Output ONLY raw JSON. Format: { 'quiz': [ { 'question': str, 'options': [str, str, str, str], 'answer': str } ] }"

    # Call the model
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Generate 5 questions about {topic}"},
        ],
    )

    return response["message"]["content"]  # Return the raw string


try:
    # STEP 5 (Part 1): Get raw response and attempt to parse
    raw_response = generate_quiz(topic)
    quiz_json = json.loads(raw_response)

except json.JSONDecodeError:
    # STEP 5 (Part 3): This runs ONLY if the JSON parsing fails
    print("\n❌ ERROR: LLM failed to output valid JSON.")
    print("Raw Output (for debugging): \n" + raw_response)

else:
    # STEP 5 (Part 2): This runs ONLY if the JSON parsing succeeds
    print("\n✅ Successfully generated and parsed Quiz data:")
    # Print the first question to confirm data integrity
    print(f"Question 1: {quiz_json['quiz'][0]['question']}")
    print("-" * 30)
    print("All questions:", [item["question"] for item in quiz_json["quiz"]])
