#!/usr/bin/env bash
# Create PR 1
PAYLOAD='{"title":"promote(ai-lab): DeepSeek V4 Fast → Flash as production primary model","head":"promote-dsv4-flash","base":"main","body":"Promotes DeepSeek V4 from almost prod ready (amber) to production primary model (emerald).\n\n- Renames V4 Fast to V4 Flash (correct model branding)\n- Changes status from amber almost prod ready to emerald production primary model\n- Visual amber to green"}'

TOKEN="*** auth token --user CharlesDupee)"

curl -s -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -X POST "https://api.github.com/repos/CharlesDupee/CharlesDupee.github.io/pulls" \
  -d "$PAYLOAD" | python3 -c "
import sys, json
d = json.load(sys.stdin)
print(d.get('html_url', json.dumps(d, indent=2)))
"