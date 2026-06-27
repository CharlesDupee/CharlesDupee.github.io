TOKEN=$(gh auth token --user CharlesDupee)
curl -s -H "Authorization: Bearer *** \
  -H "Accept: application/vnd.github+json" \
  -X POST \
  "https://api.github.com/repos/CharlesDupee/CharlesDupee.github.io/pulls" \
  --data @pr1_payload.json | python3 -c "
import sys, json
d = json.load(sys.stdin)
print(d.get('html_url', json.dumps(d, indent=2)))
"