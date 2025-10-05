# AI Content Generator

A Flask web application that leverages OpenAI's API to generate various types of content including marketing, blog posts, and social media captions.

## Features

- 🚀 Generate marketing content with persuasive call-to-actions
- 📝 Create blog post outlines with meta descriptions
- 💬 Generate social media captions with emojis and hashtags
- 🎨 Adjustable creativity and length settings
- 🎯 Real-time content generation

## Setup

1. Clone the repository
2. Install dependencies:
```sh
pip install -r requirements.txt
```

3. Configure environment variables:
```sh
cp .env.example .env
# Add your OpenAI API key and Secret key to .env
```

4. Run the application:
```sh
python run.py
```

## Docker Support

Build and run with Docker Compose:
```sh
docker-compose up --build
```

## Technologies

- Flask
- OpenAI API
- TailwindCSS
- Python 3.11+

## License

MIT
