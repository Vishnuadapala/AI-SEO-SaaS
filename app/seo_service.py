import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_seo_content(topic):

    prompt = f"""
Generate SEO optimized content about {topic}.

Return the response in EXACT format:

SEO_TITLE:
<only title>

META_DESCRIPTION:
<only meta description>

KEYWORDS:
<10 comma separated keywords>

BLOG_OUTLINE:
<structured outline>

FAQ:
<5 FAQs>

FULL_BLOG:
<complete blog article>
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        text = response.text

        # 🔥 SECTION SPLIT LOGIC
        sections = {
            "title": "",
            "meta": "",
            "keywords": "",
            "outline": "",
            "faq": "",
            "blog": ""
        }

        current = None

        for line in text.splitlines():
            line = line.strip()

            if line == "SEO_TITLE:":
                current = "title"
            elif line == "META_DESCRIPTION:":
                current = "meta"
            elif line == "KEYWORDS:":
                current = "keywords"
            elif line == "BLOG_OUTLINE:":
                current = "outline"
            elif line == "FAQ:":
                current = "faq"
            elif line == "FULL_BLOG:":
                current = "blog"
            elif current:
                sections[current] += line + "\n"

        return sections

    except Exception as e:
        return {"title": "", "meta": "", "keywords": "", 
                "outline": "", "faq": "", "blog": f"Error: {str(e)}"}