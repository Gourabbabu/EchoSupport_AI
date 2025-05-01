from flask import request
from twilio.twiml.voice_response import VoiceResponse
from openai_helper import ask_openai
from github_helper import get_repo_info, list_open_issues

def handle_call():
    user_input = request.values.get("SpeechResult", "")
    
    # GitHub trigger (simple logic)
    if "issues" in user_input.lower():
        issues = list_open_issues()
        if not issues:
            reply = "There are no open issues right now."
        else:
            reply = f"There are {len(issues)} open issues. For example, {issues[0]['title']}"
    elif "repository" in user_input.lower():
        info = get_repo_info()
        reply = f"Repository {info['name']} has {info['stargazers_count']} stars and {info['forks_count']} forks."
    else:
        reply = ask_openai(user_input)

    response = VoiceResponse()
    response.say(reply, voice='Polly.Matthew')  # Use Amazon Polly voices (optional)
    return str(response)
