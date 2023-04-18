# AnalystGPT

I built a GPT4 chatbot, to take a deeper look at LLMs and GPTs.  

AnalystGPT is an advanced conversational AI agent (i.e., a chatbot) that leverages the capabilities of <a href="https://platform.openai.com/docs/models/gpt-3-5" target="_blank">text-davinci-003</a> and <a href="https://platform.openai.com/docs/models/gpt-4" target="_blank">GPT4</a> architectures. My objective is to harness the potential of AnalystGPT in performing tasks typically executed by an analyst and to assess the extent of its analytical proficiency. I will explore use of various strategies, such as zero-shot, few-shot, Chain-of-Thought, and automatic prompt configurations, to optimize the prompt and evaluate the AI's performance. Additionally, I aim to investigate the integration of large language models (LLMs) and GPT-based models into UX and workflow. To examine the capabilities of AnalystGPT, pose a question below:</p>

It is hosted as a web application using a Flask framework for the webapp backend, a modular Blueprint structure, and a combination of HTML, CSS, and JavaScript for the frontend. The application utilizes the __[OpenAI Python Library](https://pypi.org/project/openai/)__ to interact with the GPT-4 model, generating text completions based on user input. The application is containerized with Docker and currently deployed as a Cloud Run service on GCP. I will move it to its own domain, www.analyst-gpt.com, and upgrade the deployment to GKE/nginix to improve performance.  I will probably re-write the UXUI with React JS to obtain a more intuitive analyst experience.

# Current setup

Flask app: A lightweight Flask web application framework in Python is used to build the backend of the AnalystGPT webapp. It handles incoming requests, processes them, and returns the desired output to the user.

Blueprint structure: The webapp is organized using Flask's Blueprint, which allows for a modular and scalable structure. This helps separate different parts of the application and makes the code more maintainable.

CSS and HTML: The frontend of the webapp is built using HTML and styled with CSS. 

JavaScript: is used to make the frontend more interactive and dynamic, enabling client-side processing, and providing a better user experience. It currently handles user input, form submissions, and communication with the backend.

UX/UI concepts: include designing an intuitive layout, user-friendly navigation, and clear presentation of information. I have kept things clean and minimal.

completions.py: Python module containing the functions that interact with the OpenAI library to generate responses using the text-davinci-003 and GPT-4 models. It handles requests to the OpenAI API to obtain the desired output based on user input.

OpenAI library: The the __[OpenAI Python Library](https://pypi.org/project/openai/)__ is a Python package that provides an interface to interact with the OpenAI API, enabling access to the GPT-4 model for generating text completions.

Deployment: The application is containerized with Docker and currently deployed as a Cloud Run service on GCP.
