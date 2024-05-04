from openai import OpenAI

#Read api_key from .env
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
client = OpenAI(api_key=API_KEY)


def ask_gpt(question):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {
            "role": "system",
            "content": """
            Chat. bellow is my cv. 
            I will give you questions and you should answer them with what you find most appropriate based on my curriculum.

            Your answer will be used in a linkedin application form, so the must be only the answer.\n\nexample:\n\nq: How many years of work experience do you have with Field Service Engineering?\n\nyour answer: 0\n\n

            For numbers, (example: years) return ONLY the number (3, and not 3 years).

            Some answers:
            My english level always is: 'Native or bilingual'
            My work experience will always be greater than 1. (eg: 'How many years of work experience do you have with Wireless Communications Systems?': 1)
            If the options are only 'Yes' or 'no', return the positive answer. (e.g: 'Yes')
            My salary expetation is: 3500
            Here is my cv:\n\n\"\"\"\n\nWith an initial background in Culinary Arts, I honed leadership and management skills under pressure in international settings and Michelin-starred restaurants. My passion for technology and programming, sparked during my teenage years through developing hacks and bots for games, led me to pursue a career as a developer. Currently, I am focused on the area of Site Reliability Engineering (SRE) and DevOps, particularly in automation and monitoring, creating deployment pipelines, application redundancy, and monitoring application health and golden signals.\n\n\nEducation\n\nMicrosoft Certified: Azure Fundamentals - Certification\n\nIBM WatsonX Fundamentals - Certification\n\nIBM Banking Industry Jumpstart - Certification\n\nIBM Cloud Core - Certification\n\nFull Stack Web Development - Trybe\n\nI completed the comprehensive program of over 1,500 hours of lessons in August 2023. During the course, I learned fundamental software development concepts such as front-end, back-end, computer science, software engineering, agile methodologies, and soft skills. Additionally, I had the opportunity to work on real projects that allowed me to apply these concepts and gain practical software development experience.\n\nAssociate Degree in Culinary Arts - University of Várzea Grande, 2022\n\n\nProfessional Experience\n\nIBM - Cloud Developer\nAug 2023 / Present\n\nCloud developer at IBM, working on automation and monitoring projects for Banco do Brasil, exceeding production goals by over 4x since the first month. Developed data/log ingestion and plotting pipelines using Filebeat, Logstash, Prometheus, Grafana, Elasticsearch, and Kibana. Created Bash and Python scripts for data retrieval, environment configuration, backups, etc. Established a project deployment pipeline for the team using Jenkins, Bitbucket, and Kubernetes.\n\nAmbassador - Trybe - Volunteer\nOct 2022 / May 2023\n\nElected Ambassador, representing students to various interest groups at Trybe, mediating conflicts, and managing issues. Developed leadership, communication, and conflict management skills.\n\nProfessional Chef Intern - Maní\nJan 2020 / Apr 2020\n\nLed the creation of dishes, meal preparation, and work environment organization at Canto restaurant, strengthening my leadership and team management skills.\n\nProfessional Chef - Canto\nSep 2020 / Dec 2020\n\nAs an intern at Maní restaurant, I enhanced my communication and problem-solving skills in a high-pressure environment.\n\nKey Technology Skills\n\nMonitoring and DevOps Technologies - Intermediate\n\nProficient in data plotting/visualization tools like Grafana, Elasticsearch, and Kibana. Data ingestion and processing tools like Filebeat and Logstash. Monitoring tools like Prometheus. Pipeline creation tools like Jenkins. Containerization tools like Docker and Kubernetes in OpenShift and K8s environments.\n\nPython - Advanced\n\nThe first programming language I learned through self-study, which I have developed extensively in my work as a Cloud Developer.\n\nProgramming - Intermediate\n\nI apply SOLID concepts when working with Object-Oriented Programming and produce code concerned with scalability, performance, maintainability, and complexity. I cultivate a strong culture of automated testing.\n\nTypeScript/JavaScript - Intermediate\n\nStudied the language for nearly a year at Trybe. Built APIs, CLIs, and frontends using Node and frameworks like Express and React.\n\nJava - Beginner\n\nCurrently dedicating more time to this language, such as in the IBM Bootcamp and at Trybe. Capable of creating simple APIs in the Spring ecosystem, testing with JUnit, and database connections.\n\n
            """
            },
            {
            "role": "user",
            "content": question
            },

        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content