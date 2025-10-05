from flask import Blueprint, render_template, request, jsonify
from .openai_client import OpenAIClient

bp = Blueprint("main", __name__)
client = OpenAIClient()


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json(force=True)
    prompt = data.get("prompt", "").strip()
    content_type = data.get("content_type", "marketing")
    length = int(data.get("length", 300))
    temperature = float(data.get("temperature", 0.7))

    if not prompt:
        return jsonify({"error": "Prompt is required."}), 400

    final_prompt = build_prompt(prompt, content_type, length)

    res = client.generate(final_prompt, max_tokens=length, temperature=temperature)

    if "error" in res:
        return jsonify({"error": res["error"]}), 500

    return jsonify({"result": res["text"], "meta": res.get("meta", {})})


def build_prompt(user_prompt: str, content_type: str, length: int) -> str:
    templates = {
        "marketing": (
            "You are an expert marketing copywriter. Produce persuasive marketing copy"
            " based on the user input. Keep it concise and include a call-to-action.\n\n"
        ),
        "blog": (
            "You are an expert content writer. Produce a blog post outline and a 2-3 paragraph introduction"
            " based on the user input. Include headings and suggested meta description.\n\n"
        ),
        "social": (
            "You are a social media manager. Produce 3 short social captions with emoji and hashtags"
            " tailored to the user input. Provide variations for tone: friendly, bold, and professional.\n\n"
        ),
    }

    template = templates.get(content_type, templates["marketing"])

    return f"{template}Input: {user_prompt}\n\nLength target (tokens): {length}\n"
