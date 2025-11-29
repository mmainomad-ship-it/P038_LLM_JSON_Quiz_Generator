# STEP 1: Imports & Configuration
import json  # Import the built-in JSON library for parsing LLM output
import ollama  # Import the ollama client for connecting to the local LLM

# STEP 2: Data/Input Preparation (Updated with validation loop)
# Loop until the user provides a non-empty topic
while True:
    topic = input(
        "Enter a topic for the quiz (e.g., 'The French Revolution'): "
    ).strip()
    if topic:
        break
    print("Topic cannot be empty. Please enter a subject.")

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

# STEP 6: File Saving Logic (Modifies the existing 'else' block)
else:
    # Use the topic to create a clean filename
    filename = topic.lower().replace(" ", "_").strip() + "_quiz.json"

    # Write the Python dictionary object directly to a file as JSON
    with open(filename, "w") as f:
        json.dump(quiz_json, f, indent=4)

    # Print success messages
    print("\n✅ Successfully generated and parsed Quiz data!")
    print(f"Question 1: {quiz_json['quiz'][0]['question']}")
    print(f"💾 Quiz saved to: {filename}")
