# AI-based FAQ system for digital marketers

from transformers import pipeline

qa_pipeline = pipeline('question-answering')

def get_faq_response(question):
    faq_data = {
        "How do I improve my ad performance?": "You can improve ad performance by optimizing your targeting, using A/B testing, and improving your ad creative.",
    "What is digital marketing?": "Digital marketing refers to the use of digital channels, such as search engines, social media, email, and websites, to promote products or services.",
    "What is SEO and why is it important?": "SEO, or Search Engine Optimization, is the practice of optimizing your website to rank higher in search engine results, which can increase organic traffic and visibility.",
    "How can I increase website traffic?": "You can increase website traffic by implementing SEO strategies, running paid advertising campaigns, using social media marketing, and creating engaging content.",
    "What is PPC advertising?": "PPC, or Pay-Per-Click advertising, is a form of online advertising where you pay a fee each time your ad is clicked. It’s commonly used in search engine ads and social media ads.",
    "How can I use social media for marketing?": "Social media marketing involves creating and sharing content on social media platforms to engage with your audience, build brand awareness, and drive website traffic.",
    "What is the difference between organic and paid search?": "Organic search refers to unpaid listings that appear in search engine results based on relevance, while paid search involves paying for ads to appear in search engine results.",
    "How do I measure the success of a digital marketing campaign?": "You can measure success through key metrics such as website traffic, conversion rates, ROI, click-through rates (CTR), and engagement on social media platforms.",
    "What are the best platforms for digital marketing?": "The best platforms for digital marketing include Google Ads, Facebook, Instagram, LinkedIn, Twitter, and email marketing platforms like Mailchimp.",
    "What is email marketing and how can it benefit my business?": "Email marketing involves sending promotional messages to your audience via email. It helps nurture leads, increase customer engagement, and drive sales."
    }
    if question in faq_data:
        return faq_data[question]
    
    answer = qa_pipeline({'question': question, 'context': "Digital marketing FAQ data."})
    return answer['answer']
