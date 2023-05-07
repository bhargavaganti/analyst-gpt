# Analyst-GPT

### Summary
AnalystGPT is a versatile AI-powered analysis tool that generates comprehensive reports in various domains such as business, investigation, and finance. The application leverages the state-of-the-art GPT-4 language model from OpenAI to generate tailored reports based on user inputs.

### Features
1. AI-powered analysis using the GPT-4 language model
2. Support for multiple report types (business, investigation, finance)
3. Asynchronous data fetching using the JavaScript fetch API
4. Structured report display on the webpage
5. PDF report generation with custom formatting
6. Responsive design for optimal user experience across devices

### Usage
To use AnalystGPT:

1. Choose a report type (business, investigation, finance) by clicking on the corresponding button.
2. Enter your query in the input field and click the "Submit" button.
3. Wait for the AI-generated report to appear on the webpage.
4. Optionally, click the "Download PDF" button to download the report as a PDF file.

### User Interface
The UI of AnalystGPT is built using HTML, CSS, and JavaScript. Users can choose from three different types of reports (business, investigation, and finance) and submit their queries. The interface includes a spinner animation to indicate the processing time while the AI generates the report.

### AI-powered Analysis
AnalystGPT employs GPT-4, the current state-of-the-art language model from OpenAI, to generate comprehensive reports based on user queries. Users can expect relevant and accurate information tailored to their specific requirements.

### Asynchronous Data Fetching
The application leverages the JavaScript fetch API to communicate with the server and retrieve report data. The implementation uses async/await to handle asynchronous requests, ensuring a smooth user experience.

### Report Display and Download
Once the AI has generated the report, it is displayed in a structured format on the webpage. Users can also download the report as a PDF file with a custom format based on the chosen report type. The PDF generation is powered by the pdf-lib library, which provides a flexible and efficient way to create, modify, and save PDF files in the browser.

### Responsive Design
AnalystGPT uses a responsive design that ensures the application looks and functions well on different devices and screen sizes. The CSS styling, in particular, adapts to different viewports, providing an optimal user experience across devices.

### Technologies Used
1. GPT-4: OpenAI's current state-of-the-art language model for report generation
2. HTML, CSS, and JavaScript: Frontend development
3. pdf-lib: PDF report generation and manipulation in the browser
4. Fetch API: Asynchronous data fetching and communication with the server

### Deployment
AnalystGPT is deployed on a Google Kubernetes Engine (GKE) cluster with three nodes, each running Kubernetes. The cluster leverages Nginx Ingress controller to route external traffic to the application.

The application is deployed using a Deployment resource, with its container image pulled from Google Artifact Registry. The Deployment specifies resource requests and limits, as well as required environment variables such as the OpenAI API key, which is obtained from a Kubernetes Secret resource. The application is exposed on port 8080 via a NodePort Service resource.

To secure the application, Cert-Manager is installed to manage SSL certificates. The certificate issuer, Let's Encrypt, is configured using an Issuer resource, specifying the ACME server, email, and privateKeySecretRef along with the http01 solver for domain validation.

An Ingress resource is created to route traffic to the service, using an allocated static IP address, and hosting both analyst-gpt.com and www.analyst-gpt.com domains. TLS termination is configured using a Certificate resource, which is issued by Let's Encrypt and managed by cert-manager, ensuring HTTPS for all connections.

### License
AnalystGPT is released under the MIT License.