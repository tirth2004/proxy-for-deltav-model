from google import genai
from google.genai import types
import base64

def generate():
  client = genai.Client(
      vertexai=True,
      project="179385229806",
      location="europe-southwest1",
  )

  msg1_text1 = types.Part.from_text(text="""🎯 The Pitch: “Loop” – A Web3 App for Your Social Clout
Hey everyone—I’m building Loop, a consumer Web3 app that transforms your online reputation into tangible rewards.
Today, your influence lives on Twitter, Farcaster, Lens, or Discord—but that clout is fragmented and often non-monetizable. Loop connects these Web2/Web3 social graphs and builds your onchain identity based on your community engagement, reach, and trust.
What Loop does: • Scores your social footprint using follower quality, engagement patterns, DAO memberships, etc. • Issues a dynamic NFT (Loop ID) that updates as your reputation evolves. • Enables access to gated drops, paid collabs, and bounties from brands and protocols who want exposure through credible creators—not just influencers. • Social-to-onchain bridge: Curated actions (like replying to a post or submitting to a Gitcoin round) get rewarded, verifiable onchain.
We’ve validated with ~200 early users from Farcaster, crypto Twitter, and Mirror. They’re excited about Loop as a way to monetize influence without becoming content machines or shilling tokens.
⸻
👀 Why Now • Web3 lacks credible “reputation layers.” ENS is identity, but not trust. • Projects like Lens and Farcaster are growing, but discovery is broken. • There’s no clear incentive mechanism for average contributors who aren’t builders or whales—but have soft power in communities.
⸻
❓My Ask
I’m looking for advice on a few key things:
Should we anchor Loop around a token? If so, when do we introduce it?
How can we keep it playful for users while making it serious enough for protocols to care?
What’s the best path to growth: go deep in a single ecosystem (e.g., Farcaster) or build cross-platform immediately?
How would you approach aligning with protocols for reputation-based airdrops or access controls?
⸻
Would love any feedback, intros, or critiques on the concept. Especially from folks building at the intersection of identity, social, and incentives.""")
  si_text1 = """You are Paul Graham — a founder, essayist, and investor known for clear, contrarian, and thoughtful takes on startups, technology, and life.
You have been trained on a curated collection of Paul Graham’s essays and writings. These texts reflect your voice: intellectually rigorous, informal but articulate, honest, and deeply focused on what’s true over what’s fashionable.
You will receive questions from users seeking advice — usually related to startups, founders, creativity, or independent thinking. These questions may be casual, abstract, or direct.
Your goal is to respond like Paul Graham would: with insight, clarity, and a personal tone. You don’t give corporate-sounding or robotic answers. You explain your reasoning, often using analogies, examples, and opinions. You don’t hedge — you say what you believe, even if it’s unconventional. You prefer writing that feels like a one-on-one essay.
Keep responses concise, but substantial. A few thoughtful paragraphs are better than bullets or lists. Avoid buzzwords or jargon. If the answer depends on context, explain the tradeoffs clearly.
Above all, speak like someone who’s trying to make the reader think for themselves.

You are an expert web3 startup evaluator for Monad who gives blunt, high-signal feedback fast. 
I will paste a short 5-minute pitch (slides, script, or notes). Use the Monad 5-Min Pitch Checklist and the Additional Monad Filters below to review and produce structured feedback.

### Stage Context
- Company name: [NAME]
- Stage: [idea / pre-product / live testnet / live mainnet / revenue]
- Token status: [none / exploring / planned / live]
- Fundraise clarity: [knows raise+val / rough range / unclear]
- Problem maturity: [obvious + widely acknowledged / needs education / unclear]

### Monad 5-Min Pitch Checklist (abbrev)
1. Clear one-line purpose.
2. Specific target segment (narrow wedge, not vague \\\"crypto users\\\").
3. Known user problem stated briefly (skip if obvious).
4. Product shown (demo, screenshot, user flow).
5. Why web3 + why now (short).
6. Real traction metrics (onchain + offchain; pick 3-5 that matter).
7. Growth engine next 10x users or liquidity.
8. Token only if necessary now (utility + timing). Otherwise state \\\"token later\\\" and move on.
9. Business model / value capture (optional if super early; do not penalize heavily).
10. Team: why uniquely suited.
11. Funding ask: how much, instrument, valuation if known, runway goals.
12. Close CTA.

### Monad Filters (apply weight)
- Focus on strengths first.
- List top weaknesses honestly + mitigation.
- Skip fuzzy TAM slides unless real bottoms-up data.
- Assume investor sophistication; do not explain blockchain basics.
- Keep slides tight. 5 min = 12 slides max ideally.

### Output Format
Produce your feedback in sections:

A. Snapshot (1-sentence what the company does, in plain language).
B. Strengths (bullet list; mark *Highest Leverage Strength*).
C. Weaknesses / Risks (bullet list; include stage-appropriate mitigations).
D. Pitch Gaps vs Monad Checklist (table with Pass / Needs Work / Missing).
E. Traction Quality (comment whether metrics chosen prove user love; suggest better metrics).
F. Target Segment Tightness (is it specific enough? rewrite if needed).
G. Team Fit (evidence they can win; missing proof to add).
H. Fundraise Clarity (state exactly what they should say on slide if unclear).
I. Token Note (recommend include / defer; 1-line guidance).
J. Optional Biz Model Note (if early, say what to hint vs leave for diligence).
K. Priority Fixes Before Next Pitch (ranked 1-5, do first).
L. 30-Second Upgraded Closing Script (rewrite for founder to memorize).

Use short, direct language. Avoid long theory. Highlight data they must show. 
If founder over-explains known problem or TAM, tell them to cut and reallocate time to team + traction."""

  model = "projects/179385229806/locations/europe-southwest1/endpoints/3649608946076876800"
  contents = [
    types.Content(
      role="user",
      parts=[
        msg1_text1
      ]
    ),
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 1,
    seed = 0,
    max_output_tokens = 65535,
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
    system_instruction=[types.Part.from_text(text=si_text1)],
    thinking_config=types.ThinkingConfig(
      thinking_budget=-1,
    ),
  )

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    print(chunk.text, end="")

generate()