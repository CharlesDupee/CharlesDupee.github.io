# Create PR 2: Demote Qwen to rotational
import subprocess, json, urllib.request

token = subprocess.run(["gh", "auth", "token", "--user", "CharlesDupee"], capture_output=True, text=True).stdout.strip()

payload = json.dumps({
    "title": "rotate(ai-lab): demote Qwen3.5-122B to previously primary, now rotational",
    "head": "demote-qwen-rotational",
    "base": "main",
    "body": (
        "Demotes Qwen3.5-122B from 'primary' (emerald) to 'previously primary, "
        "still in rotation via vLLM' (amber), reflecting that DeepSeek V4 Flash "
        "is now the primary serving model.\n\n"
        "- Qwen: green -> amber with updated status\n"
        "- Explanatory paragraph rewritten: DSv4 Flash is primary, Qwen is rotation\n"
        "- Visual: Green -> Yellow"
    )
})

req = urllib.request.Request(
    "https://api.github.com/repos/CharlesDupee/CharlesDupee.github.io/pulls",
    data=payload.encode(),
    headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
    },
    method="POST"
)

with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    print("PR 2:", result["html_url"])
