# Create PR 1: Promote DeepSeek V4 Flash
import subprocess, json, urllib.request

token = subprocess.run(["gh", "auth", "token", "--user", "CharlesDupee"], capture_output=True, text=True).stdout.strip()

payload = json.dumps({
    "title": "promote(ai-lab): DeepSeek V4 Fast to Flash as production primary model",
    "head": "promote-dsv4-flash",
    "base": "main",
    "body": (
        "Promotes DeepSeek V4 from 'almost prod ready' (amber) "
        "to 'production — primary model' (emerald).\n\n"
        "- Renames V4 Fast to V4 Flash (correct model branding)\n"
        "- Changes status from amber 'almost prod ready' to emerald "
        "'production — primary model'\n"
        "- Visual: Yellow -> Green"
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
    print("PR 1:", result["html_url"])
