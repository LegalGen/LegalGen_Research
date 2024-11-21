import openai

openai.api_key = "YOUR_API_KEY"

def segment_text(text, max_tokens=4000):
    segments = []
    current_segment = []
    current_token_count = 0

    sentences = text.split('.')

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        token_count = len(sentence.split())

        if current_token_count + token_count > max_tokens:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an assistant for analyzing legal documents. "
                            "Determine if the following sentence represents a semantic breakpoint:"
                        )
                    },
                    {
                        "role": "user",
                        "content": f"Sentence: \"{sentence}\". Answer 'Yes' or 'No'."
                    }
                ],
                max_tokens=10
            )
            is_breakpoint = "Yes" in response["choices"][0]["message"]["content"].strip()

            if is_breakpoint:
                segments.append(' '.join(current_segment))
                current_segment = []
                current_token_count = 0

        current_segment.append(sentence)
        current_token_count += token_count

    if current_segment:
        segments.append(' '.join(current_segment))
    
    return segments

if __name__ == "__main__":
    example_text = """
    This is a sample legal agreement that covers various financial terms and conditions. 
    It includes clauses about payment, termination, and other legal obligations. 
    The agreement must adhere to Section 409A and other regulatory requirements.
    """
    
    segments = segment_text(example_text)

    for idx, segment in enumerate(segments, 1):
        print(f"Segment {idx}:\n{segment}\n")
