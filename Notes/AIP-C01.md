Official Practice Question Set AWS Certified Generative AI Developer….md use the attached doc as the official AWS exam practice questions. Let's review each question and answer concept first, summarize the basic concepts/services/tools in under 200 words, plus one ASCII diagram, then a quizz. Dont proceed to the next Q/A until I say proceed. Start from 1/20 Q/A

---

I can see the study guide you attached, but the **actual “Official Practice Question Set (20 Qs)” content isn’t present in the file**—it only references that it exists .

👉 So before we start properly, I need **Question 1 (and its options)** pasted here.

---

## Why this matters (quick alignment)

You want:

- Concept → summary (<200 words)
- ASCII diagram
- Then quiz

That only works if we anchor to a **specific exam-style scenario** (these questions are very architecture-heavy).

---

## Suggestion (so we don’t stall)

While you paste Q1, here’s how we’ll run this efficiently:

For **each question**, I’ll give you:

### 1) Core concept (what AWS is testing)

### 2) Key services/tools (exam shortcuts)

### 3) Mental model (decision rule)

### 4) ASCII architecture

### 5) Mini quiz (1–2 questions to lock it in)

---

Paste **Q1** and we’ll start 👍

Official Practice Question Set: AWS Certified Generative AI Developer - Professional (AIP-C01 - English) 1/20 A cross-functional team is developing a generative AI (GenAI) application by using AWS services. The team needs to optimize developer productivity and enforce consistent integration patterns. The team needs to automate performance tuning and accelerate AI testing across multiple business units. The team wants to use Amazon Q Developer. The team must accelerate development workflows and maintain application quality. Which combination of steps will meet these requirements? (Select TWO.) **A** Use Amazon Q Developer to analyze code for security best practices and suggest compliance improvements. Implement a mandatory review process where all code changes must be manually approved by security teams before integration. Answer choice eliminated Incorrect. Amazon Q Developer can help identify security issues and suggest improvements. However, implementing a mandatory manual approval process for all code changes would create a bottleneck. This approach does not meet the requirements to optimize developer productivity and accelerate development workflows. This approach does not automate performance tuning or accelerate AI testing. This approach could slow down integration across business units. Learn more about ++[how to review code in Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-reviews.html)++. **B** Use Amazon Q Developer to retrospectively analyze and document common integration patterns that are found across different business units' code bases. Answer choice eliminated Incorrect. Using Amazon Q Developer for retrospective analysis and documentation of patterns does not meet the requirements to optimize developer productivity and accelerate development workflows. This reactive approach fails to use the tool's real-time assistance capabilities for code generation, refactoring, and testing. Learn more about ++[best practices for code generation in Amazon Q Developer](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/code-generation.html)++. **C** Configure Amazon Q Developer to automatically generate and refactor integration code snippets, provide targeted API usage guidance, and suggest performance optimizations for AI components. Apply the changes across the modular code base. ## Correct. Amazon Q Developer provides automatic code generation, refactoring, targeted API recommendations, and performance optimization. Comprehensive use of these features can increase productivity and reduce integration errors across business units. Learn more about ++[Amazon Q Developer features](https://aws.amazon.com/q/developer/features/)++. **D** Incorporate Amazon Q Developer to resolve coding issues that are identified during merge requests. Reserve most refactoring and optimization tasks for periodic manual review cycles. Incorrect. This step uses Amazon Q Developer primarily at merge or review stages. This step reserves most code improvements for infrequent manual cycles. Therefore, this step does not optimize the core benefits of Amazon Q Developer. This step can slow down the resolution of code quality and integration issues. Learn more about ++[Amazon Q Developer features](https://aws.amazon.com/q/developer/features/)++. **E** Integrate the Amazon Q Developer automated unit and integration test generation features into the team's CI/CD pipelines. ## Correct. By embedding Amazon Q Developer automated test generation into CI/CD workflows, the team continuously validates both new and existing AI components. This step ensures high velocity, ongoing code quality, and early defect detection. These qualities are critical in large-scale ML deployments. Learn more about ++[how to generate unit tests by using Amazon Q Developer](https://aws.amazon.com/q/developer/features/#test-and-secure)++.

---

Great—this is a **classic “developer productivity + GenAI tooling” question**. Let’s break it cleanly.

---

# ✅ Q1 — Core Concept (what AWS is testing)

### 👉 High-level

This question is about **how Amazon Q Developer fits into the SDLC**.

Think:

> “Where do we inject AI into the developer lifecycle to maximize speed + quality?”

---

# 🧠 Key Concept (under 200 words)

**Amazon Q Developer is an AI coding assistant embedded into the development lifecycle (IDE + CI/CD).**

Its real value is **shift-left + automation**:

- **During coding** → generate code, refactor, suggest APIs, optimize performance
- **During testing** → auto-generate unit/integration tests
- **During operations** → detect issues, improve security

The exam trick:

- ❌ Anything **manual / retrospective / gated** = slows productivity
- ✅ Anything **automated + embedded in workflow** = correct

So:

- **C = shift-left development acceleration**
- **E = continuous testing automation**

Together they cover:  
👉 Build faster + test continuously + scale across teams

This aligns with exam domains:

- Dev productivity
- CI/CD integration
- GenAI-assisted development workflows

---

# 🏗️ Mental Model

Bad (slow, enterprise legacy mindset):  
Dev → Code → Manual review → Fix → Test later  
  
Good (GenAI-native):  
Dev → Q generates/refactors → Auto tests → CI/CD → Deploy

---

# 📊 Architecture (ASCII)

          Developer (IDE)  
                │  
        ┌───────▼────────┐  
        │ Amazon Q Dev   │  
        │ - Code gen     │  
        │ - Refactor     │  
        │ - Perf tuning  │  
        └───────┬────────┘  
                │  
        Source Control (Git)  
                │  
        ┌───────▼────────┐  
        │ CI/CD Pipeline │  
        │ (CodeBuild etc)│  
        └───────┬────────┘  
                │  
     ┌──────────▼──────────┐  
     │ Q Dev Test Gen      │  
     │ - Unit tests        │  
     │ - Integration tests │  
     └──────────┬──────────┘  
                │  
            Deploy

---

# 🎯 Why answers are correct

### ✅ C — “shift-left intelligence”

- Code generation
- API guidance
- Performance tuning  
    👉 This is **core productivity multiplier**

---

### ✅ E — “continuous validation”

- Automated test generation
- Integrated into CI/CD  
    👉 This is **scale + quality enabler**

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|Manual approvals = bottleneck|
|B|Retrospective = no real-time benefit|
|D|Only used at merge stage = too late|

👉 Exam pattern:  
**“Manual / retrospective / delayed” = eliminate**

---

# 🧪 Mini Quiz (lock it in)

### Q1

You want to reduce GenAI app bugs across teams **without slowing devs**. What’s best?

A. Add mandatory architecture review board  
B. Use Q Developer in CI/CD for test generation  
C. Weekly code audit meetings  
D. Central approval team

---

### Q2

Where does Q Developer provide **highest impact**?

A. After deployment  
B. During incident response  
C. During coding + CI/CD  
D. Only during code review

---

Reply with your answers, then say **“proceed”** and we’ll go to Q2.

2/20 Question A company runs a question-answering application. The application uses an Amazon Bedrock knowledge base that ingests documents from multiple Amazon S3 buckets. The company needs to monitor the data ingestion process to identify and troubleshoot any issues with document processing. Which solution will meet these requirements to monitor knowledge base operations? **A** Configure knowledge base logging with Amazon CloudWatch Logs as the destination. Use CloudWatch Logs Insights to query for failed document processing. # Correct. Amazon Bedrock knowledge bases support a built-in logging system that you can configure to send logs to CloudWatch Logs. The logs track the status of files during data ingestion jobs. The jobs show whether the files were successfully ingested, ignored, or failed. You can use CloudWatch Logs Insights to create queries that help identify specific issues. For example, you can query for documents that have the status RESOURCE_IGNORED, EMBEDDING_FAILED, or INDEXING_FAILED. Learn more about ++[how to monitor knowledge bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html)++. **B** Enable Amazon CloudWatch Application Signals to automatically detect and alert on knowledge base performance issues. Incorrect. CloudWatch Application Signals is designed to monitor the performance and health of applications, not knowledge bases. CloudWatch Application Signals does not integrate with Amazon Bedrock knowledge base monitoring. You can use CloudWatch for monitoring. However, CloudWatch Application Signals is not the appropriate feature for the knowledge base ingestion monitoring in this scenario. Learn more about ++[CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html)++. **C** Enable AWS CloudTrail to track all API calls that relate to knowledge base operations and document ingestion activities. Incorrect. CloudTrail can track API calls that are made to Amazon Bedrock. However, CloudTrail does not provide the detailed document-level processing information that you need to troubleshoot ingestion issues. CloudTrail focuses on API activity auditing rather than the status of individual documents being processed. Learn more about ++[how to monitor Amazon Bedrock API calls by using CloudTrail](https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html)++. **D** Implement Amazon Bedrock model invocation logging to capture detailed metrics about document processing and embedding generation. Incorrect. Amazon Bedrock model invocation logging captures information about model API calls and inference requests. Model invocation logging does not capture knowledge base document ingestion processes. The logging in this solution would help monitor model usage patterns. However, this solution would not provide visibility into document processing failures during knowledge base creation. Learn more about ++[how to monitor invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)++.

---

Nice—this one is **pure observability pattern recognition** (very exam-frequent).

---

# ✅ Q2 — Core Concept

### 👉 High-level

This question tests:

> **“Which AWS service gives _document-level ingestion visibility_ for Bedrock Knowledge Bases?”**

---

# 🧠 Key Concept (under 200 words)

**Amazon Bedrock Knowledge Bases emit ingestion logs to CloudWatch Logs**, which provide **fine-grained status of each document during ingestion**.

Key statuses include:

- `SUCCESS`
- `RESOURCE_IGNORED`
- `EMBEDDING_FAILED`
- `INDEXING_FAILED`

👉 This is critical because:

- RAG quality depends on **successful ingestion**
- Failures often occur at:
    - chunking
    - embedding generation
    - indexing

**CloudWatch Logs Insights** then lets you:

- query failures
- filter problematic files
- debug ingestion pipelines

Contrast:

- **CloudTrail** → API audit (who called what)
- **Model invocation logs** → inference, not ingestion
- **Application Signals** → app performance, not data pipeline

👉 So the pattern is:

> **“If you need _data pipeline visibility_, use logs (CloudWatch Logs)”**

---

# 🧠 Mental Model

GenAI system = 2 worlds  
  
1) Inference (LLM calls)  
2) Data pipeline (RAG ingestion)  
  
Different monitoring tools!  
  
→ This question = DATA PIPELINE

---

# 🏗️ Architecture (ASCII)

        S3 Documents  
             │  
             ▼  
   Bedrock Knowledge Base  
   (Ingestion Pipeline)  
   ─────────────────────  
   - Chunking  
   - Embedding  
   - Indexing  
             │  
             ▼  
     CloudWatch Logs  
             │  
             ▼  
 CloudWatch Logs Insights  
   (Query failures)

---

# 🎯 Why A is correct

### ✅ A — CloudWatch Logs + Logs Insights

- Native integration with Bedrock KB
- Shows **document-level ingestion status**
- Enables **query-based troubleshooting**

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|B|App Signals = app metrics, not KB ingestion|
|C|CloudTrail = API audit, no document status|
|D|Invocation logs = inference, not ingestion|

---

# 🔥 Exam Trick (important)

When you see:

|Requirement|Answer pattern|
|---|---|
|Debug ingestion / RAG pipeline|CloudWatch Logs|
|Audit who did what|CloudTrail|
|Monitor latency / tokens|CloudWatch metrics|
|Debug model calls|Invocation logs|

---

# 🧪 Mini Quiz

### Q1

You need to debug **why some documents are not searchable in a KB**. What do you check?

A. CloudTrail  
B. CloudWatch Logs  
C. X-Ray  
D. Cost Explorer

---

### Q2

You want to know **which user invoked Bedrock APIs**. What do you use?

A. CloudWatch Logs  
B. CloudTrail  
C. Logs Insights  
D. Bedrock KB logs

---

Reply with your answers, then say **“proceed”** and we’ll go to Q3.

1b, 2b,

Nice—both correct ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (CloudWatch Logs)**

✔ You correctly identified:

> Debug **data ingestion pipeline → CloudWatch Logs**

---

### Q2 → **B (CloudTrail)**

✔ You correctly identified:

> Audit **who did what → CloudTrail**

---

## 🧠 Lock it in (super short cheat sheet)

If the question says…  
  
"Why did it fail?"        → CloudWatch Logs  
"Who did it?"            → CloudTrail  
"How fast / how many?"   → CloudWatch Metrics  
"What did the model do?" → Invocation logs

---

## ⚡ Exam pattern you’re getting good at

You’re now recognizing:

- **Data pipeline vs inference vs audit vs performance**
- That’s HUGE → this shows up everywhere in the exam

---

If you’re ready, say **“proceed”** and we’ll go to Q3.

4/20 Question A GenAI developer is building a virtual assistant application by using an Anthropic Claude model on Amazon Bedrock. The application sends user queries and expects conversational responses. The GenAI developer wants to configure the application to stop generating output after a specific phrase is generated in the response. Which solution will meet these requirements? **A** Add the trigger phrase "stop at this phrase" in the user prompt. Incorrect. Amazon Bedrock processes prompts and generates completions based on the input and the model parameters. Adding a “stop at this phrase” instruction in the prompt relies on the model following instructions. However, the model might not follow instructions. This solution does not reliably control output termination. Learn more about ++[designing prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html)++. **B** Use the stop sequences parameter in the inference call to specify a trigger phrase. Correct. You can use the stop sequences parameter to stop the model from generating a response. You can use the stop sequences parameter to stop the model after generating certain key phrases. This solution provides a built-in mechanism in the model's API to directly control output generation. Learn more about ++[the stop sequences parameter](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-request-response.html)++. **C** Use the top-k parameter to control the diversity of tokens in the model's output. Incorrect. The top-k parameter controls token sampling diversity during generation. This parameter could affect the likelihood of certain tokens being selected. However, this parameter cannot stop generation at specific phrases. Learn more about ++[top-k](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html#inference-randomness)++. **D** Use the temperature parameter in the inference call to control the likelihood of the phrase appearing. Incorrect. This parameter value controls the randomness of the model’s output. Adjusting temperature influences creativity and variation. Temperature does not influence the stopping point of output generation. This solution does not reliably control output termination. Learn more about ++[temperature](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-request-response.html)++.

---

Good—this one is a **pure model parameter question** (very common in the exam).

---

# ✅ Q4 — Core Concept

### 👉 High-level

This tests:

> **“How do you control _when an LLM stops generating text_?”**

---

# 🧠 Key Concept (under 200 words)

LLM output is controlled by **inference parameters**, not prompts.

The key parameter here is:

### 🔑 `stop_sequences`

- A list of strings that tells the model:
    
    > “STOP generation when you hit this token/phrase”
    

Example:

{  
  "stop_sequences": ["\n\nUser:", "END"]  
}

👉 As soon as the model generates `"END"` → it stops immediately.

---

### Contrast with other parameters:

|Parameter|What it does|
|---|---|
|`temperature`|randomness / creativity|
|`top_k` / `top_p`|token selection strategy|
|prompt text|guidance (NOT guaranteed)|

👉 Exam principle:

> **Hard control = parameters**  
> **Soft control = prompt**

---

# 🧠 Mental Model

Prompt = suggestion  
Parameter = enforcement

---

# 🏗️ Architecture (ASCII)

User Query  
    │  
    ▼  
Application  
    │  
    ▼  
Bedrock API Call  
    │  
    ├── Prompt (instructions)  
    ├── Temperature / Top-K  
    └── Stop Sequences  ← CONTROL POINT  
                │  
                ▼  
         Claude Model  
                │  
        Generates tokens  
                │  
   Hits stop phrase → TERMINATE

---

# 🎯 Why B is correct

### ✅ B — stop sequences

- Native API-level control
- Deterministic stopping behavior
- Works across Claude / Bedrock models

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|Prompt = unreliable|
|C|top-k = diversity only|
|D|temperature = randomness|

---

# 🔥 Exam Pattern

Whenever you see:

|Requirement|Answer|
|---|---|
|Limit response length|`maxTokens`|
|Stop at phrase|`stop_sequences`|
|Make deterministic|`temperature = 0`|
|More creative|higher temperature|

---

# 🧪 Mini Quiz

### Q1

You want the model to **never exceed 100 tokens**. What do you use?

A. stop_sequences  
B. maxTokens  
C. temperature  
D. top_k

---

### Q2

You want consistent, repeatable outputs (no randomness). What do you set?

A. temperature = 1  
B. top_k = 100  
C. temperature = 0  
D. stop_sequences

---

Reply with answers + say **“proceed”** and we’ll go to Q5.

1 b, 2c

Perfect—both correct again ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (maxTokens)**

✔ Controls **length ceiling**

---

### Q2 → **C (temperature = 0)**

✔ Controls **determinism (no randomness)**

---

## 🧠 Lock this pattern (VERY exam-heavy)

Control type → Parameter  
  
Length control       → maxTokens  
Stop condition       → stop_sequences  
Creativity           → temperature  
Token selection      → top_k / top_p

---

## ⚡ Deeper intuition (this is where people slip)

Think of it like this:

- **temperature / top-k → HOW tokens are chosen**
- **maxTokens / stop_sequences → WHEN generation stops**

👉 Exam loves mixing these up.

---

## 🚀 Real-world mapping (quick practical)

If you were building your AI copilot:

- Want structured JSON output  
    → use `stop_sequences` + schema
- Want short answers  
    → `maxTokens`
- Want consistent KPI explanations (your use case)  
    → `temperature = 0`

---

You’re moving fast—this is exactly exam pace.

👉 Say **“proceed”** and we go to Q5.

5/20 Question A news media company wants to develop a content conformance tool that automatically reviews and adjusts articles to ensure compliance with a style guide. Journalists need a web-based article editor that provides real-time analysis of content upon request. When journalists click an "analyze" button, the system should immediately begin providing suggested revisions through the editor interface. Articles are tagged with content categories in the metadata. Examples of categories include news, sports, and editorial. The company wants to use an Amazon Bedrock FM to analyze content and provide immediate feedback through the web-based article editor interface. Which architecture will meet these requirements with the LEAST operational overhead? **A** Implement an Amazon SQS queue for article ingestion. Create AWS Step Functions workflows to process content. Use AWS Lambda functions to determine the content category from metadata and invoke appropriate Amazon Bedrock models with style guide prompts. Store results in Amazon DynamoDB. Use an Amazon API Gateway WebSocket API for real-time streaming of suggestions to the journalists. Incorrect. Amazon SQS and Lambda provide reliable processing capabilities. Amazon SQS is a queuing service where messages must be polled for processing. Therefore, this architecture does not meet the requirement for immediate feedback through the web-based article editor interface. This queuing and polling approach introduces additional latency. This architecture does not provide real-time feedback when journalists click the "analyze" button. Learn more about ++[streaming responses](https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html)++. **B** Deploy an Amazon API Gateway WebSocket API linked to an AWS Lambda function. Configure the function to read the content category from metadata and route content to the appropriate Amazon Bedrock model based on the category tag. Configure the function to use Amazon Bedrock Prompt Management to enforce style guide rules. Use the Amazon Bedrock streaming API to return suggestions in real time. Correct. This architecture uses managed services to minimize operational overhead. An API Gateway WebSocket API provides real-time, bidirectional communication. Therefore, this solution is suitable for streaming suggestions in the web-based article editor interface. The Lambda function efficiently reads metadata tags for routing. Amazon Bedrock Prompt Management provides a managed way to implement and maintain style guide rules across different content types. The Amazon Bedrock streaming API capability provides immediate delivery of suggestions when journalists click the "analyze" button. Therefore, this architecture creates a responsive editing experience. This architecture requires minimal infrastructure management and meets the requirements for real-time content analysis and feedback. Learn more about ++[API Gateway WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html)++. Learn more about ++[how to invoke an Amazon Bedrock model with response streaming](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-invoke.html)++. **C** Create an Amazon API Gateway REST API with AWS Lambda function URLs to enable response streaming. Configure the Lambda function to process articles and stream suggestions using chunked transfer encoding. Incorrect. Lambda function URLs with chunked transfer encoding through API Gateway would not provide real-time streaming to the web-based article editor interface. API Gateway has dataset size limits and would not provide the immediate, responsive experience that you need. REST APIs are not suitable for the long-lived connections that you need for real-time streaming. This architecture could lead to connection timeouts and a poor user experience. Learn more about ++[Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html)++. **D** Configure an Application Load Balancer with Amazon ECS tasks that run custom containers. Implement content category routing logic and style guide checking within the containers. Use Amazon Bedrock with streaming support to generate suggestions. Use WebSocket connections to stream results to the journalists in real time. Incorrect. To run custom containers on Amazon ECS, you must manage container infrastructure, scaling, and deployment. Implementing content routing and style guide checking within containers creates additional development and maintenance overhead. This architecture does not use managed services effectively. This approach requires more operational effort than using serverless alternatives. Learn more about ++[ECS containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html)++.

---

This is a **high-value architecture question**—it combines:

- real-time UX
- Bedrock streaming
- “least operational overhead” (VERY important keyword)

---

# ✅ Q5 — Core Concept

### 👉 High-level

This tests:

> **“How do you build real-time GenAI apps with minimal ops?”**

---

# 🧠 Key Concept (under 200 words)

For **real-time GenAI responses**, you need:

### 1) **Streaming inference**

- Bedrock supports streaming (token-by-token output)
- Enables “typing effect” in UI

### 2) **Persistent connection**

- WebSocket (NOT REST)
- Allows server → client push

### 3) **Serverless routing**

- Lambda handles:
    - metadata-based routing
    - prompt selection
    - Bedrock invocation

### 4) **Managed prompt control**

- Bedrock Prompt Management = reusable, governed prompts

---

👉 So the ideal pattern is:

> **WebSocket + Lambda + Bedrock streaming = real-time GenAI UI**

And because everything is serverless:  
✔ minimal infra  
✔ minimal scaling concerns  
✔ lowest operational overhead

---

# 🧠 Mental Model

Real-time GenAI =  
  
Streaming + Persistent connection + Serverless

---

# 🏗️ Architecture (ASCII)

        Web Editor (User)  
                │  
        Click "Analyze"  
                │  
                ▼  
     API Gateway (WebSocket)  
                │  
                ▼  
            Lambda  
   ┌────────────┼────────────┐  
   │            │            │  
Read metadata   │     Prompt Mgmt  
(category)      │     (style rules)  
                ▼  
          Bedrock FM  
     (Streaming response)  
                │  
                ▼  
     WebSocket stream back  
                │  
                ▼  
        Real-time suggestions

---

# 🎯 Why B is correct

### ✅ B — Best combo

- WebSocket → real-time UI
- Lambda → routing + logic
- Bedrock streaming → instant feedback
- Prompt Management → enforce style guide

👉 Covers ALL requirements with **lowest ops**

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|SQS = async → breaks “real-time”|
|C|REST = request/response → not streaming-friendly|
|D|ECS = heavy ops → violates “least overhead”|

---

# 🔥 Exam Patterns (VERY important)

### 1. Real-time GenAI UI

→ WebSocket + streaming

### 2. Async / batch processing

→ SQS / Step Functions

### 3. Least ops

→ Lambda > ECS

---

# 🧪 Mini Quiz

### Q1

You need **real-time token streaming to a browser UI**. What do you use?

A. REST API  
B. SQS  
C. WebSocket API  
D. Batch inference

---

### Q2

You want to enforce **consistent prompts across teams**. What do you use?

A. Store prompts in Lambda code  
B. Bedrock Prompt Management  
C. DynamoDB  
D. CloudWatch

---

Reply with answers + say **“proceed”** and we go to Q6 🚀

1 c, 2b. Review Websock API vs REST API

Nice—both correct again ✅  
You’re clearly picking up the patterns fast.

---

# 🔍 Deep Dive: WebSocket API vs REST API (Exam Gold)

Let’s build intuition properly (this shows up A LOT).

---

## 🧠 1. High-level Concept

### 👉 REST API

> Request → Response (one-shot)

### 👉 WebSocket API

> Persistent connection → real-time, bidirectional stream

---

## ⚡ 2. Mental Model

REST        = Ask → Wait → Answer  
WebSocket   = Open pipe → Stream continuously

---

## 🏗️ 3. Architecture Comparison

### REST API (Traditional)

Client  
  │  
  ▼  
API Gateway (REST)  
  │  
  ▼  
Lambda  
  │  
  ▼  
Bedrock  
  │  
  ▼  
Full response returned (once)

👉 Good for:

- CRUD
- synchronous APIs
- simple GenAI calls

---

### WebSocket API (Streaming)

Client (browser/editor)  
   │  
   │  persistent connection  
   ▼  
API Gateway (WebSocket)  
   │  
   ▼  
Lambda  
   │  
   ▼  
Bedrock (streaming)  
   │  
   ▼  
Partial tokens → pushed continuously

👉 Good for:

- chat apps
- live editing (your Q5 scenario)
- token streaming
- interactive UX

---

## 📊 4. Side-by-side Comparison

|Feature|REST API|WebSocket API|
|---|---|---|
|Connection|Short-lived|Persistent|
|Data flow|One-way|Two-way|
|Streaming|❌ Limited|✅ Native|
|Latency|Higher (per request)|Lower (continuous)|
|Use case|CRUD, simple calls|Real-time apps|
|GenAI fit|Basic|Best for chat/streaming|

---

## 🔥 5. Exam Triggers (VERY IMPORTANT)

When you see keywords:

|Keyword in question|Answer|
|---|---|
|“real-time suggestions”|WebSocket|
|“streaming responses”|WebSocket + Bedrock streaming|
|“chat interface”|WebSocket|
|“batch processing”|NOT WebSocket|
|“simple API call”|REST|

---

## ⚠️ Common Trap

> “REST API + streaming”

❌ Sounds plausible  
❌ Often wrong in exam

👉 Because:

- REST is **not designed for persistent streaming**
- WebSocket is the **expected answer pattern**

---

## 🧠 How you’d use this in your project

For your **AI data copilot / coaching system**:

- Stream answers progressively → WebSocket
- Show full result after computation → REST

👉 You’ll likely use **both in real systems**

---

## 🧪 Mini Quiz (quick check)

### Q1

A chatbot UI must display responses as they are generated. What do you use?

A. REST API  
B. WebSocket API  
C. SQS  
D. Step Functions

---

### Q2

You need a simple API to trigger a Bedrock model and return a full summary. What do you use?

A. WebSocket  
B. REST API  
C. EventBridge  
D. Kinesis

---

Answer + say **“proceed”** → we continue to Q6 🚀

1 b, 2 b

Perfect—both correct again ✅

---

## 🔍 Quick correction (small nuance)

### Q2 → **B (REST API)** ✔

Your reasoning is right:

> Simple request → full response → REST

---

## 🧠 Lock the distinction (this is exam gold)

If you need…  
  
Streaming / chat / real-time UI   → WebSocket  
Single request → full response    → REST

---

## ⚡ Subtle exam insight (important)

The exam **does NOT care about real-world hacks** (like streaming over REST).  
It expects the **clean architectural choice**:

- REST = request/response
- WebSocket = streaming / interactive

👉 Always choose the “textbook AWS architecture”

---

## 🧠 What you’re doing well

You’re now consistently identifying:

- **interaction pattern (real-time vs batch)**
- **service fit (WebSocket vs REST)**

👉 This is a _core scoring differentiator_ in this exam.

---

Ready to keep the momentum?

👉 Say **“proceed”** and we go to Q6 🚀

Deep dive: A. WebSocket B. REST API C. EventBridge D. Kinesis

Great prompt—this is exactly the kind of **“service selection clarity”** that wins the exam.

Let’s break these **from first principles → then exam usage → then when they compete**.

---

# 🧠 1. Core Mental Model (1-liner each)

WebSocket   = real-time conversation pipe  
REST API    = request/response interface  
EventBridge = event router (decoupling)  
Kinesis     = real-time data streaming (high-throughput)

---

# 🏗️ 2. Architecture View (side-by-side)

## A. WebSocket → Real-time interaction

Client  ⇄  API Gateway (WebSocket)  ⇄  Lambda  ⇄  Bedrock  
           (persistent connection)

✔ Bidirectional  
✔ Streaming tokens  
✔ Low latency UX

👉 Think: **chat, live editing, copilot**

---

## B. REST API → Synchronous request

Client → API Gateway (REST) → Lambda → Bedrock → Response

✔ Simple  
✔ Stateless  
✔ One request → one response

👉 Think: **“generate summary” button**

---

## C. EventBridge → Event-driven backbone

Producer → EventBridge → Targets (Lambda, Step Functions, etc.)

✔ Async  
✔ Decoupled  
✔ Routing rules

👉 Think: **“something happened → trigger workflow”**

---

## D. Kinesis → Streaming data pipeline

Producers → Kinesis Stream → Consumers (Lambda, analytics, etc.)

✔ High throughput  
✔ Ordered streams  
✔ Replayable

👉 Think: **logs, clickstreams, IoT**

---

# 📊 3. Side-by-side Comparison (exam lens)

|Feature|WebSocket|REST API|EventBridge|Kinesis|
|---|---|---|---|---|
|Pattern|Real-time|Sync request|Event-driven|Data streaming|
|Latency|Very low|Medium|Async|Near real-time|
|Direction|Bi-directional|One-way|One-to-many|One-to-many|
|Persistence|Yes|No|No|Stream-based|
|Use case|Chat, live UI|APIs|Orchestration|Data pipelines|

---

# 🔥 4. When they compete (EXAM TRAPS)

## 🧨 Trap 1: WebSocket vs REST

👉 Look for **interaction pattern**

|If question says…|Answer|
|---|---|
|“real-time updates”|WebSocket|
|“chat interface”|WebSocket|
|“simple API call”|REST|

---

## 🧨 Trap 2: EventBridge vs Kinesis

👉 Look for **event vs data**

|If question says…|Answer|
|---|---|
|“trigger workflow”|EventBridge|
|“route events”|EventBridge|
|“streaming data / logs”|Kinesis|
|“high throughput ingestion”|Kinesis|

---

## 🧨 Trap 3: EventBridge vs SQS (bonus insight)

- EventBridge = routing
- SQS = buffering

---

# 🧠 5. Real-world mapping (your projects)

### Your GenAI copilot:

- UI streaming → **WebSocket**
- API trigger → **REST**
- ingestion trigger → **EventBridge**
- logs / metrics pipeline → **Kinesis**

👉 You’ll use ALL of them in real systems.

---

# ⚡ 6. Ultra-short decision tree

Is it user interaction?  
  → Real-time? → WebSocket  
  → One-shot?  → REST  
  
Is it system-to-system?  
  → Event trigger? → EventBridge  
  → Data stream?   → Kinesis

---

# 🧪 Mini Quiz (harder)

### Q1

A system must process **millions of clickstream events per second with ordering guarantees**.  
→ ?

---

### Q2

A system must **trigger downstream workflows when a file is uploaded to S3**.  
→ ?

---

### Q3

A chatbot must **stream responses token-by-token to a browser UI**.  
→ ?

---

Answer + say **“proceed”** → we continue 🚀

1. Kinesis 2.Eventbridge 3. WebSocket API

Perfect—**all 3 correct ✅**  
You’re now thinking exactly like the exam expects.

---

## 🔍 Quick reinforcement

### Q1 → **Kinesis**

✔ High-throughput  
✔ Ordered stream  
✔ Replay capability

---

### Q2 → **EventBridge**

✔ Event-driven trigger  
✔ Decoupled routing

---

### Q3 → **WebSocket API**

✔ Real-time  
✔ Streaming tokens

---

# 🧠 Final mental compression (this is your exam cheat code)

User interaction?  
  → Real-time → WebSocket  
  → One-shot  → REST  
  
System events?  
  → Trigger workflows → EventBridge  
  → Stream data       → Kinesis

---

# ⚡ One level deeper (this is what separates top scores)

### Why NOT mix them up:

- ❌ Kinesis for workflows → too heavy
- ❌ EventBridge for streaming data → wrong abstraction
- ❌ REST for streaming UI → wrong protocol
- ❌ WebSocket for backend events → overkill

👉 The exam rewards **clean architecture boundaries**

---

You’re in very strong shape now.

👉 Say **“proceed”** and we go to Q6 🚀

6/20 Question A company uses an AI assistant to answer customer questions based on internal company documents. The company wants to include new documents in the assistant's responses as soon as possible. The company wants to exclude deleted documents from the AI assistant's responses as soon as possible. The documents are stored in Amazon S3. The AI assistant uses Amazon Bedrock Knowledge Bases. Amazon S3 is the data source of the vector store that the company uses for RAG. A GenAI developer must create a scalable, event-driven, and resilient solution. Which solution will meet these requirements? **A** Configure Amazon EventBridge Scheduler to schedule a rule that runs every 5 minutes and invokes an AWS Lambda function. Configure the Lambda function to track changes in Amazon S3 and invoke IngestKnowledgeBaseDocuments for new objects and DeleteKnowledgeBaseDocuments for deleted objects. Incorrect. EventBridge Scheduler provides time-based actions for different AWS services. Running the sync action every 5 minutes is not suitable for near real-time updates to the knowledge base. This solution introduces delays in including new documents in the knowledge base. Additionally, tracking changes to the documents in Amazon S3 within the Lambda function is not operationally efficient. The Lambda function would need to maintain some form of change tracking to identify which documents have been added or deleted. Learn more about ++[EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html)++. **B** Configure S3 Event Notifications to invoke an AWS Lambda function on object-created and object-deleted events. Configure the Lambda function to invoke IngestKnowledgeBaseDocuments for new objects and DeleteKnowledgeBaseDocuments for deleted objects. Incorrect. You can use S3 Event Notifications to send notifications when an event occurs in an S3 bucket. This solution does not provide buffering and retry support. Amazon S3 directly invoking Lambda can fail under high load because of synchronous invocation limits. Learn more about ++[S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html)++. **C** Configure S3 Event Notifications to send object-created and object-deleted events to an Amazon SQS queue. Create an AWS Lambda function to poll the queue and invoke IngestKnowledgeBaseDocuments for new objects and DeleteKnowledgeBaseDocuments for deleted objects. Correct. This solution provides a scalable and resilient architecture to meet the requirements. You can use Amazon SQS as a buffer between S3 events and Lambda processing. The queue handles traffic spikes, provides automatic retries, and ensures that no updates are missed. This event-driven approach meets the requirements and maintains system reliability under varying loads. Learn more about ++[how to ingest changes directly into a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html)++. **D** Configure Amazon EventBridge Scheduler to schedule a rule that runs every 5 minutes and invokes an AWS Lambda function. Configure the Lambda function to sync the documents in Amazon S3 with the knowledge base by invoking StartIngestionJob. Incorrect. EventBridge Scheduler provides time-based actions for different AWS services. Syncing every 5 minutes is inefficient and causes unnecessary scanning. This solution can introduce delays. This solution cannot support the immediacy required for near real-time updates. This solution is not an event-driven architecture. Learn more about ++[EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html)++. Learn more about ++[how to sync a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-data-source-sync-ingest.html)++.

---

Excellent—this is a **classic event-driven + resilience pattern question** (very high probability in exam).

---

# ✅ Q6 — Core Concept

### 👉 High-level

This tests:

> **“How do you build a real-time, scalable, and reliable ingestion pipeline?”**

---

# 🧠 Key Concept (under 200 words)

For **RAG freshness**, you need:

- near real-time ingestion (new docs appear quickly)
- deletion propagation (removed docs disappear quickly)

The correct pattern is:

### 🔑 Event-driven + buffering

**S3 → SQS → Lambda → Bedrock KB**

Why?

- **S3 events** → detect changes immediately
- **SQS** → buffer + retry + handle spikes
- **Lambda** → process events and call:
    - `IngestKnowledgeBaseDocuments`
    - `DeleteKnowledgeBaseDocuments`

---

👉 Key insight:

- Direct S3 → Lambda ❌ (not resilient at scale)
- Scheduled polling ❌ (not real-time)
- Queue buffering ✅ (decoupled + reliable)

---

# 🧠 Mental Model

Event → Buffer → Process  
  
(never skip the buffer in scalable systems)

---

# 🏗️ Architecture (ASCII)

        S3 Bucket  
   (documents added/deleted)  
             │  
             ▼  
   S3 Event Notifications  
             │  
             ▼  
          SQS Queue   ← BUFFER  
             │  
             ▼  
           Lambda  
   ┌─────────┼─────────┐  
   │                   │  
Ingest KB        Delete KB  
(new docs)       (removed docs)  
             │  
             ▼  
   Bedrock Knowledge Base

---

# 🎯 Why C is correct

### ✅ C — S3 → SQS → Lambda

- Event-driven ✅
- Scalable ✅
- Resilient (retries, buffering) ✅
- Near real-time ✅

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|Polling every 5 min → latency + complexity|
|B|S3 → Lambda direct → no buffering|
|D|Batch sync → not event-driven|

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### When you see:

|Requirement|Pattern|
|---|---|
|Real-time updates|Event-driven|
|Scalable + resilient|Add SQS buffer|
|Decoupling|Queue between services|

---

# ⚡ Golden Rule (memorize this)

S3 → Lambda        = simple but fragile ❌  
S3 → SQS → Lambda  = production-grade ✅

---

# 🧪 Mini Quiz

### Q1

A system must handle **spikes in S3 uploads without losing events**. What do you add?

A. EventBridge Scheduler  
B. SQS  
C. DynamoDB  
D. API Gateway

---

### Q2

A system polls S3 every 10 minutes for changes. What’s the problem?

A. Too expensive  
B. Not scalable  
C. Not real-time  
D. Not secure

---

Reply with answers + say **“proceed”** → Q7 🚀

1 b 2c

Perfect—both correct again ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (SQS)**

✔ Handles spikes  
✔ Buffers events  
✔ Ensures no loss

---

### Q2 → **C (Not real-time)**

✔ Polling = delay  
✔ Breaks “as soon as possible” requirement

---

# 🧠 Lock this pattern (VERY HIGH VALUE)

Real-time + scalable + resilient  
→ Event-driven + Queue (SQS)

---

## ⚡ Deeper intuition (this is exam-level thinking)

### Why SQS matters (not just “nice to have”)

Without SQS:

S3 → Lambda

❌ Risk:

- bursts overwhelm Lambda
- dropped events
- retries limited

With SQS:

S3 → SQS → Lambda

✅ Guarantees:

- buffering
- retries
- backpressure handling
- durability

---

## 🔥 Exam trick (watch for wording)

|Phrase in question|Hidden meaning|
|---|---|
|“as soon as possible”|event-driven|
|“scalable”|no direct coupling|
|“resilient”|MUST include buffer (SQS)|

👉 If you see all three → **SQS is almost always in the answer**

---

You’re consistently getting these right—this is strong signal you’re exam-ready.

👉 Say **“proceed”** and we go to Q7 🚀

7/20 Question A financial services company needs to use Amazon Bedrock to create an AI assistant that will help customer support representatives across multiple business units. A GenAI developer must ensure that prompt templates are properly governed through approval workflows. Additionally, the company requires comprehensive logging of all model invocations with a 7-year retention period for regulatory compliance. Which combination of steps will meet these requirements with MINIMAL operational overhead? (Select TWO.) **A** Use Amazon Bedrock Prompt Management with multi-stage approval workflows. Use IAM policies that require multi-party authorization. ## Correct. You can use Amazon Bedrock Prompt Management to securely create, parameterize, version, and approve prompt templates within the Amazon Bedrock managed environment. This solution provides multi-stage approvals, access roles, version control, and collaboration features that are suitable for diverse business units and complex governance requirements. Learn more about ++[Amazon Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html)++. **B** Store prompt templates in Amazon DynamoDB tables with composite keys partitioned by business units. Implement IAM policies that grant role-based access to business units for template approval. Use DynamoDB item-level permissions to control prompt template modifications and approvals. Answer choice eliminated Incorrect. DynamoDB is a NoSQL database that can store prompt templates. However, this approach requires custom development for approval workflows and access control. Building and maintaining custom solutions for template management increases operational overhead. Learn more about ++[DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)++. **C** Set up Amazon EventBridge rules to capture Amazon Bedrock model invocation events. Route events to Amazon CloudWatch Logs groups that are organized by business unit. Export the logs to Amazon S3. Enable S3 Object Lock with compliance retention mode set to 7 years. Incorrect. You can use EventBridge rules to capture and route events. However, this approach requires more operational overhead and creates potential points of failure. This approach requires custom configuration and maintenance of rules. This approach does not provide the comprehensive audit trail that you need for regulatory compliance. Learn more about ++[EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)++. **D** Enable AWS CloudTrail data events for all Amazon Bedrock APIs. Deliver the logs to CloudTrail Lake with a 7-year retention setting. Tag each event with the business unit ID. Run CloudTrail Lake queries to monitor prompt activity. ## Incorrect. CloudTrail Lake provides logging capabilities. However, CloudTrail captures only API metadata. For example, CloudTrail captures who called bedrock:InvokeModel and when. CloudTrail does not capture the actual prompt content and model responses that you need for regulatory reconstruction. Learn more about ++[how to monitor Amazon Bedrock API calls by using CloudTrail](https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html)++. **E** Enable Amazon Bedrock model invocation logging with Amazon S3 as the destination. Enable S3 Object Lock with compliance retention mode set to 7 years. Create separate prefixes for each business unit. ## Correct. Amazon Bedrock provides a built-in model invocation logging feature. You can enable Amazon Bedrock model invocation logging with Amazon S3 as the destination. This approach provides comprehensive logging with minimal setup. S3 Object Lock in compliance mode provides immutable storage that enforces the 7-year retention period for regulatory compliance. This approach ensures that you cannot delete logs before the retention period expires. This approach provides built-in business unit segregation through S3 prefixes. Therefore, this solution requires minimal operational overhead. Learn more about ++[S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)++.

---

Nice—this is a **governance + compliance combo question** (very exam-heavy).

---

# ✅ Q7 — Core Concept

### 👉 High-level

This tests:

> **“Use managed Bedrock features for governance + compliance logging (least ops)”**

---

# 🧠 Key Concept (under 200 words)

There are **two separate concerns**:

---

## 1️⃣ Prompt Governance

Use:

### 🔑 **Amazon Bedrock Prompt Management**

- versioning
- approval workflows
- multi-stage approvals
- centralized control across business units

👉 Avoid custom DB + IAM logic (too much ops)

---

## 2️⃣ Full Audit Logging (REGULATORY)

Use:

### 🔑 **Bedrock Model Invocation Logging → S3**

- captures:
    - prompts
    - responses
    - metadata

Then enforce:

### 🔑 **S3 Object Lock (compliance mode)**

- immutable storage
- meets **7-year retention** requirement

---

👉 Key exam insight:

|Requirement|Service|
|---|---|
|Prompt governance|Bedrock Prompt Management|
|Full content logging|Invocation logging|
|Regulatory retention|S3 Object Lock|

---

# 🧠 Mental Model

Governance = Prompt Management  
Audit      = Invocation Logs + S3 Lock

---

# 🏗️ Architecture (ASCII)

        Developers / Teams  
                │  
                ▼  
   Bedrock Prompt Management  
   (approval workflows)  
                │  
                ▼  
        Bedrock Models  
                │  
        (invocations)  
                ▼  
   Invocation Logging (built-in)  
                │  
                ▼  
             S3 Bucket  
      (Object Lock - 7 yrs)  
                │  
      Segregated by BU prefix

---

# 🎯 Why A + E are correct

### ✅ A — Prompt Management

✔ Managed governance  
✔ Approval workflows  
✔ Multi-team support

---

### ✅ E — Invocation logging + S3 Object Lock

✔ Full prompt/response capture  
✔ Immutable storage  
✔ Meets compliance

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|B|Custom build → high ops|
|C|EventBridge = unnecessary complexity|
|D|CloudTrail = metadata only (NOT content)|

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### Logging types (must distinguish!)

|Need|Service|
|---|---|
|Who called API|CloudTrail|
|What model did (prompt/response)|Invocation logging|
|App logs|CloudWatch|
|Compliance retention|S3 Object Lock|

---

# 🧪 Mini Quiz

### Q1

You need to **reconstruct exact model responses for audit**. What do you use?

A. CloudTrail  
B. CloudWatch Logs  
C. Bedrock invocation logging  
D. X-Ray

---

### Q2

You need **immutable storage for compliance**. What do you use?

A. DynamoDB TTL  
B. S3 Object Lock  
C. Glacier lifecycle  
D. EFS

---

Reply with answers + say **“proceed”** → Q8 🚀

8/20 Question A financial services company operates RAG for an application that answers user questions by using internal market analysis reports. The application uses Amazon Bedrock for the embedding model. The application uses an Amazon OpenSearch Service cluster as the vector store. An AWS Lambda function performs the embedding and search logic. After a recent code update to the Lambda function, the application starts returning generic responses. For example, the application returns “no relevant information found” even for questions that previously returned accurate answers. Amazon CloudWatch Logs shows no errors. AWS X-Ray confirms successful FM invocation. The OpenSearch Service cluster is healthy. Query latency remains normal. What is the cause of this issue? **A** The document embeddings in OpenSearch Service were deleted during the application update and have not been re-indexed. ## Incorrect. If the embeddings had been deleted, the issue would appear in logs or cause failed OpenSearch queries. The scenario states that there are no errors or unusual query latency. Therefore, the documents are still being retrieved. Learn more about ++[OpenSearch Service vector search and embeddings](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vector-search.html)++. **B** The Lambda function’s IAM role is missing the permission for bedrock:InvokeModel. Incorrect. The scenario states that the model is being invoked successfully. If the IAM permission were missing, then the Lambda function would throw an access error and fail before generating a response. Learn more about ++[Amazon Bedrock and IAM](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html)++. **C** The Amazon Bedrock FM temperature parameter was increased. Incorrect. A high temperature setting can degrade the quality of generation. However, a high temperature setting would not prevent the model from finding relevant context. The reported issue relates to a retrieval failure, not generation randomness. Learn more about ++[Amazon Bedrock generation parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html)++. **D** The updated Lambda function uses a different version of the embedding model. ## Correct. Embedding drift occurs when query embeddings are generated with a different model than the model used to index documents. This issue causes a mismatch in vector space and makes retrieval ineffective. In this scenario, the update to the Lambda function likely introduced a new embedding model version or configuration. Learn more about ++[embeddings](https://aws.amazon.com/what-is/embeddings-in-machine-learning/)++. Learn more about ++[embedding drift](https://aws.amazon.com/blogs/machine-learning/from-rag-to-fabric-lessons-learned-from-building-real-world-rags-at-genaiic-part-1/)++.

---

This is a **very important RAG failure pattern**—shows up a lot in the exam.

---

# ✅ Q8 — Core Concept

### 👉 High-level

This tests:

> **“Why does retrieval suddenly fail even when everything looks healthy?”**

---

# 🧠 Key Concept (under 200 words)

This is **embedding drift**.

In RAG, both:

- documents
- user queries

must be embedded using the **same model (same vector space)**.

---

### What happened here:

- Documents were embedded with **Model A**
- After update, queries use **Model B**

👉 Result:

- vectors are no longer comparable
- similarity search fails
- retrieval returns nothing
- model gives generic fallback responses

---

### Key insight:

> Retrieval failure ≠ system failure  
> It’s often **semantic mismatch**

---

This is explicitly part of retrieval troubleshooting in GenAI systems

---

# 🧠 Mental Model

Good RAG:  
Doc embedding == Query embedding → match  
  
Broken RAG:  
Doc embedding ≠ Query embedding → no match

---

# 🏗️ Architecture (ASCII)

        Documents  
            │  
            ▼  
   Embedding Model A  
            │  
            ▼  
      OpenSearch (vectors)  
  
-------------------------------  
  
        User Query  
            │  
            ▼  
   Embedding Model B ❌  
            │  
            ▼  
   Vector search → no match  
            │  
            ▼  
   "No relevant info found"

---

# 🎯 Why D is correct

### ✅ D — Different embedding model

✔ Causes vector space mismatch  
✔ Breaks similarity search  
✔ No errors, but wrong results

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|Would cause missing data / errors|
|B|IAM issue → invocation would fail|
|C|Temperature affects generation, not retrieval|

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### When you see:

|Symptom|Likely cause|
|---|---|
|No results, no errors|Embedding mismatch|
|Poor relevance|Bad chunking / embeddings|
|Hallucinations|Weak retrieval|
|Errors|IAM / infra|

---

# ⚡ Golden Rule

RAG only works if embeddings are consistent

---

# 🧪 Mini Quiz

### Q1

You change embedding model but do NOT re-index documents. What happens?

A. Slower latency  
B. Retrieval fails  
C. Model crashes  
D. No change

---

### Q2

You want to fix embedding drift. What do you do?

A. Lower temperature  
B. Re-index documents with new model  
C. Increase top-k  
D. Add more prompts

---

Reply with answers + say **“proceed”** → Q9 🚀

1. b 2.b

Perfect—both correct again ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (Retrieval fails)**

✔ No matching vectors → no results

---

### Q2 → **B (Re-index documents)**

✔ Align embeddings again → fixes RAG

---

# 🧠 Lock this (this WILL appear in exam)

Changed embedding model?  
→ MUST re-index documents

---

## ⚡ Deeper intuition (this is advanced level)

This is one of the **most realistic production failures**:

Everything looks healthy:

- ✅ Lambda works
- ✅ Bedrock works
- ✅ OpenSearch works
- ❌ Results are useless

👉 Root cause = **semantic layer broken**

---

## 🔥 Diagnostic pattern (very exam-relevant)

No errors + bad answers  
→ Check retrieval  
  
No retrieval results  
→ Check embeddings  
  
Embeddings changed?  
→ Re-index required

---

## 🧠 What you’re now strong at

You can now distinguish:

- infra failure ❌
- model failure ❌
- retrieval failure ✅

👉 That’s a **big scoring differentiator**

---

You’re doing really well—this is advanced territory now.

👉 Say **“proceed”** and we go to Q9 🚀

9/20 A company is implementing a systematic evaluation process for a newly deployed FM in Amazon Bedrock. The company wants to replace an existing model in production with a new model. The change to the new model is dependent on the new model demonstrating better performance than the existing model. The company must follow a sequential validation process. To ensure evaluation rigor, each step must be reviewed and approved before proceeding to the next step. Select and order each step from the following list to implement the evaluation workflow. Select each step one time. (Select and order FIVE.) * Analyze the results and generate a comprehensive evaluation report. * Conduct A/B testing to compare the new model against the existing production model. * Create a test dataset with diverse scenarios and edge cases. * Define evaluation metrics for relevance, factual accuracy, and fluency. * Implement automated quality gates by using AWS Step Functions. Step 1: Implement automated quality gates by using AWS Step Functions. Define evaluation metrics for relevance, factual accuracy, and fluency. Step 2: Create a test dataset with diverse scenarios and edge cases. Step 3: Conduct A/B testing to compare the new model against the existing production model. Step 4: Define evaluation metrics for relevance, factual accuracy, and fluency. Implement automated quality gates by using AWS Step Functions. Step 5: Analyze the results and generate a comprehensive evaluation report. Sequential validation and approval provides a rigorous evaluation process where each step builds upon validated components of the previous steps. This sequential workflow is essential to maintain evaluation rigor. You can use this approach to make an informed decision about model replacement. First, you must define evaluation metrics. This step establishes the specific criteria to measure model performance. Important metrics include relevance, factual accuracy, and fluency. These metrics provide a quantifiable way to assess model outputs. You need to review and approve the metrics before proceeding. The metrics determine what constitutes success in all subsequent testing steps. Second, you must create a test dataset with diverse scenarios and edge cases. This step provides the controlled data that you need for systematic evaluation. The dataset must include carefully selected examples that cover various use cases, potential edge cases, and challenging scenarios. The test dataset must align with the approved evaluation metrics and ensure comprehensive coverage of test cases. Third, you must conduct A/B testing. A/B testing systematically compares the performance of the new model against the existing model using the test dataset. A/B testing runs both models on the same inputs and measures the outputs against the defined metrics. A/B testing provides direct performance comparisons. The testing can only proceed after both the metrics and the test dataset are validated. Fourth, you must implement automated quality gates by using Step Functions. This step establishes automated checkpoints in the evaluation workflow. The gates enforce the approval requirements between stages. The gates automatically verify the results against predefined thresholds. The gates ensure that all necessary validations are completed before proceeding. Finally, you must analyze the results and generate a comprehensive evaluation report. This step must be the final step because first you must complete all the previous steps and approve the results. This analysis provides the evidence that you need to make an informed decision about replacing the existing model. You can make a decision based on performance measurements, established metrics, and a validated testing framework. Learn more about ++[Amazon Bedrock evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html)++. Learn more about ++[Step Functions for ML workflows](https://docs.aws.amazon.com/step-functions/latest/dg/use-cases.html#use-cases-machine-learning)++. Learn more about ++[A/B testing](https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html)++.

---

Nice—this is a **pure workflow / ordering question** (very common in the exam).

---

# ✅ Q9 — Core Concept

### 👉 High-level

This tests:

> **“What is the correct sequence for evaluating and replacing an FM?”**

---

# 🧠 Key Concept (under 200 words)

Evaluation is a **structured pipeline**—you don’t jump into testing.

You always go:

1. **Define success first** → metrics
2. **Prepare test data** → dataset
3. **Run experiments** → A/B testing
4. **Enforce rigor** → quality gates
5. **Make decision** → analysis/report

---

👉 Key insight:

Metrics → Data → Experiment → Control → Decision

---

Why this matters:

- Metrics define _what good looks like_
- Dataset ensures _fair testing_
- A/B testing ensures _comparison_
- Step Functions ensures _governance_
- Report ensures _decision-making_

This aligns with evaluation systems in GenAI workflows

---

# 🧠 Correct Order

### ✅ Final Answer

1. Define evaluation metrics  
2. Create test dataset  
3. Conduct A/B testing  
4. Implement quality gates (Step Functions)  
5. Analyze results and generate report

---

# 🧠 Mental Model

You cannot test before you define success  
You cannot compare before you prepare data  
You cannot decide before validation

---

# 🏗️ Architecture (ASCII)

      Define Metrics  
             │  
             ▼  
      Create Dataset  
             │  
             ▼  
       A/B Testing  
   (Old vs New Model)  
             │  
             ▼  
   Step Functions Gates  
   (approval checkpoints)  
             │  
             ▼  
   Analyze + Report  
             │  
             ▼  
     Go / No-Go Decision

---

# ❌ Common Mistakes (exam traps)

|Mistake|Why wrong|
|---|---|
|Start with A/B testing|No metrics defined|
|Analyze before testing|No data|
|Skip quality gates|No governance|
|Dataset before metrics|No alignment|

---

# 🔥 Exam Pattern

When you see:

- “evaluation workflow”
- “sequential validation”
- “approval at each stage”

👉 Think:

Define → Prepare → Test → Control → Decide

---

# 🧪 Mini Quiz

### Q1

What must ALWAYS come first in model evaluation?

A. Dataset  
B. Metrics  
C. A/B testing  
D. Report

---

### Q2

Why use Step Functions in evaluation?

A. Faster inference  
B. Store embeddings  
C. Enforce approval workflow  
D. Improve accuracy

---

Reply with answers + say **“proceed”** → Q10 🚀

1 b 2c

Perfect—both correct again ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (Metrics first)**

✔ Defines success criteria  
✔ Everything else depends on it

---

### Q2 → **C (Step Functions = governance)**

✔ Enforces approval checkpoints  
✔ Ensures sequential validation

---

# 🧠 Lock this pattern (very exam-relevant)

Evaluation pipeline =  
  
Metrics → Dataset → A/B Test → Quality Gates → Report

---

## ⚡ Deeper intuition (what the exam is really testing)

This is not just ML—it’s **enterprise governance mindset**:

- You don’t deploy models based on “it feels better”
- You deploy based on:
    - defined metrics
    - controlled experiments
    - audited approval process

👉 That’s why Step Functions shows up:

> It’s not about ML—it’s about **control + compliance**

---

## 🔥 Pattern you should now recognize

|Question type|Hidden answer|
|---|---|
|“sequential validation”|ordered pipeline|
|“approval between steps”|Step Functions|
|“compare models”|A/B testing|
|“evaluation rigor”|metrics first|

---

You’re consistently getting these right—this is strong exam readiness.

👉 Say **“proceed”** and we go to Q10 🚀

10/20 Question A company is developing an AI assistant that processes customer data by using Amazon Bedrock. The AI assistant has multiple guardrails. The guardrails include prompt injection detection, sensitive information filtering, and denied topic blocking. When a customer query is blocked, a GenAI developer needs a detailed analysis of which specific guardrail rule was invoked and why the content was flagged. Then, the GenAI developer must fine-tune guardrail configurations and distinguish between legitimate customer queries and actual security threats. Which configuration provides the MOST detailed analysis of guardrail decision-making for content filtering? **A** Enable Amazon Bedrock model evaluation with automated evaluation jobs that include guardrail assessment metrics. Configure the evaluation framework to test prompt injection resistance by using company-specific test cases. Use the evaluation dashboard to analyze which guardrail policies are most effective at blocking malicious content while preserving legitimate queries. Incorrect. Amazon Bedrock model evaluation provides analysis based on measurable tests. Model evaluation can create a report about correctness, toxicity, accuracy, and other parameters during evaluation. However, you would not use Amazon Bedrock model evaluation during inference. Learn more about ++[Amazon Bedrock model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html)++. **B** Enable Amazon Bedrock model invocation logging to capture full request and response data. Configure Amazon CloudWatch alarms on InvocationsIntervened metrics filtered by GuardrailContentSource dimensions. Analyze patterns by using CloudWatch Insights queries to identify which content source triggered interventions. Incorrect. Amazon Bedrock model invocation logging can log the input, output, and metadata of invocations. However, model invocation logging does not provide details about guardrail interventions. Learn more about ++[how to monitor model invocations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)++. **C** Configure guardrail tracing with `{"trace": "enabled"}` in guardrailConfig. Monitor InvocationsIntervened metrics filtered by the GuardrailContentSource dimension to identify whether input prompts or output responses triggered interventions. Incorrect. The GuardrailContentSource dimension can distinguish between input and output. However, this dimension does not indicate the layer of the guardrail that intervened. Learn more about ++[CloudWatch metrics to monitor Amazon Bedrock guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-guardrails-cw-metrics.html)++. Learn more about ++[the Converse API and setting up guardrailConfig](https://docs.aws.amazon.com/cli/latest/reference/bedrock-runtime/converse.html)++. Learn more about ++[Converse and guardrailConfig](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/converse.html)++. **D** Configure guardrail tracing with `{"trace": "enabled"}` in guardrailConfig. Monitor InvocationsIntervened metrics filtered by the GuardrailPolicyType dimensions: ContentPolicy, TopicPolicy, and SensitiveInformationPolicy. # Correct. GuardrailPolicyType provides detailed information on which policy intervened in the guardrail. The GenAI developer can use this configuration to make an informed decision based on specific metrics. Learn more about ++[CloudWatch metrics to monitor Amazon Bedrock guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-guardrails-cw-metrics.html)++. Learn more about ++[the Converse API and setting up guardrailConfig](https://docs.aws.amazon.com/cli/latest/reference/bedrock-runtime/converse.html)++. Learn more about ++[Converse and guardrailConfig](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/converse.html)++.

---

This is a **precision observability question**—they’re testing how deep you can go into **guardrail debugging**.

---

# ✅ Q10 — Core Concept

### 👉 High-level

This tests:

> **“How do you get _fine-grained visibility_ into WHICH guardrail triggered and WHY?”**

---

# 🧠 Key Concept (under 200 words)

For **guardrail debugging**, you need **two layers**:

---

## 1️⃣ Enable tracing

{"trace": "enabled"}

This turns on **detailed decision tracking** inside Bedrock guardrails.

---

## 2️⃣ Use the RIGHT dimension for analysis

### 🔑 Critical dimension:

**GuardrailPolicyType**

This tells you:

- `ContentPolicy` → toxicity / harmful content
- `TopicPolicy` → denied topics
- `SensitiveInformationPolicy` → PII / secrets

---

👉 Why this matters:

- You don’t just know _something was blocked_
- You know **exactly WHICH rule triggered**

---

### Contrast:

|Dimension|What it tells you|
|---|---|
|GuardrailContentSource|input vs output ❌|
|GuardrailPolicyType|WHICH rule triggered ✅|

---

# 🧠 Mental Model

Tracing = visibility  
PolicyType = root cause

---

# 🏗️ Architecture (ASCII)

        User Input  
             │  
             ▼  
     Bedrock Guardrails  
   ┌─────────┼─────────┐  
   │         │         │  
Content   Topic    Sensitive Info  
Policy    Policy      Policy  
   │         │         │  
   └───────Decision────┘  
             │  
     Trace Enabled ✅  
             │  
             ▼  
   CloudWatch Metrics  
   (GuardrailPolicyType)  
             │  
             ▼  
   Root cause analysis

---

# 🎯 Why D is correct

### ✅ D — Trace + PolicyType

✔ Enables tracing  
✔ Identifies **exact guardrail layer**  
✔ Supports tuning + debugging

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|Evaluation ≠ runtime debugging|
|B|Invocation logs ≠ guardrail logic|
|C|ContentSource only = input/output, not rule|

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### When you see:

|Requirement|Answer|
|---|---|
|“which guardrail triggered”|PolicyType|
|“debug guardrails”|tracing enabled|
|“input vs output issue”|ContentSource|
|“full prompt/response”|invocation logs|

---

# ⚡ Golden Rule

Need root cause of guardrail?  
→ Enable trace + use PolicyType

---

# 🧪 Mini Quiz

### Q1

You want to know **if the issue came from input vs output filtering**. What do you use?

A. PolicyType  
B. ContentSource  
C. Invocation logs  
D. CloudTrail

---

### Q2

You want to know **which guardrail rule blocked the request**. What do you use?

A. ContentSource  
B. PolicyType  
C. Temperature  
D. Step Functions

---

Reply with answers + say **“proceed”** → Q11 🚀

1 b 2b

Almost perfect—just one small correction 👇

---

## 🔍 Q1

### Your answer: **B (ContentSource)** ❌

### Correct: **B (ContentSource)** ✅

✔ You got it right:

> ContentSource = input vs output

---

## 🔍 Q2

### Your answer: **B (PolicyType)** ✅

✔ Correct:

> PolicyType = WHICH guardrail triggered

---

# 🧠 Lock this final distinction (important)

ContentSource → where? (input vs output)  
PolicyType    → why?  (which rule triggered)

---

## ⚡ This is subtle but high-value

Think like debugging:

|Question you ask|Dimension|
|---|---|
|“Was it input or output?”|ContentSource|
|“Which rule blocked it?”|PolicyType|

---

## 🧠 Why this matters in real systems

When tuning guardrails:

- First → identify source (input vs output)
- Then → identify rule (policy type)
- Then → adjust thresholds / prompts

---

You’re now operating at **fine-grained observability level**—this is advanced.

👉 Say **“proceed”** and we go to Q11 🚀

11/20 Question A company is implementing AI governance policies. The policies require all FM interactions to be secured with guardrails. The company configures Amazon Bedrock guardrails. The company must ensure that all InvokeModel and Converse API calls to FMs apply the guardrails. Which solution will enforce guardrail compliance for the API calls in the MOST operationally efficient way? **A** Configure IAM policies for the InvokeModel and Converse API calls with both bedrock:GuardrailIdentifier and bedrock:PromptRouterArn condition keys. Apply the policies to all IAM roles. Require prompt router validation before allowing access to Amazon Bedrock FMs. Incorrect. The PromptRouterArn condition key is designed to filter access by the specified prompt router. The prompt router manages prompt templates and configurations. This condition key is unrelated to guardrail enforcement. Using both conditions creates more complex IAM policies to maintain without providing additional security benefits. Learn more about ++[condition keys](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html#amazonbedrock-bedrock_PromptRouterArn)++. **B** Create an AWS Lambda function that validates and enforces guardrails before proxying requests to Amazon Bedrock. Use the Lambda function as the exclusive endpoint for all FM interactions. ## Incorrect. Creating a Lambda function to proxy and validate all requests introduces an additional point of failure and a potential performance bottleneck. You must maintain custom code for guardrail enforcement. Therefore, this solution is less operationally efficient and more error-prone than using built-in capabilities. Learn more about ++[Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)++. **C** Store guardrail identifiers in AWS Systems Manager Parameter Store. Create an AWS Lambda function that retrieves the guardrail identifier from Parameter Store each time before making calls to Amazon Bedrock FMs. Incorrect. Parameter Store provides a centralized location to store guardrail identifiers. However, using a Lambda function to retrieve the identifier for each API call adds additional operational overhead and latency. You must create and maintain the Lambda function. This solution requires the retrieval of the guardrail identifier each time before making a call to the model. Learn more about ++[Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)++. Learn more about ++[Amazon API Gateway Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)++. **D** Configure IAM policies for the InvokeModel and Converse API calls with the bedrock:GuardrailIdentifier condition key. Apply the policies to all IAM roles that access the Amazon Bedrock FMs. ## Correct. This solution uses IAM policies with the bedrock:GuardrailIdentifier condition key to enforce guardrail compliance for InvokeModel and Converse API calls. IAM policies are a centralized and efficient way to control access to AWS resources. You can apply the policies to roles that access Amazon Bedrock FMs. This solution ensures that guardrails are consistently applied across all relevant API calls in the most operationally efficient way. Learn more about ++[guardrail enforcement during inference](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-permissions-id.html)++. Learn more about ++[using IAM policies with Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_service-with-iam.html)++. Learn more about ++[condition keys](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html#amazonbedrock-bedrock_PromptRouterArn)++.

---

This is a **governance enforcement pattern question**—and the key phrase is:

> **“MOST operationally efficient”**

---

# ✅ Q11 — Core Concept

### 👉 High-level

This tests:

> **“How do you enforce guardrails centrally without adding custom components?”**

---

# 🧠 Key Concept (under 200 words)

The best way to enforce policies in AWS is:

### 🔑 **Use IAM, not custom code**

---

## Guardrail enforcement mechanism

Amazon Bedrock supports:

### 👉 `bedrock:GuardrailIdentifier` (IAM condition key)

This allows you to:

- enforce that **every model call MUST include a guardrail**
- block requests that don’t specify it

---

### Why this is optimal:

- ✅ Centralized enforcement
- ✅ No extra services (Lambda, API Gateway)
- ✅ No latency overhead
- ✅ No custom logic to maintain

---

👉 Exam principle:

If AWS provides a native control → use it over custom solutions

---

# 🧠 Mental Model

Security enforcement layers:  
  
Best → IAM policy  
Okay → service config  
Worst → custom code (Lambda)

---

# 🏗️ Architecture (ASCII)

        Application / Users  
                │  
                ▼  
           IAM Policy  
   (GuardrailIdentifier required)  
                │  
                ▼  
        Bedrock API Calls  
      (InvokeModel / Converse)  
                │  
      Guardrail enforced ✅  
                │  
                ▼  
          Foundation Model

---

# 🎯 Why D is correct

### ✅ D — IAM + GuardrailIdentifier

✔ Enforces guardrails on ALL calls  
✔ No custom code  
✔ Centralized governance  
✔ Lowest operational overhead

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|Adds unnecessary PromptRouter complexity|
|B|Lambda proxy = extra layer + bottleneck|
|C|Parameter Store + Lambda = overhead + latency|

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### When you see:

|Requirement|Answer|
|---|---|
|“enforce policy”|IAM|
|“least operational overhead”|avoid Lambda|
|“central control”|IAM condition keys|
|“guardrails required”|GuardrailIdentifier|

---

# ⚡ Golden Rule

Enforcement → IAM  
Customization → Lambda

---

# 🧪 Mini Quiz

### Q1

You must ensure **all Bedrock calls include a guardrail**. What do you use?

A. Lambda proxy  
B. IAM condition key  
C. API Gateway  
D. CloudWatch

---

### Q2

Why is IAM preferred over Lambda for enforcement?

A. Faster model  
B. Lower latency and no maintenance  
C. Better embeddings  
D. More storage

---

Reply with answers + say **“proceed”** → Q12 🚀

what is the AWS Lakehouse solution

Great question—this is **core architecture thinking** (and shows up indirectly in the exam a lot).

---

# 🧠 High-Level Concept

### 👉 What is a Lakehouse?

A **Lakehouse = Data Lake + Data Warehouse combined**

It gives you:

- **flexibility of a data lake (S3)**
- **performance & structure of a warehouse (SQL, ACID, governance)**

---

# ⚡ Simple Intuition

Data Lake     → cheap, flexible, messy  
Warehouse     → structured, governed, expensive  
  
Lakehouse     → flexible + structured + governed ✅

---

# 🏗️ AWS Lakehouse Architecture

            Data Sources  
      (apps, logs, APIs, IoT)  
                │  
                ▼  
        Amazon S3 (Data Lake)  
        ────────────────────  
        Raw / Curated / Semantic  
                │  
        ┌───────┼────────┐  
        ▼                ▼  
   AWS Glue         Lake Formation  
 (catalog + ETL)   (governance)  
        │                │  
        └───────┬────────┘  
                ▼  
        Query / Processing Layer  
   ┌────────────┼────────────┐  
   ▼            ▼            ▼  
 Athena     Redshift     EMR / Spark  
                │  
                ▼  
        BI / AI / GenAI Apps  
      (QuickSight, Bedrock)

---

# 🧩 Key AWS Components

### 1. Storage (foundation)

- **Amazon S3**
    - raw + curated data
    - cheap, scalable

---

### 2. Metadata & Catalog

- **AWS Glue Data Catalog**
    - schema
    - table definitions
    - discovery

---

### 3. Governance

- **AWS Lake Formation**
    - fine-grained access control
    - data security
    - auditing

---

### 4. Query & Processing

- **Athena** → serverless SQL
- **Redshift** → warehouse performance
- **EMR / Spark** → big data processing

---

### 5. AI / GenAI Layer

- **Bedrock / SageMaker**
    - RAG pipelines
    - embeddings
    - model inference

---

# 🔥 Why Lakehouse matters (especially for GenAI)

For your exam + real-world:

👉 GenAI needs:

- structured + unstructured data
- governed access
- scalable retrieval (RAG)

Lakehouse provides:

- ✅ unified data platform
- ✅ governed semantic layer
- ✅ perfect base for RAG

---

# 🧠 Mental Model (important)

Lakehouse = System of record for GenAI  
  
S3 = storage  
Glue = metadata  
Lake Formation = control  
Athena/Redshift = access  
Bedrock = intelligence

---

# ⚡ Exam Angle (how it shows up)

You won’t see “Lakehouse” directly often, but:

|If question mentions|Think|
|---|---|
|S3 + Glue + Lake Formation|Lakehouse|
|governed data access|Lake Formation|
|RAG + enterprise data|Lakehouse|
|semantic layer|curated datasets|

---

# 🧪 Quick Quiz

### Q1

Which service provides **fine-grained access control in a lakehouse**?

A. S3  
B. Glue  
C. Lake Formation  
D. Athena

---

### Q2

Which service acts as the **central metadata catalog**?

A. Redshift  
B. Glue Data Catalog  
C. Kinesis  
D. Lambda

---

If you want, next step I can:  
👉 map **Lakehouse → your AI copilot architecture (very powerful insight)**

Review Lake Formation

Perfect—this is a **must-know service** for both the exam and your architecture thinking.

---

# 🧠 1. What is AWS Lake Formation (concept first)

### 👉 High-level

**AWS Lake Formation = Governance layer on top of your data lake (S3)**

It turns:

Messy S3 data lake → Governed, secure, queryable data platform

---

# ⚡ Simple intuition

S3 = storage  
Glue = metadata  
Lake Formation = CONTROL (who can see what)

---

# 🏗️ 2. Where it sits in architecture

        Data Sources  
             │  
             ▼  
           S3 (Data Lake)  
             │  
     ┌───────┼────────┐  
     ▼                ▼  
  Glue Catalog   Lake Formation  
 (tables/schema) (permissions)  
     │                │  
     └───────┬────────┘  
             ▼  
   Athena / Redshift / EMR  
             │  
             ▼  
        Users / Apps / AI

---

# 🔑 3. Core Capabilities

## 1️⃣ Fine-grained access control

- Table-level
- Column-level
- Row-level (via filters)

👉 Example:

- Finance team → only `/finance` data
- Analysts → masked PII columns

---

## 2️⃣ Centralized governance

- One place to manage permissions
- Works across:
    - Athena
    - Redshift Spectrum
    - EMR

---

## 3️⃣ Data catalog integration

- Built on **Glue Data Catalog**
- Uses metadata for enforcement

---

## 4️⃣ Auditing & compliance

- Tracks:
    - who accessed data
    - what queries were run

---

## 5️⃣ Data lake setup automation

- Create DB
- Register S3 paths
- Apply permissions

---

# 🧠 Mental Model (important)

Lake Formation = IAM for DATA

👉 Instead of:

- IAM → controls access to services
- Lake Formation → controls access to DATA inside S3

---

# 🔥 4. Why it matters for GenAI (very relevant to you)

For your **AI copilot / RAG system**:

Without Lake Formation:

LLM can access raw S3 → risky ❌

With Lake Formation:

LLM → only certified / governed data ✅

---

👉 This aligns exactly with your:

- semantic layer
- certified views
- governed AI approach

---

# ⚠️ 5. Common Exam Traps

|Trap|Reality|
|---|---|
|“Use IAM for data access”|❌ Use Lake Formation|
|“S3 bucket policy is enough”|❌ Not fine-grained|
|“Glue controls access”|❌ Only metadata|
|“Lake Formation is optional”|❌ Required for governance|

---

# ⚡ 6. When to use Lake Formation (exam triggers)

If you see:

|Requirement|Answer|
|---|---|
|Fine-grained data access|Lake Formation|
|Column/row-level security|Lake Formation|
|Data lake governance|Lake Formation|
|Compliance / audit|Lake Formation|

---

# 🧪 Mini Quiz

### Q1

You need to restrict access to **specific columns (PII)** in S3 data. What do you use?

A. IAM  
B. S3 bucket policy  
C. Lake Formation  
D. Glue

---

### Q2

Which service actually **stores metadata for Lake Formation**?

A. Athena  
B. Glue Data Catalog  
C. DynamoDB  
D. Redshift

---

If you want next level:  
👉 I can map **Lake Formation → your governed GenAI architecture (this is exactly what enterprises expect)**

1 c, 2b

Perfect—both correct ✅

---

## 🔍 Quick reinforcement

### Q1 → **C (Lake Formation)**

✔ Column-level (PII masking)  
✔ Fine-grained control

---

### Q2 → **B (Glue Data Catalog)**

✔ Stores schema + tables  
✔ Lake Formation enforces on top

---

# 🧠 Lock this relationship (VERY important)

Glue = metadata (what data is)  
Lake Formation = permissions (who can access it)  
S3 = storage (where data lives)

---

## ⚡ One level deeper (this is the real architecture thinking)

Think of it like layers:

S3              → raw data  
Glue Catalog    → structure (tables)  
Lake Formation  → control (security)  
Athena/Redshift → consumption

---

## 🔥 Why this matters for your GenAI / RAG setup

This is exactly your pattern:

Ungoverned RAG:  
LLM → raw S3 ❌ (risk, hallucination, PII leak)  
  
Governed RAG:  
LLM → certified views → Lake Formation enforced ✅

👉 This is literally:

> **Enterprise GenAI = RAG + Governance (Lake Formation / Collibra-like)**

---

## ⚡ Exam-level insight

If you see:

- “governed data access”
- “restrict by column / row”
- “data lake security”
- “compliance”

👉 90% of the time → **Lake Formation**

---

You’ve now covered:

- RAG failures
- guardrails
- event-driven ingestion
- real-time architectures
- governance (Lake Formation)

👉 That’s already **a big chunk of the exam**.

---

If you want:  
👉 we can continue to Q11+  
or  
👉 I can give you a **10-question mock exam at this difficulty level**

Lake Formation vs Collibra

Great comparison—this is exactly the **platform vs governance plane** distinction you’ve been thinking about.

---

# 🧠 High-Level Concept

### 👉 Short answer

Lake Formation = enforcement (runtime, AWS-native)  
Collibra       = governance (enterprise-wide, business layer)

They solve **different layers of the same problem**.

---

# ⚡ Simple intuition

Lake Formation → "Can you access this data?"  
Collibra       → "What is this data and should you use it?"

---

# 🏗️ Architecture View (together)

          Business / Governance Layer  
        ┌────────────────────────────┐  
        │        Collibra            │  
        │ - Glossary                │  
        │ - Data ownership          │  
        │ - Policies                │  
        │ - Lineage                │  
        └────────────┬─────────────┘  
                     │  
                     ▼  
          Enforcement / Runtime Layer  
        ┌────────────────────────────┐  
        │     Lake Formation         │  
        │ - Access control           │  
        │ - Row/column security      │  
        │ - Audit                   │  
        └────────────┬─────────────┘  
                     │  
                     ▼  
                 S3 / Data Lake

---

# 📊 Side-by-side Comparison

|Area|Lake Formation|Collibra|
|---|---|---|
|Type|AWS service|Enterprise tool|
|Role|Enforcement|Governance|
|Scope|AWS data lake|Enterprise-wide|
|Controls|Row/column access|Policies, stewardship|
|Metadata|Uses Glue|Full business catalog|
|Users|Engineers|Data stewards, business|
|Runtime|Yes|No|

---

# 🔑 Key Differences (exam + real world)

## 1️⃣ Enforcement vs Definition

- **Lake Formation**
    - enforces access at query time
    - blocks/filters data
- **Collibra**
    - defines rules (policies, glossary)
    - does NOT enforce directly

---

## 2️⃣ Technical vs Business layer

- Lake Formation → technical security
- Collibra → business meaning

Example:

Collibra:  
"Customer = active account holder (business definition)"  
  
Lake Formation:  
User X cannot access customer_email column

---

## 3️⃣ Scope

- Lake Formation → AWS only
- Collibra → multi-platform (Snowflake, Databricks, AWS, etc.)

---

# 🔥 How they work together (THIS is the real answer)

Collibra → defines policy  
Lake Formation → enforces policy

---

### Example (your GenAI use case)

Collibra:  
- defines "PII"  
- marks datasets as "certified"  
- tracks lineage  
  
Lake Formation:  
- masks PII columns  
- restricts access to certified datasets only

---

# 🧠 Mental Model (important)

Collibra = brain (decides rules)  
Lake Formation = muscle (enforces rules)

---

# ⚡ Exam Angle

You won’t see Collibra directly, but:

|If question says|Think|
|---|---|
|governance, glossary, lineage|Collibra-like|
|access control, row/column security|Lake Formation|
|enforce permissions in AWS|Lake Formation|

---

# 🧪 Quick Quiz

### Q1

Which tool enforces **column-level security in S3**?

A. Collibra  
B. Lake Formation  
C. Glue  
D. Athena

---

### Q2

Which tool defines **business meaning and data ownership**?

A. Lake Formation  
B. IAM  
C. Collibra  
D. S3

---

If you want next level:  
👉 I can map this directly into your **“governed GenAI copilot architecture” (this is exactly what interview panels look for)**

1 b 2c

Perfect—both correct ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (Lake Formation)**

✔ Enforces column-level security  
✔ Runtime access control

---

### Q2 → **C (Collibra)**

✔ Defines business meaning  
✔ Ownership + governance

---

# 🧠 Lock this (this is _architect-level thinking_)

Collibra       → define (what, why, who owns)  
Lake Formation → enforce (who can access)

---

## ⚡ The insight that matters (this is your edge)

Most people treat these as competing tools ❌  
You’re now thinking of them as **layers** ✅

---

## 🏗️ Your exact architecture (what you’ve been building)

Business Layer (Collibra mindset)  
- glossary.yaml  
- certification rules  
- semantic definitions  
  
↓  
  
Enforcement Layer (Lake Formation equivalent)  
- access control  
- PII masking  
- dataset-level permissions  
  
↓  
  
Consumption Layer  
- RAG / Copilot / Bedrock

---

## 🔥 Why this is powerful for your positioning

This is exactly how you differentiate:

> ❌ “I build AI apps”  
> ✅ “I build governed AI systems where data meaning and access are controlled end-to-end”

---

## ⚡ One sentence you can reuse (interview / LinkedIn)

> “Collibra defines what data means and who owns it; Lake Formation enforces who can actually access it at runtime—both are required for enterprise-grade GenAI.”

---

You’ve now connected:

- RAG
- Guardrails
- Event-driven pipelines
- Evaluation
- Governance (Collibra + Lake Formation)

👉 That’s **top-tier exam + real-world alignment**

---

If you want next:  
👉 continue Q12  
or  
👉 I can simulate a **hard scenario question combining RAG + governance + guardrails (very exam-like)**

Lake Formation vs Redshift/Athena

Great comparison—this is a **layering question** (control vs compute).

---

# 🧠 High-Level Concept

Lake Formation → WHO can access data  
Athena/Redshift → HOW data is queried

👉 They are **not competitors**—they work together.

---

# ⚡ Simple intuition

Lake Formation = security guard 🚫  
Athena/Redshift = query engine 🔍

---

# 🏗️ Architecture View (together)

        Users / Apps / BI / GenAI  
                    │  
                    ▼  
        Athena / Redshift (SQL engines)  
                    │  
        (requests data access)  
                    │  
                    ▼  
         Lake Formation (checks permissions)  
                    │  
                    ▼  
               S3 Data Lake

---

# 📊 Side-by-side Comparison

|Area|Lake Formation|Athena|Redshift|
|---|---|---|---|
|Role|Governance / access control|Serverless query|Data warehouse|
|Purpose|Security & permissions|Query S3|High-perf analytics|
|Data storage|❌ No|❌ No|✅ Yes (also S3 external)|
|SQL engine|❌|✅|✅|
|Row/column security|✅|❌ (delegates)|❌ (delegates to LF if using S3)|
|Cost model|Free (control plane)|Pay per query|Cluster / serverless|

---

# 🔑 Key Differences

## 1️⃣ Control vs Compute

- **Lake Formation**
    - enforces access
    - does NOT query data
- **Athena / Redshift**
    - query data
    - rely on Lake Formation for permissions

---

## 2️⃣ Serverless vs Warehouse

- **Athena**
    - serverless SQL on S3
    - best for ad-hoc queries
- **Redshift**
    - high-performance warehouse
    - best for BI / dashboards

---

## 3️⃣ Data location

- Lake Formation → governs S3
- Athena → queries S3
- Redshift → stores data (and can query S3 via Spectrum)

---

# 🔥 How they work together (this is the real answer)

User → Athena query  
       ↓  
Lake Formation checks permissions  
       ↓  
If allowed → query S3 data  
       ↓  
Return results

---

# 🧠 Mental Model (important)

Lake Formation = gatekeeper  
Athena         = reader  
Redshift       = optimized analytics engine

---

# ⚡ Example (GenAI / RAG)

RAG pipeline:  
  
S3 (documents)  
  ↓  
Lake Formation (restrict access)  
  ↓  
Athena / OpenSearch / Bedrock retrieval  
  ↓  
LLM

👉 Without Lake Formation:

- LLM may access sensitive data ❌

---

# ⚠️ Exam Traps

|Trap|Reality|
|---|---|
|“Use Athena for security”|❌ Use Lake Formation|
|“Redshift controls access to S3”|❌ Lake Formation does|
|“Lake Formation queries data”|❌ Athena/Redshift do|

---

# 🧪 Mini Quiz

### Q1

You need to run SQL queries on S3 with **no infrastructure management**. What do you use?

A. Lake Formation  
B. Athena  
C. Redshift  
D. Glue

---

### Q2

You need to restrict access to **specific rows of S3 data**. What do you use?

A. Athena  
B. Redshift  
C. Lake Formation  
D. Lambda

---

If you want next:  
👉 I can map **Lakehouse + RAG + Bedrock into one clean enterprise diagram (very useful for your exam + interviews)**

1b 2c

Perfect—both correct ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (Athena)**

✔ Serverless SQL on S3  
✔ No infra to manage

---

### Q2 → **C (Lake Formation)**

✔ Row-level security  
✔ Fine-grained access control

---

# 🧠 Lock the architecture (this is the key takeaway)

Lake Formation → controls access  
Athena         → queries data  
Redshift       → optimizes analytics

---

## ⚡ The real insight (this is architect-level)

These are **stacked, not competing**:

User → Athena query  
        ↓  
Lake Formation checks permissions  
        ↓  
S3 data accessed (if allowed)

---

## 🔥 Why this matters for your GenAI work

This is exactly how you should think about **governed RAG**:

LLM / Bedrock  
      ↓  
Query layer (Athena / OpenSearch)  
      ↓  
Lake Formation (enforces access)  
      ↓  
S3 (data)

👉 This ensures:

- no PII leakage
- only certified data used
- compliance-ready AI

---

## ⚡ Exam shortcut (memorize this)

|Requirement|Service|
|---|---|
|Query S3 with SQL|Athena|
|Data warehouse analytics|Redshift|
|Data lake security|Lake Formation|

---

You’ve now nailed:

- governance layer
- query layer
- enforcement vs compute

👉 This is **exactly how AWS expects you to reason**

---

If you’re ready:  
👉 say **“proceed”** and we’ll continue with Q12 🚀

map Lakehouse + RAG + Bedrock into one clean enterprise ascii diagram

Love this—this is exactly how you _tie everything together_ into an enterprise-grade GenAI platform.

---

# 🧠 Concept First (big picture)

Lakehouse = governed data foundation  
RAG       = retrieval layer  
Bedrock   = intelligence layer

👉 Together:

Governed Data → Retrieval → LLM → Answer

---

# 🏗️ Enterprise Lakehouse + RAG + Bedrock (clean ASCII)

┌──────────────────────────────────────────────────────────────┐  
│                  LAYER 1 — EXPERIENCE                        │  
│  Web App / Chat UI / API / Copilot                          │  
└───────────────────────────┬──────────────────────────────────┘  
                            │  
                            ▼  
┌──────────────────────────────────────────────────────────────┐  
│               LAYER 2 — APPLICATION / ORCHESTRATION          │  
│  API Gateway / Lambda / Step Functions                      │  
│  - Prompt construction                                      │  
│  - Query routing                                            │  
│  - Guardrails + policies                                    │  
└───────────────┬───────────────────────────────┬──────────────┘  
                │                               │  
                ▼                               ▼  
┌──────────────────────────────┐   ┌───────────────────────────┐  
│     LAYER 3 — RAG / SEARCH   │   │   LAYER 4 — LLM (BEDROCK) │  
│  OpenSearch / KB / Retriever │   │  Claude / Titan / Llama   │  
│  - Vector search             │   │  - Generation             │  
│  - Hybrid search             │   │  - Guardrails             │  
└───────────────┬──────────────┘   └──────────────┬────────────┘  
                │                               │  
                └──────────────┬────────────────┘  
                               ▼  
                   Context + Prompt + Query  
                               │  
                               ▼  
┌──────────────────────────────────────────────────────────────┐  
│        LAYER 5 — LAKEHOUSE (DATA FOUNDATION)                 │  
│                                                              │  
│   ┌──────────────────────────────────────────────────────┐   │  
│   │ Amazon S3 (RAW / CURATED / SEMANTIC)                │   │  
│   └───────────────┬─────────────────────────────────────┘   │  
│                   │                                         │  
│   ┌───────────────▼──────────────┐   ┌───────────────────┐  │  
│   │ Glue Data Catalog            │   │ Lake Formation    │  │  
│   │ - schema / tables            │   │ - row/column ACL  │  │  
│   │ - metadata                   │   │ - governance      │  │  
│   └───────────────┬──────────────┘   └─────────┬─────────┘  │  
│                   │                            │            │  
│                   └──────────────┬─────────────┘            │  
│                                  ▼                          │  
│                  Athena / Redshift / ETL                    │  
│                  (query + transformation layer)             │  
└──────────────────────────────────────────────────────────────┘  
  
                         ▲  
                         │  
         Embedding + Index Pipeline (Event-driven)  
                         │  
┌──────────────────────────────────────────────────────────────┐  
│      INGESTION / INDEXING PIPELINE                          │  
│  S3 → EventBridge/SQS → Lambda → Bedrock Embeddings         │  
│      → OpenSearch / Vector Store                            │  
└──────────────────────────────────────────────────────────────┘

---

# 🔥 How to read this (important)

## 1️⃣ Bottom = Truth layer (Lakehouse)

- S3 = data
- Glue = structure
- Lake Formation = governance

👉 **This is your governed source of truth**

---

## 2️⃣ Middle = Retrieval (RAG)

- embeddings
- vector search
- hybrid retrieval

👉 **This controls what context goes into LLM**

---

## 3️⃣ Right = Intelligence (Bedrock)

- FM (Claude, Titan)
- Guardrails
- Prompt logic

👉 **This generates answers**

---

## 4️⃣ Top = Application layer

- API Gateway + Lambda
- orchestration
- streaming / WebSocket

👉 **This delivers user experience**

---

# ⚡ Critical Insight (this is what most people miss)

LLM does NOT access S3 directly ❌  
LLM ONLY sees retrieved + governed context ✅

---

# 🧠 Your architecture (mapped directly)

This diagram is basically:

Your design:  
- dataset_register.yaml → Glue / semantic layer  
- certified views       → Lake Formation concept  
- retrieve_context.py   → RAG layer  
- build_sql / execute   → query layer  
- llm_generate          → Bedrock

👉 You’ve already built this pattern.

---

# 🔥 One-line summary (use this in interviews)

> “Enterprise GenAI is a layered system where a governed lakehouse feeds a retrieval layer, which constrains what the LLM can see, ensuring secure and explainable AI outputs.”

---

If you want next level:  
👉 I can turn this into a **1-page exam cheat sheet (all patterns combined)** or  
👉 simulate a **full architecture question combining all layers (very close to exam difficulty)**

12/20 Question An ecommerce company has an application that uses Amazon Bedrock to generate product descriptions and recommendations. Currently, the application resides in a single AWS Region. When invoking a model in Amazon Bedrock during peak periods, the application receives an error. The error message says, "Too many requests, please wait before trying again." The company must increase the throughput for invocations during peak periods without introducing additional operational overhead. The company must maintain compatibility with the existing Amazon Bedrock API. The company must use the same FM. Which solution will meet these requirements in the MOST cost-effective way? **A** Create an AWS Lambda function to invoke the model in Amazon Bedrock with the original Region as the default. Configure the Lambda function to fall back to Amazon Bedrock in a secondary Region. Incorrect. You can create a Lambda function to invoke an Amazon Bedrock model. The Lambda function is an intermediary that you must manage and maintain. Therefore, this solution increases cost and operational overhead compared to using a built-in feature of Amazon Bedrock. Learn more about ++[Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)++. **B** Use cross-Region inference to distribute traffic across multiple Regions within a geographic area. Correct. Cross-Region inference automatically distributes traffic across multiple Regions within your geographic area to process your inference request. Learn more about ++[cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)++. **C** Use prompt routing to distribute traffic across multiple FMs from the same family. Incorrect. Amazon Bedrock intelligent prompt routing provides a single endpoint to efficiently route requests between different FMs within the same model family. This solution requires at least two different models from the same family. The models cannot be exactly the same. However, the company in the scenario must use the same FM. Learn more about ++[intelligent prompt routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html)++. **D** Use provisioned throughput to provision a higher level of throughput for the FM. Incorrect. Provisioned throughput will provide higher throughput for the number of I/O rates that a model can process. However, the application needs a solution for peak periods, not for consistent usage. Learn more about ++[provisioned throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html)++.

---

This is a **throughput + scaling pattern question**—very typical in the exam.

---

# ✅ Q12 — Core Concept

### 👉 High-level

This tests:

> **“How do you handle Bedrock throttling (TooManyRequests) with minimal ops + cost?”**

---

# 🧠 Key Concept (under 200 words)

The error:

> **“Too many requests” = throttling**

So you need:

- more capacity
- but **only during peaks**
- with **no extra infrastructure**

---

## 🔑 Best solution: **Cross-Region Inference**

- Automatically distributes requests across multiple regions
- Uses the **same FM**
- No code change needed
- No infra to manage

---

### Why this works:

Instead of:  
All traffic → 1 Region ❌ (bottleneck)  
  
Do:  
Traffic → multiple Regions ✅ (load distributed)

---

### Contrast:

|Option|Problem|
|---|---|
|Lambda fallback|adds ops + cost|
|Prompt routing|different models (not allowed)|
|Provisioned throughput|overkill for peak-only|

---

👉 Exam principle:

Elastic scaling → use managed feature (not custom code)

---

# 🧠 Mental Model

Peak traffic?  
→ Spread load (cross-region)  
  
Constant traffic?  
→ Provision capacity

---

# 🏗️ Architecture (ASCII)

         Application  
              │  
              ▼  
     Bedrock API (same model)  
              │  
   ┌──────────┼──────────┐  
   ▼          ▼          ▼  
Region A   Region B   Region C  
  FM          FM          FM  
              │  
       Load distributed

---

# 🎯 Why B is correct

### ✅ B — Cross-Region Inference

✔ Handles peak spikes  
✔ Same FM  
✔ No infra  
✔ Cost-efficient (on-demand scaling)

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|Lambda = extra layer|
|C|Requires different models|
|D|Provisioned = always-on cost|

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### When you see:

|Requirement|Answer|
|---|---|
|“Too many requests”|scaling issue|
|“peak periods”|elastic solution|
|“same model”|no routing|
|“least overhead”|managed feature|

---

# ⚡ Golden Rule

Peak scaling → Cross-Region inference  
Steady scaling → Provisioned throughput

---

# 🧪 Mini Quiz

### Q1

You have **constant high traffic all day**. What should you use?

A. Cross-region inference  
B. Provisioned throughput  
C. Lambda fallback  
D. SQS

---

### Q2

You need to reduce throttling but **keep cost low for spiky traffic**. What do you use?

A. Provisioned throughput  
B. Cross-region inference  
C. Redshift  
D. EventBridge

---

Reply with answers + say **“proceed”** → Q13 🚀

1 b 2 b

Perfect—both correct again ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (Provisioned throughput)**

✔ Constant load → reserve capacity  
✔ predictable performance

---

### Q2 → **B (Cross-region inference)**

✔ Handles spikes  
✔ no idle cost

---

# 🧠 Lock this (this WILL appear in exam)

Traffic pattern → Solution  
  
Spiky / bursty → Cross-region inference  
Steady / constant → Provisioned throughput

---

## ⚡ Deeper intuition (this is where people lose marks)

### Think in terms of **capacity strategy**

Provisioned throughput  
= pre-buy capacity (like reserved seats)  
  
Cross-region inference  
= spread traffic (like opening more lanes)

---

## 🔥 Subtle exam trick

They often combine these constraints:

|Constraint|Meaning|
|---|---|
|“same FM”|eliminate prompt routing|
|“least cost”|avoid provisioned|
|“peak periods”|avoid always-on|
|“no overhead”|avoid Lambda|

👉 Only one answer survives → **Cross-region inference**

---

## 🧠 You’re now strong at

- scaling strategies
- cost vs performance trade-offs
- managed vs custom solutions

👉 This is **core domain 4 (optimization)**

---

You’re doing really well—this is exam-level reasoning now.

👉 Say **“proceed”** and we go to Q13 🚀

13/20 Question A company needs secure authentication for a third-party application that uses Amazon Bedrock. The solution must integrate with the company's existing identity provider (IdP). The solution must maintain comprehensive audit logs of authentication and API calls. The solution must eliminate long-lived credentials and provide temporary access to Amazon Bedrock. Which solutions will meet these requirements? (Select TWO.) Report Content Errors **A** Implement an OpenID Connect (OIDC) integration with Amazon Cognito. Configure the integration to authenticate users through the IdP and exchange tokens for temporary AWS credentials. Configure the integration to allow the application to access Amazon Bedrock. Correct. Amazon Cognito with OIDC integration provides a secure way to authenticate users through the company's existing IdP. This solution can exchange identity tokens for temporary AWS credentials. Therefore, this solution eliminates long-lived credentials. This solution allows the application to access Amazon Bedrock using short-term credentials and to integrate with an existing IdP. This solution provides comprehensive logging through AWS CloudTrail. Learn more about ++[Amazon Cognito and OIDC](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-oidc-idp.html)++. **B** Configure an Amazon API Gateway Lambda authorizer. Configure the authorizer to validate credentials against the company's LDAP server and then issue signed JSON Web Tokens (JWTs) for Amazon Bedrock access. Incorrect. API Gateway Lambda authorizers can provide authentication. However, this solution does not meet the requirement for temporary AWS credentials. This solution requires custom development to manage credential exchange. This solution does not use built-in integration capabilities for identity federation. Learn more about ++[API Gateway Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)++. **C** Create IAM users for each employee that needs access to the application. Assign permissions through IAM policies. Implement credential rotation by using AWS Secrets Manager. Incorrect. Creating IAM users for each employee does not meet the requirement to eliminate long-lived credentials. Secrets Manager can assist with credential rotation. However, this solution relies on persistent access keys. This solution does not integrate with the existing IdP. This solution does not provide temporary access. Learn more about ++[IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)++. **D** Create an IAM role and configure federation by using AWS STS AssumeRole API calls. Store the application's IAM user credentials in the application configuration. Incorrect. AWS STS AssumeRole allows applications to acquire temporary credentials. However, storing the application's IAM user credentials in the configuration violates the requirement to eliminate long-lived credentials. This solution does not properly integrate with the existing IdP. Learn more about ++[AWS STS temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)++. **E** Deploy AWS IAM Identity Center with SAML federation to the IdP. Configure custom permission sets that grant access to Amazon Bedrock. Correct. IAM Identity Center with SAML federation can provide secure authentication and integration with the IdP. IAM Identity Center provides federation with IdPs. IAM Identity Center eliminates long-lived credentials by providing temporary security credentials. This solution provides audit logging through AWS CloudTrail. This solution meets all the requirements by integrating with the existing IdP while maintaining secure access control. Learn more about ++[IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)++.

---

Nice—this is a **security + identity federation pattern question** (very common in exam).

---

# ✅ Q13 — Core Concept

### 👉 High-level

This tests:

> **“How do you integrate external identity + eliminate long-lived credentials?”**

---

# 🧠 Key Concept (under 200 words)

You need **federated authentication + temporary credentials**.

---

## 🔑 Two valid AWS-native patterns

### 1️⃣ Cognito + OIDC (A)

- integrates with external IdP
- exchanges tokens → temporary AWS credentials
- supports apps (web/mobile/backend)

---

### 2️⃣ IAM Identity Center + SAML (E)

- enterprise SSO
- integrates with corporate IdP
- issues temporary credentials via STS

---

👉 Both:

- ❌ no long-lived credentials
- ✅ federation
- ✅ CloudTrail logging

---

## ❌ What to avoid

- IAM users → long-lived keys ❌
- custom auth (Lambda authorizer) → high ops ❌
- storing credentials → security risk ❌

---

# 🧠 Mental Model

External IdP → Federation → Temporary credentials → AWS access

---

# 🏗️ Architecture (ASCII)

        User / App  
            │  
            ▼  
     External IdP  
 (OIDC / SAML auth)  
            │  
            ▼  
   Cognito / Identity Center  
            │  
   (token exchange via STS)  
            ▼  
   Temporary AWS Credentials  
            │  
            ▼  
        Bedrock API

---

# 🎯 Why A + E are correct

### ✅ A — Cognito + OIDC

✔ App-level integration  
✔ token exchange → temp creds  
✔ IdP integration

---

### ✅ E — IAM Identity Center + SAML

✔ Enterprise SSO  
✔ centralized identity  
✔ temp credentials

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|B|Custom auth, no temp creds|
|C|IAM users = long-lived keys|
|D|Still uses stored credentials|

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### When you see:

|Requirement|Answer|
|---|---|
|“existing IdP”|federation (OIDC / SAML)|
|“no long-lived credentials”|STS / temporary creds|
|“enterprise access”|IAM Identity Center|
|“app authentication”|Cognito|

---

# ⚡ Golden Rule

Never use IAM users for apps or humans  
→ always use federation + temporary credentials

---

# 🧪 Mini Quiz

### Q1

You need **enterprise SSO with existing IdP**. What do you use?

A. Cognito  
B. IAM Identity Center  
C. IAM users  
D. Lambda

---

### Q2

You need **temporary credentials for an app using external login**. What do you use?

A. IAM access keys  
B. Cognito with OIDC  
C. S3 presigned URL  
D. CloudTrail

---

Reply with answers + say **“proceed”** → Q14 🚀

1 b 2 b

Perfect—both correct again ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (IAM Identity Center)**

✔ Enterprise SSO  
✔ integrates with IdP  
✔ temp credentials via STS

---

### Q2 → **B (Cognito + OIDC)**

✔ App-level authentication  
✔ token → temporary AWS credentials

---

# 🧠 Lock this identity pattern (VERY important)

Human users (enterprise) → IAM Identity Center (SAML)  
  
Applications / users → Cognito (OIDC)

---

## ⚡ Deeper intuition (this is exam gold)

### Think in terms of **who is accessing AWS**

|Actor|Service|
|---|---|
|Employees (SSO)|IAM Identity Center|
|App users (web/mobile)|Cognito|
|AWS services|IAM roles|

---

## 🔥 Subtle exam trick

They often mix these:

|Requirement|Eliminate|
|---|---|
|“no long-lived credentials”|IAM users ❌|
|“existing IdP”|must use federation|
|“least overhead”|avoid custom auth|

👉 Leaves only:

- Cognito
- Identity Center

---

## 🧠 What you’ve now mastered

You can now confidently handle:

- federation patterns
- temporary credentials
- security + compliance

👉 This is **Domain 3 (Security & Governance)**

---

You’re very consistent now—this is strong exam readiness.

👉 Say **“proceed”** and we go to Q14 🚀

draw an ascii diagram for Requirement Answer “existing IdP” federation (OIDC / SAML) “no long-lived credentials” STS / temporary creds “enterprise access” IAM Identity Center

Here’s a **clean enterprise-grade ASCII diagram** mapping your requirements → solution pattern:

---

# 🏗️ Federation + Temporary Credentials (Enterprise Pattern)

┌──────────────────────────────────────────────────────────────┐  
│                    ENTERPRISE IDENTITY                       │  
│                                                              │  
│   Existing IdP (Azure AD / Okta / Ping / ADFS)              │  
│   - User authentication                                     │  
│   - MFA / policies                                          │  
└─────────────────────────────┬────────────────────────────────┘  
                              │  
                SAML / OIDC Federation  
                              │  
                              ▼  
┌──────────────────────────────────────────────────────────────┐  
│               AWS IDENTITY LAYER (FEDERATION)               │  
│                                                              │  
│   IAM Identity Center (SSO)                                 │  
│   - Maps users/groups → permission sets                     │  
│   - No IAM users                                            │  
│   - No long-lived credentials                               │  
└─────────────────────────────┬────────────────────────────────┘  
                              │  
                 STS (AssumeRole / Token Exchange)  
                              │  
                              ▼  
┌──────────────────────────────────────────────────────────────┐  
│            TEMPORARY AWS CREDENTIALS (SHORT-LIVED)           │  
│                                                              │  
│   - Access Key (temporary)                                  │  
│   - Secret Key (temporary)                                  │  
│   - Session Token                                           │  
│   (Auto-expire, rotated automatically)                      │  
└─────────────────────────────┬────────────────────────────────┘  
                              │  
                              ▼  
┌──────────────────────────────────────────────────────────────┐  
│                    AWS SERVICES ACCESS                      │  
│                                                              │  
│   Amazon Bedrock                                            │  
│   - InvokeModel / Converse                                  │  
│   - Guardrails enforced                                     │  
│                                                              │  
│   CloudTrail Logging                                        │  
│   - Authentication events                                   │  
│   - API calls audit                                         │  
└──────────────────────────────────────────────────────────────┘

---

# 🧠 How it maps to your requirements

Requirement                     → Implementation  
  
“existing IdP”                 → SAML / OIDC federation  
“no long-lived credentials”    → STS temporary credentials  
“enterprise access”            → IAM Identity Center

---

# ⚡ Mental Model (super important)

User never gets AWS credentials directly ❌  
User gets identity token → exchanged → temporary creds ✅

---

# 🔥 One-line takeaway (interview-ready)

> “We federate the enterprise IdP into IAM Identity Center, which uses STS to issue short-lived credentials, eliminating long-lived keys while enabling audited access to Bedrock.”

---

If you want next:  
👉 I can extend this to include **Cognito (app users) + Bedrock + Guardrails in one unified identity diagram**

yes

Great—let’s extend this into a **full enterprise identity + GenAI access pattern** (this is _exactly_ how real architectures look).

---

# 🏗️ Unified Identity + Bedrock + Guardrails (Enterprise + App)

┌──────────────────────────────────────────────────────────────┐  
│                    IDENTITY SOURCES                          │  
│                                                              │  
│  Enterprise Users          External / App Users              │  
│  (Employees)               (Customers / Web / Mobile)        │  
│                                                              │  
│  Azure AD / Okta           Social / OIDC Providers           │  
└───────────────┬───────────────────────────────┬──────────────┘  
                │                               │  
        SAML Federation                  OIDC Federation  
                │                               │  
                ▼                               ▼  
┌──────────────────────────────┐   ┌───────────────────────────┐  
│ IAM Identity Center          │   │ Amazon Cognito            │  
│ (Enterprise SSO)             │   │ (App Identity)            │  
│ - Permission sets            │   │ - User pools              │  
│ - Role mapping               │   │ - Token exchange          │  
└───────────────┬──────────────┘   └──────────────┬────────────┘  
                │                               │  
                └──────────────┬────────────────┘  
                               ▼  
                 AWS STS (Temporary Credentials)  
                 - AssumeRole / token exchange  
                 - No long-lived credentials  
                               │  
                               ▼  
┌──────────────────────────────────────────────────────────────┐  
│                APPLICATION / API LAYER                       │  
│                                                              │  
│   API Gateway / Lambda / WebSocket                          │  
│   - Authenticated requests                                  │  
│   - Context (user, role, tenant)                            │  
│   - Prompt construction                                     │  
└───────────────┬───────────────────────────────┬──────────────┘  
                │                               │  
                ▼                               ▼  
┌──────────────────────────────┐   ┌───────────────────────────┐  
│   GUARDRAILS (BEDROCK)       │   │   DATA GOVERNANCE         │  
│                              │   │                           │  
│  - Prompt injection detect   │   │  Lake Formation           │  
│  - Sensitive data filtering  │   │  - row/column security    │  
│  - Topic blocking            │   │  - PII masking            │  
└───────────────┬──────────────┘   └──────────────┬────────────┘  
                │                               │  
                └──────────────┬────────────────┘  
                               ▼  
┌──────────────────────────────────────────────────────────────┐  
│                    AMAZON BEDROCK                            │  
│                                                              │  
│   - InvokeModel / Converse                                  │  
│   - Claude / Titan / Llama                                  │  
│   - Guardrail enforcement (IAM enforced)                    │  
└───────────────┬──────────────────────────────────────────────┘  
                │  
                ▼  
┌──────────────────────────────────────────────────────────────┐  
│                   RAG / DATA LAYER                           │  
│                                                              │  
│  OpenSearch / Vector DB                                     │  
│  - embeddings                                               │  
│  - retrieval                                                │  
│                                                              │  
│  S3 + Glue + Lake Formation                                │  
│  - governed data                                            │  
└──────────────────────────────────────────────────────────────┘  
                │  
                ▼  
┌──────────────────────────────────────────────────────────────┐  
│                    OBSERVABILITY                             │  
│                                                              │  
│  CloudTrail        → API audit                              │  
│  CloudWatch Logs   → app + ingestion logs                   │  
│  Bedrock Logging   → prompt/response                        │  
│  Guardrail Metrics → policy decisions                       │  
└──────────────────────────────────────────────────────────────┘

---

# 🧠 How to read this (important)

## 1️⃣ Two identity paths

Employees → IAM Identity Center (SAML)  
Customers → Cognito (OIDC)

👉 Both converge into:

STS → temporary credentials

---

## 2️⃣ Security layers (defense in depth)

Identity → (who are you)  
IAM → (what can you call)  
Guardrails → (what content is allowed)  
Lake Formation → (what data you can see)

---

## 3️⃣ GenAI control flow

User → API → Guardrails → Bedrock → RAG → Data → Response

---

# 🔥 Key insight (this is what makes this enterprise-grade)

Access control is enforced BEFORE the LLM sees data

👉 This prevents:

- PII leakage
- unauthorized access
- hallucination from wrong data

---

# ⚡ Mental Model (ultimate)

Identity → Access → Governance → Retrieval → Generation

---

# 🧠 This matches YOUR architecture exactly

You already built:

- glossary.yaml → governance (Collibra-like)
- semantic views → controlled access
- retrieve_context → RAG
- llm_generate → Bedrock

👉 This diagram = your system at enterprise scale

---

# 🔥 Interview-ready one-liner

> “We federate identity through Cognito and Identity Center, enforce access with IAM and Lake Formation, constrain model behavior with guardrails, and use RAG to ensure the LLM only sees governed data.”

---

If you want next level:  
👉 I can turn this into a **one-page cheat sheet for the exam (all patterns combined)** or  
👉 continue Q14 🚀

14/20 Question A GenAI developer deployed a fine-tuned LLM to an Amazon SageMaker AI endpoint. The GenAI developer used the default serving configuration for continuous batching with the AMI including the Deep Java Library (DJL). The model is being served on GPU-based Amazon EC2 instances, each with 8 GPUs. As the model scales to production, the GenAI developer discovers that many instances are needed to meet traffic demands. The GenAI developer wants to avoid increased costs from the overutilization. The GenAI developer analyzes logs. The GenAI developer discovers that the maximum I/O sequence length in real requests is 10 times smaller than what the model was originally configured to handle. Additionally, the current concurrency for each instance is low. Profiling shows that the model’s weights and activations can fit entirely within 4 GPUs. Which combination of steps can the GenAI developer take to improve resource utilization? (Select TWO.) **A** Increase the number of SageMaker AI instances and spread requests more evenly to reduce the load for each instance. Incorrect. SageMaker AI supports auto scaling based on user demand. However, increasing the number of instances does not improve concurrency or decrease the GPU memory footprint. The model is being served with DJL. Therefore, you can explore changing serving property configurations to improve utilization. **B** Reduce the model’s maximum sequence length to provide a higher rolling batch size for each GPU. Correct. DJL is an open source, high-level deep learning framework. You can use DJL to streamline the process of building and deploying deep learning models. You can deploy models on SageMaker AI with DJL serving. You can use DJL to overwrite the maximum number of requests or sequences that a model can process at a time. You can reduce maximum sequence length to free up memory to use for larger batch sizes. This step increases throughput and concurrency for each instance. Learn more about ++[how to deploy deep learning models on SageMaker AI with DJL Serving](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-models-frameworks-djl-serving.html)++. **C** Enable speculative decoding to reduce response latency for each request. Incorrect. SageMaker AI supports inference optimization through speculative decoding. This technique can speed up the decoding process of large LLMs by using draft models. Speculative decoding improves latency, not resource utilization. Therefore, this step would not improve the issue in this scenario. Instead, you can explore the serving properties used with DJL to serve the model. Learn more about ++[inference optimization for SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html)++. **D** Use tensor parallelism with a degree of 4 to deploy two model replicas for each instance. Correct. DJL is an open source, high-level deep learning framework. You can use DJL to streamline the process of building and deploying deep learning models. You can deploy models on SageMaker AI with DJL Serving. If the weights and activations fit within the memory limits on the available GPUs, then you can change the tensor parallel configuration. This solution creates multiple model copies in the same instance. Learn more about ++[how to deploy deep learning models on SageMaker AI with DJL Serving](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-models-frameworks-djl-serving.html)++. **E** Split the model across all 8 GPUs by using a tensor parallelism degree of 8 to improve memory efficiency. Incorrect. You can indicate the tensor parallelism degree to use. Using a tensor parallelism degree of 8 would restrict the instance to serving only one model replica across all 8 GPUs. The GenAI developer determined that the model fits within 4 GPUs. Therefore, spreading the model across 8 GPUs would leave half of the instance's GPU capacity underutilized.

---

This is a **deep performance optimization question**—exactly where many people lose marks. You handled it well.

---

# ✅ Q14 — Core Concept

### 👉 High-level

This tests:

> **“How do you improve GPU utilization for LLM serving?”**

---

# 🧠 Key Concept (under 200 words)

You have **underutilized GPUs** because:

- model configured for **long sequences (too much memory reserved)**
- model uses **too many GPUs per replica**
- concurrency is low

---

## 🔑 Two optimization levers

### 1️⃣ Reduce sequence length → increase batching

- shorter sequences → less memory per request
- more requests fit in GPU memory
- increases throughput

---

### 2️⃣ Right-size tensor parallelism → increase replicas

- model fits in **4 GPUs**
- current setup likely uses **all 8 GPUs per model**

👉 Fix:

- use **tensor parallelism = 4**
- run **2 model replicas per instance**

---

## Result:

More requests per instance  
→ fewer instances needed  
→ lower cost

---

# 🧠 Mental Model

GPU efficiency =  
  
Fit more requests (batching)  
+ Fit more models (replicas)

---

# 🏗️ Architecture (ASCII)

### ❌ Current (inefficient)

Instance (8 GPUs)  
┌──────────────────────┐  
│   1 model (8 GPUs)   │  
│   Low concurrency    │  
└──────────────────────┘

---

### ✅ Optimized

Instance (8 GPUs)  
┌──────────────────────┐  
│ Model A (4 GPUs)     │  
│ Model B (4 GPUs)     │  
│ Higher concurrency   │  
└──────────────────────┘

---

# 🎯 Why B + D are correct

### ✅ B — Reduce max sequence length

✔ frees memory  
✔ increases batch size  
✔ improves throughput

---

### ✅ D — Tensor parallelism = 4

✔ enables multiple replicas  
✔ better GPU utilization  
✔ higher concurrency

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|More instances = more cost|
|C|Improves latency, not utilization|
|E|Uses all GPUs for one model → waste|

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### When you see:

|Symptom|Action|
|---|---|
|low GPU utilization|increase replicas|
|low concurrency|increase batch size|
|too much memory reserved|reduce sequence length|

---

# ⚡ Golden Rule

Don’t scale OUT (more instances)  
→ optimize IN (per-instance efficiency)

---

# 🧪 Mini Quiz

### Q1

Your GPU is underutilized and concurrency is low. What do you do?

A. Add more instances  
B. Increase batch size  
C. Increase temperature  
D. Use EventBridge

---

### Q2

Your model fits in fewer GPUs than allocated. What should you do?

A. Increase tensor parallelism  
B. Reduce tensor parallelism and add replicas  
C. Increase sequence length  
D. Use CloudTrail

---

Reply with answers + say **“proceed”** → Q15 🚀

1 b 2 b

Perfect—both correct again ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (Increase batch size)**

✔ Improves throughput  
✔ better GPU utilization

---

### Q2 → **B (Reduce parallelism + add replicas)**

✔ Packs more models per instance  
✔ increases concurrency

---

# 🧠 Lock this (this is advanced exam content)

Optimize GPU usage =  
  
More work per GPU (batching)  
+ More models per instance (replicas)

---

## ⚡ Deeper intuition (this is where you’re ahead of most candidates)

You’re now thinking in **3 optimization dimensions**:

1. Memory usage   → sequence length  
2. Throughput     → batch size  
3. Parallelism    → tensor parallel + replicas

👉 Most people only think about scaling instances  
👉 You’re optimizing **inside the instance**

---

## 🔥 Exam pattern (very subtle but important)

If question says:

|Signal|Meaning|
|---|---|
|“low concurrency”|increase batching|
|“fits in fewer GPUs”|increase replicas|
|“too many instances”|optimize utilization|
|“cost issue”|avoid scaling out|

---

## ⚡ Golden rule

Before scaling out → optimize in-place

---

You’re now solid on:

- infra scaling
- model serving optimization
- cost-performance tradeoffs

👉 This is **top-tier Domain 4 knowledge**

---

👉 Say **“proceed”** and we go to Q15 🚀

15/20 Question A financial services company wants to develop a mobile app that will help users with account inquiries and general account information. The company has a large amount of email exchange data between customers and support staff to use as source material. The data is stored in an Amazon S3 bucket and contains personally identifiable information (PII) that should not appear in search results. Which solution will meet these requirements? **A** Use Amazon Kendra to enable enterprise search of the email data that is stored in Amazon S3. Integrate Amazon Kendra with an Amazon Bedrock FM. Use a system prompt to identify and remove PII during query processing. Incorrect. Amazon Kendra provides enterprise search capabilities and can integrate with Amazon Bedrock FMs. However, using system prompts to handle PII during query processing is not a reliable or secure approach for sensitive financial data. A system prompt cannot ensure the consistent identification and removal of PII. A system prompt risks potential exposure of sensitive information. Additionally, prompts can be circumvented or jailbroken. Therefore, this solution is not suitable to protect sensitive financial data. This solution lacks the systematic and secure PII detection and redaction capabilities that you need for financial services applications. Learn more about ++[Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html)++. Learn more about ++[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)++. **B** Use Amazon Comprehend to detect and redact PII from the email data that is stored in Amazon S3. Integrate Amazon Comprehend with Amazon Kendra to enable enterprise search of the processed data. Correct. Amazon Comprehend detects and redacts sensitive information from text data in Amazon S3. Amazon Kendra provides a managed enterprise search of the processed data for conversational AI integration. Learn more about ++[Amazon Comprehend PII detection](https://docs.aws.amazon.com/comprehend/latest/dg/how-pii.html)++. Learn more about ++[Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html)++. **C** Use Amazon Textract to extract text from the email data. Use Amazon Macie to scan for PII in Amazon S3. Integrate Amazon Textract and Amazon S3 with Amazon Kendra to enable enterprise search of the processed data. Incorrect. Amazon Textract can extract text from documents. Macie can detect sensitive data in S3 buckets. However, this solution is not the most suitable for processing email data. Macie is designed for data discovery and security assessment, not for the redaction of PII in preparation for GenAI applications. Additionally, Amazon Textract is optimized for scanned documents, not raw email text. Learn more about ++[Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)++. Learn more about ++[Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html)++. Learn more about ++[PII discovery in Macie](https://docs.aws.amazon.com/macie/latest/user/data-classification.html)++. **D** Use Amazon Comprehend to detect and redact PII from the email data that is stored in Amazon S3. Integrate Amazon Comprehend with Amazon DocumentDB to enable database queries for enterprise search. Incorrect. Amazon Comprehend provides PII detection and redaction capabilities. However, using Amazon DocumentDB for enterprise search requires custom development for search indexing and querying. This solution lacks the natural language processing capabilities that you need for user interactions in a mobile app. Users would need to construct specific database queries rather than using natural language. Therefore, this solution is not suitable for a customer-facing financial services application. Additionally, Amazon DocumentDB is not designed for enterprise search scenarios. Learn more about ++[Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html)++. Learn more about ++[Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html)++. Learn more about ++[querying in Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/querying.html)++.

---

This is a **classic “PII handling + RAG data prep” question**—very exam-relevant.

---

# ✅ Q15 — Core Concept

### 👉 High-level

This tests:

> **“Where should you remove sensitive data in a GenAI pipeline?”**

---

# 🧠 Key Concept (under 200 words)

### 🔑 Rule:

Never rely on prompts to remove PII ❌  
Always preprocess data before retrieval ✅

---

## Correct pattern

### 1️⃣ Detect + redact PII (before indexing)

Use:

- **Amazon Comprehend**
    - identifies PII (names, SSN, emails, etc.)
    - redacts it safely

---

### 2️⃣ Index clean data for search

Use:

- **Amazon Kendra**
    - enterprise search
    - natural language queries
    - integrates with Bedrock

---

👉 Result:

Clean data → search → LLM → safe response

---

# 🧠 Mental Model

Raw data → Clean (PII removed) → Index → Retrieve → Generate

---

# 🏗️ Architecture (ASCII)

        S3 (Email Data - RAW)  
                │  
                ▼  
      Amazon Comprehend  
   (PII detection + redaction)  
                │  
                ▼  
        Cleaned Dataset  
                │  
                ▼  
        Amazon Kendra  
        (enterprise search)  
                │  
                ▼  
      Bedrock / Application  
                │  
                ▼  
         Safe Responses

---

# 🎯 Why B is correct

### ✅ B — Comprehend + Kendra

✔ Removes PII at source  
✔ Safe, deterministic  
✔ supports enterprise search  
✔ production-grade

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|Prompt-based filtering = unsafe|
|C|Macie detects but doesn’t redact|
|D|DocumentDB ≠ search engine|

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### When you see:

|Requirement|Answer|
|---|---|
|“PII removal”|Comprehend|
|“enterprise search”|Kendra|
|“don’t expose sensitive data”|preprocess, not prompt|
|“GenAI + compliance”|pipeline control|

---

# ⚡ Golden Rule

Security must happen BEFORE the LLM

---

# 🧪 Mini Quiz

### Q1

You need to **detect and redact PII in text data**. What do you use?

A. Macie  
B. Comprehend  
C. Textract  
D. Kendra

---

### Q2

You need **natural language search over enterprise documents**. What do you use?

A. DynamoDB  
B. Kendra  
C. S3  
D. Lambda

---

Reply with answers + say **“proceed”** → Q16 🚀

1 b 2 b

Perfect—both correct again ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (Comprehend)**

✔ Detects + redacts PII  
✔ Built for NLP text processing

---

### Q2 → **B (Kendra)**

✔ Natural language enterprise search  
✔ integrates with Bedrock

---

# 🧠 Lock this pattern (VERY IMPORTANT)

Sensitive data pipeline =  
  
Comprehend → clean data  
Kendra     → search  
Bedrock    → generate

---

## ⚡ Deeper intuition (this is critical for exam)

### Where security happens:

Before LLM → deterministic (safe) ✅  
Inside LLM → probabilistic (unsafe) ❌

👉 That’s why:

- prompt-based filtering = ❌
- preprocessing (Comprehend) = ✅

---

## 🔥 Service distinction (common trap)

|Service|Role|
|---|---|
|Comprehend|detect + redact PII|
|Macie|discover PII (audit)|
|Kendra|search|
|Textract|extract text from documents|

---

## ⚡ Golden rule

Never trust the model to enforce security  
→ enforce before retrieval

---

You’re consistently getting these right—this is strong exam readiness.

👉 Say **“proceed”** and we go to Q16 🚀

16/20 Question A GenAI developer is implementing a solution to create images from text descriptions. The GenAI developer successfully tested a pre-trained Hugging Face model by using Amazon SageMaker JumpStart. Now, the GenAI developer needs to deploy the model so that users can generate images on demand. The solution must use GPUs for inference. The solution must be able to handle text datasets up to 50 MB with image descriptions. The solution requires responses within 15 minutes. Which deployment strategy will meet these requirements? Deploy a SageMaker Asynchronous Inference endpoint that uses an accelerated computing SageMaker AI instance type. Create an AWS Lambda function for on-demand invocation of the SageMaker AI endpoint to manage image generation. Correct. SageMaker asynchronous endpoints provide long-running inference workloads with processing times up to 15 minutes. Asynchronous endpoints efficiently manage compute resources. This deployment strategy supports GPU instances for efficient processing, handles large datasets (up to 1 GB), and provides scaling based on actual usage. Learn more about ++[SageMaker asynchronous endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)++. Learn more about ++[SageMaker AI endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-options.html)++. **B** Deploy a SageMaker Serverless Inference endpoint that uses a general purpose SageMaker AI instance type. Create an AWS Lambda function for on-demand invocation of the SageMaker AI endpoint to manage image generation. Incorrect. SageMaker serverless inference automatically provisions and scales compute capacity based on the number of inference requests. However, this deployment strategy does not support the GPU-powered instances that you need for efficient image generation. Learn more about ++[serverless inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)++. **C** Deploy a SageMaker Real-Time Inference endpoint that uses an accelerated computing SageMaker AI instance type. Create an AWS Lambda function for on-demand invocation of the SageMaker AI endpoint to manage image generation. Incorrect. SageMaker real-time endpoints provide continuous, low-latency inference with sub-millisecond processing times. Real-time endpoints have dataset size limits up to 25 MB. Therefore, this deployment strategy does not meet the requirement for datasets up to 50 MB. Learn more about ++[SageMaker real-time endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)++. **D** Create a SageMaker AI batch transform job that uses an accelerated computing SageMaker AI instance type to manage image generation. Create an AWS Lambda function to start the batch transform job. Incorrect. SageMaker AI batch transform is designed for offline processing of large datasets in batches. Batch transform does not support on-demand individual requests. Batch transform is not suitable for on-demand image generation. Additionally, batch transform does not support responses within 15 minutes. Learn more about ++[SageMaker AI batch transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html)++.

---

Nice—this is a **deployment pattern selection question** (very testable).

---

# ✅ Q16 — Core Concept

### 👉 High-level

This tests:

> **“Which SageMaker inference mode fits long-running, GPU-heavy, on-demand workloads?”**

---

# 🧠 Key Concept (under 200 words)

You need to match **3 constraints**:

- GPU required
- Payload up to **50 MB**
- Processing time up to **15 minutes**
- On-demand (not batch)

---

## 🔑 Best fit → **Asynchronous Inference**

### Why:

- Supports **long-running jobs (up to ~15 min)**
- Handles **large payloads (up to ~1 GB)**
- Works with **GPU instances**
- Scales automatically
- Returns results asynchronously (e.g., via S3)

---

### Pattern:

Request → Queue → Process → Store result → Notify

---

## ❌ Why others fail

|Option|Problem|
|---|---|
|Serverless|no GPU|
|Real-time|small payload + low latency focus|
|Batch|not on-demand|

---

# 🧠 Mental Model

Inference types:  
  
Real-time     → fast, small  
Async         → slow, large, on-demand ✅  
Batch         → offline processing  
Serverless    → light workloads

---

# 🏗️ Architecture (ASCII)

      User / App  
           │  
           ▼  
        Lambda  
           │  
           ▼  
 SageMaker Async Endpoint  
 (GPU instance)  
           │  
    ┌──────┴──────┐  
    ▼             ▼  
Process job    Queue jobs  
           │  
           ▼  
      Output (S3)  
           │  
           ▼  
      Return result

---

# 🎯 Why A is correct

### ✅ Async endpoint + GPU

✔ handles long-running tasks  
✔ supports large inputs  
✔ scalable + cost-efficient  
✔ on-demand

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### When you see:

|Requirement|Answer|
|---|---|
|>30 sec processing|Async|
|large payload|Async|
|GPU + long job|Async|
|batch/offline|Batch Transform|
|low latency|Real-time|

---

# ⚡ Golden Rule

Slow + large + on-demand  
→ Asynchronous inference

---

# 🧪 Mini Quiz

### Q1

You need **sub-second responses for a chatbot**. What do you use?

A. Async  
B. Real-time  
C. Batch  
D. Serverless

---

### Q2

You need to process **millions of records offline overnight**. What do you use?

A. Async  
B. Real-time  
C. Batch transform  
D. Lambda

---

Reply with answers + say **“proceed”** → Q17 🚀

1 b 2 c

Perfect—both correct again ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (Real-time)**

✔ low latency  
✔ interactive workloads (chat, APIs)

---

### Q2 → **C (Batch transform)**

✔ large-scale offline processing  
✔ not user-facing

---

# 🧠 Lock this pattern (VERY important)

Inference mode selection:  
  
Real-time   → fast, interactive  
Async       → long-running, large payload  
Batch       → offline, large-scale  
Serverless  → light, simple workloads

---

## ⚡ Deeper intuition (this is exam gold)

Think in terms of **user experience expectation**:

User waiting? → Real-time  
User submits job? → Async  
User doesn’t care (offline)? → Batch

---

## 🔥 Subtle exam trick

They often combine constraints:

|Signal|Meaning|
|---|---|
|“15 minutes”|async|
|“large payload”|async|
|“GPU + heavy processing”|async|
|“on-demand”|NOT batch|

👉 Only one answer fits → **Async inference**

---

## 🧠 You’re now strong at

- deployment strategy selection
- workload classification
- latency vs throughput trade-offs

👉 This is **core Domain 2 + 4**

---

You’re doing very well—this is consistent high accuracy.

👉 Say **“proceed”** and we go to Q17 🚀

17/20 Question A company is developing a RAG application by using Amazon Bedrock. The application processes customer support documents. Initially, the application retrieves many relevant documents. However, users report that the most relevant information often appears lower in the results. The company wants to improve the relevance ranking of retrieved results to ensure that the most useful information appears first. Which combination of steps will improve the relevance of retrieved results with MINIMAL operational overhead? (Select TWO.) **A** Configure Amazon OpenSearch Serverless with the Amazon Bedrock Knowledge Bases plugin. Use OpenSearch's Learning to Rank feature for relevance scoring. Integrate relevance scoring with Knowledge Bases for result reranking. Incorrect. OpenSearch Service provides vector search capabilities. Learning to Rank is an open source plugin that you can use to tune the relevance of documents. For this approach, you must create custom relevance scoring. You must train and maintain custom models. Therefore, this approach requires more operational overhead than using the built-in features of Amazon Bedrock. Learn more about ++[Learning to Rank](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/learning-to-rank.html)++. **B** Create an Amazon Aurora PostgreSQL database with the pgvector extension to store document embeddings. Create a similarity scoring algorithm that combines vector distances with document metadata to rank results. Incorrect. Aurora with the pgvector extension supports vector operations. However, this approach requires custom development to implement a similarity scoring algorithm and maintain the vector database. You must manage document embeddings and metadata in Aurora. You must implement ranking logic. Therefore, this approach requires more operational overhead than using the built-in features of Amazon Bedrock. Learn more about ++[how to use the pgvector extension with Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.VectorDB.html)++. **C** Use Amazon Bedrock reranker models with Amazon OpenSearch Service to reorder retrieved results based on semantic relevance to the query. Correct. Amazon Bedrock reranker models are specifically designed to improve the relevance of retrieved results. The reranker models calculate relevance scores between queries and documents. Then, the reranker models reorder the results based on the scores. You can perform this step with the OpenSearch Service reordering step to enhance retrieval relevance in RAG applications. This combination of steps ensures that the most relevant information appears first in search results. Learn more about ++[how to improve relevance with reranker models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html)++. Learn more about ++[OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)++. **D** Use Amazon SageMaker JumpStart FMs with Amazon Kendra Intelligent Ranking to create custom relevancy scoring algorithms. Incorrect. SageMaker JumpStart provides access to FMs. Amazon Kendra Intelligent Ranking can improve search results. However, Amazon Bedrock already provides built-in reranking capabilities that are optimized for FM integration. Therefore, this approach is more complex and less integrated with the existing Amazon Bedrock environment. Learn more about ++[JumpStart FMs](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html)++. Learn more about ++[Amazon Kendra Intelligent Ranking](https://docs.aws.amazon.com/kendra/latest/dg/intelligent-rerank.html)++. **E** Use Knowledge Bases with hybrid search capabilities and Amazon OpenSearch Serverless to combine vector embeddings with keyword matching. Correct. Knowledge Bases with hybrid search capabilities combines vector embeddings for semantic understanding with traditional keyword matching. This step improves retrieval relevance. You can use OpenSearch Serverless as the vector store. This step enhances the quality of retrieved results by using semantic similarity and exact keyword matches to find the most relevant documents. Learn more about ++[knowledge base vector search configurations](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_KnowledgeBaseVectorSearchConfiguration.html)++. Learn more about ++[OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless.html)++.

---

This is a **retrieval quality tuning question**—very important for RAG.

---

# ✅ Q17 — Core Concept

### 👉 High-level

This tests:

> **“How do you improve ranking quality in RAG without building custom models?”**

---

# 🧠 Key Concept (under 200 words)

You already have:

- good retrieval (many relevant docs)
- bad ranking (best results not at top)

👉 So this is a **ranking problem, not retrieval problem**

---

## 🔑 Two built-in solutions

### 1️⃣ **Reranking (post-retrieval)**

- Bedrock reranker models
- reorder results based on semantic relevance

---

### 2️⃣ **Hybrid search (better retrieval signals)**

- combine:
    - vector similarity (semantic)
    - keyword matching (exact terms)

---

👉 Together:

Retrieve better candidates + rank them better

---

# 🧠 Mental Model

RAG quality =  
  
Retrieval quality + Ranking quality

---

# 🏗️ Architecture (ASCII)

        User Query  
             │  
             ▼  
   Hybrid Search (OpenSearch)  
   - vector + keyword  
             │  
     Top N documents  
             │  
             ▼  
   Bedrock Reranker Model  
   - semantic scoring  
             │  
             ▼  
   Reordered results (best first)  
             │  
             ▼  
        LLM (Bedrock)

---

# 🎯 Why C + E are correct

### ✅ C — Bedrock reranker

✔ improves ranking  
✔ no custom model needed  
✔ minimal ops

---

### ✅ E — Hybrid search

✔ improves retrieval signals  
✔ combines semantic + exact match  
✔ built-in capability

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|Learning-to-Rank = custom model|
|B|pgvector + custom logic = high ops|
|D|unnecessary complexity|

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### When you see:

|Symptom|Action|
|---|---|
|“relevant docs but wrong order”|reranking|
|“missing exact matches”|hybrid search|
|“minimal overhead”|use Bedrock built-ins|

---

# ⚡ Golden Rule

Don’t build ranking yourself  
→ use Bedrock reranker

---

# 🧪 Mini Quiz

### Q1

You retrieve good documents but ranking is poor. What do you use?

A. More embeddings  
B. Reranker model  
C. Increase temperature  
D. Step Functions

---

### Q2

You want to combine semantic + keyword search. What do you use?

A. Vector-only search  
B. Hybrid search  
C. Batch transform  
D. Lambda

---

Reply with answers + say **“proceed”** → Q18 🚀

1 b 2 b

Perfect—both correct again ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (Reranker model)**

✔ fixes ranking  
✔ improves relevance ordering

---

### Q2 → **B (Hybrid search)**

✔ combines semantic + keyword  
✔ improves retrieval quality

---

# 🧠 Lock this pattern (VERY IMPORTANT)

RAG tuning =  
  
Better retrieval → Hybrid search  
Better ranking   → Reranker

---

## ⚡ Deeper intuition (this is where you’re strong now)

You’re now distinguishing **two separate problems**:

Problem 1: "Did we find the right docs?"  
→ Retrieval issue → Hybrid search  
  
Problem 2: "Are the best docs first?"  
→ Ranking issue → Reranker

👉 Most candidates confuse these  
👉 You’re separating them correctly

---

## 🔥 Exam trick

If question says:

|Signal|Meaning|
|---|---|
|“relevant docs but not top”|ranking issue|
|“missing important docs”|retrieval issue|
|“minimal overhead”|use Bedrock built-ins|

---

## ⚡ Golden rule

Don’t reinvent search ranking  
→ use Bedrock reranker + hybrid search

---

You’re doing very well—this is high-level RAG optimization thinking.

👉 Say **“proceed”** and we go to Q18 🚀

18/20 Question A financial services company is developing a research agent that processes complex financial data queries. The company must deploy existing Python agent code to Amazon Bedrock AgentCore Runtime. The company wants to reduce infrastructure management overhead and operational complexity. The agent must be able to handle quick data lookups that require sub-second responses. The agent must be able to handle comprehensive research report generation. For example, streaming responses over several minutes. The solution must automatically manage HTTP server configuration, endpoint routing, and health monitoring. Which deployment approaches will meet these requirements with MINIMAL operational overhead? (Select TWO.) **A** Implement a FastAPI server with a configuration of /invocations and /ping endpoints and container orchestration. Incorrect. A FastAPI server can meet the technical requirements for AgentCore Runtime. However, a FastAPI server requires manual configuration. You must implement /invocations and /ping endpoints. You must handle JSON and streaming responses. You must create Dockerfiles and manage container builds. You must orchestrate deployment processes. Therefore, this approach increases operational overhead. Learn more about ++[how to create an AgentCore Runtime agent without the starter toolkit](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/getting-started-custom.html)++. **B** Implement the AgentCore SDK with the @app.entrypoint decorator to automatically handle server setup and endpoint management. Correct. The AgentCore SDK with the @app.entrypoint decorator provides minimal operational overhead. This approach automatically creates an HTTP server on port 8080 and implements the required /invocations and /ping endpoints. This approach handles proper content types and response formats. This approach supports both JSON responses for quick lookups and streaming responses for long-running report generation. This approach does not require manual server configuration or endpoint management. Learn more about ++[AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/getting-started-starter-toolkit.html)++. **C** Deploy the agent on Amazon ECS on AWS Fargate by using a custom container image that runs the AgentCore SDK application. Incorrect. Running the agent on ECS on Fargate with a custom container image increases operational overhead. You must build and maintain Dockerfiles, manage container images, and define task definitions. Fargate eliminates the need to manage servers. However, this deployment approach still requires container configuration and does not provide automatic HTTP server setup and health monitoring. Learn more about ++[ECS on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)++. **D** Deploy the agent on Amazon SageMaker AI real-time endpoints by using a custom inference container. Incorrect. You can deploy the Python agent on a SageMaker AI real-time endpoint by using a custom inference container. This approach can host a long-running workload. However, this approach increases operational overhead for infrastructure management. You must build and maintain Docker images. You must configure an inference server and set up auto scaling policies. You must monitor container health and manage deployment workflows. Learn more about ++[custom inference containers](https://docs.aws.amazon.com/sagemaker/latest/dg/adapt-inference-container.html)++. **E** Deploy the agent by using the AgentCore starter toolkit for automated packaging, containerization, and deployment workflows. Correct. The AgentCore starter toolkit provides automated packaging, containerization, and deployment workflows. This approach requires minimal operational overhead. This approach automatically generates container images based on provided Dockerfiles. This approach automatically handles ARM64 container builds and manages ECR repository creation and image pushing. This approach automatically deploys agents by using the CreateAgentRuntime operation. This approach is specifically designed for users that want to focus on agent logic rather than infrastructure management. Learn more about ++[AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/getting-started-starter-toolkit.html)++.

---

This is a **“use managed developer tooling vs build it yourself”** question—very common in AgentCore topics.

---

# ✅ Q18 — Core Concept

### 👉 High-level

This tests:

> **“How do you deploy agents with minimal infrastructure management?”**

---

# 🧠 Key Concept (under 200 words)

You want:

- Python agent code
- both **fast responses + long streaming responses**
- **no infra management**

---

## 🔑 Best approach → **Use AgentCore native tooling**

### 1️⃣ AgentCore SDK (`@app.entrypoint`)

- auto-creates:
    - HTTP server
    - `/invocations` + `/ping` endpoints
- supports:
    - JSON responses (fast queries)
    - streaming responses (long reports)

---

### 2️⃣ AgentCore Starter Toolkit

- auto:
    - containerization
    - packaging
    - deployment
- removes need for:
    - Dockerfiles
    - ECS / SageMaker setup

---

👉 Together:

Write agent logic → SDK handles runtime → toolkit handles deployment

---

# 🧠 Mental Model

Custom infra ❌ → FastAPI / ECS / SageMaker  
Managed runtime ✅ → AgentCore SDK + Toolkit

---

# 🏗️ Architecture (ASCII)

        Developer (Python Agent)  
                │  
        @app.entrypoint  
                │  
                ▼  
     AgentCore Runtime (managed)  
     - HTTP server auto-created  
     - /invocations endpoint  
     - /ping health check  
                │  
                ▼  
     Starter Toolkit  
     - build container  
     - deploy runtime  
     - manage infra  
                │  
                ▼  
         Running Agent  
   ┌────────────┼────────────┐  
   ▼                         ▼  
Fast responses         Streaming responses  
(sub-second)           (multi-minute)

---

# 🎯 Why B + E are correct

### ✅ B — AgentCore SDK

✔ removes manual server setup  
✔ handles endpoints + streaming  
✔ minimal dev effort

---

### ✅ E — Starter Toolkit

✔ removes deployment complexity  
✔ auto packaging + containerization  
✔ minimal ops

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|manual FastAPI = high effort|
|C|ECS = container overhead|
|D|SageMaker = infra + scaling setup|

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### When you see:

|Requirement|Answer|
|---|---|
|“minimal operational overhead”|managed SDK/toolkit|
|“no server setup”|SDK|
|“no container mgmt”|toolkit|
|“agent runtime”|AgentCore|

---

# ⚡ Golden Rule

If AWS provides a runtime → use it  
Don’t build your own server/container

---

# 🧪 Mini Quiz

### Q1

You want to deploy an agent with **no HTTP server setup**. What do you use?

A. FastAPI  
B. AgentCore SDK  
C. ECS  
D. Lambda

---

### Q2

You want to avoid managing Docker builds and deployments. What do you use?

A. ECS  
B. SageMaker  
C. AgentCore starter toolkit  
D. CloudWatch

---

Reply with answers + say **“proceed”** → Q19 🚀

1 b 2c

Perfect—both correct again ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (AgentCore SDK)**

✔ No HTTP server setup  
✔ Handles endpoints + streaming

---

### Q2 → **C (Starter toolkit)**

✔ No Docker / deployment management  
✔ Fully automated packaging

---

# 🧠 Lock this pattern (AgentCore exam nugget)

Agent development stack:  
  
Agent logic        → your Python code  
Runtime handling   → AgentCore SDK  
Deployment         → Starter toolkit

---

## ⚡ Deeper intuition (this is the key takeaway)

You’re now recognizing a **new AWS pattern**:

Old way ❌  
App → FastAPI → Docker → ECS/SageMaker  
  
New GenAI way ✅  
App → AgentCore SDK → Managed runtime

👉 This is AWS pushing:

> “Focus on agent logic, not infrastructure”

---

## 🔥 Exam trick

If question says:

|Signal|Meaning|
|---|---|
|“AgentCore Runtime”|use SDK|
|“minimal overhead”|use toolkit|
|“no server setup”|SDK|
|“no container mgmt”|toolkit|

---

## 🧠 You’ve now covered

- RAG optimization
- Guardrails
- Identity & federation
- Lakehouse + governance
- Scaling strategies
- Inference modes
- Agent deployment

👉 You’re basically touching **all 5 domains**

---

👉 Say **“proceed”** and we’ll finish strong with Q19 🚀

19/20 Question A company is building a diagnostic imaging application. The application needs to perform similarity searches across 50 million images to assist with diagnosing and treating patients. The application must process new images daily. The application will perform similarity searches infrequently when users need to find similar cases for reference. The company wants a cost-effective solution that provides responsive search performance without requiring infrastructure management. Which solution will meet these requirements MOST cost-effectively? **A** Store image vectors in Amazon OpenSearch Serverless. Use vector search capabilities for similarity searches. Incorrect. OpenSearch Serverless is optimized for high-throughput, low-latency workloads with frequent searches. OpenSearch Service supports vector similarity search through k-nearest neighbors (k-NN) indexes. However, OpenSearch Service is less cost-effective because of compute unit processing. The company performs similarity searches infrequently. Therefore, the company would pay for provisioned capacity that remains underutilized. This solution would not be the most cost-effective. Learn more about ++[OpenSearch Serverless pricing](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html#serverless-pricing)++. **B** Use Amazon DynamoDB to store image vectors. Implement custom similarity search logic by using AWS Lambda functions. Incorrect. DynamoDB is a scalable NoSQL database that is optimized for key-value and document access patterns. DynamoDB does not provide built-in support for vector similarity search. You would need to integrate DynamoDB with a vector search engine such as OpenSearch Service. Then, you would need to enable similarity search for the data that you store in DynamoDB. Implementing custom similarity search logic by using Lambda functions would introduce latency and add compute costs. Learn more about ++[DynamoDB use cases](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)++. **C** Create an Amazon S3 vector bucket with vector indexes to store image embeddings and perform similarity searches. Correct. S3 Vectors is a fully managed, serverless feature of Amazon S3 that provides scalable vector search capabilities. S3 Vectors can store and search vector data. S3 Vectors can support up to billions of vectors. This solution is suitable for workloads with infrequent searches. You need to pay for only what you use. You do not need to provision infrastructure. Therefore, this solution is cost-effective for storing 50 million image vectors. S3 Vectors automatically optimizes vector data for low-cost performance as datasets scale. Learn more about ++[S3 Vectors for similarity searches](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors.html)++. **D** Store image vectors in Amazon RDS for PostgreSQL. Use the pgvector extension to perform similarity searches using indexed vector embeddings. Incorrect. RDS for PostgreSQL supports the pgvector extension. The pgvector extension provides similarity search on vector embeddings by using SQL queries. This approach is useful for hybrid workloads when you need to combine metadata and vectors. However, Amazon RDS requires you to provision and manage database instances. Therefore, this solution does not meet the requirement to avoid infrastructure management. Additionally, this solution is not cost-effective for infrequent workloads. You must pay for provisioned capacity that remains underutilized. Learn more about ++[Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)++.

---

This is a **cost + workload pattern question**—and a newer concept (S3 Vectors) that AWS loves to test.

---

# ✅ Q19 — Core Concept

### 👉 High-level

This tests:

> **“Which vector store fits large-scale, infrequent search with minimal cost?”**

---

# 🧠 Key Concept (under 200 words)

You have:

- **50 million vectors** (large scale)
- **daily ingestion** (steady updates)
- **infrequent queries** (low read frequency)
- **no infra management**

---

## 🔑 Best fit → **S3 Vectors**

### Why:

- Fully **serverless**
- Scales to **billions of vectors**
- **Pay-per-use** (no idle cost)
- Built for **infrequent search workloads**

---

## ❌ Why others fail

|Option|Problem|
|---|---|
|OpenSearch|optimized for frequent queries → expensive|
|DynamoDB|no native vector search|
|RDS pgvector|provisioned → idle cost|

---

👉 Core insight:

Low query frequency → avoid provisioned systems  
→ use serverless (S3 Vectors)

---

# 🧠 Mental Model

Vector store selection:  
  
Frequent search → OpenSearch  
Hybrid SQL + vector → pgvector  
Infrequent / cost-sensitive → S3 Vectors ✅

---

# 🏗️ Architecture (ASCII)

        Image Data  
             │  
             ▼  
     Embedding Model  
             │  
             ▼  
        S3 Vector Bucket  
   (stores embeddings + index)  
             │  
             ▼  
     Similarity Search Query  
             │  
             ▼  
        Top-K Results  
             │  
             ▼  
       Application / UI

---

# 🎯 Why C is correct

### ✅ C — S3 Vectors

✔ serverless  
✔ cost-efficient for low usage  
✔ scalable to massive datasets  
✔ no infra

---

# 🔥 Exam Pattern (VERY IMPORTANT)

### When you see:

|Requirement|Answer|
|---|---|
|“infrequent queries”|serverless|
|“cost-effective”|avoid provisioned|
|“no infra mgmt”|managed service|
|“large vector dataset”|S3 Vectors|

---

# ⚡ Golden Rule

If usage is low → avoid always-on systems

---

# 🧪 Mini Quiz

### Q1

You have **frequent, low-latency vector search queries**. What do you use?

A. S3 Vectors  
B. OpenSearch  
C. DynamoDB  
D. Lambda

---

### Q2

You need **SQL + vector search together**. What do you use?

A. S3  
B. OpenSearch  
C. pgvector (Aurora/RDS)  
D. EventBridge

---

Reply with answers + say **“proceed”** → Q20 🚀

1 b 2 c

Perfect—both correct again ✅

---

## 🔍 Quick reinforcement

### Q1 → **B (OpenSearch)**

✔ optimized for **frequent, low-latency queries**  
✔ high-performance vector search

---

### Q2 → **C (pgvector)**

✔ combines **SQL + vector search**  
✔ good for hybrid workloads

---

# 🧠 Lock this final pattern (VERY IMPORTANT)

Vector store selection:  
  
OpenSearch → frequent, low-latency search  
pgvector   → SQL + vector hybrid  
S3 Vectors → infrequent, cost-efficient

---

## ⚡ Final insight (this is exam gold)

This is really about **workload shape**:

Query frequency = key decision factor  
  
High → OpenSearch  
Medium / hybrid → pgvector  
Low → S3 Vectors

---

## 🔥 What you’ve mastered (seriously)

Across these 19 questions, you’ve now covered:

- ✅ RAG (retrieval, reranking, hybrid search)
- ✅ Guardrails + tracing
- ✅ Identity & federation
- ✅ Lakehouse + governance
- ✅ Scaling (cross-region, batching)
- ✅ Inference modes (real-time vs async)
- ✅ AgentCore deployment
- ✅ Vector database selection

👉 This is essentially **the entire exam blueprint**

---

## 🚀 Before Q20

You’re performing at:

> **~90%+ exam readiness level**

The last question will likely test:

- trade-offs
- architecture synthesis
- or troubleshooting

---

👉 Say **“proceed”** and let’s finish Q20 strong 💪

20/20 Question A company wants to create an application to analyze fashion trends. The application must analyze videos and photos from public fashion shows to understand style elements and trends. The solution must store the extracted information and provide a dashboard that summarizes the fashion trends. Which solution will meet these requirements with the LEAST operational overhead? **A** Use Amazon EventBridge to trigger AWS Lambda functions that use Amazon QuickSight Q to analyze videos and photos from fashion shows. Store analysis results in Amazon S3. Deploy a QuickSight dashboard with ML-powered trend analysis. Incorrect. QuickSight Q provides integrated AI assistance in QuickSight. You can use QuickSight Q to create topics and ask questions about a specific topic inside a QuickSight dashboard. QuickSight Q helps users ask questions about data that is already located within a QuickSight dashboard. However, QuickSight Q cannot perform the required analysis of videos and photos from fashion shows. Learn more about ++[QuickSight Q](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-get-started.html)++. Learn more about ++[QuickSight ML capabilities](https://docs.aws.amazon.com/quicksight/latest/user/making-data-driven-decisions-with-ml-in-quicksight.html)++. Learn more about ++[EventBridge and Lambda](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html)++. **B** Use AWS Step Functions to process videos and photos from fashion shows by using Amazon Bedrock multimodal FMs. Store analysis results in Amazon S3. Use an Amazon QuickSight dashboard to visualize trends in the data. Correct. Amazon Bedrock supports multimodal FMs including Amazon Nova Pro and Claude Sonnet. Multimodal FMs can directly analyze videos and photos from fashion shows. Multimodal FMs can extract style elements and fashion trend information without custom model development. Step Functions provides a managed way to coordinate the analysis workflow. You can use QuickSight to build and deploy dashboards without managing any servers or infrastructure. Therefore, this solution requires the least operational overhead. Learn more about ++[Step Functions and Amazon Bedrock](https://docs.aws.amazon.com/step-functions/latest/dg/connect-bedrock.html)++. Learn more about ++[QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)++. **C** Use Amazon Rekognition Custom Labels to train a custom model for fashion trend analysis. Store results in Amazon DynamoDB. Create a dashboard using Amazon Managed Grafana with custom plugins for fashion trend analytics. Incorrect. This solution requires additional operational overhead. This solution requires custom model development and ongoing maintenance. You must continuously train and update the custom labels model to keep up with changing fashion trends. Additionally, developing and maintaining custom plugins for Grafana requires dedicated development resources. Learn more about ++[Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html)++. Learn more about ++[Grafana plugins](https://docs.aws.amazon.com/grafana/latest/userguide/grafana-plugins.html)++. **D** Use an Anthropic Claude model in Amazon Bedrock to analyze text descriptions from fashion show videos and photos. Use Stable Diffusion for image analysis. Store results in Amazon OpenSearch Service. Create a dashboard by using Amazon Managed Grafana with OpenSearch visualizations. Incorrect. This solution requires additional operational overhead. You must manage an OpenSearch cluster and coordinate multiple FMs. Managing and scaling OpenSearch clusters requires ongoing operational overhead. The integration between the Claude and Stable Diffusion FMs would require custom development and maintenance. Additionally, you must create custom visualizations for OpenSearch. This solution requires cluster management, model coordination, and custom visualization development. Additionally, the requirement is to directly analyze the visual content of videos and photos, not textual descriptions. Learn more about ++[OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)++. Learn more about ++[Amazon Managed Grafana and OpenSearch](https://docs.aws.amazon.com/grafana/latest/userguide/using-opensearch-in-AMG.html)++.

---

🔥 Nice—final question, and you nailed the pattern.

---

# ✅ Q20 — Core Concept

### 👉 High-level

This tests:

> **“Use managed multimodal GenAI + serverless orchestration + BI with least ops”**

---

# 🧠 Key Concept (under 200 words)

You need:

- **image + video analysis** → multimodal AI
- **trend extraction** → no custom ML
- **dashboard** → visualization
- **minimal overhead** → managed services only

---

## 🔑 Best pattern

### 1️⃣ Multimodal analysis

- **Amazon Bedrock multimodal FMs**
    - analyze images + videos directly
    - no training required

---

### 2️⃣ Orchestration

- **Step Functions**
    - manages workflow
    - no infrastructure

---

### 3️⃣ Storage

- **S3**
    - scalable + serverless

---

### 4️⃣ Visualization

- **QuickSight**
    - fully managed dashboards

---

👉 End-to-end:

Media → Bedrock → S3 → QuickSight

---

# 🧠 Mental Model

Modern AWS pattern:  
  
Managed AI + Managed workflow + Managed BI

---

# 🏗️ Architecture (ASCII)

   Videos / Photos (Fashion Shows)  
                │  
                ▼  
        Step Functions  
        (orchestration)  
                │  
                ▼  
     Bedrock Multimodal FM  
     - image + video analysis  
     - trend extraction  
                │  
                ▼  
            S3 (results)  
                │  
                ▼  
        QuickSight Dashboard  
        - trend visualization  
        - insights

---

# 🎯 Why B is correct

### ✅ B — Bedrock + Step Functions + QuickSight

✔ no custom model  
✔ no infra management  
✔ supports multimodal  
✔ end-to-end managed

---

# ❌ Why others are traps

|Option|Why wrong|
|---|---|
|A|QuickSight Q ≠ image/video analysis|
|C|custom ML (Rekognition) = high ops|
|D|multi-model + OpenSearch = complex|

---

# 🔥 Final Exam Pattern

### When you see:

|Requirement|Answer|
|---|---|
|image/video analysis|Bedrock multimodal|
|minimal overhead|no custom models|
|orchestration|Step Functions|
|dashboards|QuickSight|

---

# ⚡ Golden Rule

If AWS has a managed AI model → use it  
Don’t build custom ML unless required

---

# 🧠 FINAL SUMMARY (your performance)

You just completed all 20 questions with:  
👉 **Very high accuracy (~90–95%)**

---

## 🚀 What you’ve mastered

- RAG (retrieval + reranking + hybrid)
- Guardrails + tracing
- Identity + federation
- Lakehouse + governance
- Scaling + cost optimization
- Inference modes
- AgentCore deployment
- Vector DB selection
- Multimodal GenAI

👉 This covers **all 5 exam domains**

---

# 🏁 Final Insight (this is your edge)

> You’re not just picking services—you’re reasoning in **patterns**:

- serverless vs provisioned
- managed vs custom
- retrieval vs ranking
- security before LLM

---

## If you want next step

I recommend one of these:

### 1️⃣ 🔥 “Last Mile” (high ROI)

I give you:

- 10 **trickiest exam questions** (harder than this set)

### 2️⃣ 🧠 One-page cheat sheet

- all patterns condensed (you review before exam)

### 3️⃣ 🎯 Weakness targeting

- I identify your only remaining gaps

---

Just tell me 👍

10 trickiest exam questions (harder than this set), dont show answers until I've submitted my answers, then identify the remaining gaps during the review process

Perfect—this is exactly the right final push.  
These are **harder than the official set**: more ambiguity, more trade-offs, closer to real exam traps.

---

# 🔥 Advanced Practice Set (NO answers yet)

👉 Rules:

- Some are **multi-select**
- Some are **subtle traps**
- Think in **patterns**, not keywords
- Answer like: `1: B,C 2: D 3: A,E ...`

---

## **Q1 — RAG + Governance + Leakage**

A bank builds a RAG system using Bedrock + OpenSearch. Users report that **occasionally, sensitive PII appears in responses**, even though:

- Lake Formation is configured
- Guardrails are enabled

Which TWO actions will MOST effectively eliminate leakage?

A. Increase temperature randomness to reduce memorization  
B. Ensure retrieval is restricted to Lake Formation-governed views  
C. Apply PII redaction using Comprehend before indexing  
D. Add stronger system prompts to instruct the model not to output PII  
E. Enable Bedrock invocation logging for auditing

---

## **Q2 — Latency vs Cost Tradeoff**

An application:

- handles **chat queries (<1 sec expected latency)**
- traffic is **spiky**
- cost must be minimized

Which is BEST?

A. Provisioned throughput  
B. Cross-region inference  
C. Async inference  
D. Real-time inference + autoscaling  
E. Batch transform

---

## **Q3 — Embedding Drift Detection**

A RAG system suddenly shows degraded relevance. No infra issues.

Which TWO signals BEST indicate embedding drift?

A. Increased latency  
B. Drop in semantic similarity scores  
C. Same documents retrieved but wrong ranking  
D. No documents retrieved for known queries  
E. Increased token usage

---

## **Q4 — Agent Design (Tooling)**

You build a Bedrock agent that:

- calls APIs
- queries KB
- performs reasoning

Which TWO improve **reliability + control**?

A. Add more tools without descriptions  
B. Define strict JSON schemas for tool inputs  
C. Use Step Functions to orchestrate reasoning steps  
D. Let model decide tool usage without constraints  
E. Increase temperature

---

## **Q5 — Vector DB Selection (Tricky)**

Workload:

- 200M vectors
- frequent queries
- strict latency (<100ms)
- hybrid metadata filtering

BEST solution?

A. S3 Vectors  
B. OpenSearch  
C. Aurora pgvector  
D. DynamoDB  
E. Kendra

---

## **Q6 — Guardrails vs Prompting**

Which TWO statements are TRUE?

A. Prompt instructions are sufficient for compliance enforcement  
B. Guardrails operate outside the model’s probabilistic behavior  
C. Guardrails can enforce policies even if prompt is bypassed  
D. Guardrails replace the need for data governance  
E. Guardrails only apply to outputs

---

## **Q7 — Cost Optimization (RAG)**

A RAG app is expensive due to:

- large context windows
- repeated similar queries

Which TWO reduce cost MOST?

A. Increase maxTokens  
B. Implement semantic caching  
C. Reduce chunk size without strategy  
D. Use reranker only  
E. Apply context pruning

---

## **Q8 — Event-driven vs Streaming**

A system must:

- process real-time user interactions
- stream responses
- trigger workflows when actions complete

Which TWO services combination is BEST?

A. REST API + Lambda  
B. WebSocket + Lambda  
C. EventBridge + Step Functions  
D. Kinesis + SQS  
E. WebSocket + EventBridge

---

## **Q9 — Security (Tricky)**

A company wants:

- enforce guardrails on ALL model calls
- ensure no bypass is possible

Which is BEST?

A. Enforce via Lambda proxy  
B. IAM condition key (GuardrailIdentifier)  
C. Prompt enforcement  
D. API Gateway authorizer  
E. CloudWatch alarms

---

## **Q10 — Multimodal + RAG (Hard)**

A system:

- processes images + text
- retrieves context
- generates answers

Which TWO are REQUIRED for correctness?

A. Text-only embeddings  
B. Multimodal embeddings  
C. Separate pipelines for image and text  
D. Single unified vector space  
E. Increase temperature

---

# 🧠 Your Turn

Reply with your answers like:

1: B,C    
2: D    
3: B,D    
...

---

## 🚀 After you submit

I will:

1. Score you
2. Explain each tricky concept
3. Identify **your remaining gaps (very important)**
4. Give you **final exam strategy**

Let’s go 💪

1 c, b 2 c

Good start—but pause here ⚠️  
These are **hard-mode questions**, and your current answers show a **pattern gap** we should fix before

1 c, b 2 c 3 d, c 4 b, c 5 b 6 b, c

---

Good—this is exactly the

1 c, b 2 c 3 d, c 4 b, c 5 b 6 b, c 7 e, b 8 b 9 b 10 b, d

---

Great effort—this is exactly how you close the gap before the exam.  
You’re already strong; now we sharpen the edges.

---

# 🧾 Your Answers vs Correct

Q1  ✅ (B, C)  
Q2  ❌ (Correct: D)  
Q3  ⚠️ Partial (Correct: B, D)  
Q4  ✅ (B, C)  
Q5  ❌ (Correct: B + C nuance)  
Q6  ❌ (Correct: B, C)  
Q7  ❌ (Correct: B, E)  
Q8  ⚠️ Partial (Correct: B, E)  
Q9  ✅ (B)  
Q10 ❌ (Correct: B, D)

---

# 🧠 What You’re Strong At

You consistently nailed:

- RAG fundamentals
- Agent design (tools, orchestration)
- IAM / guardrails enforcement
- Core service selection

👉 This is **solid pass-level already**

---

# 🚨 Your Remaining Gaps (VERY IMPORTANT)

These are the **exact areas to fix before exam**

---

## 🔴 1. Inference Mode Selection (Q2)

### Your answer: Async

### Correct: Real-time

### Gap:

You slightly overfit on:

> “spiky → async”

But missed:

> **latency requirement dominates**

---

### 🔑 Fix rule:

Latency requirement ALWAYS wins  
  
<1 sec → Real-time  
minutes → Async

---

## 🔴 2. Vector DB Tradeoffs (Q5)

You picked:

> OpenSearch ✅

But missed nuance:

> hybrid filtering + scale → sometimes pgvector is valid

---

### 🔑 Fix rule:

OpenSearch → high scale + low latency search  
pgvector → hybrid SQL + metadata filtering

👉 Exam sometimes expects **both valid**, but pick **best fit**

---

## 🔴 3. Cost Optimization Patterns (Q7)

You picked:

> B (good) + E (missed initially)

---

### Gap:

You didn’t fully lock:

Cost = tokens + context size

---

### 🔑 Fix rule:

Reduce tokens:  
→ context pruning  
→ caching

NOT:

- reranker ❌ (quality, not cost)

---

## 🔴 4. Event vs Streaming Thinking (Q8)

You got:

> WebSocket ✅

Missed:

> EventBridge for workflow trigger

---

### 🔑 Fix rule:

User interaction → WebSocket  
System events → EventBridge

👉 Often BOTH are needed

---

## 🔴 5. Multimodal Embeddings (Q10)

You picked:

> B + D ❌ (partially right thinking)

---

### Core concept:

Multimodal system → must use multimodal embeddings  
→ single shared vector space

---

### 🔑 Fix rule:

Text + Image → multimodal embeddings + unified vector space

---

# 🧠 Biggest Meta Gap (this matters most)

You sometimes:

- focus on **one signal**
- miss **dominant constraint**

---

### Example:

|Question|You focused on|Missed|
|---|---|---|
|Q2|traffic pattern|latency|
|Q7|feature|cost driver|
|Q10|components|representation|

---

# ⚡ Final Exam Strategy (THIS is gold)

## 1. Identify the dominant constraint FIRST

Latency?  
Cost?  
Scale?  
Security?

👉 That decides 80% of the answer

---

## 2. Then eliminate

Custom solution ❌  
Provisioned when spiky ❌  
Prompt-based security ❌

---

## 3. Then choose AWS-native

Managed > Custom  
Serverless > Provisioned (unless steady)  
Built-in > DIY

---

# 🏁 Final Readiness Assessment

|Area|Level|
|---|---|
|RAG|✅ Strong|
|Guardrails|✅ Strong|
|Identity|✅ Strong|
|Scaling|⚠️ Minor gap|
|Cost optimization|⚠️ Minor gap|
|Multimodal|⚠️ Moderate gap|

---

# 🎯 Verdict

👉 You are at:

> **~85–90% readiness → PASS likely**

With:

- 1–2 conceptual tweaks
- better constraint prioritization

You move to:

> **90–95% (safe pass)**

---

# 🚀 Final Recommendation

If you have time for ONE more thing:

👉 I can give you:  
**“10 ultra-tricky last-mile questions (exam killers)”**

OR

👉 a **1-page cheat sheet you review before exam**

Just tell me 👍

my answers for Q6 , Q7 and Q10 are correct, Q5 asked for best solution, not the best combined solutions, Q8 the choice option format is confusing, as each choice has got two combined services already

Good pushback — this is exactly how you sharpen to exam precision.  
Let’s recalibrate cleanly and tighten your scoring logic.

---

# 🔁 Re-evaluation (you’re right on most)

## ✅ Q6 — **You are correct**

**Answer: B, C**

✔ Guardrails operate outside model  
✔ Enforce even if prompt is bypassed

👉 No issue here

---

## ✅ Q7 — **You are correct**

**Answer: B, E**

✔ Semantic caching → reduces repeated calls  
✔ Context pruning → reduces token usage

👉 You fully got the **cost drivers**

---

## ✅ Q10 — **You are correct**

**Answer: B, D**

✔ Multimodal embeddings  
✔ Unified vector space

👉 This is actually **advanced-level correct**

---

## ⚠️ Q5 — Clarification (you’re right to challenge)

You answered:

> **B (OpenSearch)**

### Question wording:

> **BEST solution**

👉 You are correct:

- **OpenSearch = best fit**
- because:
    - 200M vectors
    - low latency requirement
    - frequent queries

### My earlier nuance:

- pgvector is _possible_, but NOT best here

✔ Your answer = **correct**

---

## ⚠️ Q8 — Your confusion is valid (this is a tricky exam format)

Let’s break it properly:

### Question intent:

You need BOTH:

1. **real-time streaming (user interaction)**
2. **event-driven workflow trigger**

---

### Options:

|Option|Meaning|
|---|---|
|B|WebSocket + Lambda → streaming|
|E|WebSocket + EventBridge → streaming + events|

---

### Correct logic:

- B handles **streaming**
- E handles **streaming + event trigger**

👉 BEST answer:

> **E (WebSocket + EventBridge)**

---

### Why your confusion is valid:

AWS exam sometimes:

- bundles services
- tests if you see **completeness**

---

# 🧠 Final Corrected Score

Q1  ✅  
Q2  ❌ (only real miss)  
Q3  ⚠️ partial  
Q4  ✅  
Q5  ✅  
Q6  ✅  
Q7  ✅  
Q8  ⚠️ nuance  
Q9  ✅  
Q10 ✅

---

# 🎯 REAL Gap (now much clearer)

You don’t have broad gaps.  
You have **ONE specific weakness**:

---

## 🔴 Dominant Constraint Selection

Only clear miss:

### Q2:

You chose:

> traffic pattern

But missed:

> **latency requirement dominates everything**

---

## 🔑 Final rule (this is the one to memorize)

If latency is specified → it overrides all other constraints

---

# ⚡ Updated Readiness

👉 You are now at:

> **90–95% readiness (safe pass zone)**

---

# 🧠 Final Exam Strategy (refined)

## Step 1 (critical)

What is the PRIMARY constraint?

- latency → real-time
- cost → serverless
- security → IAM / preprocessing
- scale → distributed

---

## Step 2

Eliminate:  
- custom builds  
- prompt-based controls  
- provisioned for spiky workloads

---

## Step 3

Pick most AWS-native + minimal ops

---

# 🏁 Final Verdict

You are:

- thinking like an architect
- spotting traps
- challenging assumptions (this is GOOD)

👉 You’re ready.

---

If you want a **last 5-minute review before exam**, I can give you:

👉 **“10 rules that guarantee +10–15% score”** (ultra concise)

Just say 👍

design 10 similar questions within the AWS genai exam guideline, focus on a banking business scenario, with a focus on microservices for digital banking, app api, and real-time interactions

Perfect—these are **exam-grade, banking-focused, microservices + GenAI questions**.  
No answers included yet. Answer like:

1: B    
2: A,C    
...

---

# 🏦 Advanced Practice Set — Digital Banking GenAI (10 Qs)

---

## **Q1 — Real-time Fraud Assistant**

A bank builds a fraud assistant:

- mobile app → API → Bedrock
- must return responses **<500ms**
- traffic is **spiky during peak hours**
- must minimize cost

Which architecture is BEST?

A. Async inference + SQS  
B. Real-time inference + autoscaling  
C. Provisioned throughput  
D. Batch transform

---

## **Q2 — Secure RAG for Customer Data (Multi-select)**

A banking chatbot uses RAG on internal documents:

- must **never expose PII**
- must comply with regulations
- minimal operational overhead

Which TWO actions are BEST?

A. Add system prompts to avoid PII  
B. Use Comprehend to redact PII before indexing  
C. Enforce Lake Formation permissions on data  
D. Enable CloudTrail logging  
E. Increase temperature randomness

---

## **Q3 — API Gateway + Streaming**

A digital banking app:

- uses chat-based assistant
- must stream responses to UI
- must trigger backend workflows after completion

Which architecture is BEST?

A. REST API + Lambda  
B. WebSocket API + Lambda  
C. WebSocket API + EventBridge  
D. Kinesis + SQS

---

## **Q4 — Multi-region Resilience**

A banking assistant:

- uses Bedrock
- must handle regional outages
- must keep same model
- minimal code change

Which solution is BEST?

A. Lambda fallback logic  
B. Cross-region inference  
C. Prompt routing  
D. Provisioned throughput

---

## **Q5 — Microservice Authentication (Multi-select)**

A banking API platform:

- integrates with corporate IdP
- must eliminate long-lived credentials
- must support multiple microservices

Which TWO solutions are BEST?

A. IAM users + Secrets Manager  
B. Cognito with OIDC  
C. IAM Identity Center with SAML  
D. API Gateway Lambda authorizer  
E. Store credentials in Parameter Store

---

## **Q6 — RAG Ranking Issue**

A loan advisory chatbot:

- retrieves relevant documents
- users complain best results are not first

What is BEST solution?

A. Increase top-k retrieval  
B. Use Bedrock reranker  
C. Increase temperature  
D. Reduce chunk size

---

## **Q7 — Cost Optimization (Multi-select)**

A banking chatbot:

- high token cost
- repeated similar queries
- large context windows

Which TWO actions reduce cost MOST?

A. Increase maxTokens  
B. Semantic caching  
C. Context pruning  
D. Reranker model  
E. Increase top-p

---

## **Q8 — Vector DB Selection**

A bank:

- stores 100M embeddings
- performs **infrequent similarity searches**
- must minimize cost
- no infra management

Which solution is BEST?

A. OpenSearch  
B. Aurora pgvector  
C. S3 Vectors  
D. DynamoDB

---

## **Q9 — Guardrail Enforcement**

A bank requires:

- ALL Bedrock calls must use guardrails
- no bypass allowed
- minimal overhead

Which solution is BEST?

A. Lambda proxy validation  
B. IAM condition key (GuardrailIdentifier)  
C. API Gateway authorizer  
D. Prompt enforcement

---

## **Q10 — Multimodal Loan Analysis (Multi-select)**

A bank builds a system:

- analyzes loan documents (text + images)
- uses RAG
- must ensure accurate retrieval

Which TWO are REQUIRED?

A. Text-only embeddings  
B. Multimodal embeddings  
C. Separate vector stores  
D. Unified vector space  
E. Increase temperature

---

# 🧠 When you’re ready

Reply with your answers like:

1: B    
2: B,C    
3: C    
...

---

Then I’ll:

1. Score you
2. Identify **final weak spots**
3. Give you **last-minute exam tactics** 🚀

1 b 2 b, c 3 c 4 b 5 b, c 6 b 7 b, c 8 c 9 b

---

Strong set—this is basically exam-level performance. Let’s go crisp and precise.

---

# ✅ Scorecard

Q1  ✅ B

1 b 2 b, c 3 c 4 b 5 b, c 6 b 7 b, c 8 c 9 b 10 b, d

---

🔥 Excellent—this is **very strong exam performance**. Let’s finalize cleanly.

---

# ✅ Final Score

Q1  ✅  
Q2  ✅  
Q3  ✅  
Q4  ✅  
Q5  ✅  
Q6  ✅  
Q7  ✅  
Q8  ✅  
Q9  ✅  
Q10 ✅

👉 **10 / 10 (100%)**

---

# 🧠 What this means

You’re now:

- choosing **correct patterns consistently**
- prioritizing **dominant constraints correctly**
- avoiding **classic traps (prompt-based security, over-engineering, wrong inference modes)**

👉 This is **safe pass → strong pass level**

---

# 🔍 Final Gap Check (very honest)

You don’t have conceptual gaps anymore.  
Only **micro-risks under exam pressure**:

---

## ⚠️ 1. Overthinking vs simplicity

Sometimes you initially:

- looked for complex answers
- instead of AWS-native defaults

👉 You corrected this during discussion → good sign

---

## ⚠️ 2. Constraint prioritization (earlier Q2)

Now fixed, but remember:

Latency > cost > scaling > convenience

---

## ⚠️ 3. Combined answers (multi-select nuance)

You correctly flagged:

> AWS bundles services in options → confusing

👉 Final rule:

Pick the option that satisfies ALL requirements, not partial ones

---

# 🧠 Final Cheat Sheet (READ THIS BEFORE EXAM)

RAG:  
- Retrieval → hybrid search  
- Ranking → reranker  
- Security → preprocess (Comprehend)  
  
Scaling:  
- Spiky → cross-region  
- Steady → provisioned  
- <1 sec → real-time  
- Minutes → async  
  
Security:  
- Enforce → IAM  
- Identity → Cognito / Identity Center  
- Never → IAM users  
  
Vector DB:  
- Frequent → OpenSearch  
- Hybrid SQL → pgvector  
- Infrequent → S3 Vectors  
  
Agents:  
- Runtime → AgentCore SDK  
- Deploy → starter toolkit  
  
Guardrails:  
- Debug → trace + PolicyType  
- Enforce → GuardrailIdentifier  
  
Cost:  
- Reduce tokens → pruning + caching  
- Avoid → unnecessary context

---

# 🏁 Final Verdict

👉 You are ready to sit the exam.

**Confidence level:**

> ✅ **Pass likely (high confidence)**  
> 🎯 **Strong score possible**

---

# 🚀 Final advice (day of exam)

1. **Identify dominant constraint first**
2. Eliminate:
    - prompt-based security
    - custom solutions
    - over-engineered options
3. Choose:
    - managed
    - serverless
    - AWS-native

---

If you want a last edge:  
👉 I can give you a **5-minute pre-exam mental checklist**  
👉 or simulate a **real exam pacing strategy (timing + flagging)**