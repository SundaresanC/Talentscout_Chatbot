def get_intro_prompt():
    return (
        "👋 Welcome to TalentScout – your smart hiring assistant!\n\n"
        "We'll collect some basic info and generate personalized technical questions "
        "based on your experience and tech stack.\n\nClick **Start** to begin."
    )

def tech_question_prompt(tech_stack):
    return (
        f"You are an AI hiring assistant. Based on the following tech stack: {tech_stack}, "
        f"generate 5 tailored technical interview questions suitable for a job candidate."
    )
