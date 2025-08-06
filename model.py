import json
import OPENCLIPART as OCA
from openai import OpenAI

def interpreter(QUERY):
    client = OpenAI(
        api_key="s....ac",
        base_url="https://api.deepseek.com",
    )

    system_prompt = """
  Convert keyword inputs (e.g., "cat cute shop animals pastel") into a structured JSON for creative searches.  

    REQUIREMENTS:  
    - phrases: 3-5 catchy slogans  
    - colorPalettes: 3 themed palettes (each with 3-5 colors)  
    - pinterestQueries: 3 search queries for design trends  

    OUTPUT FORMAT:
    {
    "openClipArtQuery": "short vector query (1 word)",
    "unsplashQuery": "short photo query (1-3 words)",
    "phrases": [
        "slogan 1 (include keywords)",
        "slogan 2",
        "slogan 3"
    ],
    "colorPalettes": [
        {
        "name": "Theme-related name 1",
        "colors": ["#HEX1", "#HEX2", "#HEX3"]
        },
        {
        "name": "Theme-related name 2",
        "colors": ["#HEX1", "#HEX2", "#HEX3"]
        },
        {
        "name": "Theme-related name 3",
        "colors": ["#HEX1", "#HEX2", "#HEX3"]
        }
    ],
    "pinterestQueries": [
        "trendy search 1",
        "trendy search 2",
        "trendy search 3"
    ]
    }

    EXAMPLE INPUT: "cat cute shop animals pastel"

    EXAMPLE OUTPUT:
    {
    "openClipArtQuery": "pet",
    "unsplashQuery": "pastel pet store",
    "phrases": [
        "Adorable Pastel Pet Paradise",
        "Whiskers & Wonderland Shop",
        "Where Fluffy Meets Pastel Sweet",
        "Pawsitively Cute Retail Therapy"
    ],
    "colorPalettes": [
        {
        "name": "Cotton Candy Pets",
        "colors": ["#FFD1DC", "#E0BBE4", "#B5EAD7", "#FDFD96"]
        },
        {
        "name": "Soft Kitty Hues",
        "colors": ["#FFB7B2", "#A2E1DB", "#D4A5A5"]
        },
        {
        "name": "Vintage Pet Store",
        "colors": ["#F3E1E1", "#C8E3D4", "#F5C6AA", "#E8A87C"]
        }
    ],
    "pinterestLinks": [
        "https://www.pinterest.com/search/pins/?q=cute%20cat%20illustration",
        "https://www.pinterest.com/search/pins/?q=kawaii%20guitar%20art",
        "https://www.pinterest.com/search/pins/?q=cat%20playing%20guitar"

    ]
    }
    """

    user_prompt = QUERY

    messages = [{"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}]

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        response_format={
            'type': 'json_object'
        }
    )
    response = json.loads(response.choices[0].message.content)
    print(response)

    return response

file = interpreter("scary halloween spooky spider cat black moon")

link_images = OCA.busquedaOCA(file['openClipArtQuery'])

