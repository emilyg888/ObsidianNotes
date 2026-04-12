18/75 Question A digital content company is building a generative AI (GenAI) application that summarizes news articles. The application needs to route requests to different LLMs based on language and content types. For regulatory compliance, certain content types must use specific model providers. A GenAI developer must create a solution that can switch between model providers without code changes. The model providers include Amazon Bedrock and third-party APIs. The solution must securely store API keys and maintain consistent response formatting regardless of the underlying model. The solution must optimize costs by using cached responses when appropriate. Which solution will meet these requirements? Report Content Errors A Create separate Amazon API Gateway REST APIs for each model provider with unique endpoints. Use a client-side routing application to determine which API endpoint to call based on language and content type. Store API keys in client-side code. Cache responses at the client layer for improved performance. Incorrect. Separate API Gateway REST APIs with client-side routing is an architectural pattern where each model provider gets its own dedicated API endpoint. This solution implements routing logic in the client application. This solution exposes API keys in client-side code and relies on client-side caching. Therefore, this solution creates security vulnerabilities and inconsistent performance across different client sessions. Learn more about API Gateway security best practices. B Create a single Amazon API Gateway REST API with an AWS Lambda proxy integration. Configure routing logic in the Lambda function to select the appropriate model based on request parameters. Store API keys in AWS Secrets Manager. Configure the function to retrieve the secrets. Incorrect. Lambda proxy integration passes the entire request to the Lambda function without transformation. Then, the function handles routing logic and provider selection. This solution requires code changes in the Lambda function to support new providers. Additionally, this solution does not provide a built-in caching mechanism to optimize costs. Learn more about Lambda proxy integrations. C Create a single Amazon API Gateway REST API with non-proxy integrations. Configure mapping templates to transform requests and responses for each model provider. Use header-based routing that directs traffic to store endpoint URLs based on content type and stage variables. Use AWS Secrets Manager for API key storage. Correct. API Gateway non-proxy integrations with mapping templates provide request and response transformation without code changes. You can combine header-based routing with stage variables for dynamic provider selection. Mapping templates ensure consistent response formatting across different providers. Secrets Manager provides secure API key storage. The API Gateway built-in caching capabilities optimize costs by caching responses when appropriate. Learn more about parameter mapping in API Gateway. D Deploy all models to Amazon SageMaker AI endpoints. Create a single Amazon API Gateway REST API with a SageMaker AI integration. Use path parameters to determine which SageMaker AI endpoint to invoke. Add model metadata to SageMaker AI endpoints to ensure consistent response formatting. Store credentials in the SageMaker AI configuration. Incorrect. SageMaker AI endpoints provide managed infrastructure to host ML models with built-in scaling and monitoring capabilities. However, you must deploy all models to SageMaker AI. Therefore, this solution does not support integration with third-party APIs. Path-based routing is less flexible for complex routing requirements. SageMaker AI configuration storage is not designed to manage multiple provider credentials securely. Learn more about SageMaker AI deployment options.

---

### ✅ Correct Answer: **C**

---

## 🧠 Core Concept (High level)

This question is testing **“decoupled model routing + abstraction layer”**.

You need a solution that:

1. **Switches models without code changes**
2. **Supports multiple providers (Bedrock + external APIs)**
3. **Normalizes request/response formats**
4. **Secures API keys**
5. **Adds caching for cost optimization**

👉 Translation:  
You’re building a **GenAI gateway layer** (very exam-relevant pattern).

---

## 🏗️ Why Option C Works

### 1. **No code changes → API Gateway mapping templates**

- Non-proxy integration = API Gateway handles transformation
- You don’t rely on Lambda logic (which would require code updates)

➡️ This aligns with exam requirement:

> _“dynamic model selection without code changes”_

---

### 2. **Routing logic (language/content type)**

- Header-based routing + stage variables  
    → dynamically choose model/provider

💡 Think of this like:

- “router agent” but implemented at **API layer (deterministic)**

---

### 3. **Consistent response format**

- Mapping templates normalize outputs across providers

👉 This is key:  
Different LLMs → different schemas  
API Gateway → **standard contract**

---

### 4. **Security (API keys)**

- Stored in **AWS Secrets Manager**

✔ Best practice:

- Never expose keys in client or code

---

### 5. **Cost optimization**

- API Gateway **caching**

✔ Built-in feature → reduces repeated LLM calls  
✔ Directly aligns with:

> “optimize costs using cached responses”

---

## 🧩 Mental Model (Exam shortcut)

Client  
   ↓  
API Gateway (SMART LAYER)  
   ├── Routing (headers / stage vars)  
   ├── Transform (mapping templates)  
   ├── Cache (responses)  
   └── Secure (Secrets Manager)  
   ↓  
Model Providers (Bedrock / External APIs)

---

## ❌ Why Others Fail (quick elimination logic)

### A — ❌ Client-side routing

- Breaks security (API keys exposed)
- No centralized control
- No consistent formatting

👉 Immediate reject

---

### B — ❌ Lambda proxy

- Routing in code → violates “no code change”
- No built-in caching
- Adds unnecessary compute layer

👉 Classic trap: “Lambda = flexible” but not **config-driven**

---

### D — ❌ SageMaker-only

- Doesn’t support **third-party APIs**
- Over-engineered
- Wrong abstraction layer

---

## 🧠 Key Exam Pattern

When you see:

- “no code changes”
- “multiple providers”
- “consistent format”

👉 Think:

> **API Gateway + mapping templates (non-proxy)**

---

## 🔥 Pro Insight (what AWS wants you to learn)

This question is actually about:

👉 **GenAI Gateway Pattern**

- API Gateway = abstraction layer
- Decouples:
    - client ↔ model provider
- Enables:
    - model switching
    - governance
    - cost control

This shows up heavily in:

- Enterprise GenAI architectures
- Multi-model routing systems

---

## ⚡ Quick Quiz (your turn)

You want to **A/B test two models (Claude vs Titan)** without redeploying anything.

Which is the BEST approach?

A. Add logic inside Lambda  
B. Use API Gateway stage variables  
C. Hardcode model selection in app  
D. Deploy two APIs

---

Answer when ready 👇

proxy integration vs non-proxy integration

## 🧠 Concept First (big picture)

Think of Amazon API Gateway integrations as:

- **Proxy = “pass-through”**
- **Non-proxy = “controlled transformation layer”**

👉 The difference is **who owns the logic**:

- Proxy → your backend (Lambda)
- Non-proxy → API Gateway itself

---

## ⚡ 1. Proxy Integration (Lambda proxy)

### 🧩 Idea

API Gateway just forwards everything to backend.

Client → API Gateway → Lambda → Model/API → Response

### 🔍 Characteristics

- Full request passed (headers, body, query params)
- Backend handles:
    - routing
    - validation
    - formatting
- Minimal API Gateway config

### ✅ When to use

- You want **full control in code**
- Rapid development
- Simple APIs

### ❌ Trade-offs

- Requires **code changes for everything**
- No built-in transformation
- Limited caching control

---

## ⚡ 2. Non-Proxy Integration (Custom integration)

### 🧩 Idea

API Gateway becomes a **smart middleware layer**

Client → API Gateway (mapping + routing + caching)  
        → Backend (Bedrock / HTTP / Lambda)  
        → API Gateway (transform response)  
        → Client

### 🔍 Characteristics

- Uses **mapping templates (VTL)**
- API Gateway handles:
    - request transformation
    - response normalization
    - routing decisions
- Backend receives **clean, controlled payload**

---

## 🔥 Side-by-side comparison

|Feature|Proxy Integration|Non-Proxy Integration|
|---|---|---|
|Control location|Lambda/backend|API Gateway|
|Transformation|❌ None|✅ Mapping templates|
|Flexibility|✅ High (code)|✅ High (config)|
|Code changes needed|✅ Yes|❌ No|
|Response standardization|❌ Manual|✅ Built-in|
|Caching|Limited|✅ Strong support|
|Complexity|Low|Medium|

---

## 🧠 Exam Insight (this is the key)

👉 If the question says:

- **“without code changes”**
- **“standardize responses across providers”**
- **“dynamic routing”**

➡️ ALWAYS think:

> **Non-proxy integration**

Because:

- Mapping templates = config-driven logic
- No Lambda change required

This is exactly why your previous question → **Option C**

---

## 🧠 Mental Shortcut

Proxy        = Developer-controlled (code)  
Non-proxy    = Platform-controlled (API Gateway)

---

## 💡 Real-world analogy

- Proxy = “just deliver the message”
- Non-proxy = “translate, route, format, and deliver”

---

## 🚀 Practical GenAI Angle (important for your exam)

For GenAI architectures:

- Proxy → good for:
    - agents
    - orchestration
    - custom pipelines
- Non-proxy → perfect for:
    - **LLM gateway layer**
    - multi-model routing
    - response normalization
    - cost control (caching)

---

## ⚡ Quick check question

You need to:

- switch between Bedrock and OpenAI
- normalize JSON output
- avoid redeploying code

👉 Which integration?

A. Proxy  
B. Non-proxy

Answer when ready 👇

19/75 Question A company is building a generative AI (GenAI) powered application that uses Amazon API Gateway, AWS Lambda, and Amazon Bedrock. The application must support summarization, classification, and translation tasks. A separate FM performs each task. A GenAI developer must configure the application to meet the following requirements: Route inference requests to different FMs dynamically based on task type and customer configuration. Update routing logic at runtime without redeploying the application. Implement automatic failover to an alternate model or AWS Region if the primary model or Region is unavailable. Maintain low latency, resilience, and cross-Region support for multiple providers. Which solution will meet these requirements with the LEAST operational overhead? Report Content Errors A Create a Lambda function that retrieves model routing rules from an AWS AppConfig hosted configuration profile at runtime. Use an AWS Step Functions state machine with branching paths for each task type and a circuit breaker pattern for failover. Invoke Amazon Bedrock by using Regional endpoints. Retry in a secondary Region if the primary model is unavailable. Correct. An AWS AppConfig hosted configuration is a managed way to provide dynamic application configuration updates without redeployment. Step Functions is a serverless workflow service that orchestrates multiple AWS services by using state machines with built-in error handling. AWS AppConfig provides runtime routing updates. Step Functions provides resilient failover patterns. Regional endpoints ensure cross-Region support. Therefore, this solution provides flexibility and resilience with the least operational overhead. Learn more about AWS AppConfig. Learn more about error handling in Step Functions workflows. Learn more about Amazon Bedrock endpoints. B Embed a hardcoded task type-to-model mapping dictionary in a Lambda function. Call Amazon Bedrock InvokeModel synchronously from the Lambda function. Use a try/catch block to retry with an alternate model or Region if the primary model or Region is unavailable. Deploy separate Lambda versions for each Region to manage routing. Incorrect. Lambda is a serverless compute service that runs code in response to events. Lambda functions can implement try/catch error handling and model invocation logic. However, hardcoding model mappings does not meet the requirement to update routing logic at runtime without redeployment. Learn more about Lambda environment variables. C Deploy a Flask-based model router in Amazon ECS with routing metadata stored in Amazon Aurora. Route inference requests from API Gateway to the router. Configure the router to select and invoke the appropriate model by using the Amazon Bedrock SDK. Set up Amazon CloudWatch alarms to trigger route table updates when model errors occur. Incorrect. Amazon ECS is a container management service. With Amazon ECS, you must maintain container infrastructure. Aurora is a relational database service that requires ongoing database administration. Implementing a custom Flask-based router requires additional operational overhead for container management, database maintenance, and custom routing logic. You can use CloudWatch alarms for monitoring and alerting. However, using CloudWatch alarms to route updates increases complexity and could cause reliability issues. Learn more about Amazon ECS. Learn more about CloudWatch alarms. D Configure API Gateway request mappings to send each task type to a dedicated Lambda function with a fixed model and Region configuration. Use AWS Step Functions for fallback processing if the Lambda invocation fails. Implement fallback logic in separate state machines. Incorrect. API Gateway is a fully managed service to create, publish, and manage APIs. API Gateway supports request mapping and Lambda integration. However, using fixed configurations in dedicated Lambda functions cannot dynamically route updates. Step Functions can handle fallback processing. However, implementing separate state machines for each fallback scenario increases operational overhead. This solution does not provide the flexibility that you need to route updates at runtime without redeployment. Learn more about template transformations in API Gateway.

---

### ✅ Correct Answer: **A**

---

## 🧠 Core Concept (High level)

This question is testing:

> **Dynamic model routing + runtime config + resilient orchestration**

This is a **classic GenAI “control plane vs execution plane” pattern**.

---

## 🧩 Break the requirements down

|Requirement|What AWS wants|
|---|---|
|Dynamic routing|Config-driven (NOT hardcoded)|
|No redeploy|External config (AppConfig)|
|Failover|Step Functions / circuit breaker|
|Multi-region|Bedrock regional endpoints|
|Low ops overhead|Serverless (no ECS, no DB mgmt)|

---

## 🏗️ Why Option A is correct

### 1. **Runtime routing → AWS AppConfig**

- Dynamic config without redeploy
- Perfect for:
    - model selection rules
    - feature flags

👉 This is explicitly called out as best practice  

---

### 2. **Orchestration + failover → Step Functions**

- Built-in:
    - retries
    - branching (task-based routing)
    - circuit breaker pattern

👉 Key exam signal:

> “resilience + failover” → Step Functions

---

### 3. **Failover design (important)**

Try primary model (Region A)  
   ↓  
If fail → retry  
   ↓  
If still fail → fallback model / Region B

✔ No custom code needed  
✔ Fully managed

---

### 4. **Cross-region + Bedrock**

- Use **regional endpoints**
- Retry in another region

👉 This aligns with:

- Bedrock cross-region inference patterns
- Resilient AI systems design

---

## 🧠 Architecture (clean mental model)

Client  
  ↓  
API Gateway  
  ↓  
Lambda (lightweight)  
  ↓  
AppConfig (routing rules)  
  ↓  
Step Functions (brain)  
  ├── Task: Summarization → Model A  
  ├── Task: Translation → Model B  
  ├── Task: Classification → Model C  
  └── Failover → Alternate model / region  
  ↓  
Amazon Bedrock

---

## ❌ Why others fail

### B — ❌ Hardcoded mapping

- Violates:
    - runtime updates
    - flexibility

👉 Immediate elimination

---

### C — ❌ ECS + Aurora

- Over-engineered
- Not serverless
- High operational burden

👉 Violates:

> “least operational overhead”

---

### D — ❌ Static routing (API Gateway)

- Fixed Lambda per task
- Cannot dynamically change routing

👉 Also:

- Multiple Step Functions = complexity explosion

---

## 🧠 Exam Pattern (VERY important)

When you see:

- “update without redeploy”
- “dynamic routing”
- “runtime config”

👉 Think:

> **AWS AppConfig**

---

When you see:

- “failover”
- “resilience”
- “multi-step logic”

👉 Think:

> **AWS Step Functions**

---

## 🔥 Pro Insight (this is what they’re really testing)

This is not about services.

This is about **separation of concerns**:

Config Layer     → AppConfig  
Execution Layer  → Step Functions  
Compute Layer    → Lambda  
Inference Layer  → Bedrock

👉 This is **enterprise GenAI architecture thinking**

---

## ⚡ Quick quiz

You need to:

- dynamically switch models
- A/B test routing rules
- rollback instantly

What should you use?

A. Lambda env variables  
B. AppConfig  
C. DynamoDB  
D. CloudWatch

---

Answer when ready 👇

explain the requirements for 18/75 vs 19/75

Great question — this is exactly how AWS tests **pattern recognition**.

Let’s zoom out first, then contrast.

---

# 🧠 Big Picture

Both Q18 and Q19 are about:

> **“Dynamic model routing in GenAI systems”**

But they test **two very different layers**:

Q18 → API layer (Gateway / transformation / abstraction)  
Q19 → Control + orchestration layer (routing logic + failover)

---

# 🧩 Q18 — Requirements Breakdown (API Gateway problem)

## 🎯 What it’s really asking

> “How do I expose multiple LLM providers behind ONE consistent API?”

### Key signals

- Switch providers **without code changes**
- Support **Bedrock + third-party APIs**
- **Normalize responses**
- **Secure API keys**
- **Cache responses**

---

## 🧠 What layer is this?

👉 **API abstraction layer (GenAI Gateway)**

Client  
  ↓  
API Gateway (routing + mapping + caching)  
  ↓  
Multiple LLM providers

---

## 🔑 Core problem type

> **“Standardization + decoupling + cost optimization”**

---

## 💡 Translation

- Not about workflow
- Not about orchestration
- Not about failover

👉 It’s about:

> “Hide complexity of multiple models behind a clean API”

---

# 🧩 Q19 — Requirements Breakdown (Orchestration problem)

## 🎯 What it’s really asking

> “How do I dynamically decide WHICH model to call, and handle failures?”

### Key signals

- Route based on **task type + customer config**
- Update logic **at runtime**
- **Failover across model / region**
- Maintain **resilience + low latency**
- **Least operational overhead**

---

## 🧠 What layer is this?

👉 **Control plane + orchestration layer**

Client  
  ↓  
API Gateway  
  ↓  
Lambda  
  ↓  
AppConfig (rules)  
  ↓  
Step Functions (decision + failover)  
  ↓  
Bedrock models

---

## 🔑 Core problem type

> **“Dynamic routing + resilience + orchestration”**

---

## 💡 Translation

This is about:

- Decision making
- Workflow execution
- Failure handling

👉 NOT about API formatting

---

# ⚔️ Q18 vs Q19 (Side-by-side)

|Aspect|Q18|Q19|
|---|---|---|
|Core focus|API abstraction|Orchestration|
|Main service|API Gateway (non-proxy)|AppConfig + Step Functions|
|Routing logic lives in|API Gateway config|Step Functions|
|Code changes needed|❌ No|❌ No|
|Response formatting|✅ Important|❌ Not relevant|
|Failover|❌ Not required|✅ Critical|
|Multi-region resilience|❌ No|✅ Yes|
|Caching|✅ Yes|❌ Not main concern|
|Operational complexity|Low|Managed but more logic|

---

# 🧠 Mental Model (this is gold for exam)

Q18 → “How do I expose models?”  
Q19 → “How do I choose and manage models?”

---

# 🧠 Even simpler

Q18 = API Gateway problem  
Q19 = Step Functions problem

---

# 🔥 Exam Trick (very high value)

## If you see:

### 🟢 Keywords like:

- “consistent response format”
- “multiple providers”
- “no code changes”
- “mapping / transformation”

👉 Answer = **API Gateway (non-proxy)**

---

### 🔵 Keywords like:

- “dynamic routing”
- “runtime config”
- “failover”
- “resilience”

👉 Answer = **AppConfig + Step Functions**

---

# 🧠 Why AWS splits these

This maps directly to exam domain:

- **Q18 → Integration pattern**
- **Q19 → Intelligent model routing system**

---

# ⚡ Quick test (you answer)

You need:

- route requests based on complexity
- fallback to cheaper model
- retry across regions

👉 Which pattern?

A. API Gateway mapping  
B. Step Functions + AppConfig  
C. Lambda only  
D. CloudWatch

---

Answer when ready 👇

B

💯 **Correct — B (AppConfig)**

---

## 🧠 Why this is the right instinct

You just picked the **control-plane tool for GenAI systems**.

### Concept first:

> **AppConfig = dynamic decision engine (without redeploy)**

---

## 🔍 What the question was really testing

You needed:

- Switch models dynamically
- A/B test routing rules
- Rollback instantly

👉 That is **configuration management**, NOT compute or storage.

---

## 🧩 Why each option behaves differently

### ✅ **B — AWS AppConfig (Correct)**

- Runtime config updates
- Feature flags
- A/B testing
- Instant rollback

👉 This is exactly how AWS expects you to:

> “enable dynamic model selection without code changes”

---

### ❌ A — Lambda env variables

- Static at runtime
- Requires redeploy

👉 Violates requirement

---

### ❌ C — DynamoDB

- Can store config, BUT:
    - No rollout control
    - No validation
    - No deployment strategy

👉 Too low-level

---

### ❌ D — CloudWatch

- Monitoring only
- No control logic

---

## 🧠 Mental Model (important for exam)

Static config        → Lambda env vars ❌  
Dynamic config       → AppConfig ✅  
Workflow decisions   → Step Functions ✅  
Data storage         → DynamoDB ❌  
Monitoring           → CloudWatch ❌

---

## 🔥 Pro Insight (this connects everything)

From your study guide:

- **AppConfig = dynamic model routing control**
- **Step Functions = execution + failover orchestration**
- Together → **full GenAI routing system**

---

## 🧠 Real-world analogy

- AppConfig = **brain rules (policy)**
- Step Functions = **execution engine (actions)**

---

## ⚡ Next-level thinking (you’ll see this in exam)

If the question says:

|Requirement|Answer|
|---|---|
|Change logic without deploy|AppConfig|
|Route dynamically|AppConfig / Step Functions|
|Failover / retries|Step Functions|
|Standardize API|API Gateway|

---

## 🚀 One step deeper (your level)

You can actually combine them:

AppConfig → decides routing rules  
Step Functions → executes routing + failover  
Bedrock → runs models

👉 This is **enterprise GenAI routing architecture**

---

## ⚡ Quick challenge

You need:

- route simple queries → cheap model
- complex queries → expensive model
- update threshold logic daily

👉 What combo?

A. Lambda only  
B. AppConfig + Step Functions  
C. API Gateway only  
D. DynamoDB + Lambda

---

Answer when ready 👇

21/75 Question A company is developing a product description generator by using Amazon Bedrock. The generator must provide creative but controlled product descriptions between 50–100 words. The descriptions must maintain consistency with brand guidelines but provide some variation in style. The company needs to optimize the model's output parameters to achieve the desired balance. Which configuration will meet these requirements? Report Content Errors A Set the temperature to 0.2. Set top-k to 4. Configure strict stop sequences for brand-specific terms. Incorrect. Temperature controls randomness in token selection. A lower temperature produces a more deterministic output. A temperature of 0.2 combined with a top-k of 4 creates a restrictive sampling strategy. This configuration forces the model to choose from only the four highest-probability tokens at each step. This configuration will provide nearly identical outputs for similar prompts. Strict stop sequences can help maintain brand consistency. However, this overly deterministic approach would produce repetitive, uncreative content. Therefore, this configuration would not provide stylistic variation in product descriptions. Learn more about randomness and diversity. Learn more about length parameters. B Set the temperature to 0.5. Set top-p to 0.8. Configure length penalties for responses that exceed brand guidelines. Correct. Temperature controls randomness in token selection. A higher temperature increases variability for creative output. Top-p (nucleus sampling) selects tokens from the most likely subset to balance diversity and coherence. Length penalties control verbosity. A temperature of 0.5 provides creativity while maintaining reasonable control. A top-p of 0.8 ensures that the model considers a range of options and stays within acceptable probability bounds. Length penalties help maintain consistency with the guidelines but permit some creative expression. Learn more about randomness and diversity. Learn more about length parameters. C Set the temperature to 0.5. Configure response length limits. Disable all diversity parameters. Incorrect. A mid-range temperature balances determinism and randomness. You can disable the diversity parameters top-p or top-k to apply strict length limits. This configuration will keep outputs concise and consistent. This configuration reduces variability and helps enforce brand rules. However, this configuration limits creativity. To meet the requirements, you must balance consistency with creativity. Learn more about randomness and diversity. Learn more about length parameters. D Set the temperature to 0.9. Set top-k to 50. Remove all response length limitations. Incorrect. High temperature and large top-k maximizes randomness and creativity. This configuration removes response limits and allows unconstrained text generation. This configuration provides high creativity. However, this configuration does not provide consistency or control. Without constraints, the model is more prone to hallucinations and off-brand outputs. Therefore, this configuration does not meet the requirement for controlled, guideline-aligned text. Learn more about randomness and diversity. Learn more about length parameters.

---

### ✅ Correct Answer: **B**

---

# 🧠 Concept First (what they’re testing)

This is a **“generation control tuning”** question.

👉 You’re balancing two forces:

Creativity  ←→  Control

- Too much control → boring, repetitive
- Too much creativity → inconsistent, off-brand

---

# 🧩 Requirements → Translate to parameters

|Requirement|What it means|
|---|---|
|“creative but controlled”|medium randomness|
|“consistent with brand”|bounded sampling|
|“variation in style”|allow diversity|
|“50–100 words”|length control|

---

# 🏗️ Why B is correct

### 1. **Temperature = 0.5 → balanced creativity**

- Not too deterministic (0.2 ❌)
- Not too chaotic (0.9 ❌)

👉 Middle ground = variation + control

---

### 2. **Top-p = 0.8 → controlled diversity**

- Limits token choices to **most probable subset**
- Still allows variation

👉 This is called **nucleus sampling**

From your study guide:

- Top-p controls probability mass → balances quality + diversity

---

### 3. **Length penalties → enforce brand constraints**

- Keeps output within **50–100 words**
- Prevents:
    - overly long descriptions
    - inconsistent verbosity

---

# 🧠 Mental Model (very exam useful)

Temperature → “how creative”  
Top-p       → “how safe the creativity is”  
Length ctrl → “how disciplined the output is”

---

# ❌ Why others fail (fast elimination)

### A — ❌ Too restrictive

- Temp 0.2 + top-k 4  
    👉 Almost deterministic → repetitive

---

### C — ❌ Not enough diversity

- Disables diversity controls  
    👉 Loses variation

---

### D — ❌ Too creative (chaos mode)

- Temp 0.9 + top-k 50  
    👉 Off-brand risk, no control

---

# 🔥 Exam Pattern (IMPORTANT)

When you see:

|Requirement|Think|
|---|---|
|“creative but controlled”|temp ~0.4–0.6|
|“variation”|top-p (0.7–0.9)|
|“consistency”|avoid high temp|
|“length constraint”|penalties / max tokens|

---

# 🧠 Quick intuition cheat sheet

Low temp (0–0.3)   → deterministic  
Mid temp (0.4–0.6) → balanced ✅  
High temp (0.8–1)  → creative / risky

Top-p low  → safe, narrow  
Top-p mid  → balanced ✅  
Top-p high → diverse / risky

---

# ⚡ Quick challenge

You need:

- highly creative marketing copy
- but still mostly on-brand

What would you pick?

A. temp 0.2, top-p 0.3  
B. temp 0.5, top-p 0.9  
C. temp 0.9, top-p 1.0  
D. temp 0.3, no sampling

---

Answer when ready 👇

do temperature normally used in conjunction with Top-p

## 🧠 Short answer

👉 **Yes — but not always.**

They are **often used together in practice**, but **not always recommended to tune both at the same time** (especially in exam context).

---

# 🧩 Concept First (how they differ)

Think of generation as:

Token selection process  
   ↓  
1. Filter candidates (top-p / top-k)  
2. Add randomness (temperature)  
   ↓  
Pick next token

---

## 🎯 What each one does

### 🔥 Temperature = randomness control

- 0 → deterministic
- 1 → very creative

👉 Controls **“how bold the model is”**

---

### 🎯 Top-p (nucleus sampling) = probability filter

- Select tokens within top X% probability mass
- Example: top-p = 0.8 → only consider most likely tokens

👉 Controls **“how safe the choices are”**

---

# 🧠 Do we use them together?

### ✅ In real-world

👉 Yes, commonly:

temperature = 0.5  
top-p = 0.8

- Temperature → adds variation
- Top-p → keeps it coherent

👉 This is exactly your Q21 answer pattern

---

### ⚠️ But in theory / exam nuance

AWS guidance:

> “Top_p … specify this OR temperature”

👉 Meaning:

- They **overlap in purpose**
- Using both can make tuning harder

---

# 🧠 Mental Model (important)

Temperature → randomness intensity  
Top-p       → boundary of allowed tokens

---

# ⚖️ When to use what

## 🎯 Use Temperature only

- Simple tuning
- Deterministic vs creative control

Use case: summarization, classification

---

## 🎯 Use Top-p only

- Want **controlled diversity**
- More stable than temperature

Use case: production systems needing consistency

---

## 🎯 Use BOTH (common in practice)

- Fine-tuned balance
- Marketing / creative generation

Use case: product descriptions, storytelling ✅

---

# 🔥 Exam Strategy (this is key)

### If question says:

- “balance creativity and control”  
    👉 Choose **temperature + top-p**

---

### If question says:

- “strict consistency”  
    👉 Low temperature, maybe no top-p

---

### If question says:

- “maximum creativity”  
    👉 High temperature OR high top-p (not both extreme)

---

# 🧠 Pro Insight (your level)

Think of it like:

Top-p = guardrails  
Temperature = personality

- Top-p keeps model “on-brand”
- Temperature gives it “style”

---

# ⚡ Quick challenge

You want:

- highly consistent legal summaries
- zero variation

What config?

A. temp 0.7 + top-p 0.9  
B. temp 0.2 + no sampling  
C. temp 0.8 + top-k 50  
D. temp 0.5 + top-p 0.8

---

Answer when ready 👇

b

✅ **Correct — B**

---

## 🧠 Why this is right (quick intuition)

You want:

> **“highly consistent + zero variation”**

👉 That translates to:

Deterministic output

---

## 🔍 What B does

**temp = 0.2 + no sampling**

- Very low temperature → almost no randomness
- No top-p / top-k → no diversity introduced

👉 Model will:

- pick highest-probability tokens
- produce nearly identical outputs every time

---

## 🧩 Why others are wrong

### A — ❌ temp 0.7 + top-p 0.9

👉 Too creative → variability

---

### C — ❌ temp 0.8 + top-k 50

👉 Chaos mode → unpredictable

---

### D — ❌ temp 0.5 + top-p 0.8

👉 Balanced (good for marketing, not legal)

---

## 🧠 Mental model (lock this in)

Legal / compliance → LOW temp (0–0.3) ✅  
Creative writing   → MID temp (0.4–0.7)  
Brainstorming      → HIGH temp (0.8–1)

---

## 🔥 Exam takeaway

When you see:

- “consistent”
- “repeatable”
- “deterministic”
- “regulated / legal”

👉 ALWAYS go:

> **Low temperature + minimal/no sampling**

---

## ⚡ Next level question

You want:

- chatbot replies slightly varied
- but still predictable and safe

👉 What would you pick?

A. temp 0.3 + top-p 0.7  
B. temp 0.9 + top-p 1  
C. temp 0.1 only  
D. temp 0.7 only

---

Answer when ready 👇

a

✅ **Correct — A**

---

## 🧠 Why A is the BEST answer

You want:

> “slightly varied but still predictable and safe”

👉 That translates to:

Controlled variation (NOT too random)

---

## 🔍 What A does

**temp = 0.3 + top-p = 0.7**

- Low-ish temperature → keeps outputs stable
- Moderate top-p → allows _some variation_
- Combined → safe + slightly diverse

👉 This is exactly the **“production-safe variability” zone**

---

## 🧠 Why this matches AWS guidance

From your study guide:

- Temperature → controls randomness
- Top-p → controls probability boundary
- Both are tuned **based on use case**

---

## ⚖️ Compare with other options

### B — ❌ Too random

- temp 0.9 + top-p 1  
    👉 Unpredictable, off-brand risk

---

### C — ❌ Too deterministic

- temp 0.1 only  
    👉 No variation (boring, repetitive)

---

### D — ❌ Not bounded

- temp 0.7 only  
    👉 Creative but no safety guardrail

---

## 🧩 Mental model (lock this in)

Safe chatbot = low temp + moderate top-p ✅  
Legal/compliance = very low temp only  
Creative writing = higher temp + higher top-p

---

## 🔥 Pro insight (exam gold)

From AWS exam perspective:

> You tune parameters based on **business intent**

Not just:

- “what does temperature do”

But:

- “what behaviour do I want from the model”

👉 This is explicitly part of:

- **Domain 4: Optimization & performance tuning**

---

## ⚡ Final intuition shortcut

Too stable → increase temp or top-p    
Too random → decrease temp or top-p  

---

## 🚀 Next (optional, high-value)

Want me to give you a **1-page cheat sheet** for:

- temperature vs top-p vs top-k
- with exact exam ranges + use cases

This is one of the highest ROI topics for AP1 👍

23/75 Question A media company uses various AI agents to automate content preparation tasks. One system automatically generates social media posts from news articles. One of the agentic workflows frequently encounters errors when interacting with the company's legacy content management system (CMS) API. The CMS API has inconsistent endpoint designs and poorly documented response schemas. Multiple AI agent workflows need to interact with the CMS API. A development team is spending significant time handling edge cases and API inconsistencies. The development team needs to implement a solution that standardizes and reduces the complexity of interactions with the CMS. The solution must maintain the existing API endpoints for legacy applications. The solution must be reusable across different AI agent workflows. Which solution will meet these requirements with the LEAST operational overhead? Report Content Errors A Create a new REST API transformation layer that standardizes the CMS API responses and provides detailed OpenAPI documentation. Deploy the layer as a proxy service between AI agents and the CMS. Incorrect. This solution would improve documentation and standardize responses. However, this solution does not address the needs of the AI agents. This solution requires custom integration work for each agent. This solution does not use function calling interfaces that are specifically designed for AI interactions. This solution could introduce additional latency. This solution does not provide the semantic understanding that MCP provides. Learn more about developing REST APIs by using OpenAPI in Amazon API Gateway. B Develop a custom middleware layer that transforms API requests and responses. Deploy the custom middleware layer as a sidecar container alongside each AI agent to handle CMS interactions. Incorrect. This solution could address the immediate issue. However, this solution is not scalable or maintainable. You must deploy and maintain separate middleware for each AI agent. Therefore, this solution requires additional operational overhead. Additionally, this solution does not use the standardized function calling interface that would help AI agents interact with the CMS semantically. Learn more about sidecar containers. C Refactor the existing CMS API to follow modern REST principles and add comprehensive documentation. Update all AI agents to use the new standardized endpoints. Incorrect. This solution requires significant changes to the existing CMS. Therefore, this solution could break compatibility with legacy applications. Additionally, this solution does not address the needs of AI agents for function calling interfaces. This solution requires substantial operational overhead to update all existing AI agents. Learn more about REST API development in Amazon API Gateway. D Implement a Model Context Protocol (MCP) server that provides a standardized interface to the CMS. Define function schemas for CMS operations. Implement the functions to handle API inconsistencies internally. Configure Amazon Bedrock AgentCore to interact with the CMS through the MCP function calls. Correct. MCP is designed to provide a consistent interface for AI models and agents to interact with external tools and APIs. The MCP server provides function schemas that define a standardized way to interact with the CMS. The implementation of the functions handles the API inconsistencies internally. This solution abstracts the complexities of the underlying CMS API from the agents. Therefore, this solution provides a clean, consistent interface. This solution is reusable across different agent workflows. The workflows can all interact with the CMS through the same MCP functions. This solution reduces integration complexity and operational overhead. You can update API changes or new edge cases in one central location rather than in each individual agent. Learn more about MCP for richer context. Learn more about MCP.

---

### ✅ Correct Answer: **D (MCP server)**

---

# 🧠 Concept First (what this question is REALLY testing)

This is a **“AI-native integration pattern”** question.

👉 Not just API design — but:

> **How do AI agents interact with messy external systems cleanly?**

---

# 🧩 Problem Translation

You’re dealing with:

Legacy CMS API = messy, inconsistent, hard to use  
AI agents       = need clean, structured interfaces  
Multiple agents = reuse required

---

# 🎯 What AWS wants you to recognize

👉 This is NOT:

- API Gateway problem ❌
- Lambda problem ❌

👉 This IS:

> **Tool abstraction problem for agents**

---

# 🏗️ Why MCP is the correct solution

## 1. **Standard interface for AI agents**

MCP (Model Context Protocol):

- Defines **function schemas**
- Provides **structured inputs/outputs**
- Makes APIs “AI-friendly”

👉 Like turning messy REST APIs into **clean function calls**

---

## 2. **Encapsulates complexity (key requirement)**

AI Agent → MCP → CMS API

- MCP hides:
    - inconsistent endpoints
    - bad schemas
    - edge cases

👉 Agents don’t deal with chaos anymore

---

## 3. **Reusable across workflows**

- One MCP server
- Many agents reuse same interface

👉 Centralized integration layer

---

## 4. **Lowest operational overhead**

Instead of:

Agent A → custom fix  
Agent B → custom fix  
Agent C → custom fix ❌

You get:

All agents → MCP → CMS ✅

👉 Fix once, reuse everywhere

---

## 🧠 Architecture (important)

AI Agents (Bedrock / Strands / AgentCore)  
        ↓  
   MCP Server (function schemas)  
        ↓  
   CMS API (messy legacy system)

---

# ❌ Why others are wrong (exam traps)

---

### A — ❌ REST transformation layer

- Good for humans / apps
- NOT for AI agents

👉 Missing:

- function calling
- semantic interface

---

### B — ❌ Sidecar per agent

- Duplicated logic
- High maintenance

👉 Violates:

> “least operational overhead”

---

### C — ❌ Refactor CMS

- Breaks legacy systems
- Massive effort

👉 Overkill + risky

---

# 🧠 Mental Model (THIS is gold)

REST API         → human / app interface  
MCP              → AI / agent interface ✅

---

# 🔥 Exam Pattern (very high value)

When you see:

|Requirement|Answer|
|---|---|
|“AI agents interacting with tools”|MCP|
|“standardized function interface”|MCP|
|“reuse across agents”|MCP|
|“abstract messy API”|MCP|

---

# 🧠 From your study guide

MCP:

- “standardized interface for agent-tool interactions”
- “consistent access patterns for external systems”

---

# ⚡ Real-world intuition

- REST API = “raw database query”
- MCP = “clean business function”

---

# 🚀 Pro insight (your level)

This question is testing:

> **Agent architecture maturity**

Basic:

- Call API directly

Advanced:

- Wrap API with MCP → clean tools → reusable agents

---

# ⚡ Quick challenge

You have:

- multiple agents
- each calling different internal APIs
- want unified interface + tool reuse

What should you build?

A. API Gateway mapping  
B. Lambda wrappers per agent  
C. MCP server  
D. Step Functions

---

Answer when ready 👇

c

❌ **Not quite — the correct answer is D (MCP)**  
But your instinct is interesting — let’s sharpen it.

---

# 🧠 Why C feels tempting (and why it’s wrong)

### Your choice:

> Refactor CMS API

👉 That _sounds_ clean from a **data architect mindset** (which is your strength)

- Standardize upstream system ✅
- Clean architecture ✅
- Long-term fix ✅

BUT…

---

## ❌ Why it fails the question

### 1. Breaks key requirement

> “must maintain existing API endpoints”

👉 Refactoring CMS violates this immediately

---

### 2. High operational overhead

- Rebuild API
- Update all clients
- Migration risk

👉 Opposite of:

> “LEAST operational overhead”

---

### 3. Wrong abstraction layer

This is subtle but **very exam-important**:

You tried to fix the system  
AWS wants you to abstract the system

---

# 🧠 What the question is REALLY testing

👉 This is testing:

> **Agent-tool interface standardization**

Not:

- API modernization
- System redesign

---

# 🏗️ Why D (MCP) is correct

## 🎯 Core idea

> Wrap the messy system → don’t fix it

---

## 🧩 Architecture

AI Agents  
   ↓  
MCP Server (clean function interface)  
   ↓  
Legacy CMS (messy API stays unchanged)

---

## 🔑 What MCP gives you

### 1. Standard interface for agents

- Function schemas
- Structured inputs/outputs

👉 AI-friendly interface  

---

### 2. Centralized complexity handling

- Fix inconsistencies **once**
- All agents reuse

---

### 3. No impact to legacy systems

- CMS unchanged ✅
- Existing apps unaffected ✅

---

### 4. Lowest operational overhead

- No duplication
- No refactoring
- No per-agent logic

---

# 🧠 Mental Model (this is gold)

Traditional thinking → fix the API ❌  
GenAI thinking      → wrap the API with MCP ✅

---

# 🔥 Exam Pattern

When you see:

|Signal|Answer|
|---|---|
|messy API + AI agents|MCP|
|reuse across agents|MCP|
|tool/function interface|MCP|
|minimal changes to legacy|MCP|

---

# 🧠 Where this appears in exam guide

- “function calling interfaces for integration”
- “MCP for consistent access patterns”

---

# ⚡ Key mindset shift (important for you)

You naturally think:

> “fix the data platform”

AWS wants:

> “decouple + abstract for AI systems”

---

# ⚡ Quick challenge

You have:

- 10 internal APIs
- different formats
- multiple agents need to use them

You want:

- one unified interface
- minimal maintenance

👉 Best approach?

A. Refactor all APIs  
B. API Gateway mapping  
C. MCP server  
D. Lambda wrappers per agent

---

Answer when ready 👇

overview on MCP and 2 use cases

## 🧠 MCP — Concept First (high level)

> **Model Context Protocol (MCP)** = a **standard interface for AI agents to talk to external systems**

Think of it as:

AI Agents don’t call APIs directly anymore  
They call FUNCTIONS (tools) via MCP

From your study guide:

> MCP provides a standardized interface for agent–tool interactions

---

## 🧩 Why MCP exists

Traditional integration:

Agent → REST API → messy response → custom parsing ❌

MCP approach:

Agent → MCP (function call) → clean structured response ✅

👉 It **decouples agents from messy APIs**

---

## 🔑 What MCP actually provides

### 1. **Function schema (contract)**

- Defines:
    - inputs
    - outputs
    - structure

👉 Like OpenAPI, but **for AI**

---

### 2. **Standard communication**

- JSON-RPC based
- Works across tools consistently

---

### 3. **Abstraction layer**

- Hides:
    - API inconsistencies
    - auth complexity
    - edge cases

---

## 🧠 Mental Model

REST API        = system interface  
MCP             = AI interface

---

# 🏗️ Architecture (simple)

AI Agent  
   ↓ (function call)  
MCP Server  
   ↓  
External Systems (API / DB / SaaS)

---

# 🚀 Use Case 1 — Legacy System Integration (your Q23)

## Problem

- CMS API is messy
- Multiple agents using it
- High maintenance

## MCP solution

Agents → MCP → CMS API

### What happens:

- Define clean functions:
    - `create_post()`
    - `get_article()`
- MCP handles:
    - weird endpoints
    - inconsistent responses

👉 Result:

- Agents see **clean tools**
- Fix once → reused everywhere

---

## 💡 Why this is powerful

You avoid:

- rewriting CMS
- duplicating logic

---

# 🚀 Use Case 2 — Multi-tool Enterprise AI Agent

## Problem

Agent needs to:

- query database
- call CRM
- fetch documents
- trigger workflows

Each system has:

- different APIs
- different auth
- different formats

---

## MCP solution

Agent  
  ↓  
MCP Gateway  
  ├── DB tool  
  ├── CRM tool  
  ├── Search tool  
  └── Workflow tool

---

### What happens:

- Each system exposed as a **tool/function**
- Agent decides:
    - which tool to use
    - when to call

---

## 💡 Real example

Agent task:

> “Summarize customer complaint and create support ticket”

Flow:

1. MCP → get_customer_data()  
2. MCP → search_knowledge_base()  
3. MCP → create_ticket()

👉 Agent orchestrates using **clean tools**

---

# 🔥 Exam-Level Insights

## When MCP is the answer

Look for:

- “AI agents interacting with systems”
- “standardized interface”
- “function calling”
- “reuse across agents”
- “abstract complexity”

---

## When NOT MCP

|Scenario|Use|
|---|---|
|API transformation for apps|API Gateway|
|Workflow orchestration|Step Functions|
|Dynamic routing|AppConfig|
|Data retrieval|RAG / KB|

---

# 🧠 Final intuition

Without MCP → Agents fight APIs  
With MCP    → Agents use tools

---

## ⚡ Quick check

You have:

- agents calling 5 SaaS APIs
- inconsistent schemas
- repeated parsing logic

👉 Best solution?

A. API Gateway mapping  
B. Lambda per agent  
C. MCP server  
D. Step Functions

---

Answer when ready 👇

26/75 Question A GenAI developer is troubleshooting performance issues in a production RAG application. The application is built on Amazon Bedrock. The application uses Amazon OpenSearch Service for vector storage. Users report inconsistent response times. Some queries are taking significantly longer than others. The GenAI developer must implement a monitoring solution that provides comprehensive diagnostic information to identify the root cause of the issue. Which solution will meet these requirements with the LEAST operational overhead? Report Content Errors A Create custom Amazon CloudWatch metrics that combine OpenSearch Service vector search latency and Amazon Bedrock token usage patterns. Set up composite alarms that correlate high latency with vector similarity thresholds and token consumption rates. Incorrect. You can use CloudWatch custom metrics to track application-specific data points. Multiple conditions can trigger composite alarms. However, creating custom metrics and complex alarm conditions requires additional operational overhead. Correlating vector similarity thresholds with token consumption might not effectively identify the root cause of inconsistent response times. Other factors in the RAG pipeline could cause the performance issues. Learn more about CloudWatch composite alarms. Learn more about CloudWatch custom metrics. B Set up detailed monitoring in OpenSearch Service and Amazon Bedrock. Create Amazon CloudWatch metric math expressions to analyze the correlation between vector search performance and model inference times. Set up anomaly detection on the combined metrics. Incorrect. Metric math provides complex calculations on metrics. Anomaly detection uses ML to identify unusual patterns. Configuring detailed monitoring and using metric math expressions can provide insights. However, this approach could overcomplicate the analysis. Analyzing correlations between vector search and model inference times through metric math will not clearly identify whether performance issues originate in vector retrieval or model processing. Anomaly detection could generate false positives because of the complexity of RAG operations. Learn more about anomaly detection. Learn more about math expressions. C Implement distributed tracing through AWS X-Ray that focuses on OpenSearch Service vector query latency and Amazon Bedrock model response times. Create custom subsegments for vector similarity calculations and token processing to identify specific performance bottlenecks. Incorrect. X-Ray is a distributed tracing system that helps analyze and debug production-distributed applications. X-Ray can help visualize request flow. However, custom subsegments for vector operations and token processing require additional operational overhead. Custom subsegments provide detailed tracing of application-specific operations. However, this level of granularity requires additional operational overhead to identify RAG pipeline bottlenecks. Learn more about X-Ray custom subsegments. D Create a custom Amazon CloudWatch dashboard that combines context retrieval latency metrics with OpenSearch Service operation counts. Analyze Amazon Bedrock invocation logs to identify which knowledge base queries are experiencing degraded performance. Correct. CloudWatch dashboards provide a customizable view of metrics and alarms. CloudWatch dashboards provide a visual correlation of data from multiple sources. You can combine context-retrieval latency metrics from OpenSearch with operation counts to find a direct correlation between vector search performance and overall response times. You can analyze Amazon Bedrock invocation logs to help identify specific knowledge base queries that are causing issues. Amazon Bedrock invocation logs contain detailed information about model interactions. This solution uses built-in metrics and logs with the least operational overhead. Learn more about CloudWatch custom dashboards.

---

### ✅ Correct Answer: **D**

---

# 🧠 Concept First (what this question is testing)

This is a **GenAI observability / troubleshooting pattern**:

> **“Where is the latency coming from in a RAG pipeline?”**

You need:

- visibility across **retrieval + generation**
- minimal effort (no heavy custom engineering)

---

# 🧩 Break the system (RAG pipeline)

User query  
   ↓  
OpenSearch (vector retrieval)  
   ↓  
Context  
   ↓  
Bedrock (LLM inference)  
   ↓  
Response

👉 Latency can come from:

- vector search (OpenSearch)
- model inference (Bedrock)
- prompt size / tokens

---

# 🎯 What the question wants

> “Comprehensive diagnostics”  
> “Least operational overhead”

👉 Translation:

- Use **built-in observability**
- Avoid:
    - custom metrics
    - complex tracing
    - heavy engineering

---

# 🏗️ Why D is correct

## 1. **CloudWatch dashboard = unified visibility**

- Combine:
    - OpenSearch metrics (retrieval latency)
    - Bedrock metrics (invocation behavior)

👉 Single pane of glass

From study guide:

> CloudWatch dashboards provide visibility into performance metrics

---

## 2. **Bedrock invocation logs = root cause**

These logs show:

- request details
- response times
- token usage
- errors

👉 Critical for:

- identifying slow queries
- linking latency to specific prompts

---

## 3. **No custom engineering**

- Uses:
    - existing metrics
    - existing logs

👉 This satisfies:

> **least operational overhead**

---

# ❌ Why others are wrong (important patterns)

---

## A — ❌ Custom metrics

- High effort
- Hard to maintain
- Over-engineered

👉 Exam rule:

> Avoid custom metrics unless necessary

---

## B — ❌ Metric math + anomaly detection

- Too complex
- Hard to interpret
- Not direct root cause

👉 Over-analysis ≠ better observability

---

## C — ❌ X-Ray with custom subsegments

- Requires code instrumentation
- High operational overhead

👉 Good for deep tracing, NOT “least effort”

---

# 🧠 Mental Model (VERY important)

Quick diagnosis → CloudWatch + logs ✅  
Deep tracing    → X-Ray ❌ (only if needed)  
Custom metrics  → last resort ❌

---

# 🔥 Exam Pattern

When you see:

|Requirement|Answer|
|---|---|
|“least operational overhead”|built-in logs/metrics|
|“diagnose performance issues”|CloudWatch + logs|
|“RAG troubleshooting”|retrieval + inference visibility|
|“root cause analysis”|logs > metrics|

---

# 🧠 From exam guide

- Monitoring includes:
    - latency
    - token usage
    - model interactions
    - logs for debugging

---

# ⚡ Key insight (this is gold)

👉 Metrics tell you **WHAT is slow**  
👉 Logs tell you **WHY it is slow**

---

# 🚀 Practical debugging flow

Step 1 → CloudWatch dashboard (spot issue)  
Step 2 → Bedrock logs (identify slow query)  
Step 3 → Check retrieval vs inference

---

# ⚡ Quick challenge

You want:

- full request path tracing
- visualize service dependencies
- debug microservice latency

👉 What do you use?

A. CloudWatch dashboards  
B. Bedrock logs  
C. X-Ray  
D. AppConfig

---

Answer when ready 👇

Pasted text.txt

Document

### ✅ Correct Answer: **A**

---

# 🧠 Concept First (what this question is testing)

This is a **data governance + lineage + preprocessing pipeline** question.

👉 Not about GenAI itself — but:

> **“How do I prepare and govern training data for fine-tuning?”**

---

# 🧩 Requirements → Translate

|Requirement|What it really means|
|---|---|
|Track dataset origin|**Data lineage**|
|Track transformations|**ETL + metadata tracking**|
|Only approved data|**governance layer**|
|Unstructured transcripts|**need preprocessing**|
|Least effort|**serverless managed services**|

---

# 🏗️ Why A is correct

## 1. **S3 = data lake foundation**

Raw data → S3  
Curated data → S3

👉 Standard GenAI pattern:

- raw → curated → training

---

## 2. **AWS Glue = lineage + governance (key!)**

- Glue crawler → discovers schema + metadata
- Data Catalog → tracks:
    - source
    - transformations
    - datasets

👉 This is exactly what the question requires:

> “track origin + transformations”

---

## 3. **Glue ETL = transformation engine**

- Converts:
    - unstructured transcripts → structured JSONL
- Prepares data for Bedrock fine-tuning

👉 Serverless + integrated

---

## 4. **Bedrock fine-tuning (final step)**

- Uses curated S3 dataset
- Fully managed

---

## 🧠 Architecture (clean mental model)

Raw transcripts (S3)  
        ↓  
Glue Crawler → Data Catalog (lineage)  
        ↓  
Glue ETL → transform to JSONL  
        ↓  
Curated dataset (S3)  
        ↓  
Bedrock Fine-tuning

---

# ❌ Why others fail (important patterns)

---

## B — ❌ EMR (too heavy)

- Requires cluster management
- No built-in lineage tracking
- More operational overhead

👉 Exam rule:

> Prefer **Glue over EMR** for serverless ETL

---

## C — ❌ Athena only

- Good for querying
- NOT for:
    - lineage
    - governance
    - complex transformation

👉 Missing Data Catalog integration

---

## D — ❌ No transformation / governance

- Raw data ≠ training-ready
- No lineage tracking

👉 Immediate elimination

---

# 🧠 Mental Model (VERY important)

Data governance → Glue Data Catalog ✅  
Data transformation → Glue ETL ✅  
Data storage → S3 ✅  
Fine-tuning → Bedrock ✅

---

# 🔥 Exam Pattern

When you see:

|Signal|Answer|
|---|---|
|“track lineage”|Glue Data Catalog|
|“unstructured → structured”|Glue ETL|
|“least operational effort”|serverless (Glue > EMR)|
|“fine-tuning dataset prep”|S3 + Glue|

---

# 🧠 From study guide

- Glue provides:
    - schema discovery
    - metadata tracking
    - ETL pipelines

---

# ⚡ Key insight (important for your level)

👉 This is **governed data platform thinking** (your strength)

But AWS framing is:

Governance = metadata (Glue Catalog)  
NOT just data location (S3)

---

# 🚀 Practical connection (your project)

This is basically your:

- **dataset_register.yaml → Glue Data Catalog**
- **semantic layer → curated dataset**
- **pipeline → Glue ETL**

👉 Same pattern, AWS-native

---

# ⚡ Quick challenge

You need:

- track data lineage
- enforce approved datasets
- enable auditability

👉 Which is MOST critical?

A. S3 bucket  
B. Glue Data Catalog  
C. Lambda  
D. Bedrock

---

Answer when ready 👇

the reference to JSONL format confusing, The input are support chat conversations, can they fit in JSONL?

Great question — this is where **exam wording ≠ real-world intuition**, so let’s unpack it cleanly.

---

# 🧠 Concept First

👉 Yes — **chat conversations absolutely can be stored in JSONL**

But the confusion comes from:

> **“chat format” vs “fine-tuning format”**

---

# 🧩 Two different formats (this is the key)

## 1. Chat format (runtime / Converse API)

From your material:

{  
  "messages": [  
    {"role": "user", "content": [{"text": "Hi"}]},  
    {"role": "assistant", "content": [{"text": "Hello!"}]}  
  ]  
}

👉 This is for **inference (runtime)**  

---

## 2. Fine-tuning format (training)

For fine-tuning, Bedrock expects:

{"prompt": "...", "completion": "..."}

👉 Each line = one training example  

---

# 🧠 So where does JSONL fit?

👉 JSONL = **container format**, not schema

JSONL = one JSON object per line

Example:

{"prompt": "User: Hi\nAgent:", "completion": "Hello! How can I help?"}  
{"prompt": "User: Reset password\nAgent:", "completion": "Sure, follow these steps..."}

---

# 🔑 Key insight

👉 You **convert chat conversations → prompt/completion pairs**

---

# 🧩 How chat transcripts are transformed

## Raw chat

User: Hi  
Agent: Hello  
User: Reset password  
Agent: Click “Forgot password”

---

## Converted to training examples

{"prompt": "User: Hi\nAgent:", "completion": "Hello"}  
{"prompt": "User: Reset password\nAgent:", "completion": "Click 'Forgot password'"}

---

## Or multi-turn context

{"prompt": "User: Hi\nAgent: Hello\nUser: Reset password\nAgent:",   
 "completion": "Click 'Forgot password'"}

---

# 🧠 Why AWS does this

From study guide:

> “provide labeled training pairs of prompts and completions”

👉 Fine-tuning = **supervised learning**

- Input → prompt
- Output → completion

---

# 🔥 Mental Model (important)

Chat format (messages)   → inference  
Prompt/completion (JSONL) → training

---

# ⚡ Why JSONL specifically?

- Easy to stream
- Easy to scale
- Works with S3 pipelines
- Standard for ML datasets

---

# 🧠 Where your confusion is coming from (and it’s valid)

You’re thinking:

> “Chat is structured already — why convert?”

👉 Because:

LLM training ≠ chat replay  
LLM training = supervised pairs

---

# 🚀 Practical tip (your level)

In real systems (like your air-lab):

You’d likely:

Raw transcripts  
   ↓  
Glue / preprocessing  
   ↓  
Conversation segmentation  
   ↓  
Prompt-completion pairs  
   ↓  
JSONL dataset  
   ↓  
Fine-tuning

---

# ⚡ Exam takeaway

If you see:

- “fine-tuning dataset”
- “Bedrock”
- “training data”

👉 ALWAYS think:

> **JSONL prompt-completion format**

Even if input is:

- chat logs
- documents
- transcripts

---

# ⚡ Quick check

You have:

- chat transcripts
- want to fine-tune a chatbot

What must you do?

A. Store messages as-is  
B. Convert to prompt/completion pairs  
C. Store in CSV  
D. Send directly to Bedrock

---

Answer when ready 👇

AWS GLUE does the conversion but still needs a custom ETL job

Exactly — you’re thinking at the **right (real-world) level now** 👍  
Let’s refine it so it matches **exam thinking vs real implementation**.

---

# 🧠 Concept First

👉 **Glue does NOT magically convert chat → JSONL**

It provides:

- **framework + engine**
- YOU define the transformation logic

---

# 🧩 What Glue actually does

Glue = serverless ETL engine  
NOT = auto schema converter for LLM training

From your notes:

> Glue provides ETL jobs to transform data and prepare it for downstream use

---

# 🏗️ What happens in reality

## Step-by-step

Raw transcripts (S3)  
   ↓  
Glue Crawler → metadata / schema  
   ↓  
Glue ETL job (YOUR logic)  
   ↓  
Transform → prompt/completion pairs  
   ↓  
Write JSONL to S3  
   ↓  
Bedrock fine-tuning

---

# 🧠 Where YOUR statement is correct

> “still needs a custom ETL job”

👉 ✅ 100% correct

Because you must define:

- how to split conversations
- how to map:
    - user → prompt
    - agent → completion
- how much context to include

---

# 🔍 What the ETL logic actually does

Example (PySpark / Glue):

# pseudo logic  
for conversation in transcripts:  
    for turn in conversation:  
        output.append({  
            "prompt": build_prompt(turn),  
            "completion": build_response(turn)  
        })

👉 This is **business logic**, not Glue magic

---

# 🧠 Why exam still says Glue (important)

Because exam is testing:

> **“Which managed service supports this pattern with least effort?”**

NOT:

> “Who writes the transformation logic?”

---

# 🔥 Mental Model (very important)

Glue = WHERE transformation runs  
Your logic = HOW transformation works

---

# ⚖️ Glue vs EMR (this is the real exam comparison)

|Feature|Glue|EMR|
|---|---|---|
|Serverless|✅|❌|
|Lineage (Catalog)|✅|❌|
|Setup effort|Low|High|
|ETL logic|Required|Required|

👉 Both need logic  
👉 Glue wins because **less ops + lineage**

---

# 🧠 Subtle exam trick

You might think:

> “I still need to write code → so why Glue?”

AWS answer:

You ALWAYS write transformation logic  
The question is WHERE it runs

---

# 🚀 Your level insight (this is strong)

In your architecture mindset:

This maps to:

dataset_register.yaml  → Glue Catalog  
semantic layer         → curated dataset  
pipeline               → Glue ETL

👉 Same governed pattern, AWS-native

---

# ⚡ When Glue is NOT enough (real world)

You’d move beyond Glue if:

- complex NLP preprocessing
- conversation segmentation using LLM
- heavy ML transformations

👉 then:

- SageMaker Processing
- or custom pipelines

---

# ⚡ Exam takeaway

If you see:

- “unstructured → structured”
- “lineage tracking”
- “least operational effort”

👉 Answer:

> **Glue (even if logic is custom)**

---

# ⚡ Quick challenge

You need:

- heavy NLP preprocessing
- custom ML transformations
- large-scale distributed compute

👉 Better than Glue?

A. Glue  
B. SageMaker Processing  
C. Lambda  
D. API Gateway

---

Answer when ready 👇

b

✅ **Correct — B (SageMaker Processing)**

---

# 🧠 Concept First

You just made the shift from:

ETL pipeline thinking → ML data processing thinking

---

# 🧩 Why SageMaker Processing is better here

When requirements say:

- heavy NLP
- custom ML transformations
- large-scale compute

👉 This is no longer “simple ETL”

---

## 🔍 Glue vs SageMaker (real boundary)

|Capability|Glue|SageMaker Processing|
|---|---|---|
|ETL (structured/semi)|✅|✅|
|Unstructured text cleaning|⚠️ basic|✅ strong|
|NLP / ML logic|❌ limited|✅ designed for it|
|Custom Python/ML libs|⚠️ limited|✅ full flexibility|
|Distributed ML workloads|❌|✅|
|Data lineage|✅|⚠️ external|

---

# 🧠 Mental Model (important)

Glue              → data engineering  
SageMaker         → ML data processing

---

# 🏗️ Architecture difference

## Glue pipeline (Q28 scenario)

S3 → Glue → JSONL → Bedrock

👉 Best for:

- formatting
- schema transformation
- governance

---

## SageMaker Processing pipeline

S3 → SageMaker Processing (NLP / ML logic)  
   → processed dataset → training

👉 Best for:

- text cleaning
- embedding prep
- advanced transformations

---

# 🔥 Why this matters for exam

AWS is testing:

> **Choosing the RIGHT abstraction layer**

---

## Quick rule

Simple transformation → Glue ✅  
ML-heavy transformation → SageMaker Processing ✅

---

# 🧠 From exam guide

- Data pipelines may require:
    - preprocessing
    - transformation
    - ML-based enhancement

---

# 🚀 Your level insight

In your architecture style:

Glue           = governed ingestion layer  
SageMaker      = intelligent transformation layer  
Bedrock        = inference layer

👉 This is **enterprise GenAI pipeline layering**

---

# ⚡ Final intuition

If logic = rules → Glue  
If logic = intelligence → SageMaker

---

# ⚡ Next challenge (harder)

You need:

- extract entities (NER)
- remove PII
- classify transcripts
- prepare for fine-tuning

👉 Best combo?

A. Glue only  
B. Glue + Comprehend  
C. SageMaker only  
D. Lambda only

---

Answer when ready 👇

One more question on BedRock vs SageMaker, where should fine tuning be done

This is a **very high-value question** — and AWS _loves_ testing this distinction.

Let’s make it crystal clear.

---

# 🧠 Concept First (big picture)

👉 Fine-tuning can happen in **both**, but they serve **different roles**

Bedrock     → managed FM customization (preferred for GenAI apps)  
SageMaker   → full ML lifecycle (build / train / deploy anything)

---

# 🎯 Short Answer (exam version)

|Scenario|Use|
|---|---|
|Fine-tuning foundation models (Claude, Titan, etc.)|**Bedrock ✅**|
|Training / customizing your own models|**SageMaker ✅**|

---

# 🧩 1. Fine-tuning in Amazon Bedrock (primary answer)

## 🧠 What it is

> “Customize an existing foundation model with your data”

From your guide:

> Titan, Cohere, Meta models can be fine-tuned via Bedrock

---

## 🏗️ How it works

S3 training data (JSONL)  
      ↓  
Bedrock Fine-tuning job  
      ↓  
Custom Model (managed)  
      ↓  
Invoke like normal FM

---

## ✅ When to use Bedrock

- You are using:
    - Claude / Titan / Llama
- You want:
    - **no infra management**
    - serverless
    - quick customization

---

## 💡 Key benefit

No training infrastructure  
No model hosting  
No scaling concerns

👉 This is why AWS pushes Bedrock

---

# 🧩 2. Fine-tuning in SageMaker (advanced / flexible)

## 🧠 What it is

> Full ML platform — you control everything

From guide:

> SageMaker handles training, deployment, and lifecycle

---

## 🏗️ How it works

S3 data  
   ↓  
SageMaker Training job  
   ↓  
Model artifacts (S3)  
   ↓  
Deploy endpoint (or import to Bedrock)

---

## ✅ When to use SageMaker

- You need:
    - custom models (not Bedrock-supported)
    - deep ML control
    - advanced tuning (LoRA, custom training)
- Or:
    - you want to **import model into Bedrock later**

👉 (very exam-relevant pattern)

---

# ⚖️ Bedrock vs SageMaker (clear comparison)

|Feature|Bedrock|SageMaker|
|---|---|---|
|Target|Foundation models|Any ML model|
|Setup|Serverless|You manage training jobs|
|Control|Limited|Full control|
|Complexity|Low|High|
|Deployment|Built-in|Manual / endpoint|
|Exam bias|✅ Preferred|⚠️ Only when needed|

---

# 🧠 Mental Model (this is gold)

Bedrock     = “Use & customize models”  
SageMaker   = “Build & train models”

---

# 🔥 Subtle but IMPORTANT exam pattern

👉 If question says:

### 🟢 “fine-tune FM”

→ **Bedrock**

---

### 🔵 “train model / custom ML / full control”

→ **SageMaker**

---

### 🟣 “train in SageMaker then use in Bedrock”

→ Hybrid pattern (very exam favorite)

From guide:

> You can train/tune in SageMaker and deploy via Bedrock

---

# 🧠 Real-world architecture (your level)

Option 1 (simple)  
S3 → Bedrock FT → App  
  
Option 2 (advanced)  
S3 → SageMaker Training → Model → Bedrock (import) → App

---

# ⚡ Practical intuition

If you just want a better chatbot → Bedrock  
If you are building your own model → SageMaker

---

# ⚡ Quick challenge

You need:

- fine-tune Claude model
- minimal ops
- fast deployment

👉 What do you use?

A. SageMaker training job  
B. Bedrock fine-tuning  
C. EMR  
D. Lambda

---

Answer when ready 👇

You can import model from hugging face or other external source into SageMaker for fine tuning, correct?

## 🧠 Short answer

👉 **Yes — absolutely correct.**

You can **bring models from Hugging Face (or elsewhere) into Amazon SageMaker and fine-tune them.**

---

# 🧩 Concept First (what’s really happening)

Think of SageMaker as:

“Your ML workshop”

- You can bring:
    - open-source models (Hugging Face)
    - your own models
- Then:
    - fine-tune
    - train further
    - deploy

---

# 🏗️ How the flow works

## 🔹 Typical pipeline

Hugging Face Model  
        ↓  
SageMaker Training Job  
        ↓  
Fine-tuned Model (S3 artifacts)  
        ↓  
Deploy (Endpoint OR export)

---

## 🔹 Ways to bring models in

### 1. **Hugging Face integration (native)**

- SageMaker has built-in support
- Use Hugging Face DLC (Deep Learning Containers)

👉 Simplest path

---

### 2. **Custom container**

- Bring your own training script + model
- Full flexibility

---

### 3. **JumpStart**

- Prebuilt models available in SageMaker

---

# 🧠 What you can fine-tune

- LLMs (Llama, Mistral, etc.)
- NLP models (BERT, etc.)
- CV models
- Any PyTorch / TensorFlow model

👉 SageMaker is **model-agnostic**

---

# ⚖️ Bedrock vs SageMaker (now clearer)

|Capability|Bedrock|SageMaker|
|---|---|---|
|Import Hugging Face model|❌|✅|
|Fine-tune open-source models|❌|✅|
|Fine-tune managed FMs|✅|⚠️ indirect|
|Full training control|❌|✅|

---

# 🔥 Important advanced pattern (EXAM GOLD)

👉 You can do this:

Hugging Face model  
   ↓  
SageMaker fine-tuning  
   ↓  
Model artifacts (S3)  
   ↓  
Import into Bedrock (Custom Model)  
   ↓  
Serverless inference

---

## 🧠 Why this matters

You get:

- SageMaker → **flexibility**
- Bedrock → **serverless inference + integration**

---

# 📌 From your study guide

- SageMaker supports:
    - training
    - deployment
    - full ML lifecycle
- Bedrock:
    - focuses on **FM usage + customization**

---

# 🧠 Mental Model (lock this in)

SageMaker = “bring your own model + train”  
Bedrock   = “use AWS-managed models + customize”

---

# ⚡ When to choose what (practical)

## Use SageMaker when:

- you want Hugging Face models
- you need LoRA / advanced tuning
- you want full ML control

---

## Use Bedrock when:

- you just want Claude/Titan customized
- you want serverless + fast

---

# 🚀 Your level insight

This maps directly to **enterprise architecture layering**:

Model creation layer      → SageMaker  
Model serving layer       → Bedrock  
Application layer         → API / Agents

👉 This is exactly how large enterprises build GenAI platforms

---

# ⚡ Quick challenge

You need:

- fine-tune open-source Llama
- full control over training
- custom hyperparameters

👉 What do you use?

A. Bedrock  
B. SageMaker  
C. API Gateway  
D. Lambda

---

Answer when ready 👇

back to question 28/75, InvokeModel vs Converse API, why do we need Converse API in this case

This is a **very important distinction** — and AWS sneaks this into exam questions a lot.

Let’s break it down cleanly.

---

# 🧠 Concept First

👉 Both APIs call models, BUT they serve different interaction patterns:

InvokeModel   → raw inference (single-shot)  
Converse API  → structured conversation + advanced features

---

# 🧩 What each API is designed for

## 🔹 InvokeModel (low-level)

- You send:
    - prompt (string / JSON)
- You get:
    - response

App → Bedrock (InvokeModel) → Model → Response

👉 Think:

> “just run this prompt”

---

## 🔹 Converse API (high-level)

From your material:

> “Unified API for models that support messages”

It supports:

- messages (chat format)
- system prompts
- tools (function calling)
- guardrails
- structured output

App → Bedrock (Converse) → Model (chat-aware) → Response

---

# 🎯 Why Converse API is needed (for Q28-type scenarios)

## 🧠 Key difference

InvokeModel = stateless  
Converse    = stateful conversation-aware

---

## 🧩 In Q28 (likely scenario pattern)

If the question involves:

- chat application
- multi-turn interaction
- structured responses
- tool calling
- agents

👉 You NEED Converse

---

# 🏗️ What Converse gives you (this is the real answer)

## 1. **Conversation structure**

{  
  "messages": [  
    {"role": "user", "content": "..."},  
    {"role": "assistant", "content": "..."}  
  ]  
}

👉 Native chat format  

---

## 2. **Tool / function calling**

- Required for:
    - agents
    - MCP
    - action groups

👉 InvokeModel cannot do this cleanly

---

## 3. **Guardrails integration**

- Built-in:
    - safety filters
    - grounding

---

## 4. **Structured output**

- JSON schema enforcement
- tool-based structured response

---

## 5. **Unified interface across models**

- Different models → same API
- No model-specific payload differences

---

# ⚖️ When to use which

## ✅ Use InvokeModel when:

- simple prompt → response
- batch processing
- backend jobs

Example:  
Summarize this text  
Classify sentiment  
Generate embedding

---

## ✅ Use Converse when:

- chatbots
- agents
- multi-turn conversations
- tool calling
- structured outputs

Example:  
Customer support bot  
Agent with tools  
RAG chat assistant

---

# 🧠 Mental Model (this is gold)

InvokeModel = “call the brain”  
Converse    = “talk to the brain”

---

# 🔥 Exam Pattern

If question mentions:

|Signal|Answer|
|---|---|
|chat / messages|Converse|
|tools / function calling|Converse|
|agents|Converse|
|structured JSON output|Converse|
|simple inference|InvokeModel|

---

# 🧠 Subtle but critical insight

👉 Converse is not just convenience — it’s:

> **the foundation for agentic AI in Bedrock**

This ties directly to:

- Agents
- MCP
- Tool calling

---

# ⚡ Final intuition

If interaction = conversational → Converse  
If interaction = transactional → InvokeModel

---

# ⚡ Quick challenge

You are building:

- RAG chatbot
- with memory
- with tool calling (CRM lookup)

👉 Which API?

A. InvokeModel  
B. Converse  
C. Lambda  
D. API Gateway

---

Answer when ready 👇

b

✅ **Correct — B (Converse API)**

---

# 🧠 Why this is the RIGHT mental model

You selected **Converse** because the system has:

- RAG chatbot
- memory (multi-turn)
- tool calling (CRM lookup)

👉 That combination = **agent-style interaction**

---

# 🧩 Let’s map your scenario to capabilities

Requirement            → Needed capability  
-----------------------------------------  
RAG chatbot            → multi-turn context  
Memory                 → message history  
Tool calling           → function/tool interface

👉 Only **Converse API supports ALL of these natively**

---

# 🏗️ Why InvokeModel fails here

InvokeModel is:

Single request → single response  
No conversation memory  
No tool orchestration

👉 You would have to:

- manually manage chat history
- manually inject tools
- manually enforce structure

❌ High complexity  
❌ Not scalable

---

# 🚀 What Converse gives you (this is key)

From your study guide:

> Converse provides:

- messages (chat structure)
- toolConfig (tool calling)
- guardrails
- inferenceConfig (temperature, tokens)

---

## 🧩 Architecture with Converse

User  
  ↓  
Application  
  ↓  
Bedrock Converse API  
  ├── messages (history)  
  ├── tools (CRM lookup)  
  ├── guardrails  
  ↓  
Model  
  ↓  
Response (structured / tool-aware)

---

# 🧠 Why AWS pushes Converse (important insight)

👉 Converse = **foundation for agentic AI**

From exam guide:

- “function calling interfaces”
- “agent-tool interactions”
- “standardized access patterns”

---

# 🔥 Exam shortcut (lock this in)

Chat + tools + memory → Converse ✅  
Simple prompt → InvokeModel

---

# 🧠 Your level insight

This aligns perfectly with your architecture thinking:

InvokeModel → stateless execution layer  
Converse    → interaction + orchestration layer

👉 Converse = **interaction contract**  
👉 MCP = **tool contract**

---

# ⚡ Final intuition

InvokeModel = function call  
Converse    = conversation system

---

# ⚡ Next challenge (harder)

You need:

- streaming responses (token-by-token)
- chat interface
- tool calling

👉 Which API?

A. InvokeModel  
B. InvokeModelWithResponseStream  
C. Converse  
D. ConverseStream

---

Answer when ready 👇

32/75 Question A company develops an AI-powered product support chat assistant for a website. The architecture requires the chaining of the following three LLM calls: The first LLM call classifies the sentiment of the messages. The second LLM call summarizes documents from a product database. The third LLM call creates the final response. The company wants to maintain versions of the LLM prompts. The company wants to be able to roll back quickly if a new prompt underperforms. Which solution will meet these requirements with the LEAST development effort? Report Content Errors A Create an Amazon Bedrock knowledge base to retrieve documents from the product database. Use Amazon Bedrock Prompt Management to store the LLM prompts for each of the three LLM calls. Orchestrate the three LLM calls in a sequential workflow by using Amazon Bedrock Flows. Correct. Knowledge Bases is a managed RAG service that you can use to securely connect an LLM to enterprise data. Prompt Management provides lifecycle control for prompts. Flows is a visual orchestration service that you can use to chain multiple LLM calls. This solution chains multiple LLM calls together, maintains versions of prompts, and retrieves information from the product database. Learn more about Knowledge Bases. Learn more about Prompt Management. Learn more about Flows. B Create an Amazon Bedrock knowledge base to retrieve documents from the product database. Use Amazon Bedrock Prompt Management to store the LLM prompts for each of the three LLM calls. Orchestrate the three LLM calls in a sequential workflow by using AWS Step Functions. Incorrect. Knowledge Bases is a managed RAG service that you can use to securely connect an LLM to enterprise data. Prompt Management provides lifecycle control for prompts. Step Functions is an orchestration service. You can use Step Functions to orchestrate the three LLM calls. However, you must create and manage the Step Functions workflow and task functions. Therefore, this solution requires additional development effort. Learn more about Knowledge Bases. Learn more about Prompt Management. Learn more about Step Functions and Amazon Bedrock. C Create an Amazon Bedrock knowledge base to retrieve documents from the product database. Use AWS Systems Manager Parameter Store to store the LLM prompts for each of the three LLM calls. Orchestrate the three LLM calls in a sequential workflow by using Amazon Bedrock Flows. Incorrect. Knowledge Bases is a managed RAG service that you can use to securely connect an LLM to enterprise data. Parameter Store is a service that can manage configuration data such as environment variables. Flows is a visual orchestration service that you can use to chain multiple LLM calls. Parameter Store is not the most suitable service to store the prompts. Parameter Store supports the versioning of parameters and the rollback to previous versions. However, Parameter Store is not designed to store prompts for LLMs. Learn more about Knowledge Bases. Learn more about Parameter Store. Learn more about Flows. D Use Amazon Q Business to retrieve documents from the product database. Use Amazon Bedrock Prompt Management to store the LLM prompts for each of the three LLM calls. Orchestrate the three LLM calls in a sequential workflow by using Amazon Bedrock Flows. Incorrect. Amazon Q Business is a low-code no-code (LCNC) GenAI assistant that you can use to connect enterprise data and applications. Prompt Management provides lifecycle control for prompts. Flows is a visual orchestration service that you can use to chain multiple LLM calls. Amazon Q Business includes capabilities to automate multi-step processes. However, Amazon Q Business is not suitable for this scenario. You must manage Amazon Q Business prompts and conversational flows within Amazon Q Business itself. Amazon Q Business prompts and conversational flows cannot be version-controlled through Prompt Management. Therefore, Amazon Q Business is not suitable for this scenario. Learn more about Amazon Q Business. Learn more about Prompt Management. Learn more about Flows.

---

### ✅ Correct Answer: **A**

---

# 🧠 Concept First (what this question is testing)

This is a **“prompt orchestration + lifecycle management”** question.

👉 NOT just chaining LLMs — but:

How do I:  
1) Chain multiple LLM calls  
2) Manage prompts (version + rollback)  
3) Do it with LOWEST effort

---

# 🧩 Break the requirements

## 🎯 What you need

### 1. **Chaining LLM calls**

- sentiment → summarization → response  
    👉 multi-step workflow

---

### 2. **Prompt versioning + rollback**

👉 this is the KEY signal

From your study guide:

> Bedrock Prompt Management supports versioning and reuse of prompts

---

### 3. **Least development effort**

👉 means:

- no custom orchestration
- no manual workflow coding

---

# 🏗️ Why A is correct (the perfect combo)

## 🔹 1. Knowledge Base (RAG)

- Handles document retrieval automatically
- No need to build custom retrieval

---

## 🔹 2. Prompt Management (CRITICAL)

- Store prompts centrally
- Version control
- Rollback capability

👉 Exactly matches requirement

---

## 🔹 3. Bedrock Flows (THIS is the winner)

From your material:

> Flows allow chaining prompts and models visually

LLM1 → LLM2 → LLM3

- Visual / declarative
- No code orchestration
- Built for prompt chaining

---

# 🧠 Architecture (clean mental model)

User  
  ↓  
Bedrock Flow  
  ├── LLM 1: Sentiment  
  ├── LLM 2: Summarization (via KB)  
  └── LLM 3: Final response  
        ↑  
   Prompt Management (versioned prompts)

---

# ❌ Why others fail (important patterns)

---

## B — ❌ Step Functions

- Works technically
- BUT:
    - requires workflow definition
    - more dev effort

👉 violates:

> “LEAST development effort”

---

## C — ❌ Parameter Store

- Can version configs
- BUT:
    - not designed for prompts
    - no prompt lifecycle tooling

👉 wrong abstraction

---

## D — ❌ Amazon Q Business

- Managed assistant
- NOT flexible for custom chaining + prompt versioning

👉 wrong tool

---

# 🧠 Mental Model (THIS is exam gold)

Prompt lifecycle → Prompt Management ✅  
Prompt chaining  → Bedrock Flows ✅  
Workflow control → Step Functions (only if needed)

---

# 🔥 Exam Pattern

When you see:

|Requirement|Answer|
|---|---|
|prompt versioning|Prompt Management|
|chain LLM calls|Flows|
|least dev effort|managed service (Flows > Step Functions)|
|RAG|Knowledge Base|

---

# 🧠 From exam guide

- Prompt Management = governance + versioning
- Prompt Flows = chaining + orchestration

---

# ⚡ Key insight (very important)

👉 This question is about:

“Declarative GenAI pipelines” vs “programmatic pipelines”

- Flows → declarative (LOW effort) ✅
- Step Functions → programmatic (MORE effort) ❌

---

# 🚀 Your level insight

This maps to your architecture thinking:

Prompt layer        → Prompt Management  
Orchestration layer → Flows  
Execution layer     → Bedrock models

👉 This is **clean separation of concerns**

---

# ⚡ Quick challenge

You need:

- complex branching logic
- retries
- error handling
- human approval

👉 What do you use?

A. Bedrock Flows  
B. Step Functions  
C. Prompt Management  
D. Lambda

---

Answer when ready 👇

Step Funcs vs Bedrock Flows

This is a **core exam distinction** — and also maps directly to real architecture decisions.

---

# 🧠 Concept First (big picture)

Bedrock Flows   → GenAI-native orchestration (LLM workflows)  
Step Functions  → General-purpose orchestration (any workflow)

👉 Same idea (workflow), different **scope + abstraction level**

---

# 🧩 1. Bedrock Flows (GenAI-native)

From your notes:

> Flows chain prompts, models, and conditions visually

## 🎯 What it is

> **Low-code orchestration for LLM pipelines**

---

## 🏗️ What it looks like

LLM1 → LLM2 → LLM3  
   ↓      ↓      ↓  
Prompt   Prompt  Prompt

---

## ✅ Strengths

- Built for:
    - prompt chaining
    - RAG pipelines
    - GenAI workflows
- Native features:
    - Prompt Management integration
    - Knowledge Base integration
    - Conditional routing
- Minimal effort:
    - visual builder
    - declarative JSON

---

## ❌ Limitations

- Limited:
    - error handling
    - retries
    - complex branching
    - external system orchestration

---

## 🧠 When to use

Simple GenAI workflows  
Prompt pipelines  
RAG flows  
Multi-step LLM processing

---

# 🧩 2. Step Functions (General orchestration)

## 🎯 What it is

> **Full workflow engine for distributed systems**

---

## 🏗️ What it looks like

Task → Choice → Retry → Parallel → Wait → Human approval

---

## ✅ Strengths

- Powerful:
    - retries
    - error handling
    - circuit breakers
    - human-in-the-loop
- Integrates with:
    - Lambda
    - APIs
    - Bedrock
    - databases

---

## ❌ Trade-offs

- More:
    - code/config
    - setup effort
    - maintenance

---

## 🧠 When to use

Complex workflows  
Cross-service orchestration  
Failover logic  
Human approval  
Production-grade pipelines

---

# ⚔️ Side-by-side comparison

|Feature|Bedrock Flows|Step Functions|
|---|---|---|
|Purpose|GenAI workflows|Any workflow|
|Abstraction|High (LLM-native)|Low (general-purpose)|
|Setup effort|✅ Low|❌ Higher|
|Prompt integration|✅ Native|❌ Manual|
|RAG support|✅ Built-in|❌ Custom|
|Error handling|⚠️ Basic|✅ Advanced|
|Retry / fallback|❌ Limited|✅ Full control|
|Human approval|❌|✅|
|Best for exam|“least effort”|“complex logic”|

---

# 🧠 Mental Model (THIS is gold)

Flows           = LLM pipeline builder  
Step Functions  = system workflow engine

---

# 🔥 Exam Pattern (very important)

## 🟢 Choose **Bedrock Flows** when:

- “chain prompts”
- “multi-step LLM”
- “least development effort”
- “RAG + prompt pipeline”

---

## 🔵 Choose **Step Functions** when:

- “failover”
- “retry”
- “error handling”
- “human approval”
- “complex orchestration”

---

# 🧠 Real-world mapping (your level)

Flows           → your “prompt contract layer”  
Step Functions  → your “control plane orchestration”

---

# ⚡ Key insight

👉 AWS is pushing:

Simple GenAI → Flows  
Enterprise GenAI → Step Functions

---

# ⚡ Final intuition

If it's mostly LLM logic → Flows  
If it's system logic → Step Functions

---

# ⚡ Quick challenge

You need:

- sentiment → summarization → response
- prompt versioning
- minimal code

👉 What do you use?

A. Step Functions  
B. Bedrock Flows  
C. Lambda chain  
D. API Gateway

---

Answer when ready 👇

37/75 Question A large company is using Amazon Bedrock. The company wants to limit access to FMs to specific AWS and Anthropic models within designated development accounts. The company strictly prohibits third-party marketplace models. The company requires comprehensive logging of all model interactions for auditing purposes. The company uses AWS Organizations and AWS IAM Identity Center for account and user management. A security team must implement the solution while maintaining operational efficiency. Which combination of steps will meet these requirements with MINIMAL operational overhead? (Select TWO.) Report Content Errors A Create an RCP that denies access to marketplace models and unapproved built-in models. Apply the policy to the designated development accounts in the organization. Use a condition block to allow only approved AWS and Anthropic model IDs for bedrock:InvokeModel* actions. Incorrect. RCPs are an organization policy that you can use to manage the maximum permissions for resources in an organization. RCPs do not support all AWS services. RCPs do not support Amazon Bedrock. You cannot use an RCP to control access to Amazon Bedrock models. Learn more about RCPs. Learn more about how Amazon Bedrock works with IAM. Learn more about security in Amazon Bedrock. B Create an SCP that denies bedrock:InvokeModel* actions for unapproved or marketplace models by using the bedrock:ModelID condition key. Apply the policy to the root of the organization. Enable Amazon Bedrock model invocation logging. Correct. SCPs provide organization-wide preventive controls. SCPs can effectively deny access to marketplace models across all accounts. You can scope bedrock:InvokeModel* actions to only approved AWS and Anthropic model IDs. You can deny all other marketplace models. This step provides organization-wide governance with minimal operational overhead. You can enable Amazon Bedrock model invocation logging to capture all model interactions for auditing purposes, including inputs and outputs. Learn more about how Amazon Bedrock works with IAM. Learn more about SCPs. C Deploy AWS CloudFormation StackSets to provision standardized IAM roles across development accounts. Create IAM roles that allow access to only approved AWS and Anthropic models. Enable AWS CloudTrail logging for all Amazon Bedrock interactions. Incorrect. StackSets can deploy standardized IAM roles across multiple accounts. CloudTrail can capture API calls for Amazon Bedrock. However, this step is redundant and increases operational overhead. You must create and manage IAM roles in each account. The company is already using IAM Identity Center to manage permissions. Therefore, this step requires additional management overhead and could conflict with existing IAM Identity Center configurations. Learn more about IAM Identity Center. Learn more about StackSets. D Create a permission set in IAM Identity Center that allows bedrock:InvokeModel* actions only for specific AWS and Anthropic model ARNs by using IAM policy conditions. Apply the permission set to designated development accounts. Correct. IAM Identity Center permission sets provide a centralized way to manage user access to AWS services across accounts. You can scope Amazon Bedrock permissions to only specific AWS and Anthropic model ARNs by using condition keys. This step provides control over which models developers can invoke. This step uses the existing IAM Identity Center implementation to manage permissions. Therefore, this step minimizes operational overhead. Learn more about IAM Identity Center permission sets. E Create a custom AWS Config rule to detect when Amazon Bedrock model invocations include unapproved model IDs. Configure Amazon EventBridge to capture the noncompliant findings and invoke an AWS Lambda function. Configure the function to notify the security team and remove offending IAM permissions. Incorrect. You can create AWS Config custom rules to evaluate Amazon Bedrock usage against compliance requirements. EventBridge can trigger a Lambda function. However, this approach is reactive rather than preventative. This approach detects violations only after they occur. The company requires preventative enforcement. Learn more about custom rules. Learn more about EventBridge and Lambda.

---

### ✅ Correct Answers: **B + D**

---

# 🧠 Concept First (what this question is REALLY testing)

This is a **governance + access control pattern across an organization**

👉 Two layers:

Org-level guardrails   → SCP  
User-level access      → IAM Identity Center

---

# 🧩 Break the requirements

|Requirement|What it implies|
|---|---|
|Restrict models (AWS + Anthropic only)|**Prevent access → SCP**|
|Block marketplace models|**Org-wide deny → SCP**|
|Dev accounts only|**OU/account scoping**|
|Logging all interactions|**Bedrock invocation logs**|
|Minimal overhead|**centralized controls (no per-account setup)**|

---

# 🏗️ Why B is correct (ORG-level control)

## 🔹 SCP (Service Control Policy)

👉 This is the **strongest control layer**

AWS Organization  
   ↓  
SCP (deny unapproved models)  
   ↓  
All accounts (including dev)

---

## 🔑 Key feature

- Uses condition:
    - `bedrock:ModelID`
- Denies:
    - marketplace models
    - unapproved models

👉 Prevents misuse **before it happens**

---

## 🔹 Logging (important!)

- Enable Bedrock invocation logging
- Captures:
    - inputs
    - outputs
    - usage

👉 Required for audit

From study guide:

> CloudTrail and logs provide auditability of model usage

---

# 🏗️ Why D is correct (USER-level control)

## 🔹 IAM Identity Center (permission sets)

👉 This is **access assignment layer**

User → Permission Set → Allowed models

---

## 🔑 What it does

- Restrict:
    - specific model ARNs
- Assign:
    - to dev accounts
- Centralized:
    - no per-account IAM role sprawl

---

## 🧠 Why this is important

👉 SCP alone is NOT enough

SCP = maximum boundary (deny)  
IAM = actual access (allow)

You need BOTH:

---

# 🧠 Combined Architecture (THIS is gold)

AWS Organization  
   ↓  
SCP (deny everything except approved models)  
   ↓  
IAM Identity Center  
   ↓  
Users → allowed models only  
   ↓  
Bedrock  
   ↓  
Invocation logs (audit)

---

# ❌ Why others are wrong (exam patterns)

---

## A — ❌ RCP

- Not supported for Bedrock  
    👉 Immediate elimination

---

## C — ❌ StackSets + IAM roles

- Duplicates IAM Identity Center
- Higher overhead

👉 violates:

> minimal operational overhead

---

## E — ❌ Config + Lambda

- Reactive (detect after violation)
- Requirement = **preventative**

---

# 🧠 Mental Model (VERY important)

SCP → “what is forbidden” (org-wide)  
IAM → “what is allowed” (user-level)  
Logs → “what happened” (audit)

---

# 🔥 Exam Pattern

When you see:

|Requirement|Answer|
|---|---|
|org-wide restriction|SCP|
|restrict specific models|condition keys (ModelID)|
|centralized access|IAM Identity Center|
|audit / logging|Bedrock logs + CloudTrail|
|minimal ops|avoid per-account IAM|

---

# 🧠 From exam guide

- Governance includes:
    - IAM policies
    - CloudTrail logging
    - centralized access control

---

# ⚡ Key insight (this is gold)

👉 This question is testing:

Preventive control (SCP)  
+ Access control (IAM)  
+ Observability (logs)

---

# 🚀 Your level insight

This aligns with enterprise pattern:

Control Plane:  
  SCP → global guardrails  
  
Access Plane:  
  IAM Identity Center → user access  
  
Audit Plane:  
  Logs / CloudTrail → compliance

👉 This is **regulated GenAI architecture**

---

# ⚡ Quick challenge

You need:

- block certain models org-wide
- but allow exceptions for specific teams

👉 What combo?

A. IAM only  
B. SCP only  
C. SCP + IAM  
D. Config + Lambda

---

Answer when ready 👇

46/75 Question A GenAI developer is implementing a real-time AI assistant application. The application uses Amazon API Gateway WebSocket APIs to stream responses from an AWS Lambda function that calls an Amazon Bedrock FM with response streaming. The application must support connection management, including session state across multi-step interactions, retries, and disconnect cleanup. Which combination of steps will provide this functionality with MINIMAL operational overhead? (Select THREE.) Report Content Errors A Create a custom domain name for the WebSocket API. Incorrect. You can create a custom domain name for production applications. However, you do not need this configuration to enable streaming functionality between Amazon Bedrock and clients. The WebSocket API will work with the default API Gateway endpoint without a custom domain. Learn more about WebSocket APIs. B Configure an IAM role for the Lambda function with permissions that include bedrock:InvokeModelWithResponseStream and execute-api:ManageConnections. Add resource ARNs that include the API Gateway WebSocket API ID. Correct. The Lambda function requires specific IAM permissions to both invoke Amazon Bedrock models with streaming and to manage WebSocket connections. The resource ARNs must include the specific API Gateway WebSocket API ID to properly scope the permissions. Learn more about WebSocket APIs. Learn more about how to set up a WebSocket API integration. C Configure the Lambda function to use HTTP/1.1 chunked transfer encoding to manually implement response streaming. Incorrect. You can implement custom HTTP streaming in Lambda by using chunked transfer encoding. However, you do not need this step because Amazon Bedrock already provides built-in response streaming capabilities. This step requires complex custom code to break down model responses into chunks and manage the streaming protocol manually. Additionally, this step does not use the built-in integration between the Amazon Bedrock streaming API and API Gateway WebSocket connections. Therefore, this step increases operational overhead and adds potential points of failure. Learn more about WebSocket APIs. D Set up a WebSocket API in API Gateway with route selection expressions. Integrate the API with a Lambda function that handles connection management and streams responses back to clients using the API Gateway Management API. Correct. You need a WebSocket API in API Gateway to maintain persistent client connections. You must configure the API with the appropriate route selection expressions. The route selection expressions include $connect, $disconnect, and custom routes such as chat. Then, you must integrate with a Lambda function. These routes provide proper connection lifecycle handling. The Lambda function uses the API Gateway Management API to stream Amazon Bedrock responses back to clients in real time. Learn more about WebSocket APIs. Learn more about how to set up a WebSocket API integration. E Set up an Amazon DynamoDB table to persist active WebSocket connection IDs and session metadata. Update the table on $connect and $disconnect and use TTL. Correct. API Gateway WebSocket APIs provide connection IDs but do not persist the connection IDs. For session management across multi-step interactions, you must use a database to store connection IDs and session metadata. For example, you can use DynamoDB as the database. The $connect and $disconnect routes can update DynamoDB when clients join or leave. This step enables retries. This step provides multiple Lambda workflows and the cleanup of stale connections. Learn more about WebSocket APIs. Learn more about DynamoDB WebSocket connection management. F Set up an Amazon DynamoDB table to buffer Amazon Bedrock streaming tokens for each session. Enable DynamoDB Streams to invoke a Lambda function that forwards new tokens to clients over the WebSocket connection. Incorrect. Using DynamoDB as a token buffer introduces latency. You can store streaming tokens in DynamoDB and then use DynamoDB Streams to trigger another Lambda function. However, the Lambda function alone can handle the request to directly stream responses to clients by using the API Gateway Management API. Therefore, this step increases operational overhead for real-time streaming. Learn more about DynamoDB WebSocket connection management.

---

### ✅ Correct Answers: **B + D + E**

---

# 🧠 Concept First (what this question is testing)

This is a **real-time GenAI streaming architecture pattern**:

Client ↔ WebSocket ↔ Lambda ↔ Bedrock (streaming)

But the tricky part is:

> **connection lifecycle + session state + streaming**

---

# 🧩 Break the requirements

|Requirement|What you need|
|---|---|
|Real-time streaming|Bedrock streaming + WebSocket|
|Connection management|API Gateway WebSocket routes|
|Session state|persistent store|
|Retries / cleanup|lifecycle handling|
|Minimal overhead|managed services (no custom infra)|

---

# 🏗️ Why B is correct (permissions layer)

## 🔑 IAM role is critical

Lambda needs to:

1. Call Bedrock streaming API  
2. Push messages back via WebSocket

So you need:

- `bedrock:InvokeModelWithResponseStream`
- `execute-api:ManageConnections`

👉 Without this → nothing works

---

# 🏗️ Why D is correct (core architecture)

## 🔹 WebSocket API = connection layer

From your study guide:

- API Gateway handles real-time communication
- Lambda integrates backend logic

---

## 🧠 Flow

Client  
  ↓  
API Gateway (WebSocket)  
  ├── $connect  
  ├── $disconnect  
  ├── message route  
  ↓  
Lambda  
  ↓  
Bedrock (streaming)  
  ↓  
Lambda → WebSocket (send tokens back)

---

## 🔑 Key point

👉 API Gateway does:

- connection lifecycle
- routing

👉 Lambda does:

- streaming logic
- Bedrock invocation

---

# 🏗️ Why E is correct (state management)

## 🔹 DynamoDB = session + connection state

👉 WebSocket APIs DO NOT persist state

So you must store:

connectionId  
sessionId  
chat history / metadata

---

## 🔑 Why DynamoDB?

- serverless
- low latency
- TTL support for cleanup

---

## 🧠 Lifecycle

$connect     → store connectionId  
message      → retrieve session context  
$disconnect  → delete connection  
TTL          → cleanup stale sessions

---

# ❌ Why others are wrong (important patterns)

---

## A — ❌ Custom domain

- Nice to have
- NOT required

👉 irrelevant to functionality

---

## C — ❌ Manual chunked streaming

- Reinventing the wheel
- Bedrock already streams

👉 violates:

> minimal operational overhead

---

## F — ❌ DynamoDB as token buffer

- Adds latency
- unnecessary middle layer

👉 Lambda can stream directly

---

# 🧠 Mental Model (VERY important)

WebSocket API → connection lifecycle  
Lambda        → streaming + logic  
DynamoDB      → session state  
Bedrock       → token streaming

---

# 🔥 Exam Pattern

When you see:

|Requirement|Answer|
|---|---|
|real-time streaming|WebSocket API|
|connection lifecycle|$connect / $disconnect|
|send messages back|ManageConnections|
|session persistence|DynamoDB|
|minimal ops|avoid custom streaming infra|

---

# 🧠 From exam guide

- API Gateway supports:
    - real-time interaction
    - WebSocket communication
- DynamoDB:
    - session storage / state management

---

# ⚡ Key insight (this is gold)

👉 This architecture is:

Stateful frontend (WebSocket)  
+  
Stateless compute (Lambda)  
+  
State store (DynamoDB)

---

# 🚀 Your level insight

This maps cleanly to your architecture thinking:

Interaction layer → WebSocket API  
Execution layer   → Lambda  
State layer       → DynamoDB  
AI layer          → Bedrock

👉 Classic **event-driven + stateful GenAI system**

---

# ⚡ Quick challenge

You need:

- async processing (NOT real-time)
- large batch requests
- no persistent connection

👉 What do you use?

A. WebSocket API  
B. SQS + Lambda  
C. API Gateway WebSocket  
D. DynamoDB Streams

---

Answer when ready 👇

b

✅ **Correct — B (SQS + Lambda)**

---

# 🧠 Concept First

You correctly identified this as:

Async / decoupled processing pattern

👉 NOT real-time  
👉 NOT persistent connection

---

# 🧩 Why B is correct

## 🔹 Amazon SQS + AWS Lambda

Producer → SQS → Lambda → Processing → Response (later)

---

## 🎯 What this gives you

### 1. **Decoupling**

- Frontend ≠ backend
- No waiting for response

---

### 2. **Scalability**

- SQS buffers workload
- Lambda scales automatically

---

### 3. **Reliability**

- Retry built-in
- Message durability

---

## 📌 From your study guide

- SQS:
    - decouples systems
    - enables async processing

---

# ⚖️ Why others are wrong

---

## A / C — ❌ WebSocket

- Used for:
    - real-time streaming
    - persistent connection

👉 Overkill here

---

## D — ❌ DynamoDB Streams

- Used for:
    - reacting to DB changes

👉 Not for request processing pipeline

---

# 🧠 Mental Model (VERY important)

Real-time → WebSocket  
Async     → SQS  
Event     → EventBridge  
Stream    → Kinesis

---

# 🔥 Exam Pattern

When you see:

|Requirement|Answer|
|---|---|
|async processing|SQS|
|buffering|SQS|
|decoupling|SQS|
|batch jobs|SQS + Lambda|
|real-time streaming|WebSocket|

---

# 🧠 Tie back to GenAI (important)

From exam guide:

- async patterns use:
    - SQS
    - Lambda
    - event-driven design

---

# 🚀 Your level insight

This maps to architecture patterns:

Frontend → SQS (queue)  
          ↓  
      Lambda workers  
          ↓  
      Bedrock / processing

👉 This is how you:

- handle burst traffic
- avoid blocking UI
- scale GenAI workloads

---

# ⚡ Final intuition

If user must WAIT → WebSocket  
If user can WAIT → SQS

---

# ⚡ Next (optional but high value)

Want me to give you a **1-page cheat sheet** for:

- WebSocket vs SQS vs EventBridge vs Kinesis
- with exact exam triggers

This is one of the highest ROI topics for AP1 👍

when to use REST API

Great question — this is one of those **“choose the right interaction pattern”** topics that shows up everywhere in the exam.

---

# 🧠 Concept First

REST API = request → response (synchronous, stateless)

👉 It’s the **default integration pattern** unless something else is explicitly required.

---

# 🧩 When to use REST API (core scenarios)

## ✅ 1. Synchronous request–response

Client → API Gateway (REST) → Lambda → Bedrock → Response

Use when:

- user expects **immediate answer**
- request completes in **seconds**

👉 Example:

- “Summarize this document”
- “Classify this text”

---

## ✅ 2. Stateless interactions

- Each request is independent
- No persistent connection
- No session required

👉 Classic web/API pattern

---

## ✅ 3. Simple GenAI inference

From your study guide:

- API Gateway + Lambda is common for FM integration

👉 Use REST when:

- single prompt → single response
- no conversation memory needed

---

## ✅ 4. External / public APIs

- expose GenAI services to:
    - frontend apps
    - mobile apps
    - partners

👉 REST = industry standard

---

## ✅ 5. Low operational complexity

- easy to implement
- widely supported
- integrates with:
    - Lambda
    - Bedrock
    - Step Functions

---

# ⚖️ Compare with other patterns (THIS is exam gold)

## 🔹 REST vs WebSocket

REST       → one request, one response  
WebSocket  → continuous streaming / real-time

Use WebSocket when:

- streaming tokens
- chat typing experience

---

## 🔹 REST vs SQS

REST → synchronous  
SQS  → asynchronous

Use SQS when:

- long-running tasks
- batch jobs
- decoupling

---

## 🔹 REST vs EventBridge

REST        → direct call  
EventBridge → event-driven (pub/sub)

Use EventBridge when:

- loosely coupled systems
- event propagation

---

## 🔹 REST vs Step Functions

REST           → single operation  
Step Functions → multi-step workflow

---

# 🧠 Mental Model (lock this in)

Default → REST API  
Need real-time streaming → WebSocket  
Need async → SQS  
Need orchestration → Step Functions  
Need events → EventBridge

---

# 🏗️ Typical GenAI architecture with REST

User  
  ↓  
API Gateway (REST)  
  ↓  
Lambda  
  ↓  
Bedrock (InvokeModel / Converse)  
  ↓  
Response

---

# 🔥 Exam Pattern

If question says:

|Signal|Answer|
|---|---|
|“real-time API”|REST|
|“request/response”|REST|
|“frontend calls backend”|REST|
|“simple inference”|REST|
|“no mention of streaming/async”|REST|

---

# ⚡ Subtle trap (important)

👉 If question mentions:

- **streaming tokens**
- **live updates**
- **chat UI typing effect**

❌ NOT REST  
👉 Use WebSocket or streaming API

---

# 🚀 Your level insight

Think of REST as:

“control plane for GenAI calls”

- clean entry point
- enforce auth / throttling
- integrate with Lambda

---

# ⚡ Quick challenge

You are building:

- chatbot
- but responses are short (no streaming needed)
- stateless
- HTTP-based frontend

👉 Best choice?

A. REST API  
B. WebSocket  
C. SQS  
D. EventBridge

---

Answer when ready 👇

51/75 Question A company is building a generative AI (GenAI) application that uses Amazon Bedrock. The company uses AWS Organizations for its AWS accounts. The company's AWS accounts are divided into two OUs: development and production. The company uses IAM roles to grant the application access to Amazon Bedrock across both development and production accounts. Access to the Amazon Bedrock API from production accounts in the organization must not traverse the public internet. A GenAI developer must enforce this restriction, regardless of IAM role configuration or application behavior. Which solution will meet this requirement? Report Content Errors A Create an interface VPC endpoint for Amazon Bedrock in each production VPC where the application that requires access is deployed. Create an SCP that denies Amazon Bedrock actions unless the request comes through an approved VPC endpoint. Attach the SCP to the production OU. Correct. Interface VPC endpoints provide private connectivity to Amazon Bedrock within the AWS network. SCPs are an organization policy that you can use to manage permissions across accounts in an organization. The SCP enforces this control regardless of the IAM configuration in the accounts. This solution ensures that Amazon Bedrock actions are denied unless the requests originate from an approved VPC endpoint. Learn more about Amazon Bedrock interface VPC endpoints. Learn more about SCPs. B Create an interface VPC endpoint for Amazon Bedrock in each production VPC where the application that requires access is deployed. Create an IAM policy in each production account that denies Amazon Bedrock actions unless the request comes through an approved VPC endpoint. Attach the policy to the IAM roles in the account. Incorrect. Using interface VPC endpoints provides private access to Amazon Bedrock. However, IAM policies are attached to individual roles. Account administrators can modify or misconfigure IAM policies. This solution does not provide organization-wide enforcement. This solution does not ensure compliance if IAM roles are changed or improperly assigned. Learn more about IAM policies. C Create a NAT gateway in each production VPC where the application that requires access is deployed. Set the NAT gateway connectivity type to private. Update the route tables associated with the subnets to route Amazon Bedrock traffic to the NAT gateway. Incorrect. NAT gateways are a managed NAT service that allows network access from private subnets to the internet or other AWS services. NAT gateways do not allow inbound access from the internet. NAT gateways provide outbound connectivity from private subnets to other VPCs or on-premises networks. However, NAT gateways cannot route traffic to public AWS services unless the gateways are exposed through private connectivity mechanisms like interface VPC endpoints. An example of a public AWS service is Amazon Bedrock. This solution does not enforce organization-wide controls or block direct access to public Amazon Bedrock endpoints. Learn more about NAT gateways. D Create an interface VPC endpoint for Amazon Bedrock in each production VPC where the application that requires access is deployed. Attach endpoint policies to the endpoints to allow access from only the approved application. Incorrect. VPC endpoint policies are resource-based policies that you can attach to VPC endpoints. Endpoint policies can enforce which principals can access the service behind the endpoint. However, endpoint policies control access to only the endpoint itself. Endpoint policies do not control access to the service if accessed through the public endpoint. This solution does not prevent an application from bypassing the endpoint and calling the public Amazon Bedrock API directly. Learn more about VPC endpoint policies.

---

### ✅ Correct Answer: **A**

---

# 🧠 Concept First (what this question is REALLY testing)

This is a **network-level enforcement question**:

> ❗ “Must NOT traverse public internet”  
> ❗ “Enforce regardless of IAM / app behavior”

👉 Translation:

You need BOTH:  
1) Private connectivity  
2) Hard enforcement at org level

---

# 🧩 Break the requirement

## 🎯 Key signals

|Requirement|Meaning|
|---|---|
|no public internet|**PrivateLink / VPC endpoint**|
|regardless of IAM|**SCP (org-level enforcement)**|
|production accounts only|**OU-level control**|

---

# 🏗️ Why A is correct (perfect combo)

## 🔹 1. Interface VPC Endpoint (PrivateLink)

From your study guide:

> VPC endpoints provide private access to AWS services within a VPC

---

### What it does

App (VPC) → VPC Endpoint → Bedrock (private AWS network)

👉 No internet involved  
👉 Traffic stays inside AWS network

---

## 🔹 2. SCP (the KEY part)

👉 This is the real enforcement mechanism

SCP:  
DENY Bedrock unless request comes from VPC endpoint

---

### Why SCP is critical

Without SCP:  
App can still call public Bedrock endpoint ❌  
  
With SCP:  
Public calls are BLOCKED globally ✅

---

# 🧠 Architecture (THIS is gold)

Production VPC  
   ↓  
Interface VPC Endpoint (PrivateLink)  
   ↓  
Bedrock  
  
+ SCP (attached to Production OU)  
   ↓  
Deny if NOT via endpoint

---

# 🔥 Mental Model

Private access = VPC Endpoint  
Enforcement     = SCP

---

# ❌ Why others fail

---

## B — ❌ IAM policy

- Can be bypassed / changed
- Not org-enforced

👉 Requirement says:

> “regardless of IAM role configuration”

---

## C — ❌ NAT Gateway

- Still uses internet
- Does NOT enforce private access

👉 NAT ≠ PrivateLink

---

## D — ❌ Endpoint policy

- Controls access TO endpoint
- DOES NOT block public API access

👉 Big exam trap

---

# 🧠 From exam guide

- Private connectivity uses:
    - VPC endpoints
    - AWS PrivateLink

---

# ⚡ Key insight (VERY important)

👉 This question is testing:

“Network isolation + Org-level enforcement”

---

# 🧠 Pattern to remember

|Layer|Tool|
|---|---|
|Network (private access)|VPC Endpoint|
|Org enforcement|SCP|
|User access|IAM|

---

# 🚀 Your level insight

This maps perfectly to enterprise security:

Control plane → SCP (non-bypassable)  
Network plane → PrivateLink  
Access plane  → IAM

👉 This is **zero-trust GenAI access pattern**

---

# ⚡ Quick challenge

You need:

- ensure S3 access ONLY via VPC endpoint
- block internet access completely
- enforce across all accounts

👉 What do you use?

A. IAM policy  
B. Endpoint policy  
C. SCP + VPC endpoint  
D. NAT gateway

---

Answer when ready 👇

draw ASCII diagram for option A

Here’s a clean **exam-ready ASCII diagram** for **Option A** — showing both **network path + enforcement layer**.

---

# 🏗️ Architecture — Private Bedrock Access with SCP Enforcement

┌──────────────────────────────────────────────────────────────┐  
│                    AWS ORGANIZATION                          │  
│                                                              │  
│   ┌──────────────────────────────────────────────────────┐   │  
│   │  Service Control Policy (SCP)                         │   │  
│   │                                                      │   │  
│   │  DENY bedrock:InvokeModel*                           │   │  
│   │  IF request NOT via approved VPC Endpoint            │   │  
│   │                                                      │   │  
│   └──────────────────────────────────────────────────────┘   │  
│                           │                                  │  
│                           ▼                                  │  
│                ┌──────────────────────┐                       │  
│                │   Production OU      │                       │  
│                └──────────────────────┘                       │  
│                           │                                  │  
│        ┌──────────────────┴──────────────────┐                │  
│        │                                     │               │  
│  ┌───────────────┐                   ┌───────────────┐        │  
│  │ Prod Account A │                  │ Prod Account B │        │  
│  └───────────────┘                   └───────────────┘        │  
│        │                                     │               │  
│        ▼                                     ▼               │  
│  ┌──────────────────────────────┐   ┌────────────────────────┐│  
│  │          VPC                 │   │          VPC            ││  
│  │                              │   │                        ││  
│  │  ┌────────────────────────┐  │   │  ┌──────────────────┐  ││  
│  │  │   Application (EC2 /   │  │   │  │   Application     │  ││  
│  │  │   Lambda / ECS)        │  │   │  │                   │  ││  
│  │  └────────────┬───────────┘  │   │  └────────┬─────────┘  ││  
│  │               │              │   │           │            ││  
│  │               ▼              │   │           ▼            ││  
│  │    ┌─────────────────────┐   │   │   ┌─────────────────┐ ││  
│  │    │ Interface VPC       │   │   │   │ Interface VPC   │ ││  
│  │    │ Endpoint (PrivateLink)│ │   │   │ Endpoint        │ ││  
│  │    └─────────┬───────────┘   │   │   └────────┬────────┘ ││  
│  │              │               │   │            │          ││  
│  └──────────────┼───────────────┘   └────────────┼──────────┘│  
│                 │                                │           │  
│                 ▼                                ▼           │  
│        ┌────────────────────────────────────────────────┐    │  
│        │        Amazon Bedrock (Private AWS Network)    │    │  
│        └────────────────────────────────────────────────┘    │  
│                                                              │  
└──────────────────────────────────────────────────────────────┘

---

# 🧠 How to read this (important)

## 🔹 1. **Data path (network)**

App → VPC Endpoint → Bedrock

👉 Uses:

- **AWS PrivateLink**
- No public internet

---

## 🔹 2. **Control path (enforcement)**

SCP → denies any request NOT via endpoint

👉 Even if someone tries:

App → public Bedrock endpoint ❌ BLOCKED

---

# 🔥 Key exam insight (this is the takeaway)

Private connectivity alone ≠ secure  
You MUST enforce it with SCP

---

# 🧠 Mental model (lock this in)

VPC Endpoint → HOW traffic flows  
SCP          → WHAT is allowed

---

# ⚡ One-liner to remember

👉 **“PrivateLink + SCP = non-bypassable private access”**

---

If you want, I can draw the **“wrong architecture” (Option D)** side-by-side — that’s actually a really powerful way to lock this concept in.

52/75 Question A company is using an Amazon Bedrock agent that assists customers. The company must implement comprehensive observability capabilities. The company wants to understand and track the agent's reasoning process in making decisions. The solution must provide detailed visibility into the agent's reasoning process. The solution must provide quick identification of potential hallucinations. Which solution will meet these requirements? Report Content Errors A Implement OrchestrationTrace with CustomOrchestrationTrace analysis. Use Amazon CloudWatch metrics for token usage patterns and FM performance monitoring. Validate agent behavior against a golden dataset to detect anomalies. Incorrect. OrchestrationTrace provides insights into action invocations and knowledge base queries. Using OrchestrationTrace with CustomOrchestrationTrace does not capture critical pre-processing and post-processing validation steps. OrchestrationTrace alone traces only the I/O of the orchestration step. This solution does not provide complete visibility into the entire reasoning process. Learn more about OrchestrationTrace. Learn more about CustomOrchestrationTrace. B Configure GuardrailTrace with RoutingClassifierTrace. Use ModelInvocationInput analysis to validate the agent's decision boundaries and response patterns. Compare outputs against a golden dataset. Incorrect. GuardrailTrace and RoutingClassifierTrace can help with I/O assessment and routing decisions. However, GuardrailTrace and RoutingClassifierTrace focus primarily on content filtering and routing rather than comprehensive reasoning analysis. GuardrailTrace is specifically designed for content intervention and policy enforcement rather than full reasoning process validation. Learn more about GuardrailTrace. Learn more about RoutingClassifierTrace. C Enable PreProcessingTrace, OrchestrationTrace, and PostProcessingTrace components with golden dataset validation and systematic trace analysis. Correct. This solution provides end-to-end visibility into the agent's reasoning process. Each step in the console or trace in the API includes these three essential components. Together these components provide complete coverage of the agent's processing pipeline. Additionally, the golden dataset validation provides systematic detection of hallucinations and reasoning failures. Learn more about PreProcessingTrace. Learn more about OrchestrationTrace. Learn more about PostProcessingTrace. D Combine FailureTrace monitoring with PostProcessingTrace analysis. Implement custom parser modes with override AWS Lambda functions for response validation. Use a golden dataset for periodic checks of output consistently. Incorrect. FailureTrace and PostProcessingTrace with custom parsers can help identify failures and validate final outputs. However, this solution does not capture critical insights from the pre-processing and orchestration phases. FailureTrace provides information only about step failures. FailureTrace does not provide proactive insight into the agent's reasoning process. Learn more about FailureTrace. Learn more about PostProcessingTrace.

---

### ✅ Correct Answer: **C**

---

# 🧠 Concept First (what this question is testing)

This is **Agent Observability — specifically reasoning visibility**

👉 Not logs, not metrics — but:

“How did the agent THINK?”

---

# 🧩 Key requirement signals

|Requirement|What it implies|
|---|---|
|track reasoning process|**Agent Tracing (full pipeline)**|
|detailed visibility|**end-to-end trace coverage**|
|detect hallucinations|**compare reasoning vs expected (golden dataset)**|

---

# 🏗️ Why C is correct (FULL coverage)

From your study guide:

> Bedrock Agent Tracing provides visibility into the agent’s reasoning process

---

## 🔹 Three critical trace components

### 1. **PreProcessingTrace**

User input → interpretation → classification

- intent detection
- input transformation
- routing decisions

---

### 2. **OrchestrationTrace**

Agent → tools / KB → actions

- which tools were called
- which KB was queried
- intermediate reasoning steps

---

### 3. **PostProcessingTrace**

Raw output → final response

- formatting
- filtering
- final answer generation

---

# 🧠 Combined = FULL reasoning visibility

User Input  
   ↓  
PreProcessingTrace  
   ↓  
OrchestrationTrace  
   ↓  
PostProcessingTrace  
   ↓  
Final Response

👉 This is the **complete reasoning pipeline**

---

# 🔥 Why this matters for hallucination detection

👉 Hallucination ≠ just wrong answer

It’s:

Wrong reasoning path  
OR  
Missing grounding  
OR  
Incorrect tool usage

---

## With full tracing:

You can see:

- Did it retrieve correct context?
- Did it call the right tool?
- Did it misinterpret input?

👉 This is how you **diagnose hallucination root cause**

---

# 🧪 Golden dataset (second key piece)

From exam guide:

> Golden datasets help detect hallucinations and validate outputs

---

## What it does

Expected output vs actual output  
+  
Trace comparison

👉 Detect:

- drift
- hallucination
- reasoning inconsistency

---

# ❌ Why others are wrong

---

## A — ❌ Orchestration only

- Missing:
    - input reasoning
    - output validation

👉 partial visibility

---

## B — ❌ GuardrailTrace

- Focuses on:
    - safety
    - filtering

👉 NOT reasoning

---

## D — ❌ FailureTrace

- Only shows:
    - errors

👉 NOT full reasoning

---

# 🧠 Mental Model (VERY important)

Agent Observability = Full Trace Pipeline  
  
Pre + Orchestration + Post = COMPLETE reasoning

---

# 🔥 Exam Pattern

If you see:

|Signal|Answer|
|---|---|
|reasoning visibility|Agent Tracing|
|debugging agent decisions|full trace types|
|hallucination detection|golden dataset + traces|
|“comprehensive observability”|ALL trace stages|

---

# 🧠 Your level insight (this is strong)

This maps perfectly to your architecture thinking:

Deterministic system → logs + metrics  
Agent system        → reasoning traces

👉 This is the **shift from system observability → cognitive observability**

---

# ⚡ Final intuition

Logs tell you WHAT happened  
Traces tell you WHY it happened

---

# ⚡ Quick challenge

You only enable:

- OrchestrationTrace

👉 What are you missing?

A. Tool usage  
B. Input reasoning  
C. Final output  
D. Latency

---

Answer when ready 👇

confusion: reasoning is tracked in Guardrails trace?

Great confusion — and exactly the kind AWS tests 👍  
Let’s untangle it cleanly.

---

# 🧠 Concept First

👉 **“Reasoning” ≠ “Safety checks”**

Agent reasoning → how the agent decides  
Guardrails      → whether output is allowed

---

# 🧩 What each trace actually represents

## 🔹 Agent reasoning (the real “thinking”)

From your guide:

> Agent tracing shows reasoning, tool usage, KB hits

This comes from:

### ✅ Core reasoning traces

- **PreProcessingTrace** → understanding input
- **OrchestrationTrace** → planning + tool usage
- **PostProcessingTrace** → forming final answer

👉 This is the **decision pipeline**

---

## 🔹 GuardrailTrace (what it really does)

👉 GuardrailTrace is:

“Did this response violate policy?”

Examples:

- PII detected?
- harmful content?
- grounding score?

---

## 🧠 Key distinction

Reasoning = WHY the agent did something  
Guardrails = SHOULD this be allowed

---

# 🏗️ Visual comparison (this is the clarity point)

User Input  
   ↓  
PreProcessingTrace       ← reasoning starts  
   ↓  
OrchestrationTrace       ← reasoning (tools, KB, decisions)  
   ↓  
PostProcessingTrace      ← reasoning (final shaping)  
   ↓  
GuardrailTrace           ← safety check ONLY  
   ↓  
Final Output

---

# 🔥 Why your confusion makes sense

Because Guardrails can:

- detect hallucinations (via grounding)
- evaluate response quality

So it _feels like reasoning_

👉 But actually:

Guardrails = evaluation layer  
NOT decision-making layer

---

# 🧠 Analogy (very useful)

Agent = doctor diagnosing patient  
Guardrails = hospital compliance officer

- Doctor decides diagnosis → reasoning
- Compliance checks legality → guardrails

---

# ⚡ What GuardrailTrace CAN tell you

- response blocked / modified
- policy triggered
- grounding score (hallucination signal)

👉 BUT NOT:

- why agent chose a tool
- why it retrieved certain context
- how it decomposed the task

---

# 🧠 From exam perspective (important)

If question asks:

### 🔵 “reasoning process”

👉 **Agent tracing (Pre + Orchestration + Post)**

---

### 🟡 “policy / safety / filtering”

👉 **GuardrailTrace**

---

# ⚠️ Exam trap

AWS will try to trick you with:

- “detect hallucinations” → sounds like guardrails
- BUT also:
- “understand reasoning process”

👉 That combo → **full tracing (C)**

---

# 🧠 Mental Model (lock this in)

Reasoning   = trace pipeline  
Guardrails  = safety filter

---

# ⚡ Quick test

Which one tells you:

> “Why did the agent call this tool?”

A. GuardrailTrace  
B. OrchestrationTrace  
C. FailureTrace  
D. CloudWatch Logs

---

Answer when ready 👇

54/75 Question A real estate company needs to automate the extraction of specific fields from various utility bills in PDF format. The company manages thousands of commercial and residential properties and receives utility bills monthly. The utility bill types include electricity, water, and gas depending on the property location. Each bill type has its own unique format and a predefined set of fields that the company needs to extract. The solution must automatically identify the bill type and extract corresponding information when bills upload to Amazon S3. Which solution will meet these requirements with the LEAST operational overhead? Report Content Errors A Use Amazon Rekognition to create an Amazon Rekognition Custom Labels model that is trained with sample images from each bill type. Use Amazon Bedrock to create three separate Bedrock Data Automation (BDA) projects, each dedicated to a specific bill type with a corresponding blueprint and field definitions. Configure an Amazon EventBridge rule to detect S3 upload events and invoke an AWS Lambda function. Configure the function to first use Custom Labels to identify the document type, and then invoke the Amazon Bedrock InvokeDataAutomationAsync API with the corresponding project to extract the fields. Incorrect. You can use Custom Labels to train custom computer vision models to detect objects and scenes that are specific to your business needs. This solution requires additional operational overhead. You must maintain multiple BDA projects and a Custom Labels model. Using two different services for document classification (Amazon Rekognition and Amazon Bedrock) adds complexity without providing additional benefits. Learn more about BDA. Learn more about Custom Labels. B Use Amazon Rekognition to create an Amazon Rekognition Custom Labels model that is trained with sample images from each bill type. Configure an Amazon EventBridge rule to detect S3 upload events and invoke an AWS Lambda function. Configure the function to invoke the Custom Labels model to identify the bill type, invoke Amazon Textract AnalyzeDocument with queries to extract text from the document, and run custom Python code. Configure the Python code to parse and extract the required fields based on the identified document type. Incorrect. You can use Custom Labels to train custom computer vision models to detect objects and scenes that are specific to your business needs. Amazon Textract AnalyzeDocument with queries can extract structured fields from scanned utility bills. However, this solution requires additional operational overhead. You must train and manage a custom Amazon Rekognition model and maintain custom Python code for field extraction. You must orchestrate workflows across Amazon Rekognition, Amazon Textract, and Lambda. Additionally, changes in bill formats would require re-training models and updating code. Learn more about Custom Labels. Learn more about Amazon Textract. Learn more about AnalyzeDocument with queries. C Use Amazon Bedrock to create a single Bedrock Data Automation (BDA) project that contains multiple blueprints. Create one blueprint for each bill type, including the bill type description and fields to extract. Configure an Amazon EventBridge rule to detect S3 upload events and trigger an AWS Lambda function. Configure the function to invoke the Amazon Bedrock InvokeDataAutomationAsync API to process the document with the created project, automatically select the appropriate blueprint, and extract the corresponding fields. Correct. BDA is a fully managed document processing service that automates the extraction of data from documents by using AI. BDA blueprints are templates that define the structure and rules to process specific document types. You can use a single project with multiple blueprints to streamline management while maintaining functionality. BDA automatically detects the blueprint to use based on the document type. BDA handles field extraction. This solution does not require custom code maintenance or multiple service orchestration. Learn more about BDA. D Use Amazon Bedrock to create three separate Bedrock Data Automation (BDA) projects, each dedicated to a specific bill type with a corresponding blueprint and field definitions. Configure an Amazon EventBridge rule to detect S3 upload events and invoke an AWS Lambda function. Configure the function to invoke Amazon Bedrock InvokeDataAutomationAsync API to analyze the document and automatically select the appropriate project and extract the corresponding fields. Incorrect. BDA is a fully managed document processing service that automates the extraction of data from documents by using AI. BDA does not support automatic project selection from incoming documents. Each document must be explicitly processed against a specific project. Learn more about BDA.

---

### ✅ Correct Answer: **C**

---

# 🧠 Concept First (what this question is REALLY testing)

This is a **modern Intelligent Document Processing (IDP)** question.

👉 Not just OCR, not just extraction — but:

“Auto-classify + extract structured fields with MINIMAL effort”

---

# 🧩 Key requirement signals

|Requirement|Meaning|
|---|---|
|multiple bill formats|**classification needed**|
|predefined fields per type|**schema/blueprint extraction**|
|auto identify type|**no manual routing**|
|S3 upload trigger|**event-driven pipeline**|
|least operational overhead|**managed AI service (BDA)**|

---

# 🏗️ Why C is correct (perfect design)

## 🔹 Single BDA Project + Multiple Blueprints

From your study guide:

> BDA projects can contain multiple blueprints and automatically classify documents

---

## 🧠 What happens internally

S3 Upload  
   ↓  
EventBridge  
   ↓  
Lambda  
   ↓  
BDA Project  
   ├── Blueprint: Electricity bill  
   ├── Blueprint: Water bill  
   ├── Blueprint: Gas bill  
   ↓  
Auto classification + field extraction  
   ↓  
Structured JSON output

---

# 🔥 Why this is powerful

👉 You get **3 things in ONE service**

### 1. Classification

- detects bill type automatically

---

### 2. Extraction

- pulls fields (amount, date, etc.)

---

### 3. Normalization

- standard output format

---

# 🧠 Key concept (VERY important)

Blueprint = schema + extraction rules + classification hint

From guide:

> Blueprints define fields, classification, and transformations

---

# ❌ Why others are wrong

---

## A — ❌ Rekognition + multiple BDA projects

- too many moving parts
- multiple projects to manage

👉 violates:

> minimal operational overhead

---

## B — ❌ Rekognition + Textract + custom code

- heavy:
    - model training
    - parsing logic
    - maintenance

👉 classic “old-school pipeline”

---

## D — ❌ Multiple BDA projects

- BDA does NOT auto-select projects
- requires manual routing

👉 wrong assumption

---

# 🧠 Mental Model (THIS is gold)

Traditional IDP → Rekognition + Textract + code  
Modern IDP     → BDA (all-in-one)

---

# 🔥 Exam Pattern

If you see:

|Signal|Answer|
|---|---|
|document classification + extraction|BDA|
|multiple document formats|BDA blueprints|
|minimal ops|single project|
|structured output|BDA|

---

# 🧠 From your study guide

- BDA:
    - extracts structured data
    - uses blueprints
    - supports classification + extraction

---

# ⚡ Key insight (VERY important)

👉 This question is testing:

“Service consolidation vs pipeline complexity”

---

# 🚀 Your level insight

This fits your architecture style perfectly:

Ingestion layer → S3  
Processing layer → BDA  
Output layer → structured data (JSON)

👉 No:

- custom ML
- orchestration complexity
- parsing logic

---

# ⚡ Final intuition

If problem = “documents → structured fields”  
→ Use BDA FIRST

---

# ⚡ Quick challenge

You need:

- extract fields from invoices
- but ALSO perform sentiment analysis on text

👉 Best combo?

A. BDA only  
B. BDA + Comprehend  
C. Textract only  
D. Rekognition only

---

Answer when ready 👇

55/75 Question A GenAI developer builds an AI-powered customer service chat application for a company. The GenAI developer uses Amazon Bedrock to build the application. The application processes natural language inputs from users and generates real-time responses. The responses reference users' personally identifiable information (PII). The GenAI developer must configure the application to handle PII appropriately. According to internal privacy policies, PII should not be inadvertently exposed during or after inference. Prompt data cannot be retained longer than necessary. The handling of PII must comply with defined storage and retention policies. Which solution will meet these requirements? Report Content Errors A Use Amazon Macie to scan stored user prompts and responses in Amazon S3 for PII. Apply Amazon Comprehend for PII detection on stored logs to identify PII post-inference. Configure S3 Lifecycle policies to transition or expire objects after the retention period. Use AWS Config rules to monitor lifecycle policies that apply to S3 buckets and enforce remediation if a bucket is not compliant. Incorrect. In this solution, all actions occur after the data is already written to Amazon S3. Therefore, this solution could expose PII during inference. Additionally, PII could be logged in raw form. Lifecycle policies and AWS Config rules enforce storage compliance. However, this solution does not ensure that PII is redacted before or during model interaction. This solution is primarily reactive and does not meet the requirements. Learn more about Amazon Comprehend PII detection. Learn more about AWS Config rules. B Use Amazon Bedrock Guardrails to mask PII in user prompts before inference and redact PII from generated responses. Store prompts and model responses in Amazon S3. Use Amazon Macie to automatically classify and alert on PII stored in Amazon S3. Configure S3 Lifecycle policies to enforce data retention limits. Correct. Guardrails can mask PII in user prompts before the prompts reach the model. Therefore, guardrails can reduce privacy risk at inference. Guardrails ensure that unredacted PII does not persist in logs or stored outputs. The application can still present user-appropriate responses in real time. Macie provides automated sensitive data discovery in Amazon S3. S3 Lifecycle policies enforce retention limits to meet retention requirements. Learn more about guardrail sensitive data filters. Learn more about sensitive data discovery by using Macie. Learn more about data retention through S3 Lifecycle management. C Use Amazon Bedrock Guardrails to mask PII in user prompts before inference and redact PII from generated responses. Store prompts and model responses in Amazon S3. Use Amazon Macie to scan stored data for PII and trigger alerts for compliance violations. Apply an S3 Lifecycle policy to move data for archival storage. Configure IAM roles to control access to PII. Incorrect. Guardrails can mask PII before and after inference. However, this solution moves data to archival storage rather than deleting the data. Therefore, this solution might violate retention requirements. Macie can classify sensitive data post-inference. However, this solution does not ensure the removal of sensitive data in compliance with retention policies. Learn more about Guardrails. D Use Amazon Bedrock Guardrails to filter PII from prompts and responses. Store interaction logs in Amazon S3 with server-side encryption using AWS KMS. Enable AWS CloudTrail to log Amazon Bedrock API usage and apply Amazon Macie to generate compliance reports. Configure S3 Lifecycle policies to enforce data retention limits. Incorrect. Guardrails can prevent the generation of harmful or sensitive outputs. This solution uses Amazon S3 with AWS KMS for secure storage and CloudTrail for API visibility. This solution uses Macie for compliance scans. However, redacting PII from responses prevents the application from delivering user details. Additionally, compliance scans and S3 Lifecycle policies alone do not ensure the deletion of PII as required by retention policies. Learn more about Guardrails data filters. Learn more about data retention through S3 Lifecycle management.

---

### ✅ Correct Answer: **B**

---

# 🧠 Concept First (what this question is REALLY testing)

This is a **PII protection across the full GenAI lifecycle** question:

Before inference  → protect input  
During inference  → prevent leakage  
After inference   → enforce storage & retention

👉 You need **defense-in-depth**, not just one control.

---

# 🧩 Break the requirements

|Requirement|What it implies|
|---|---|
|PII not exposed during inference|**pre-inference masking**|
|PII not exposed after inference|**post-inference redaction**|
|no long retention|**lifecycle deletion**|
|compliance + audit|**classification + monitoring**|

---

# 🏗️ Why B is correct (full lifecycle coverage)

## 🔹 1. **Before & during inference → Guardrails**

From your study guide:

> Guardrails filter prompts and responses and can mask PII

---

### What happens

User input (PII)  
   ↓  
Guardrails → mask PII  
   ↓  
Model inference (safe)  
   ↓  
Guardrails → redact output

👉 This is **proactive protection**

---

## 🔹 2. **After inference → Amazon Macie**

👉 Detects:

- stored PII
- misconfigurations
- compliance issues

---

### Important

Macie = detection + audit (NOT prevention)

---

## 🔹 3. **Retention → S3 Lifecycle**

From your guide:

- lifecycle policies enforce deletion / expiry

👉 Ensures:

- data not stored longer than allowed

---

# 🧠 Full Architecture (THIS is gold)

User  
  ↓  
Guardrails (mask input PII)  
  ↓  
Bedrock model  
  ↓  
Guardrails (redact output)  
  ↓  
S3 (store sanitized data)  
  ↓  
Macie (detect / audit)  
  ↓  
S3 Lifecycle (delete after retention period)

---

# 🔥 Key insight (VERY important)

👉 This question is testing:

Preventive + Detective + Retention controls

|Layer|Tool|
|---|---|
|Prevent (before/during)|Guardrails|
|Detect (after)|Macie|
|Enforce retention|S3 Lifecycle|

---

# ❌ Why others fail

---

## A — ❌ Reactive only

- PII already stored
- no protection during inference

👉 too late

---

## C — ❌ Archival instead of deletion

- violates:
    - retention policy

👉 storing ≠ compliant

---

## D — ❌ Misunderstands redaction

- removes useful data entirely
- misses proper lifecycle handling

---

# 🧠 Mental Model (lock this in)

Guardrails → prevent leakage  
Macie      → detect issues  
Lifecycle  → enforce deletion

---

# 🔥 Exam Pattern

If you see:

|Signal|Answer|
|---|---|
|protect PII before inference|Guardrails|
|detect sensitive data in storage|Macie|
|retention / deletion|S3 Lifecycle|
|compliance|combination of all|

---

# 🧠 From exam guide

- Privacy controls include:
    - Guardrails
    - Comprehend / Macie
    - Lifecycle policies

---

# ⚡ Your level insight

This matches enterprise pattern:

Ingress control → Guardrails  
Data lake control → Macie  
Data lifecycle → S3 policies

👉 This is **regulated AI architecture**

---

# ⚡ Final intuition

If question says “PII safety”  
→ ALWAYS think:  
Guardrails + Macie + Lifecycle

---

# ⚡ Quick challenge

You need:

- detect PII in real-time BEFORE model
- block unsafe prompts
- no storage yet

👉 What do you use?

A. Macie  
B. Guardrails  
C. CloudTrail  
D. S3 Lifecycle

---

Answer when ready 👇

57/75 Question A global company is building a multilingual customer service AI assistant by using Amazon Bedrock. The company has fine-tuned multiple Amazon Bedrock FMs, each for a different support topic. For example, billing-related queries must route to a model that is fine-tuned for finance. Technical troubleshooting queries must route to a model that is fine-tuned for product diagnostics. All incoming messages are processed through an Amazon API Gateway API. The company wants to build an event-driven solution that handles routing logic and is scalable. Which solution will meet these requirements with the LEAST operational overhead? Report Content Errors A Configure the API Gateway API to proxy the request to an AWS Lambda function. Configure the Lambda function to call Amazon Comprehend to detect the dominant language of the query. Route the request to the appropriate Amazon Bedrock model based on the detected language. Incorrect. Amazon Comprehend is a natural language processing service that can identify the dominant language in text. Detecting the language is not sufficient to determine the support topic or the intent of the query. Learn more about Amazon Comprehend language detection. Learn more about the detect dominant language API. B Fine-tune an FM in Amazon Bedrock for topic classification. Configure the API Gateway API to proxy the request to an AWS Lambda function. Configure the Lambda function to invoke the trained FM to determine the topic. Route the request to the appropriate Amazon Bedrock model based on the detected topic. Incorrect. Amazon Bedrock model customization provides training data to a model to enhance its performance for targeted or specific use cases. This solution introduces unnecessary model fine-tuning and increases operational overhead. Hosting fine-tuned models on Amazon Bedrock requires provisioned throughput. Provisioned throughput can add cost depending on the expected throughput. Learn more about fine-tuning Amazon Bedrock models. C Build and deploy a custom classification model on an inference endpoint in Amazon SageMaker AI. Configure the API Gateway API to proxy the request to an AWS Lambda function. Configure the Lambda function to call the classification inference endpoint to identify the topic of the query. Route the request to the appropriate Amazon Bedrock model based on the detected topic. Incorrect. SageMaker AI is a managed service that you can use to build, train, and deploy ML models. To use SageMaker AI, you must train a model. You must provision and maintain an inference endpoint. Therefore, this solution requires additional operational overhead. Learn more about SageMaker AI model training. D Train a custom Amazon Comprehend classification model. Configure the API Gateway API to proxy the request to an AWS Lambda function. Configure the Lambda function to call Amazon Comprehend custom classification to identify the topic of the query. Route the request to the appropriate Amazon Bedrock model based on the detected topic. Correct. You can use Amazon Comprehend custom classification to train a custom model to classify text into labels. This solution can detect user-defined categories, such as billing and technical support. Amazon Comprehend is fully managed and requires no model hosting. This solution provides dynamic routing to specialized Amazon Bedrock FMs depending on the detected support topic. Learn more about Amazon Comprehend custom classification.

---

### ✅ Correct Answer: **D**

---

# 🧠 Concept First (what this question is REALLY testing)

This is a **routing + classification pattern**:

User query → classify intent → route to specialized model

👉 Key: **classification ≠ generation**

---

# 🧩 Break the requirements

|Requirement|What it implies|
|---|---|
|route to different FMs|**intent/topic classification**|
|multilingual|(nice-to-have, not core problem)|
|event-driven|Lambda / API Gateway|
|least operational overhead|**fully managed service (no model hosting)**|

---

# 🏗️ Why D is correct (best fit)

## 🔹 Amazon Comprehend Custom Classification

From your study guide:

> Comprehend custom classification organizes text into user-defined categories

---

## 🧠 What it does

User query  
   ↓  
Comprehend Custom Classifier  
   ↓  
Label:  
  - billing  
  - technical  
  - etc.  
   ↓  
Lambda routes to correct Bedrock FM

---

## 🔑 Why this is optimal

### 1. **Purpose-built for classification**

- exactly matches use case
- no overengineering

---

### 2. **Fully managed**

- no model hosting
- no endpoint management

---

### 3. **Low operational overhead**

- train once
- invoke via API

---

# ❌ Why others are wrong (important patterns)

---

## A — ❌ Language detection

- detects **language**, not **intent**

👉 wrong problem

---

## B — ❌ Fine-tuned FM

- overkill
- requires:
    - training
    - provisioning throughput

👉 violates:

> least operational overhead

---

## C — ❌ SageMaker model

- even heavier:
    - training
    - endpoint hosting
    - scaling

👉 classic “too much infra”

---

# 🧠 Mental Model (THIS is gold)

Simple classification → Comprehend ✅  
LLM reasoning        → Bedrock ❌ (overkill)  
Custom ML            → SageMaker ❌ (too heavy)

---

# 🔥 Exam Pattern

If you see:

|Signal|Answer|
|---|---|
|classify text into categories|Comprehend|
|route requests by intent|Comprehend|
|minimal ops|managed NLP (Comprehend)|
|avoid building model|NOT SageMaker|

---

# 🧠 From exam guide

- Comprehend:
    - classification
    - entity extraction
    - text analysis
- Event-driven architectures:
    - API Gateway + Lambda routing

---

# ⚡ Key insight (VERY important)

👉 This question is testing:

“Don’t use LLM when a simpler classifier exists”

---

# 🚀 Your level insight

This maps directly to your architecture thinking:

Ingress → API Gateway  
Routing → Lambda + Comprehend  
Execution → Bedrock (specialized FMs)

👉 Clean separation:

- classification layer
- execution layer

---

# ⚡ Final intuition

Routing problem → classifier  
Reasoning problem → LLM

---

# ⚡ Quick challenge

You need:

- route queries
- but ALSO extract entities (account number, product ID)

👉 Best combo?

A. Comprehend only  
B. Comprehend + NER  
C. Bedrock only  
D. SageMaker

---

Answer when ready 👇

63/75 Question A medical company that operates multiple clinics runs a generative AI (GenAI) application on AWS. The application uses AWS Step Functions to orchestrate two AWS Lambda functions. One function calls Amazon Transcribe Medical to transcribe clinic audio data. The second function uses the Amazon Nova Pro model in Amazon Bedrock to summarize the data. The company is onboarding additional clinics. Each clinic has a unique clinic ID. A GenAI developer must modify the architecture to store each clinic's data in a shared Amazon S3 bucket. The GenAI developer must use the clinic ID as the key prefix. The solution must track summarization costs for each clinic. Which combination of steps will meet these requirements MOST cost-effectively? (Select TWO.) Report Content Errors A Configure the S3 bucket to use Amazon S3 Event Notifications to capture PutObject events. Create a Lambda function. Set the function as the destination for the S3 notifications. Configure the function to invoke the Step Functions workflow when new data uploads. Incorrect. S3 Event Notifications provide data upload notifications. However, S3 Event Notifications cannot directly invoke Step Functions. This step requires an additional Lambda function as an intermediary. This step introduces extra cost because each Lambda invocation is billed by the request and execution time. Learn more about S3 Event Notifications. Learn more about S3 Event Notifications targets. B Enable S3 Storage Lens for the bucket to collect prefix-level usage metrics for each clinic. Use Amazon Athena to query the metrics, calculate summarization costs, and generate clinic reports. Incorrect. S3 Storage Lens provides metrics on storage usage. For example, the metrics include object count, object size, request activity, and prefix-level storage trends. These metrics can help analyze how each clinic uses S3 storage space. However, these metrics do not record or attribute inference usage or costs that occur in Amazon Bedrock or Lambda. Querying S3 Storage Lens data by using Athena provides storage-related insights, not operational or billing data. Therefore, this solution cannot track summarization costs for each clinic. Learn more about S3 Storage Lens. C Create an Amazon Bedrock inference profile for each clinic ID. Modify the summarization Lambda function to use the profiles based on the S3 key prefix from the uploaded data. Correct. Amazon Bedrock application inference profiles are specifically designed to manage and track FM costs in multi-tenant environments. This step efficiently handles cost attribution. The summarization Lambda can select the appropriate profile based on the clinic ID from the S3 key prefix. This step achieves per-clinic cost tracking with minimal additional configuration logic. Learn more about Amazon Bedrock application inference profiles. D Deploy an Amazon SageMaker AI endpoint for each clinic that is tagged with the clinic ID. Route summarization Lambda requests to each endpoint based on the S3 key prefix from the uploaded data. Incorrect. Amazon Bedrock is a serverless service that provides pay-as-you-go pricing. The endpoints would be billed based on the hour. You can tag SageMaker AI endpoints to track costs and to manage multiple endpoints, scaling policies, and compute resources. However, deploying a separate SageMaker AI endpoint for each clinic would introduce continuous infrastructure cost. Each endpoint incurs hourly charges even when idle. Learn more about SageMaker AI endpoints. E Create an Amazon EventBridge rule to capture PutObject events. Set the Step Functions state machine as the destination when a matching event occurs on the event bus. Correct. EventBridge provides serverless event routing that directly integrates with Step Functions. EventBridge can consume S3 events. EventBridge supports advanced prefix-based filtering. Therefore, this step provides clinic-specific routing without additional code. This step minimizes cost by eliminating intermediary Lambda functions (no per-invocation charges) and by providing direct state machine triggering. EventBridge pricing is based on the number of published events and matched rules. Therefore, this step provides pricing that is far lower than maintaining and invoking a Lambda for every event. Learn more about EventBridge rules. Learn more about EventBridge with Step Functions as the target.

---

### ✅ Correct Answers: **C + E**

---

# 🧠 Concept First (what this question is REALLY testing)

Two separate concerns:

1) Event-driven ingestion (cheap trigger)  
2) Cost attribution (multi-tenant tracking)

👉 And the constraint:

> **MOST cost-effective**

---

# 🧩 Architecture before vs after

## 🔹 Original

Audio → Lambda → Step Functions → Transcribe → Bedrock → Output

## 🔹 Required upgrade

S3 (prefix = clinicId)  
   ↓  
Trigger workflow  
   ↓  
Track cost per clinic

---

# 🏗️ Why E is correct (event-driven, low cost)

## 🔹 EventBridge → Step Functions (direct)

From your study guide:

> EventBridge enables event-driven architectures and integrates with Step Functions

---

## 🧠 Flow

S3 PutObject  
   ↓  
EventBridge Rule (filter by prefix)  
   ↓  
Step Functions

---

## 🔑 Why this is optimal

- ✅ No Lambda in between
- ✅ Native integration
- ✅ Lower cost (no per-invocation compute)

---

## ❗ Key exam insight

EventBridge > Lambda (for routing events)

👉 When:

- simple trigger
- no custom logic needed

---

# 🏗️ Why C is correct (cost tracking)

## 🔹 Bedrock Inference Profiles

👉 Purpose-built for:

Multi-tenant cost tracking

---

## 🧠 Flow

S3 key: clinicA/file1.wav  
   ↓  
Lambda extracts prefix (clinicA)  
   ↓  
Use Bedrock inference profile: clinicA

---

## 🔑 What it gives you

- cost per clinic
- usage tracking
- clean separation

---

## 📌 From guide (important concept)

- dynamic routing and cost optimization are key GenAI patterns

---

# ❌ Why others are wrong

---

## A — ❌ S3 → Lambda → Step Functions

- extra Lambda hop
- more cost

👉 violates:

> MOST cost-effective

---

## B — ❌ S3 Storage Lens

- tracks **storage**, NOT **Bedrock usage**

👉 wrong metric

---

## D — ❌ SageMaker endpoints

- always-on cost
- massive overkill

👉 kills cost efficiency

---

# 🧠 Mental Model (THIS is gold)

Event routing → EventBridge  
Workflow → Step Functions  
Cost tracking → Bedrock inference profiles

---

# 🏗️ Final Architecture (clean)

S3 (clinicId prefix)  
   ↓  
EventBridge (filter by prefix)  
   ↓  
Step Functions  
   ↓  
Lambda 1 → Transcribe Medical  
   ↓  
Lambda 2 → Bedrock (using inference profile per clinic)  
   ↓  
Output + cost attribution

---

# 🔥 Exam Pattern

If you see:

|Requirement|Answer|
|---|---|
|trigger workflow from S3|EventBridge|
|avoid Lambda trigger|EventBridge|
|cost per tenant|Bedrock inference profile|
|multi-tenant GenAI|profiles / tagging|
|cost optimization|serverless + no idle infra|

---

# ⚡ Key insight (VERY important)

👉 This question tests:

“Serverless event routing + multi-tenant cost attribution”

---

# 🚀 Your level insight

This maps exactly to enterprise SaaS pattern:

Tenant isolation:  
- Data → S3 prefix  
- Compute → shared  
- Cost → inference profile

👉 This is **multi-tenant GenAI architecture**

---

# ⚡ Quick challenge

You now need:

- different models per clinic
- AND cost tracking per clinic

👉 What do you combine?

A. Inference profiles only  
B. Routing + inference profiles  
C. Step Functions only  
D. Lambda only

---

Answer when ready 👇

66/75 Question A company is implementing a RAG-based knowledge management system. The system will use Amazon Bedrock and Amazon OpenSearch Service. The system will ingest hundreds of new documents into the knowledge base on a daily basis. The system must maintain high accuracy and reliability for content across multiple departments. A GenAI developer wants to use Amazon Bedrock model evaluation to design a comprehensive evaluation process. The process must evaluate correctness, relevance, formality scale, and company-specific tone and style. The GenAI developer must run the evaluation on a weekly basis. The GenAI developer will create a RAG evaluation with LLM-as-a-judge and select the desired metrics. Which solution will meet these requirements MOST cost-effectively? Report Content Errors A Use an industry-standard benchmark dataset. Create custom metrics for formality scale and company-specific tone and style. Incorrect. An industry-standard benchmark dataset lacks enterprise-specific context. The dataset might not accurately represent real production scenarios. You can use LLM-as-a-judge with custom metrics. However, the dataset would compromise the evaluation results. An industry-standard benchmark dataset will not capture company-specific tone and style. Learn more about RAG evaluation custom metrics. B Create a human-validated evaluation dataset. Create custom metrics for formality scale and company-specific tone and style. Correct. A human-validated dataset ensures an accurate representation of enterprise-specific use cases, terminology, and content patterns. Using LLM-as-a-judge with custom metrics provides an automated, consistent, and scalable evaluation. You can design custom metrics to assess formality scale and company-specific tone and style with consistent criteria. Learn more about how to create a dataset for a RAG evaluation. Learn more about RAG evaluation metrics. Learn more about RAG evaluation custom metrics. C Use an industry-standard benchmark dataset. Create a human-based model evaluation for formality scale and company-specific tone and style. Incorrect. An industry-standard benchmark dataset lacks enterprise-specific context. The dataset might not accurately represent real production scenarios. An industry-standard benchmark dataset will not capture company-specific tone and style. Human-based model evaluation requires higher costs, longer evaluation cycles, and potential inconsistencies in scoring compared to custom metrics. To meet the requirements, you do not need to manage multiple evaluation types. Learn more about human-based model evaluation. D Create a human-validated evaluation dataset. Create a human-based model evaluation for formality scale and company-specific tone and style. Incorrect. Using a human-validated dataset is most suitable for this scenario. However, human-based model evaluation is less efficient than custom metrics because of higher operational costs, longer evaluation cycles, and potential scoring inconsistencies. Managing both LLM and human evaluations adds unnecessary complexity to the process. Learn more about human-based model evaluation.

---

### ✅ Correct Answer: **B**

---

# 🧠 Concept First (what this question is REALLY testing)

This is a **GenAI evaluation design pattern**:

Evaluation = Dataset + Metrics + Evaluator

👉 And the key constraint:

> **RAG + enterprise-specific tone + cost-effective**

---

# 🧩 Break the requirements

|Requirement|What it implies|
|---|---|
|correctness, relevance|standard RAG metrics|
|formality + company tone|**custom metrics needed**|
|multiple departments|**enterprise-specific data**|
|weekly evaluation|**automated (LLM-as-judge)**|
|cost-effective|**avoid human evaluation**|

---

# 🏗️ Why B is correct (perfect balance)

## 🔹 1. Human-validated dataset (critical)

From study guide:

> Evaluation relies on prompt datasets with reference responses and contexts

---

### Why this matters

Generic dataset ❌ → not your company tone  
Human-validated dataset ✅ → real business context

👉 You need:

- internal terminology
- tone/style
- domain-specific answers

---

## 🔹 2. Custom metrics (second key)

You need to evaluate:

- formality
- tone
- style

👉 These are NOT standard metrics

---

From guide:

> LLM-as-judge uses prompts to define custom evaluation metrics

---

## 🔹 3. LLM-as-a-judge (cost efficiency)

LLM judge → automated scoring  
Human eval → expensive + slow

---

👉 Weekly evaluation → must be automated

---

# 🧠 Full evaluation pipeline

Prompt dataset (human-validated)  
   ↓  
RAG system generates responses  
   ↓  
LLM-as-judge evaluates:  
   - correctness  
   - relevance  
   - tone  
   - formality  
   ↓  
Scores + reports

---

# ❌ Why others are wrong

---

## A — ❌ Industry dataset

- lacks:
    - company tone
    - internal knowledge

👉 poor accuracy

---

## C — ❌ Human evaluation

- expensive
- slow
- inconsistent

👉 violates:

> MOST cost-effective

---

## D — ❌ Human + dataset

- double overhead
- unnecessary

---

# 🧠 Mental Model (THIS is gold)

Dataset quality → drives evaluation accuracy  
Metrics         → define what “good” means  
Judge           → automates scoring

---

# 🔥 Exam Pattern

If you see:

|Signal|Answer|
|---|---|
|enterprise tone/style|custom dataset|
|RAG evaluation|prompt dataset + reference|
|cost-effective|LLM-as-judge|
|automation|avoid human eval|
|custom metrics|prompt-based evaluation|

---

# 🧠 From exam guide

- RAG evaluation uses:
    - prompt dataset
    - reference responses
    - LLM judge
- Metrics include:
    - correctness
    - relevance
    - faithfulness

---

# ⚡ Key insight (VERY important)

👉 This question is testing:

“Evaluation quality depends more on DATA than models”

---

# 🚀 Your level insight

This maps directly to your enterprise mindset:

Generic benchmark → useless in enterprise  
Real dataset → real performance signal

👉 This is **governed AI evaluation**

---

# ⚡ Final intuition

If requirement = “company-specific”  
→ ALWAYS choose custom dataset

---

# ⚡ Quick challenge

You want:

- fastest evaluation
- lowest cost
- but still reliable

👉 What combo?

A. Human dataset + human eval  
B. Human dataset + LLM judge  
C. Benchmark dataset + human eval  
D. Benchmark dataset + LLM judge

---

Answer when ready 👇

71/75 Question A company has a mobile app for users to record short videos. On the app, users can apply proprietary video and audio codecs to enhance the videos locally. The company wants to add features to summarize content and generate transcripts. The company wants features to detect objects and identify celebrities in the videos. Which solution will meet these requirements with the LEAST operational overhead? Report Content Errors A Use Amazon S3 PutObject to upload videos to Amazon S3. Create an S3 event notification that invokes an AWS Step Functions state machine. Set up the state machine to orchestrate processing by using AWS Lambda functions. Use Amazon Rekognition for object detection and celebrity recognition. Use an Amazon Bedrock FM for summarization and transcription. Incorrect. Amazon S3 PutObject API operations require granting direct IAM permissions to users or applications. However, this approach violates the principle of least privilege. S3 Event Notifications cannot directly invoke Step Functions. You can use Lambda as an intermediary. However, this solution requires additional operational overhead to create and manage the functions. Learn more about S3 presigned URLs. Learn more about S3 Event Notifications and targets. Learn more about AWS service SDK integration with Step Functions. B Use Amazon S3 PutObject to upload videos to Amazon S3. Create an S3 event notification that invokes an AWS Lambda function. Configure the function to process videos in parallel. Use AWS Step Functions for error handling and retries. Use Amazon Rekognition for object detection and celebrity recognition. Use Amazon Bedrock FMs to generate summaries and transcripts. Incorrect. Amazon S3 PutObject API operations require granting direct IAM permissions to users or applications. However, this approach violates the principle of least privilege. Implementing each processing step as separate Lambda functions creates additional operational overhead. Managing multiple Lambda functions requires additional development effort. The solution relies solely on Amazon Bedrock FMs for all tasks. However, Amazon Rekognition is a specialized computer vision service that is more suitable for celebrity recognition and object detection in videos. Learn more about S3 presigned URLs. Learn more about event bus targets. Learn more about AWS service SDK integration with Step Functions. Learn more about supported models in Amazon Bedrock. C Use an Amazon S3 presigned URL to upload videos to Amazon S3. Configure Amazon S3 to send events to Amazon EventBridge. Create an EventBridge rule that invokes an AWS Step Functions state machine. Set up the state machine to orchestrate the processing steps by directly calling AWS service APIs. Use Amazon Rekognition for object detection and celebrity recognition. Use Amazon Bedrock FMs to generate summaries and transcripts. Correct. This solution implements secure video uploads by using S3 presigned URLs. This solution follows the principle of least privilege. EventBridge is a serverless event bus service that efficiently routes S3 events to Step Functions for workflow orchestration. Step Functions has direct service integration that eliminates the need for intermediate Lambda functions. Therefore, this solution reduces operational overhead. This solution uses Amazon Rekognition for video analysis tasks including celebrity recognition and object detection. This solution uses Amazon Bedrock FMs for content summarization and transcript generation. Therefore, this solution maximizes the use of managed capabilities and minimizes custom code requirements. Learn more about S3 presigned URLs. Learn more about event bus targets. Learn more about AWS service SDK integration with Step Functions. Learn more about supported models in Amazon Bedrock. Learn more about Amazon Rekognition celebrity recognition. D Use an Amazon S3 presigned URL to upload videos to Amazon S3. Create an S3 event notification that invokes a Bedrock Data Automation (BDA) blueprint to orchestrate the processing steps. Use Amazon Rekognition for object detection and celebrity recognition. Use Amazon Bedrock FMs to generate summaries and transcripts. Incorrect. Using S3 presigned URLs for secure uploads is the most suitable for this scenario. However, BDA has limitations for complex media processing workflows. S3 Event Notifications cannot directly trigger BDA blueprints. BDA has restricted FM options. This solution requires additional custom integration work and might not support all the required video processing capabilities through the BDA blueprint framework. Learn more about S3 presigned URLs. Learn more about S3 Event Notifications and targets. Learn more about BDA.

---

### ✅ Correct Answer: **C**

---

# 🧠 Concept First (what this question is REALLY testing)

This is a **“fully managed, event-driven media pipeline”** question:

Upload → Event → Orchestrate → Call managed services

👉 With constraint:

> **LEAST operational overhead = eliminate Lambda where possible**

---

# 🧩 Break the requirements

|Requirement|What it implies|
|---|---|
|mobile upload|**secure upload (presigned URL)**|
|video processing|**event-driven pipeline**|
|summarization + transcript|**Bedrock FM**|
|object + celebrity detection|**Rekognition (specialized CV)**|
|least ops overhead|**direct integrations (no Lambda)**|

---

# 🏗️ Why C is correct (clean architecture)

## 🔹 1. Secure upload → S3 presigned URL

👉 Best practice:

Mobile app → Presigned URL → S3

✔ no IAM creds on client  
✔ least privilege

---

## 🔹 2. Event routing → EventBridge

S3 → EventBridge → Step Functions

👉 Key insight:

- EventBridge = **direct integration**
- avoids Lambda

---

## 🔹 3. Orchestration → Step Functions

From guide:

> Step Functions orchestrate workflows with built-in retries and integrations

---

## 🔹 4. Direct service integrations (CRITICAL)

Step Functions → Rekognition  
Step Functions → Bedrock

👉 No Lambda needed  
👉 Lower cost + simpler

---

## 🔹 5. Right tools for the job

### 🎥 Video understanding

- **Amazon Rekognition**
    - object detection
    - celebrity recognition

---

### 🧠 Text generation

- **Amazon Bedrock**
    - summarization
    - transcript generation

---

# 🧠 Full architecture

Mobile App  
   ↓  
S3 (presigned URL upload)  
   ↓  
EventBridge  
   ↓  
Step Functions  
   ├── Rekognition (objects + celebrities)  
   ├── Bedrock (transcript + summary)  
   ↓  
Results stored / returned

---

# ❌ Why others are wrong

---

## A — ❌ Lambda orchestration

- unnecessary Lambda
- more cost + complexity

---

## B — ❌ too many Lambdas

- multiple functions
- operational overhead

---

## D — ❌ BDA misuse

- BDA ≠ orchestration engine
- limited for complex workflows

---

# 🧠 Mental Model (THIS is gold)

Upload → S3 presigned URL  
Event → EventBridge  
Workflow → Step Functions  
AI → Bedrock / Rekognition

---

# 🔥 Exam Pattern

If you see:

|Signal|Answer|
|---|---|
|mobile upload|presigned URL|
|event-driven|EventBridge|
|orchestration|Step Functions|
|reduce Lambda|direct integrations|
|video analysis|Rekognition|
|text generation|Bedrock|

---

# 🧠 From exam guide

- Event-driven architectures reduce coupling
- Step Functions orchestrate AI workflows

---

# ⚡ Key insight (VERY important)

👉 This question is testing:

“Remove Lambda when AWS already provides integration”

---

# 🚀 Your level insight

This is exactly your architecture philosophy:

Less code → more managed services  
More managed → lower ops + better scale

👉 This is **serverless GenAI pipeline design**

---

# ⚡ Final intuition

If AWS service can call another directly  
→ DON’T insert Lambda

---

# ⚡ Quick challenge

You now need:

- add moderation (unsafe content detection)

👉 What do you add?

A. Bedrock  
B. Rekognition moderation  
C. Lambda filter  
D. Step Functions retry

---

Answer when ready 👇

Question 27 Incorrect A media analytics team is building a Retrieval Augmented Generation (RAG) assistant by using Amazon Bedrock. Millions of internal articles are stored in Amazon S3 and are tagged by topic (for example, sports, finance, and entertainment). The team wants to segment the corpus by topic to improve retrieval precision. The team also wants the search tier to accept natural language queries and generate embeddings automatically so the application does not need to compute embeddings before querying the vector store. Which solution meets these requirements with the LEAST application-side implementation effort? Correct answer Store the documents in Amazon S3. Create an Amazon OpenSearch Service domain with separate indices per topic. Configure the OpenSearch Neural plugin to call an Amazon Bedrock embedding model in an ingest pipeline and use neural queries so OpenSearch generates query embeddings automatically. Explanation Correct. This design uses OpenSearch as the vector database and applies topic-based segmentation by isolating content into per-topic indices. The Neural plugin allows OpenSearch to generate embeddings during ingestion and at query time by invoking an embedding model in Amazon Bedrock, which removes the need for the application to compute embeddings before search. Your answer is incorrect Create an Amazon Bedrock Knowledge Base with the S3 bucket as the data source and an Amazon OpenSearch Serverless collection as the managed vector store. Use hierarchical chunking and let the Knowledge Base handle ingestion and retrieval for the application. Explanation Incorrect. Although a Knowledge Base can simplify RAG ingestion and retrieval, it does not directly satisfy the requirement for the search tier itself (OpenSearch) to accept natural language queries and generate embeddings automatically for ad hoc search use cases. The requirement is specifically to offload query-embedding generation into the search layer. Store documents in Amazon S3 and store embeddings in Amazon RDS for PostgreSQL as a JSON column. Use SQL to calculate similarity scores in queries and filter by topic tags to return the top matches. Explanation Incorrect. Storing embeddings as JSON and implementing similarity calculations manually increases application and database complexity and is not an optimized vector database architecture. This approach also misses purpose-built vector indexing/search capabilities needed for efficient semantic retrieval at scale. Store document text and topic tags in Amazon DynamoDB. Generate embeddings in the application with an Amazon Bedrock embedding model and store embeddings as DynamoDB attributes. Use DynamoDB Scan operations and compute cosine similarity in the application to find the closest matches. Explanation Incorrect. DynamoDB is not designed for efficient vector similarity search in this pattern. Scanning and computing similarity in the application does not provide efficient semantic retrieval at scale and significantly increases application-side complexity and latency. Overall explanation The best approach is to use Amazon OpenSearch Service as the vector store with topic-based segmentation (separate indices per topic) and integrate embedding generation directly into OpenSearch through the Neural plugin. This lets OpenSearch create embeddings for documents during ingestion and create embeddings for user queries at search time by invoking an Amazon Bedrock embedding model, enabling efficient semantic retrieval without requiring the application to generate embeddings before each query. Other approaches either don’t offload embedding generation into the search tier or require inefficient retrieval patterns and substantial custom implementation. Further reading (AWS): - Semantic search in Amazon OpenSearch Service - Amazon OpenSearch Service (AWS Documentation) - Amazon Bedrock templates - Amazon OpenSearch Service (AWS Documentation) - Power neural search with AI/ML connectors in Amazon OpenSearch Service (AWS Blog) Domain Content Domain 1: Foundation Model Integration, Data Managem

---

This is a **classic trap question** — you picked a _valid RAG architecture_, but AWS is testing a **very specific requirement**.

Let’s break it down cleanly 👇

---

# 🧠 Concept First

👉 Two different patterns:

Bedrock Knowledge Base → managed RAG (app-driven)  
OpenSearch Neural      → search-driven (search does embeddings)

---

# 🧩 What the question REALLY required

## 🔥 Critical line (the trap)

> “search tier must accept natural language queries AND generate embeddings automatically”

👉 Translation:

Embedding generation must happen INSIDE the search layer  
NOT in the application

---

# 🏗️ Why the correct answer works

## 🔹 Architecture (OpenSearch Neural plugin)

User query (natural language)  
   ↓  
OpenSearch (Neural query)  
   ↓  
OpenSearch calls Bedrock embedding model  
   ↓  
Vector search executed

---

## 🔹 Ingestion

Documents (S3)  
   ↓  
OpenSearch ingest pipeline  
   ↓  
Embedding generated automatically (via Bedrock)  
   ↓  
Stored in vector index

---

## 🔑 Key capabilities

- ✅ embedding at ingest (pipeline)
- ✅ embedding at query time (neural query)
- ✅ no app-side embedding logic
- ✅ per-topic indices → segmentation

---

# ❌ Why your answer (Knowledge Base) is wrong

## 🧠 What Knowledge Base does

App → Bedrock KB → retrieval → response

👉 It hides retrieval completely

---

## 🚫 Problem

The question explicitly wants:

Search layer handles embeddings

But KB:

- ❌ does NOT expose search tier
- ❌ does NOT let OpenSearch accept raw queries
- ❌ does NOT push embedding responsibility to search layer

---

# ⚖️ Side-by-side (this is the key insight)

|Feature|Knowledge Base|OpenSearch Neural|
|---|---|---|
|Managed RAG|✅|❌|
|App sends query|✅|✅|
|Search layer generates embeddings|❌|✅|
|Direct OpenSearch querying|❌|✅|
|Control over indices|❌|✅|

---

# 🧠 Mental Model (VERY important)

Knowledge Base → “RAG as a service”  
OpenSearch     → “RAG as infrastructure”

---

# 🔥 Exam Pattern (this will come again)

If question says:

|Signal|Answer|
|---|---|
|“least effort RAG”|Knowledge Base|
|“search layer handles embeddings”|OpenSearch Neural|
|“custom index / segmentation”|OpenSearch|
|“fine control over retrieval”|OpenSearch|

---

# 🧠 Key misunderstanding (you’re close)

You chose:

👉 **“simplify everything” (Knowledge Base)**

But the question wanted:

👉 **“push intelligence into search tier”**

---

# ⚡ One-line takeaway

If embedding must happen inside search → OpenSearch Neural plugin

---

# 🚀 Your level insight

This maps to your architecture thinking:

Option 1 (KB):  
App → Bedrock → hidden retrieval  
  
Option 2 (OpenSearch):  
App → Search layer → embedding + retrieval

👉 Option 2 = **more control, less app logic**

---

# ⚡ Quick challenge

You need:

- minimal setup
- no OpenSearch management
- standard RAG

👉 What do you choose?

A. Knowledge Base  
B. OpenSearch Neural  
C. DynamoDB vector  
D. SageMaker

---

Answer when ready 👇

summarize OpenSearch Neural

## 🧠 OpenSearch Neural — quick intuition

“Let the search engine handle embeddings + semantic search”

👉 You send **plain text**, it handles **vectorization + retrieval**

---

# 🧩 What is OpenSearch Neural?

**OpenSearch Neural (Neural Search plugin)** is a feature of Amazon OpenSearch Service that enables:

- semantic (vector) search
- automatic embedding generation
- integration with models (e.g., Bedrock embeddings)

---

# 🏗️ How it works (end-to-end)

## 🔹 1. Ingestion (documents)

![https://docs.aws.amazon.com/images/opensearch-service/latest/developerguide/images/ml_processor.png](https://docs.aws.amazon.com/images/opensearch-service/latest/developerguide/images/ml_processor.png)

![https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2024/06/14/395_Picture-1.png](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2024/06/14/395_Picture-1.png)

![https://eliatra.com/docs/2.11/images/neural-search-ingestion.png](https://eliatra.com/docs/2.11/images/neural-search-ingestion.png)

4

S3 docs  
  ↓  
OpenSearch ingest pipeline  
  ↓  
Calls embedding model (Bedrock)  
  ↓  
Stores vectors in index

---

## 🔹 2. Query (search)

User query (natural language)  
  ↓  
OpenSearch neural query  
  ↓  
Embedding generated automatically  
  ↓  
Vector similarity search  
  ↓  
Top relevant documents

---

# 🔑 Key capabilities

### ✅ 1. **Automatic embeddings**

- No need to compute in app
- Done at:
    - ingestion
    - query time

---

### ✅ 2. **Semantic search (not keyword)**

- understands meaning, not just words

---

### ✅ 3. **Model integration**

- can call embedding models (e.g., Bedrock)

---

### ✅ 4. **Index-level control**

- create:
    - per-topic indices
    - multi-index strategies

---

# ⚖️ When to use OpenSearch Neural

Use it when you need:

- fine control over retrieval
- custom indexing strategy
- search-driven architecture
- **embedding handled inside search layer**

---

# ❌ When NOT to use it

Use Bedrock Knowledge Base instead when you want:

- fully managed RAG
- minimal setup
- no search infra management

---

# 🧠 Mental Model (lock this in)

OpenSearch Neural = “vector search engine with built-in embeddings”

---

# 🔥 Exam shortcut

“search tier generates embeddings” → OpenSearch Neural ✅  
“managed RAG, minimal effort”     → Knowledge Base ✅

---

# 🚀 Your level insight

This maps cleanly to architecture layers:

App layer        → sends natural query  
Search layer     → OpenSearch Neural (embedding + retrieval)  
Model layer      → Bedrock (optional generation)

👉 You’ve **decoupled retrieval from application logic**

---

# ⚡ 1-line takeaway

👉 **OpenSearch Neural = push embedding + semantic search into the search engine**

---

If you want, I can give you a **side-by-side cheat sheet: OpenSearch vs Knowledge Base vs Aurora pgvector** — super high ROI for exam 👍

Question 29 Incorrect A global HR SaaS provider is building a semantic search feature for internal policy documents by using a RAG architecture. The team will embed millions of document chunks and store the vectors in a vector database for similarity search. The solution must keep vector storage costs low while maintaining search relevance for the organization’s terminology, and the embedding generation process must efficiently handle nightly ingestion of large document batches. Which combination of actions will meet these requirements MOST cost-effectively? (Select TWO.) Configure the embedding model to use the maximum available vector dimension to improve accuracy. Invoke the embedding model from the application for each chunk individually to avoid batching complexity. Explanation Incorrect. Always maximizing dimensionality can significantly increase storage and indexing costs and is not guaranteed to improve retrieval enough to justify the cost. Generating embeddings one chunk at a time increases invocation overhead and slows nightly ingestion compared to batching. Correct selection Run a proof of concept that generates embeddings for a representative set of documents and queries by using multiple Amazon Bedrock embedding models (for example, Amazon Titan embeddings and an alternative embedding model). Compare retrieval quality metrics (such as top-k relevance) and select the model that best fits the domain and language needs. Explanation Correct. Embedding models can differ in how well they represent domain-specific concepts and multilingual content. Evaluating retrieval performance on representative queries is an effective way to select an embedding model that best aligns with the business use case. Your selection is correct Use an Amazon Titan embedding model and configure a smaller embedding vector dimension after validating that retrieval relevance remains acceptable for the policy-document domain. Use AWS Lambda to batch-generate embeddings for new chunks before writing them to the vector store. Explanation Correct. Smaller embedding dimensionality reduces storage and indexing costs for large corpora, but should be validated to ensure it still captures the semantic detail needed for the domain. Batch generation with Lambda reduces per-item invocation overhead and improves ingestion efficiency for nightly loads. Your selection is incorrect Use Amazon Comprehend to classify each document into topics and store only the topic labels. Use keyword search on the labels instead of generating embeddings to reduce cost. Explanation Incorrect. Topic classification and keyword search do not provide the semantic similarity retrieval required for embedding-based vector search, and this approach would not meet the semantic search requirement for RAG-based retrieval. Store embeddings and chunk metadata in Amazon DynamoDB and use PartiQL queries to perform semantic similarity searches directly in DynamoDB. Explanation Incorrect. DynamoDB can store embedding vectors as attributes but does not provide native vector similarity search for k-nearest-neighbor retrieval, making it unsuitable as the primary semantic vector search engine for a RAG retriever. Overall explanation To keep costs low at scale, the embedding strategy should reduce the size and number of vectors stored while preserving retrieval quality. Configuring an embedding model with an appropriately smaller vector dimension can materially reduce vector storage and indexing costs, but it must be validated against real queries to avoid harming relevance. Because different embedding models can behave differently across domains and languages, testing multiple Bedrock embedding model options on representative data is a reliable way to choose the best fit. Finally, batching embedding generation with Lambda improves ingestion throughput and reduces per-item overhead during large nightly loads. Further reading (AWS): - Amazon Titan Text Embeddings models - Amazon Bedrock (AWS Documentation) - Get started with Amazon Titan Text Embeddings V2: A new state-of-the-art embeddings model on Amazon Bedrock | Artificial Intelligence (AWS Blog) - Using Lambda with Amazon SQS - AWS Lambda (AWS Documentation) Domain Content Domain 1: Foundation Model Integration, Data Managem

---

This was a **high-signal exam question** — and you were actually very close. Let’s tighten the mental model so you don’t miss this again.

---

# 🧠 Concept First (what this question is REALLY testing)

This is about **cost optimization in embeddings at scale**:

Cost = (# vectors) × (vector size) × (generation cost)

👉 You must optimize **ALL THREE levers**

---

# 🧩 The 3 levers (core idea)

## 🔹 1. Vector size (storage cost)

From your guide:

> Smaller vector sizes reduce storage and indexing costs

---

## 🔹 2. Embedding model choice (quality vs cost)

Different models → different:

- semantic quality
- cost
- domain fit

---

## 🔹 3. Generation efficiency (compute cost)

Batching = cheaper + faster

---

# 🏗️ Why the correct answers are correct

## ✅ 1. Evaluate embedding models (POC)

Test multiple models → choose best domain fit

👉 Why critical?

- embeddings are **not universal**
- finance vs HR vs legal → different semantics

---

👉 This aligns with exam guide:

> Select embedding solutions based on domain fit and performance

---

## ✅ 2. Reduce vector dimension + batch processing

### 🔹 Smaller dimension

1024 → 512 → 256 → lower storage cost

👉 Trade-off:

- smaller = cheaper
- but must validate relevance

---

### 🔹 Batch embedding

From guide:

> Batch embeddings improves efficiency for large ingestion

---

Chunks → batch → Bedrock → embeddings

👉 Benefits:

- fewer API calls
- faster ingestion
- lower cost

---

# ❌ Why the wrong option is wrong (important)

## ❌ “Max dimension + no batching”

Max dimension = expensive storage  
No batching    = expensive compute

👉 This is the **anti-pattern**

---

# 🧠 Mental Model (THIS is gold)

Good embedding strategy =  
  Right model (domain fit)  
+ Smallest viable dimension  
+ Batch processing

---

# 🔥 Exam Pattern (you WILL see again)

If you see:

|Signal|Answer|
|---|---|
|millions of embeddings|reduce dimension|
|cost optimization|smaller vectors|
|domain-specific relevance|model evaluation|
|large ingestion|batching|
|nightly jobs|batch processing|

---

# 🧠 From your study guide (key reinforcement)

- vector size affects cost
- batching improves efficiency
- model selection depends on domain fit

---

# ⚡ Why your instinct was close

You picked:

✅ smaller dimension + batching

👉 That’s already **half the solution**

You missed:

👉 **model selection via POC**

---

# 🚀 Your level insight

This maps exactly to real-world architecture:

Ingestion pipeline:  
S3 → Lambda batch → Bedrock embeddings → Vector DB  
  
Optimization layer:  
- tune dimension  
- choose best model  
- batch processing

---

# ⚡ Final intuition

Embedding cost problem?  
→ shrink vectors + batch + choose right model

---

# ⚡ Quick challenge (very exam-like)

You need:

- reduce latency (NOT cost)
- improve retrieval accuracy

👉 What do you tune first?

A. Reduce vector dimension  
B. Increase dimension  
C. Batch embeddings  
D. Use S3 lifecycle

---

Answer when ready 👇

Question 29 Incorrect A global HR SaaS provider is building a semantic search feature for internal policy documents by using a RAG architecture. The team will embed millions of document chunks and store the vectors in a vector database for similarity search. The solution must keep vector storage costs low while maintaining search relevance for the organization’s terminology, and the embedding generation process must efficiently handle nightly ingestion of large document batches. Which combination of actions will meet these requirements MOST cost-effectively? (Select TWO.) Configure the embedding model to use the maximum available vector dimension to improve accuracy. Invoke the embedding model from the application for each chunk individually to avoid batching complexity. Explanation Incorrect. Always maximizing dimensionality can significantly increase storage and indexing costs and is not guaranteed to improve retrieval enough to justify the cost. Generating embeddings one chunk at a time increases invocation overhead and slows nightly ingestion compared to batching. Correct selection Run a proof of concept that generates embeddings for a representative set of documents and queries by using multiple Amazon Bedrock embedding models (for example, Amazon Titan embeddings and an alternative embedding model). Compare retrieval quality metrics (such as top-k relevance) and select the model that best fits the domain and language needs. Explanation Correct. Embedding models can differ in how well they represent domain-specific concepts and multilingual content. Evaluating retrieval performance on representative queries is an effective way to select an embedding model that best aligns with the business use case. Your selection is correct Use an Amazon Titan embedding model and configure a smaller embedding vector dimension after validating that retrieval relevance remains acceptable for the policy-document domain. Use AWS Lambda to batch-generate embeddings for new chunks before writing them to the vector store. Explanation Correct. Smaller embedding dimensionality reduces storage and indexing costs for large corpora, but should be validated to ensure it still captures the semantic detail needed for the domain. Batch generation with Lambda reduces per-item invocation overhead and improves ingestion efficiency for nightly loads. Your selection is incorrect Use Amazon Comprehend to classify each document into topics and store only the topic labels. Use keyword search on the labels instead of generating embeddings to reduce cost. Explanation Incorrect. Topic classification and keyword search do not provide the semantic similarity retrieval required for embedding-based vector search, and this approach would not meet the semantic search requirement for RAG-based retrieval. Store embeddings and chunk metadata in Amazon DynamoDB and use PartiQL queries to perform semantic similarity searches directly in DynamoDB. Explanation Incorrect. DynamoDB can store embedding vectors as attributes but does not provide native vector similarity search for k-nearest-neighbor retrieval, making it unsuitable as the primary semantic vector search engine for a RAG retriever. Overall explanation To keep costs low at scale, the embedding strategy should reduce the size and number of vectors stored while preserving retrieval quality. Configuring an embedding model with an appropriately smaller vector dimension can materially reduce vector storage and indexing costs, but it must be validated against real queries to avoid harming relevance. Because different embedding models can behave differently across domains and languages, testing multiple Bedrock embedding model options on representative data is a reliable way to choose the best fit. Finally, batching embedding generation with Lambda improves ingestion throughput and reduces per-item overhead during large nightly loads. Further reading (AWS): - Amazon Titan Text Embeddings models - Amazon Bedrock (AWS Documentation) - Get started with Amazon Titan Text Embeddings V2: A new state-of-the-art embeddings model on Amazon Bedrock | Artificial Intelligence (AWS Blog) - Using Lambda with Amazon SQS - AWS Lambda (AWS Documentation)

---

Great — this one is **worth mastering**, because it’s a recurring pattern in the exam.

---

# 🧠 The core idea (compress it)

Embedding optimization = Model choice + Vector size + Generation efficiency

👉 You got **2/3**, just missed the first one.

---

# 🧩 What the question REALLY wanted

## Requirements translated:

|Requirement|What AWS wants|
|---|---|
|low storage cost|**reduce vector dimension**|
|maintain relevance|**choose right embedding model**|
|nightly large ingestion|**batch processing**|

---

# 🏗️ The TWO correct answers (clean view)

## ✅ 1. **POC → choose best embedding model**

Test models → measure relevance → pick best fit

👉 Why?

- embeddings behave differently by **domain**
- HR policies ≠ generic text

From guide:

> Embedding solutions must be selected based on domain fit and performance

---

## ✅ 2. **Reduce dimension + batch embeddings**

### 🔹 Reduce dimension

1024 → 512 → 256 → lower cost

From guide:

> Vector size directly impacts cost; balance with retrieval performance

---

### 🔹 Batch embeddings

Chunks → batch → Bedrock → vector DB

👉 Why:

- fewer API calls
- faster ingestion
- cheaper

---

# ❌ Why the wrong ones are wrong (quick kill)

## ❌ Max dimension + per-chunk calls

High cost + slow ingestion

👉 opposite of requirement

---

## ❌ Comprehend classification

Keyword search ≠ semantic search

👉 breaks RAG

---

## ❌ DynamoDB similarity search

No native vector search

👉 not scalable

---

# 🧠 The pattern you missed (important)

You focused on:

“optimize vectors”

But AWS also wanted:

“optimize model selection”

---

# 🧠 Mental Model (lock this in)

Step 1 → Choose best embedding model (POC)  
Step 2 → Minimize vector size (cost)  
Step 3 → Batch embedding generation (efficiency)

---

# 🔥 Exam Pattern (very repeatable)

If you see:

|Signal|Answer|
|---|---|
|“millions of embeddings”|reduce dimension|
|“domain-specific relevance”|evaluate models|
|“large ingestion”|batching|
|“cost-effective”|combine all three|

---

# 🚀 Your level insight

This is exactly how you’d design enterprise RAG:

Embedding layer:  
- Model selection (POC)  
- Dimension tuning  
- Batch pipeline (Lambda / Glue)  
  
Vector store:  
- OpenSearch / S3 vectors

👉 This is **production-grade embedding strategy**

---

# ⚡ Final intuition

Cheap + accurate embeddings =  
Right model + Small vectors + Batch generation

---

# ⚡ Quick check (1 min drill)

You need to:

- improve **accuracy** (not cost)
- same dataset

👉 What do you do first?

A. Reduce dimension  
B. Increase dimension  
C. Batch embeddings  
D. Use Lambda

---

Answer 👇

b

✅ Correct — **B (increase dimension)**

---

# 🧠 Concept First (what you just answered)

Accuracy ↑ → richer embeddings → more semantic detail

👉 The **first lever for accuracy = embedding quality**

---

# 🧩 Why B is correct

## 🔹 Increase vector dimension

From your study guide:

> Vector size (dimensionality) affects retrieval performance and must be balanced with cost

---

### 🧠 What happens when you increase dimension?

Low dimension  → coarse meaning  
High dimension → richer semantic representation

👉 Result:

- better similarity matching
- better retrieval accuracy

---

# ⚖️ Trade-off (VERY important)

Higher dimension = better accuracy BUT higher cost

👉 That’s why in Q29:

- you **reduced dimension (cost focus)**
- but here:
- you **increase dimension (accuracy focus)**

---

# ❌ Why others are wrong

## A — Reduce dimension

Cheaper, but worse semantic accuracy

---

## C — Batch embeddings

Improves efficiency, NOT accuracy

---

## D — Lambda

No impact on embedding quality

---

# 🧠 Mental Model (lock this in)

Need accuracy → increase dimension  
Need cost     → decrease dimension  
Need speed    → batch processing

---

# 🔥 Exam Pattern

If you see:

|Requirement|Answer|
|---|---|
|improve relevance|increase dimension|
|semantic accuracy|better embeddings|
|cost reduction|smaller vectors|
|ingestion efficiency|batching|

---

# 🧠 From exam guide (reinforcement)

- embedding choice + dimensionality = key design decision
- optimize based on:
    - cost
    - performance
    - domain fit

---

# 🚀 Your level insight

You now have the **3 knobs fully clear**:

1. Model choice      → domain accuracy  
2. Vector dimension → accuracy vs cost  
3. Batching         → efficiency

👉 This is **core RAG engineering**

---

# ⚡ Final intuition

Accuracy problem?  
→ richer embeddings (dimension or better model)

---

# ⚡ Next-level question (very exam-like)

You need:

- improve accuracy
- BUT cannot increase cost

👉 What do you do?

A. Increase dimension  
B. Better embedding model  
C. Batch embeddings  
D. Reduce chunks

---

Answer when ready 👇

Question 30 Incorrect A compliance engineering team is building an internal summarization service that uses an Amazon Bedrock text FM to produce 1-paragraph summaries of long policy documents. The team needs an evaluation approach that can be rerun for every prompt template change to detect regressions. The approach must assess the quality of summaries across multiple dimensions, including relevance to the source content, factual accuracy, consistency across runs, and fluency, while keeping the evaluation process largely automated. Which approach will meet these requirements with the LEAST manual effort? Correct answer Store a prompt dataset in Amazon S3 that includes source documents and reference summaries. Run Amazon Bedrock Model Evaluations using an LLM-as-a-judge configuration to score each generated summary on relevance, correctness (factual accuracy), consistency, and fluency. Compare scores across prompt template versions before deployment. Explanation Correct. An automated evaluation workflow that uses a prompt dataset and an evaluator (judge) model can score outputs against multiple quality dimensions beyond traditional ML metrics. This approach supports repeatable regression testing for each prompt change and minimizes manual effort while still providing structured, multi-metric quality signals. Create a benchmark dataset of source documents and use ROUGE and BLEU scores to compare model-generated summaries to reference summaries. Use the combined score as the single quality signal for go/no-go decisions. Explanation Incorrect. ROUGE and BLEU measure overlap and n-gram precision/recall-style similarity and can be helpful for certain summarization/translation comparisons, but they do not reliably capture factual accuracy (hallucination), consistency across runs, or fluency. Relying on them alone does not provide the comprehensive, multi-dimensional assessment requested. Track Amazon CloudWatch metrics for the summarization endpoint, including InputTokenCount, OutputTokenCount, and model latency. Treat lower token usage and lower latency as indicators of higher summary quality. Explanation Incorrect. Token counts and latency are useful operational metrics, but they do not evaluate output quality dimensions such as relevance, factual accuracy, consistency, or fluency. Optimizing only for speed or token usage can reduce quality and does not provide a comprehensive assessment framework. Your answer is incorrect Enable Amazon SageMaker Model Monitor on the summarization workload to detect data drift and feature attribution drift. Block deployments when drift exceeds a predefined threshold. Explanation Incorrect. SageMaker Model Monitor is designed to monitor deployed model/data characteristics (for example, drift) rather than to directly evaluate the semantic quality of LLM-generated text for relevance, factual accuracy, consistency, and fluency. Drift signals alone cannot serve as a comprehensive text quality evaluation framework for FM outputs. Overall explanation A comprehensive FM output assessment framework needs explicit quality-oriented metrics (such as relevance, factual accuracy/correctness, consistency, and fluency) and must be repeatable for regression testing when prompts or configurations change. An automated evaluation workflow that uses a curated prompt dataset with reference outputs, and applies an LLM-as-a-judge evaluator to score multiple dimensions, provides actionable quality scores at scale with minimal manual effort. Operational metrics like latency and token counts support cost/performance optimization but do not measure output quality, and traditional n-gram overlap metrics alone are not sufficient to capture hallucinations, consistency, and fluency for generative outputs. Further reading (AWS): - Evaluate model performance using another LLM as a judge - Amazon Bedrock (AWS Documentation) - Create a model evaluation job that uses an LLM as a judge - Amazon Bedrock (AWS Documentation) - Use metrics to understand model performance - Amazon Bedrock (AWS Documentation) Domain Content Domain 5: Testing, Validation, and Troubleshooting

---

This is a **very high-yield exam concept** — and it ties directly to your study guide.

---

# 🧠 Concept First (what AWS is testing)

GenAI evaluation ≠ traditional ML metrics

👉 You need:

- **multi-dimensional quality**
- **repeatable regression testing**
- **low manual effort**

---

# 🧩 What the question REALLY requires

|Requirement|What it means|
|---|---|
|rerun for every prompt change|**automated evaluation pipeline**|
|relevance, accuracy, fluency|**semantic evaluation (not ROUGE only)**|
|consistency across runs|**LLM judge / structured scoring**|
|least manual effort|**no human review loop**|

---

# 🏗️ Why the correct answer works

## ✅ Architecture (this is the key pattern)

Prompt dataset (S3)  
   ↓  
Generate summaries  
   ↓  
LLM-as-a-judge evaluates:  
   - relevance  
   - correctness  
   - consistency  
   - fluency  
   ↓  
Scores stored + compared across versions

---

## 🔑 Why this is powerful

### 1. **Repeatable regression testing**

- same dataset
- compare scores across prompt versions

---

### 2. **Multi-dimensional evaluation**

From your study guide:

> Bedrock evaluations measure correctness, completeness, helpfulness, coherence, faithfulness

---

👉 That directly maps to:

- relevance
- factual accuracy
- fluency
- consistency

---

### 3. **LLM-as-a-judge = automation**

From guide:

> LLM-as-a-judge evaluates outputs using defined prompts and metrics

---

👉 This replaces:

- human evaluation
- manual scoring

---

# ❌ Why the wrong answers fail

---

## ❌ ROUGE / BLEU only

Measures overlap, NOT meaning

👉 misses:

- hallucinations
- reasoning
- fluency

---

## ❌ CloudWatch metrics

Measures system performance, NOT output quality

👉 tokens ≠ correctness

---

## ❌ SageMaker Model Monitor

Detects drift, NOT text quality

👉 wrong layer:

- model monitoring ≠ GenAI evaluation

---

# 🧠 Mental Model (THIS is gold)

Traditional ML → accuracy metrics  
GenAI         → semantic evaluation (LLM judge)

---

# 🔥 Exam Pattern

If you see:

|Signal|Answer|
|---|---|
|prompt regression testing|prompt dataset|
|evaluate quality dimensions|LLM-as-judge|
|minimize manual effort|automated eval|
|hallucination / fluency|NOT ROUGE|
|Bedrock evaluation|always strong answer|

---

# 🧠 From exam guide (direct mapping)

- evaluation uses:
    - prompt dataset
    - reference outputs
    - LLM judge
- required:
    - regression testing
    - multi-metric evaluation

---

# 🚀 Your level insight

This is exactly your enterprise pattern:

Prompt change → run evaluation → compare scores → approve / rollback

👉 This is **GenAI CI/CD quality gate**

---

# ⚡ Final intuition

If evaluating GenAI output quality → ALWAYS think LLM-as-judge

---

# ⚡ Quick challenge (exam-style)

You want:

- fastest evaluation
- but still somewhat reliable
- no reference answers available

👉 What do you use?

A. ROUGE  
B. Human evaluation  
C. LLM-as-a-judge (no references)  
D. CloudWatch

---

Answer when ready 👇

review Amazon Bedrock Model Evaluations capabilities

Perfect timing — this is **one of the highest-weight topics (Domain 5: Evaluation)** and shows up in MANY questions.

Let’s break Amazon Bedrock **Model Evaluations** in a way that sticks for the exam 👇

---

# 🧠 1. Big Picture (what Bedrock Evaluations actually is)

“Automated + structured way to measure GenAI output quality”

👉 Not just accuracy — but **semantic quality**

From your guide:

> Bedrock evaluation jobs measure correctness, completeness, helpfulness, coherence, and faithfulness

---

# 🧩 2. Core Architecture

Prompt Dataset (S3)  
   ↓  
Model generates outputs  
   ↓  
Evaluator (LLM or human)  
   ↓  
Scores (multi-metric)

---

# 🔑 3. Key Capabilities (this is exam gold)

## ✅ A. LLM-as-a-Judge (MOST IMPORTANT)

Model A (generator)  
   ↓  
Model B (judge)  
   ↓  
Scores quality

👉 Fully automated evaluation

From guide:

> A trusted model evaluates responses using defined prompts and metrics

---

## ✅ B. Prompt Dataset (foundation of everything)

Stored in S3, includes:

- prompts
- expected outputs (optional)
- context (for RAG)

👉 Enables:

- regression testing
- A/B testing

---

## ✅ C. Multi-dimensional metrics

Not just “accuracy”

### Core metrics:

|Metric|Meaning|
|---|---|
|Correctness|factual accuracy|
|Relevance|answers the question|
|Completeness|covers all points|
|Helpfulness|useful to user|
|Coherence|logical flow|
|Faithfulness|grounded in source|

---

## ✅ D. RAG Evaluation (special mode)

Two types:

### 1. Retrieve-only

- measures:
    - context relevance
    - coverage

---

### 2. Retrieve + Generate

- measures:
    - answer quality
    - grounding

👉 Very exam-relevant

---

## ✅ E. Model comparison (A/B testing)

Prompt → Model A vs Model B → compare scores

👉 Used for:

- model selection
- cost vs performance

---

## ✅ F. Human evaluation (optional)

- Amazon A2I / Ground Truth
- subjective quality

👉 BUT:

- high cost
- NOT “least effort”

---

# 🧠 4. Evaluation Types (exam framing)

|Type|When to use|
|---|---|
|LLM-as-judge|default, automated|
|Human eval|subjective / high-risk|
|Benchmark dataset|baseline only|
|Hybrid|advanced validation|

---

# ❌ 5. What Bedrock Evaluations is NOT

|Option|Why wrong|
|---|---|
|CloudWatch metrics|performance, not quality|
|ROUGE/BLEU only|lexical, not semantic|
|Model Monitor|drift, not GenAI output|
|Logs analysis|debugging, not evaluation|

---

# 🧠 6. Mental Model (THIS is key)

Traditional ML:  
→ accuracy / precision / recall  
  
GenAI:  
→ semantic quality (LLM judge)

---

# 🔥 7. Exam Patterns (very predictable)

If question says:

|Signal|Answer|
|---|---|
|regression testing|prompt dataset|
|evaluate summaries|LLM-as-judge|
|multiple dimensions|Bedrock evaluation|
|RAG quality|RAG evaluation job|
|least manual effort|automated evaluation|

---

# 🚀 8. How this fits your architecture thinking

CI/CD for GenAI:  
  
Prompt change  
   ↓  
Run evaluation job  
   ↓  
Compare scores  
   ↓  
Deploy / rollback

👉 This is **GenAI quality gate**

---

# ⚡ 9. One-line takeaway

Bedrock Evaluations = automated, multi-metric, LLM-based quality scoring system

---

# ⚡ Quick challenge (very exam-like)

You need to:

- evaluate hallucinations
- in a RAG system
- automatically

👉 What do you use?

A. ROUGE  
B. CloudWatch logs  
C. RAG evaluation (LLM-as-judge)  
D. SageMaker Model Monitor

---

Answer when ready 👇

on 7. Exam Patterns (very predictable), include agent tracing

Great catch — this is exactly how to **level up your pattern recognition** for the exam.

Let’s extend your **Exam Patterns cheat sheet** to include **Agent Tracing** 👇

---

# 🔥 7. Exam Patterns (updated — MUST MEMORIZE)

## 🧠 Core patterns

|Signal in question|Correct answer|
|---|---|
|regression testing|prompt dataset|
|evaluate summaries|LLM-as-judge|
|multiple quality dimensions|Bedrock Model Evaluations|
|RAG quality (retrieval + answer)|RAG evaluation jobs|
|least manual effort|automated evaluation|

---

# 🧠 NEW: Agent reasoning / debugging patterns

## ✅ When question mentions **“reasoning”, “decision process”, “why agent did X”**

👉 Answer:

Bedrock Agent Tracing

---

### 🔍 What Agent Tracing actually gives you

From your guide:

> Agent tracing shows reasoning steps including preprocessing, orchestration, and postprocessing

---

### 🧩 Trace components (important for exam)

|Trace type|What it shows|
|---|---|
|PreProcessingTrace|input interpretation|
|OrchestrationTrace|tool calls / KB retrieval|
|PostProcessingTrace|final response shaping|
|RoutingClassifierTrace|how request was routed|
|GuardrailTrace|safety filtering|
|FailureTrace|errors|

---

## 🔥 Updated pattern table (THIS is gold)

|If question says…|You choose…|
|---|---|
|“evaluate output quality”|Bedrock Evaluations|
|“compare models/prompts”|LLM-as-judge|
|“measure hallucination / relevance”|RAG evaluation|
|“understand agent reasoning”|Agent Tracing|
|“debug agent workflow”|Agent Tracing|
|“see tool calls / KB usage”|OrchestrationTrace|
|“end-to-end reasoning visibility”|Pre + Orchestration + Post traces|

---

# ⚠️ Common confusion (exam trap)

## ❌ Guardrails ≠ reasoning

- Guardrails → **content filtering**
- Tracing → **reasoning visibility**

👉 You got asked this earlier — this is a classic trap.

---

# 🧠 Mental Model (combine both)

Evaluation → “Is output good?”  
Tracing    → “How did agent think?”

---

# 🚀 Your level insight (very strong)

You now have:

Quality layer → Bedrock Evaluations  
Reasoning layer → Agent Tracing

👉 This is **observability for GenAI systems**

---

# ⚡ Final intuition

“Why did the model do this?” → Tracing  
“Is the output good?”        → Evaluation

---

# ⚡ Quick challenge

You need to:

- detect hallucinations
- AND understand which step caused it

👉 What do you combine?

A. Guardrails only  
B. Evaluations only  
C. Agent Tracing only  
D. Evaluations + Agent Tracing

---

Answer when ready 👇

Model eval vs prompt eval vs RAG eval

This is one of the **most important distinctions in the entire exam** — and AWS _loves_ testing it in subtle ways.

Let’s lock it in properly 👇

---

# 🧠 Big Picture (one mental model)

Model eval   → “Is the model good?”  
Prompt eval  → “Is the prompt good?”  
RAG eval     → “Is retrieval + answer good?”

---

# 🧩 1. Model Evaluation (Bedrock Model Evaluations)

## 🔹 What it evaluates

👉 **End-to-end model output quality**

- relevance
- correctness
- fluency
- consistency

From your guide:

> Evaluate FM outputs using metrics like correctness, completeness, coherence

---

## 🔹 Architecture

Prompt dataset (S3)  
   ↓  
Model generates output  
   ↓  
LLM-as-judge OR human  
   ↓  
Scores

---

## 🔹 Key features

- LLM-as-a-judge (automated)
- human evaluation (optional)
- A/B model comparison
- regression testing

---

## 🧠 When to use

- comparing models
- validating output quality
- prompt regression testing

---

# 🧩 2. Prompt Evaluation (subset of model eval)

👉 This is where many people get confused.

## 🔹 What it evaluates

👉 **Effectiveness of prompts**

- prompt version A vs B
- instruction quality
- output consistency

---

## 🔹 How it works

Same model  
Different prompts  
   ↓  
Compare outputs  
   ↓  
Evaluation scores

---

## 🔹 Tools

- Amazon Bedrock Prompt Management
- Bedrock Evaluations
- A/B testing

---

## 🧠 Key idea

Prompt eval = “prompt engineering validation”

From exam guide:

> Prompt testing frameworks and regression testing ensure consistent FM outputs

---

## 🧠 When to use

- prompt tuning
- prompt version rollback
- prompt optimization

---

# 🧩 3. RAG Evaluation (specialized evaluation)

## 🔹 What it evaluates

👉 **Retrieval + generation pipeline**

---

## 🔹 Two modes (VERY exam-relevant)

### 1. Retrieve-only

Query → Retriever → Context

Measures:

- context relevance
- coverage

---

### 2. Retrieve + Generate

Query → Retriever → LLM → Answer

Measures:

- correctness
- faithfulness
- grounding

---

From your guide:

> RAG evaluation measures correctness, completeness, faithfulness, and context relevance

---

## 🔹 Architecture

Prompt dataset  
+ reference context (optional)  
+ reference answers (optional)  
   ↓  
RAG system  
   ↓  
LLM judge  
   ↓  
Scores

---

## 🧠 When to use

- hallucination detection
- retrieval tuning
- chunking validation
- embedding quality validation

---

# ⚖️ Side-by-side (this is what you need for exam)

|Type|Focus|Scope|Key metric|
|---|---|---|---|
|Model eval|FM output|model only|correctness, fluency|
|Prompt eval|prompt quality|same model|consistency, effectiveness|
|RAG eval|retrieval + answer|full pipeline|grounding, relevance|

---

# 🔥 Exam Patterns (VERY predictable)

|If question says…|Answer|
|---|---|
|“evaluate model outputs”|Model evaluation|
|“compare prompt templates”|Prompt evaluation|
|“prompt regression testing”|Prompt evaluation|
|“hallucination / grounding”|RAG evaluation|
|“retrieval relevance”|RAG evaluation|
|“context quality”|RAG evaluation|

---

# ⚠️ Common traps

## ❌ ROUGE / BLEU

- lexical only
- not semantic

## ❌ CloudWatch

- performance only

## ❌ Model Monitor

- drift only

---

# 🧠 Mental Model (lock this)

Model eval   = quality of answers  
Prompt eval  = quality of instructions  
RAG eval     = quality of retrieval + grounding

---

# 🚀 Your level insight

This maps perfectly to your architecture thinking:

Prompt layer   → Prompt eval  
Model layer    → Model eval  
Retrieval layer → RAG eval

👉 That’s a **3-layer QA system for GenAI**

---

# ⚡ Final takeaway

If retrieval is involved → RAG eval  
If prompt is changing   → Prompt eval  
Else                    → Model eval

---

# ⚡ Quick challenge (exam-style)

You changed chunking strategy and now want to verify:

- better grounding
- fewer hallucinations

👉 What do you use?

A. Prompt evaluation  
B. Model evaluation  
C. RAG evaluation  
D. CloudWatch

---

Answer when ready 👇

Question 31 Incorrect A platform engineering team is building an internal “Ops Copilot” that autonomously troubleshoots application incidents. The team uses AWS Agent Squad to route each user request to one of several specialized Strands agents (for example, an incident triage agent and a runbook agent). Users expect the assistant to remember conversation context within a session and also retain longer-term preferences (for example, preferred service names and escalation rules) across multiple sessions. The team wants a serverless approach that minimizes the amount of custom state-management code they must build and operate. Which solution meets these requirements with the LEAST operational overhead? Deploy the Strands agents on Amazon ECS with AWS Fargate and store state locally in the container file system so agents can reuse memory between requests. Use AWS Agent Squad only for routing decisions. Explanation Incorrect. Container-local storage is not a durable or shared state store for a multi-agent, horizontally scaled system; tasks can be replaced at any time. This approach also introduces additional container operations compared to a managed, serverless agent runtime with built-in memory services. Use Amazon Bedrock Knowledge Bases as the system of record for both short-term and long-term memory by writing each conversation turn into the knowledge base and retrieving relevant history for each request. Explanation Incorrect. Knowledge bases are designed for retrieval augmentation over curated documents and indexed content, not for maintaining structured conversational state and preferences with session semantics. Using a knowledge base for chat memory typically adds latency and requires additional ingestion and retrieval design that does not directly provide session and memory-record abstractions. Your answer is incorrect Store per-session conversation history in Amazon DynamoDB and store long-term preferences as separate DynamoDB items. Pass the session identifier between the routed agents so each agent can fetch and update the state as needed. Explanation Incorrect. DynamoDB can store chat history and preferences, but the team must design session/event schemas, implement read/write patterns, manage summarization or pruning, and coordinate consistency across multiple agents. This increases custom state-management logic and operational responsibility compared to a managed agent memory capability. Correct answer Deploy the routed Strands agents by using Amazon Bedrock AgentCore Agent Runtime and use AgentCore Memory to manage session context and long-term memory records for user preferences that the agents can read and update across sessions. Explanation Correct. AgentCore provides serverless endpoints for agents and includes managed memory capabilities. AgentCore Memory supports session-oriented context (events within a session) and longer-term memory records (such as preferences and summaries), reducing the need to build and operate custom state stores and coordination logic across multiple specialized agents. Overall explanation The core challenge is maintaining both short-term conversational state (what was said earlier in the current interaction) and durable long-term memory (user preferences and extracted insights) while coordinating that state across multiple specialized agents selected by a router. A managed agent runtime with built-in memory reduces custom engineering and operational burden because it provides purpose-built abstractions for sessions and long-term memory records, and it avoids building and maintaining bespoke storage schemas, pruning logic, and cross-agent synchronization. Alternatives such as using a general-purpose database, container-local storage, or a retrieval knowledge base can work in limited scenarios, but they either do not provide session semantics and durable multi-agent state management, or they significantly increase the amount of custom code and operations required. Further reading (AWS): - Use isolated sessions for agents - Amazon Bedrock AgentCore (AWS Documentation) - Memory types - Amazon Bedrock AgentCore (AWS Documentation) - Compare long-term memory with Retrieval-Augmented Generation - Amazon Bedrock AgentCore (AWS Documentation)

---

This question is **pure architecture pattern recognition** — and it maps directly to your study guide.

Let’s break it cleanly so you’ll _never miss this again_ 👇

---

# 🧠 Step 1 — What is the question REALLY asking?

### Requirements translated:

|Requirement|Meaning|
|---|---|
|session context|**short-term memory**|
|preferences across sessions|**long-term memory**|
|multiple agents|**shared memory across agents**|
|least operational overhead|**managed service (no DIY state)**|

---

# 🧩 Step 2 — The key concept

From your guide:

> Agents use short-term memory (sessions/events) and long-term memory (memory records, preferences)

---

## 🔥 This is the trigger

“session + long-term memory + multi-agent + low overhead”  
→ AgentCore Memory

---

# 🏗️ Correct architecture

## ✅ Using Amazon Bedrock AgentCore

User  
  ↓  
Agent Squad (routing)  
  ↓  
Strands Agents (specialized)  
  ↓  
AgentCore Runtime  
  ↓  
AgentCore Memory  
   ├─ Session memory (short-term)  
   └─ Memory records (long-term)

---

## 🧠 Why this is optimal

### ✅ 1. Built-in session memory

Session → Events → conversation context

---

### ✅ 2. Built-in long-term memory

Memory Records → preferences / summaries

---

### ✅ 3. Shared across agents

👉 critical for Agent Squad routing

---

### ✅ 4. Serverless

👉 no infra, no schema design

---

# ❌ Why your answer (DynamoDB) is wrong

Your thinking was **technically correct**, but not optimal.

## ❌ Problem:

DynamoDB = DIY memory system

You must:

- design schema
- manage session IDs
- implement pruning/summarization
- handle multi-agent consistency

👉 **violates “least operational overhead”**

---

# ❌ Why other options are wrong

## ❌ ECS + local storage

Not durable + not shared

---

## ❌ Knowledge Base

RAG ≠ memory

From guide:

> Knowledge bases are for retrieval augmentation, not session memory

---

# 🧠 Mental Model (VERY IMPORTANT)

Chat memory ≠ RAG ≠ Database

---

## 🔑 Correct mapping

|Need|Solution|
|---|---|
|short-term memory|session memory|
|long-term memory|memory records|
|multi-agent memory|AgentCore|
|retrieval knowledge|Knowledge Base|
|custom storage|DynamoDB|

---

# 🔥 Exam Pattern (VERY high frequency)

|If question says…|Answer|
|---|---|
|“session context”|Agent memory|
|“user preferences”|long-term memory|
|“multi-agent coordination”|AgentCore|
|“least operational overhead”|managed service|
|“store conversation history manually”|usually WRONG|

---

# 🧠 Your level insight (this is big)

You’re designing:

Enterprise AI system =  
  
RAG (knowledge)  
+ Memory (user context)  
+ Agents (reasoning)

👉 These are **3 separate layers**

---

# ⚡ Final intuition

If it's conversational memory → AgentCore Memory  
If it's knowledge retrieval   → Knowledge Base

---

# ⚡ Quick challenge

You need:

- store chat history
- but NOT using agents
- simple chatbot
- low complexity

👉 What do you use?

A. AgentCore Memory  
B. DynamoDB  
C. Knowledge Base  
D. OpenSearch

---

Answer when ready 👇

b

✅ Correct — **B (DynamoDB)**

---

# 🧠 Why B is correct (tie back to previous question)

This is a **different scenario from Q31**

Q31 → multi-agent + least ops → AgentCore Memory  
This → simple chatbot → DynamoDB

---

# 🧩 Concept First

Memory type depends on complexity

---

# 🏗️ When to use DynamoDB

From your study guide:

> DynamoDB can serve as long-term memory for chat history in GenAI systems

---

## ✅ Perfect fit when:

- simple chatbot
- no agent orchestration
- you control logic
- need persistence

---

## 🧠 Architecture

User → API → Lambda  
              ↓  
        DynamoDB (chat history)  
              ↓  
           Bedrock

---

# ❌ Why others are wrong

## ❌ AgentCore Memory

Overkill for simple chatbot

👉 Designed for:

- multi-agent
- shared memory
- orchestration

---

## ❌ Knowledge Base

RAG, not memory

👉 Stores:

- documents
- embeddings  
    NOT chat history

---

## ❌ OpenSearch

Vector search, not session memory

---

# 🧠 Mental Model (VERY IMPORTANT)

From your notes + guide:

Memory types:  
  
Short-term → session (chat)  
Long-term → preferences / history

And storage options:

|Scenario|Best choice|
|---|---|
|simple chatbot|DynamoDB|
|multi-agent system|AgentCore Memory|
|knowledge retrieval|Knowledge Base|
|semantic search|OpenSearch|

---

# 🔥 Exam Pattern (high confidence)

|If question says…|Answer|
|---|---|
|“chat history”|DynamoDB|
|“session state”|DynamoDB|
|“multi-agent memory”|AgentCore|
|“knowledge retrieval”|KB|
|“semantic search”|OpenSearch|

---

# 🧠 Subtle exam trick (you just saw it)

Same concept → different answers:

|Question type|Answer|
|---|---|
|enterprise agent system|AgentCore Memory|
|simple chatbot|DynamoDB|

👉 **Complexity drives service choice**

---

# 🚀 Your level insight

You now have a clean separation:

Memory layer:  
- Lightweight → DynamoDB  
- Advanced → AgentCore Memory

---

# ⚡ Final intuition

If AWS says “least operational overhead + agents”  
→ AgentCore  
  
If AWS says “simple chat persistence”  
→ DynamoDB

---

# ⚡ Quick challenge

You need:

- chat history
- semantic search over past conversations
- similarity-based recall

👉 What do you use?

A. DynamoDB only  
B. OpenSearch only  
C. DynamoDB + OpenSearch  
D. AgentCore

---

Answer when ready 👇

Question 36 Incorrect A logistics company operates a legacy on-premises shipment tracking system that can send HTTPS webhooks but cannot use AWS SDKs. The company wants to add an Amazon Bedrock FM step that summarizes shipment exception notes and stores the summaries for downstream applications. During shift changes, exception events arrive in large bursts. The on-premises system must receive an immediate acknowledgment and must not be tightly coupled to Bedrock availability. Which solution will meet these requirements with the LEAST operational overhead? Configure an Amazon API Gateway REST API that invokes an AWS Lambda function synchronously. In the Lambda function, call the Amazon Bedrock InvokeModel API and return the summary in the API response to the on-premises system. Explanation Incorrect. Synchronous invocation couples the webhook response time to Bedrock latency and availability. Bursts can cause throttling and timeouts, and the on-premises system cannot wait for the full FM inference to complete. Your answer is incorrect Store exception notes in an Amazon S3 bucket from the on-premises system. Configure Amazon EventBridge to detect new objects and invoke an AWS Step Functions workflow that calls Amazon Bedrock and writes results back to the on-premises database. Explanation Incorrect. This requires the legacy system to integrate directly with S3 uploads and adds workflow orchestration and a write-back path to on-premises systems, increasing integration complexity and operational overhead compared to a simple webhook ingestion pattern. Correct answer Configure an Amazon API Gateway REST API with an AWS service integration to Amazon SQS. Have the on-premises system send webhooks to the API. Configure an AWS Lambda function to poll the SQS queue, invoke the Amazon Bedrock model, and store the summaries in Amazon DynamoDB for downstream consumption. Explanation Correct. API Gateway provides an HTTPS integration point for the legacy system and can immediately acknowledge requests. SQS decouples ingestion from processing and buffers burst traffic. Lambda scales to process messages asynchronously and can invoke Bedrock without coupling the legacy system to inference performance or availability. DynamoDB provides a simple, scalable store for downstream applications to retrieve summaries. Deploy a containerized service on Amazon ECS behind a Network Load Balancer to receive webhooks, call Amazon Bedrock directly from the service, and store results in Amazon OpenSearch Service. Explanation Incorrect. Running and scaling a container service introduces additional operational overhead (cluster/service management, scaling policies, patching, and deployment). It also still risks coupling webhook processing to inference unless additional buffering is implemented, and OpenSearch is unnecessary if the primary need is durable asynchronous processing and simple storage of summaries.

---

This is a **classic event-driven decoupling question** — and AWS repeats this pattern a LOT.

You picked **S3 + EventBridge + Step Functions**, which _sounds good architecturally_, but misses the **core requirement**.

Let’s break it down properly 👇

---

# 🧠 1. What is the question REALLY testing?

### Key signals:

|Requirement|Meaning|
|---|---|
|legacy system (HTTPS only)|needs **simple webhook endpoint**|
|immediate acknowledgment|**async pattern required**|
|burst traffic|**buffer needed**|
|not coupled to Bedrock|**decoupling layer required**|
|least operational overhead|**serverless + simple pattern**|

---

# 🧩 2. The winning pattern (must memorize)

Webhook → API Gateway → SQS → Lambda → Bedrock → DynamoDB

👉 This is **THE standard AWS async ingestion pattern**

---

# 🏗️ Why the correct answer works

## ✅ 1. API Gateway (front door)

- supports HTTPS webhooks
- immediate response

Client → API Gateway → 200 OK (instant)

---

## ✅ 2. SQS (the KEY component)

Decoupling + buffering layer

From your study guide:

> SQS is used to decouple applications and handle burst traffic

---

👉 Handles:

- spikes (shift change bursts)
- retry
- durability

---

## ✅ 3. Lambda (async processing)

- polls SQS
- calls Bedrock
- scales automatically

---

## ✅ 4. DynamoDB (simple storage)

- fast
- serverless
- downstream access

---

# ❌ Why your answer is wrong (important nuance)

## ❌ S3 + EventBridge + Step Functions

Too complex + wrong ingestion pattern

### Problems:

### 1. ❌ Wrong entry point

- webhook → S3 = awkward
- legacy systems don’t naturally upload objects

---

### 2. ❌ Extra orchestration layer

EventBridge + Step Functions = overkill

👉 adds:

- workflow complexity
- more moving parts

---

### 3. ❌ Not optimized for burst buffering

S3:

- storage
- NOT queue

SQS:

- purpose-built for bursts

---

# ❌ Why A is wrong

Synchronous = tightly coupled

👉 violates:

- immediate response
- resilience

---

# ❌ Why ECS is wrong

Container = operational overhead

👉 violates:

- serverless
- least effort

---

# 🧠 Mental Model (THIS is exam gold)

Webhook ingestion pattern:  
  
API Gateway  
   ↓  
Queue (SQS)   ← ALWAYS for burst + decoupling  
   ↓  
Lambda  
   ↓  
FM / processing

---

# 🔥 Exam Pattern (VERY HIGH frequency)

|If question says…|Answer|
|---|---|
|webhook ingestion|API Gateway|
|burst traffic|SQS|
|decouple system|SQS|
|async processing|Lambda|
|legacy system|API Gateway|
|least ops|serverless (no ECS, no Step Functions unless needed)|

---

# 🧠 Subtle trap you fell into

You chose:

“event-driven architecture”

BUT exam wanted:

“simple async ingestion pattern”

👉 AWS prefers:

- SQS over EventBridge (for buffering)
- minimal components

---

# 🚀 Your level insight

This is your enterprise mapping:

External system → API Gateway → Queue → Processing → Storage

👉 Same pattern everywhere:

- payments
- orders
- logs
- GenAI

---

# ⚡ Final intuition

If you see:  
- webhook  
- burst traffic  
- decoupling  
  
→ ALWAYS think SQS

---

# ⚡ Quick challenge

You need:

- real-time event routing
- multiple targets
- filtering rules

👉 What do you use?

A. SQS  
B. EventBridge  
C. DynamoDB  
D. Lambda

---

Answer when ready 👇

Question 38 Incorrect A fintech company is launching a public, GenAI-powered customer support chatbot that uses Amazon Bedrock to answer account questions. Security reviewers are concerned about prompt injection attempts (for example, users trying to override instructions or request hidden system prompts) and about accidental leakage of personally identifiable information (PII) in both user inputs and model outputs. The company wants a defense-in-depth approach that adds comprehensive protection against FM misuse with the LEAST operational overhead. Which solution meets these requirements? Your answer is incorrect Use Amazon Bedrock Guardrails only, configured to block profanity and remove PII. Rely on the guardrail blocked-message response to prevent misuse, and return the model response directly to callers. Explanation Incorrect. Guardrails are an important layer, but using only guardrails is not defense in depth. Additional layers (such as input pre-processing and post-processing validation/redaction) help reduce the impact of missed detections, integration mistakes, or novel prompt injection patterns. Correct answer Implement a serverless safety pipeline where Amazon API Gateway invokes a Lambda function that uses Amazon Comprehend to detect and mask PII in user prompts before invoking Amazon Bedrock with Bedrock Guardrails enabled. After the model responds, the Lambda function performs post-processing validation and additional PII redaction before returning the response through API Gateway response mapping templates that enforce a safe, filtered response shape. Explanation Correct. This design layers multiple controls: Comprehend provides pre-processing filters (including PII detection/masking), Bedrock Guardrails provide model-based safety controls for prompts and responses, Lambda enables custom post-processing validation/redaction for anything that slips through, and API Gateway can apply response transformations to enforce a safe response contract. This matches a defense-in-depth pattern while remaining largely managed and serverless. Fine-tune a custom model in Amazon Bedrock by using past chat transcripts so the model learns the company’s policies and avoids unsafe outputs. Deploy the fine-tuned model without additional pre-processing or post-processing because the model has been customized. Explanation Incorrect. Customization (fine-tuning or continued pre-training) does not guarantee compliance with safety requirements and does not replace layered runtime controls. It also increases cost and operational effort compared to managed guardrails and lightweight pre/post-processing. Place Amazon API Gateway in front of the chatbot. Use AWS WAF managed rules to block SQL injection and common web exploits, and then invoke Amazon Bedrock directly from the application with no additional controls. Explanation Incorrect. AWS WAF protects the HTTP interface, but it does not provide LLM-specific protections such as PII detection/redaction, prompt injection handling, or output moderation. Invoking the model without additional pre-processing, guardrails, and post-processing does not provide defense in depth for FM misuse. Overall explanation A defense-in-depth safety design uses multiple independent layers to reduce the probability and impact of unsafe inputs and outputs. A practical pattern is to filter and normalize inputs before model invocation (for example, detect and mask PII and suspicious content), apply model-native safety controls during inference (guardrails for prompt/response filtering and grounding-style checks where applicable), and validate or redact again after inference before returning data to end users. Implementing these layers with serverless components (Lambda, API Gateway) and managed services (Comprehend, Bedrock Guardrails) provides comprehensive protection with minimal infrastructure management, while approaches that rely on a single control layer (only WAF or only guardrails) or on model customization alone do not provide equivalent runtime protection against FM misuse. Further reading (AWS): - Detect and filter harmful content by using Amazon Bedrock Guardrails (AWS Documentation) - Personally identifiable information (PII) - Amazon Comprehend (AWS Documentation) - Mapping template transformations for REST APIs in API Gateway (AWS Documentation)

---

This is a **very high-yield “defense-in-depth” pattern question** — and it maps directly to the exam guide.

Let’s break it the way AWS expects 👇

---

# 🧠 1. What is being tested?

### Key requirements:

|Requirement|Meaning|
|---|---|
|prompt injection|input attack|
|PII leakage|input + output risk|
|defense-in-depth|**multiple layers**|
|least overhead|managed + serverless|

---

# 🔥 Core concept (from exam guide)

> Defense-in-depth safety = pre-processing + guardrails + post-processing

---

# 🧩 The correct pattern

Client  
  ↓  
API Gateway  
  ↓  
Lambda (pre-processing)  
  ↓  
Comprehend (PII detection)  
  ↓  
Bedrock + Guardrails  
  ↓  
Lambda (post-processing)  
  ↓  
API Gateway response filter  
  ↓  
Client

---

# 🧠 Why this is correct

## ✅ Layer 1 — Pre-processing (INPUT protection)

👉 using Amazon Comprehend

- detect PII
- mask sensitive data
- sanitize prompt

From your notes:

> Lambda + Comprehend can redact PII before data hits Bedrock

---

## ✅ Layer 2 — Model-time protection

👉 using Bedrock Guardrails

- block unsafe prompts
- filter outputs
- enforce grounding

From your guide:

> Guardrails filter inputs and outputs, including PII masking

---

## ✅ Layer 3 — Post-processing (OUTPUT protection)

👉 Lambda again

- validate response
- catch missed PII
- enforce formatting

---

## ✅ Layer 4 — API contract enforcement

👉 API Gateway

- response mapping
- enforce safe structure

---

# ❌ Why your answer (Guardrails only) is wrong

## ❌ Single layer ≠ defense-in-depth

Guardrails only = weak protection

Problems:

- misses novel prompt injection
- misses edge-case PII
- no fallback safety

---

# ❌ Why fine-tuning is wrong

Training ≠ runtime safety

- cannot guarantee compliance
- expensive
- not deterministic

---

# ❌ Why WAF is wrong

WAF = HTTP security, NOT AI safety

- protects against:
    - SQL injection
    - XSS
- does NOT handle:
    - prompt injection
    - hallucination
    - PII

---

# 🧠 Mental Model (THIS is exam gold)

AI Security = 3 layers

1. Before model → sanitize input  
2. During model → guardrails  
3. After model → validate output

---

# 🔥 Exam Pattern (VERY predictable)

|If question says…|Answer|
|---|---|
|prompt injection|pre-processing + guardrails|
|PII protection|Comprehend + guardrails|
|defense in depth|multi-layer pipeline|
|least overhead|serverless (Lambda + API GW)|
|“only guardrails”|❌ wrong|

---

# 🧠 Subtle insight (important for you)

You’re basically building:

Security Layer around LLM

From your architecture mindset:

LLM ≠ trusted system

👉 Everything around it must enforce controls

---

# 🚀 Your level insight

This aligns perfectly with enterprise AI:

Deterministic controls (Lambda, Comprehend)  
+ Probabilistic reasoning (LLM)

👉 exactly your **“tug-of-war” model**

---

# ⚡ Final intuition

If question says “security / misuse / injection”  
→ NEVER choose a single service  
→ ALWAYS choose layered architecture

---

# ⚡ Quick challenge

You need:

- detect jailbreak attempts
- enforce policy rules
- minimal custom code

👉 What do you use?

A. Comprehend only  
B. Guardrails only  
C. Guardrails + Lambda filters  
D. Fine-tuning

---

Answer when ready 👇

Question 47 Incorrect A SaaS provider runs an interactive RAG assistant for internal help desk agents. The request path is Amazon API Gateway to AWS Lambda, where the function performs a vector similarity search in Amazon OpenSearch Service and then calls an Amazon Bedrock FM by using the Converse API. Users report that responses feel slow, and profiling shows frequent connection setup overhead between Lambda and downstream services and high query fan-out across many OpenSearch shards during vector searches. The provider wants to reduce p95 end-to-end latency for the chat experience without changing the FM or the underlying document corpus and with the LEAST operational overhead. Which combination of actions should the provider take? (Select TWO.) Correct selection Reindex the OpenSearch vector index with fewer, larger shards sized for semantic search workloads to reduce cross-shard coordination during k-NN queries. Explanation Correct. Vector search can be slowed by coordinating many shard-level searches and merging results. Using fewer, larger shards (appropriate shard sizing) reduces fan-out and coordination overhead, improving retrieval latency without changing the FM or the document set. Correct selection Refactor the Lambda function to reuse HTTP/AWS SDK clients across invocations (for example, initialize clients outside the handler) and configure connection pooling/keep-alive for calls to OpenSearch and Amazon Bedrock. Explanation Correct. Reusing clients allows Lambda execution environments to keep connections open across invocations, reducing repeated TLS handshakes and connection setup time. This is a low-overhead change that improves service-to-service communication efficiency and directly reduces latency for GenAI request chains. Your selection is incorrect Enable Amazon Bedrock global cross-Region inference to route all model invocations to the least busy Region for faster responses. Explanation Incorrect. Cross-Region inference is primarily a resilience/throughput strategy and can add network latency when requests are served from a different Region. It also does not address the identified retrieval and connection setup bottlenecks. Tune OpenSearch HNSW settings by increasing ef_search and M values to maximize recall for every query, even if memory usage increases. Explanation Incorrect. Increasing ef_search and M can increase query time and memory consumption. The scenario’s primary problem is latency; maximizing recall at the expense of performance typically makes p95 latency worse and does not align with the goal. Your selection is incorrect Turn on Amazon Bedrock prompt caching by placing the retrieved OpenSearch context into the cached prompt prefix so future queries can reuse it. Explanation Incorrect. Prompt caching is most effective for a stable, reusable prompt prefix (for example, instructions and few-shot examples). Retrieved RAG context is dynamic per query, so caching it as the prefix will result in low cache reuse and can increase cache write overhead without addressing OpenSearch retrieval latency. Overall explanation The largest latency gains come from optimizing the two proven bottlenecks in the workflow: service-to-service communication and vector retrieval execution. Reusing clients with connection pooling reduces repeated connection establishment overhead between Lambda and downstream services, lowering end-to-end latency without changing the FM or architecture. Separately, tuning OpenSearch for vector search by reducing shard fan-out (fewer, larger shards sized appropriately for semantic search) reduces coordination overhead and speeds retrieval, which is a major contributor to total RAG response time. Options that prioritize recall tuning, rely on cross-Region routing, or attempt to cache dynamic retrieved context either increase latency, fail to address the true bottleneck, or have low effectiveness for this workload. Further reading (AWS): - AWS Lambda client not reused | Amazon Q, Detector Library (AWS Documentation) - Reuse connections with keep-alive in Node.js - AWS SDK for JavaScript (AWS Documentation) - Choosing the number of shards - Amazon OpenSearch Service (AWS Documentation) Domain Content Domain 4: Operational Efficiency and Optimization fo

---

This is a **pure performance tuning question** — and AWS is testing whether you can **identify the real bottleneck (not guess randomly)**.

You missed it because of a **very common trap**: picking “cool GenAI features” instead of fixing **infra-level latency**.

Let’s lock this in 👇

---

# 🧠 1. What is the question REALLY saying?

### Signals (VERY IMPORTANT):

|Signal|Meaning|
|---|---|
|slow responses|latency problem|
|connection setup overhead|**network inefficiency**|
|shard fan-out|**OpenSearch issue**|
|don’t change FM or corpus|focus on **system optimization**|
|least operational overhead|**simple tuning, not redesign**|

---

# 🔥 Step 2 — Identify the TWO bottlenecks

## 🧩 Bottleneck 1: Connection overhead

Lambda → OpenSearch / Bedrock  
(repeated TLS + connection setup)

---

## 🧩 Bottleneck 2: OpenSearch shard fan-out

Query → many shards → merge results

---

# ✅ Correct Answer Breakdown

---

## ✅ 1. Fix OpenSearch shard design

Fewer, larger shards

### Why?

From your study guide:

> Vector search benefits from fewer, larger shards because there is less cross-shard coordination

---

### Concept:

Many shards → parallel queries → merge overhead → slow  
Few shards  → less coordination → faster

---

## ✅ 2. Reuse connections in Lambda

Initialize clients outside handler  
Enable keep-alive / pooling

---

### Why?

From your guide:

> Connection pooling reduces repeated connection setup overhead

---

### Concept:

Without reuse:  
Every request → new TLS handshake ❌  
  
With reuse:  
Warm Lambda → reuse connection ✅

---

# ❌ Why your choices are wrong

---

## ❌ Cross-Region inference

Adds latency, not reduces

👉 From guide:

> Cross-region inference is for resilience, not latency optimization

---

---

## ❌ Increasing HNSW params (ef_search, M)

Higher recall = slower queries ❌

👉 You optimized **accuracy**, not **latency**

---

---

## ❌ Prompt caching

Works only for static prefix

From guide:

> Prompt caching is effective for static instructions, not dynamic RAG context

---

👉 RAG context = different every query → cache useless

---

# 🧠 Mental Model (VERY IMPORTANT)

RAG latency =  
  
Retrieval latency (OpenSearch)  
+ Network latency (Lambda connections)  
+ Model latency (Bedrock)

---

👉 You ONLY optimize what is slow:

OpenSearch + connections = bottleneck  
NOT the model

---

# 🔥 Exam Pattern (VERY predictable)

|If question says…|Answer|
|---|---|
|shard fan-out|reduce shards|
|vector search slow|fewer, larger shards|
|Lambda connection overhead|reuse clients|
|TLS overhead|connection pooling|
|latency tuning|infra fixes, not model changes|
|dynamic RAG|caching usually ❌|

---

# 🧠 Subtle insight (your level)

This question is **NOT about GenAI**

It’s about:

Distributed systems performance

👉 AWS expects you to think like:

Where is time being spent?

---

# 🚀 Your architecture-level takeaway

RAG performance tuning =  
  
1. Retrieval optimization (OpenSearch)  
2. Network optimization (Lambda)  
3. Model tuning (last resort)

---

# ⚡ Final intuition

If latency issue mentions:  
- shards → OpenSearch fix  
- connections → Lambda fix  
  
→ DO NOT touch the model

---

# ⚡ Quick challenge

You see:

- slow RAG queries
- high CPU on OpenSearch
- many small shards

👉 What’s the BEST fix?

A. Increase shard count  
B. Reduce shard count  
C. Enable prompt caching  
D. Use bigger FM

---

Answer when ready 👇

Question 51 Incorrect A fintech team is deploying an open-source LLM behind an Amazon SageMaker AI real-time inference endpoint by using a custom container image in Amazon ECR. The model artifacts in Amazon S3 are very large, and the container must download and load the weights into GPU memory during startup. During deployment, the endpoint repeatedly fails with container health check errors. Logs show the model is still downloading and initializing when the health check fails. Which change will allow the team to deploy the LLM successfully while keeping the same real-time endpoint architecture with the LEAST operational overhead? Your answer is incorrect Replace the real-time endpoint with a SageMaker Asynchronous Inference endpoint and have the application poll Amazon S3 for results. Explanation Incorrect. Asynchronous inference is designed for workloads that can tolerate longer end-to-end latency and typically returns results via an output location such as Amazon S3. This changes the interaction pattern and does not meet the requirement to keep a real-time endpoint architecture. Correct answer Update the endpoint configuration to increase the container startup health check timeout and the model artifact download timeout so the container has enough time to download and load the model before being declared unhealthy. Explanation Correct. Large language models often have very large weight files and longer initialization times than traditional ML models, especially when downloading artifacts from Amazon S3 and loading them into GPU memory. Increasing the container health check timeout and download timeout accommodates these LLM-specific startup characteristics without changing the architecture or adding additional services to operate. Increase the size of the GPU instance type for the endpoint so the container can load the model faster during startup. Explanation Incorrect. A larger instance can help with memory pressure, but it does not directly address the root cause shown in the logs: the container fails health checks while it is still downloading and initializing the model. This option increases cost and may still fail if the health check and download timeout settings are not adjusted for large model startup times. Move the model inference into an AWS Lambda function that downloads the model from Amazon S3 on each invocation and runs inference in the function runtime. Explanation Incorrect. Lambda is not suitable for hosting large LLM artifacts that must be loaded into GPU memory, and downloading large model weights on every invocation would create excessive latency and operational risk. It also does not align with the container-based LLM deployment approach used for SageMaker AI endpoints. Overall explanation Container-based LLM deployments frequently fail for reasons that are uncommon in traditional ML endpoints: large artifacts take longer to download, model initialization can be slower due to GPU memory setup, and the container may not pass health checks within default time limits. The most direct, low-overhead fix is to adjust the endpoint’s startup health check and model download timeout settings so the container can complete model loading before SageMaker evaluates it as unhealthy. Alternatives either change the required real-time interaction model, add significant cost without guaranteeing success, or use a compute environment that is not appropriate for large LLM inference. Further reading (AWS): - SageMaker AI endpoint parameters for large model inference - Amazon SageMaker AI (AWS Documentation) - ProductionVariant - Amazon SageMaker (AWS Documentation) - Custom Inference Code with Hosting Services - Amazon SageMaker AI (AWS Documentation)

---

This one is **pure SageMaker operational nuance** — not GenAI logic.

You answered wrong because you **changed the architecture**, instead of fixing the **deployment constraint**.

Let’s lock this in 👇

---

# 🧠 1. What is the question REALLY testing?

### Key signals:

|Signal|Meaning|
|---|---|
|large model artifacts|slow startup|
|GPU loading|heavy initialization|
|health check failing|timeout issue|
|keep real-time endpoint|❗ cannot change architecture|
|least operational overhead|config change, not redesign|

---

# 🔥 Core concept (from your study guide)

> Large models require adjusting container health check and download timeout quotas

---

# 🧩 What is actually happening?

Container startup flow:  
  
1. Start container  
2. Download model from S3  
3. Load into GPU memory  
4. Pass health check

---

### ❌ Current problem:

Health check happens BEFORE step 3 finishes  
→ container marked unhealthy  
→ deployment fails

---

# ✅ Correct solution

Increase:  
  
- container startup health check timeout  
- model download timeout

---

## 🧠 Why this works

Give container enough time to:  
  
download → load → initialize → pass health check

---

👉 You fix the **root cause**, not the architecture

---

# ❌ Why your answer is wrong (IMPORTANT)

## ❌ Asynchronous endpoint

You changed the interaction model ❌

From exam guide:

> Real-time vs async endpoints are different deployment patterns

---

### Problem:

|Requirement|Your solution|
|---|---|
|real-time endpoint|❌ async|
|immediate response|❌ delayed|
|same architecture|❌ changed|

---

👉 This is a **hard elimination rule**

---

# ❌ Why bigger GPU is wrong

Does NOT fix timeout ❌

- faster load ≠ guaranteed within timeout
- still may fail

---

# ❌ Why Lambda is wrong

LLM + Lambda = anti-pattern ❌

- no GPU
- cold start + download every time
- huge latency

---

# 🧠 Mental Model (VERY IMPORTANT)

SageMaker LLM deployment issues:  
  
1. Model too big → increase timeout  
2. GPU memory issue → change instance  
3. Traffic issue → autoscaling

---

👉 Always identify WHICH layer is failing

---

# 🔥 Exam Pattern (VERY predictable)

|If question says…|Answer|
|---|---|
|container fails startup|increase timeout|
|large model load time|increase download timeout|
|health check failing|increase health check timeout|
|must keep architecture|❗ DO NOT redesign|
|least overhead|config change|

---

# 🧠 Subtle insight (your level)

This is NOT GenAI.

This is:

Container lifecycle management

---

👉 AWS expects:

Fix config BEFORE changing architecture

---

# 🚀 Your architecture takeaway

LLM deployment = infra problem first, AI problem second

---

# ⚡ Final intuition

If deployment fails during startup:  
  
→ 90% of time = timeout issue

---

# ⚡ Quick challenge

You see:

- SageMaker endpoint stuck in "Creating"
- logs show model still loading
- no memory errors

👉 What’s the FIRST fix?

A. Increase instance size  
B. Increase timeout  
C. Switch to async endpoint  
D. Add caching

---

Answer when ready 👇

Question 59 Incorrect A product support team has built a public FAQ assistant that uses Amazon API Gateway and AWS Lambda to invoke an Amazon Bedrock text model. The assistant does not use user-specific context, and the team has configured the model with deterministic settings so the same question produces the same answer. Metrics show that a large percentage of requests are repeated verbatim across users, and the team wants to reduce Amazon Bedrock invocation costs and improve global response latency. Which solution will meet these requirements MOST cost-effectively? Enable Amazon Bedrock prompt caching for the system prompt and few-shot examples. Keep the user question as the suffix so the prefix is reused across invocations. Explanation Incorrect. Prompt caching can reduce token processing cost and improve latency by reusing a cached prompt prefix, but it still invokes the FM for every request. It does not avoid unnecessary FM invocations when users ask the exact same question repeatedly. Purchase Amazon Bedrock provisioned throughput for the model and increase the reserved concurrency of the Lambda function to improve performance during peak traffic. Explanation Incorrect. Provisioned throughput and increased Lambda concurrency can help handle higher traffic, but they do not reduce the number of FM invocations. This approach increases cost and does not address the core requirement of avoiding unnecessary invocations for repeated identical requests. Your answer is incorrect Implement semantic caching by storing embeddings of prompts and corresponding responses in Amazon MemoryDB. For each new prompt, generate an embedding and perform nearest-neighbor lookup. If the similarity score exceeds a threshold, return the cached response instead of invoking the FM. Explanation Incorrect. Although semantic caching can reduce FM invocations for semantically similar prompts, it requires an embedding-generation step for each request and careful threshold tuning to prevent incorrect cache hits. This introduces more operational complexity than edge caching for verbatim repeated questions, and it may add latency and cost overhead compared to a simple deterministic cache key. Correct answer Place Amazon CloudFront in front of the API. Create a deterministic request fingerprint (hash) from the normalized prompt and model configuration. Send requests as GET /ask?fingerprint=<hash> so CloudFront can cache and serve identical responses from the edge, invoking Bedrock only on a cache miss. Explanation Correct. Edge caching with CloudFront can avoid unnecessary FM invocations entirely for repeated requests by serving cached responses at edge locations. Using a deterministic request hash (fingerprint) ensures that only truly identical requests map to the same cache key, and including model configuration in the fingerprint prevents incorrect reuse when settings change. This directly reduces Bedrock invocation volume and improves latency for global users. Overall explanation Because many requests are exact repeats and the responses are deterministic, the best optimization is to avoid invoking the FM when a previous identical response already exists. Edge caching with CloudFront accomplishes this by serving cached responses from edge locations, improving latency for global users while reducing total Bedrock invocations. A deterministic request fingerprint provides a stable cache key and helps ensure cache correctness when prompts or model parameters change. Prompt caching improves token efficiency but still calls the model each time, and semantic caching adds embedding overhead and tuning complexity that is unnecessary when repetition is primarily verbatim. Provisioned throughput improves capacity but does not reduce invocation volume. Further reading (AWS): - Use various origins with CloudFront distributions (AWS Documentation) - Cache content based on query string parameters - Amazon CloudFront (AWS Documentation) - Prompt caching for faster model inference - Amazon Bedrock (AWS Documentation)

---

This is a **classic trap question** — you picked something _technically advanced (semantic caching)_ instead of the **simplest and cheapest solution**.

Let’s break it down cleanly 👇

---

# 🧠 1. What is the question REALLY asking?

### Key signals:

|Signal|Meaning|
|---|---|
|repeated verbatim requests|exact same input|
|deterministic model|same output every time|
|reduce cost|avoid FM calls|
|improve global latency|edge caching|
|MOST cost-effective|simplest solution|

---

# 🔥 Core insight

Same input + same output = caching problem (NOT AI problem)

---

# ✅ Correct solution (what AWS wants)

CloudFront + deterministic cache key (fingerprint)

---

## 🧩 How it works

User → CloudFront (edge)  
  
IF cache hit:  
    return response immediately ✅  
  
IF cache miss:  
    → API Gateway → Lambda → Bedrock  
    → store result in cache

---

### 🔑 Key trick: fingerprint

GET /ask?fingerprint=hash(prompt + config)

👉 ensures:

- identical requests → same cache key
- config changes → different cache key

---

# 💡 Why this is PERFECT

### 1. Zero Bedrock calls on cache hit

Cost ↓↓↓

### 2. Edge delivery

Latency ↓↓↓ (global users)

### 3. No extra compute

Operational overhead ↓↓↓

---

# ❌ Why your answer (semantic caching) is wrong

You were thinking **too advanced**.

---

## ❌ Semantic caching

Embedding → similarity search → threshold tuning

### Problems:

1. Still compute embeddings every request
2. Need vector DB (MemoryDB / OpenSearch)
3. Risk of wrong matches
4. More latency than simple cache

---

👉 From your study guide:

> Semantic caching adds overhead and must be carefully tuned

---

### 🧠 Key insight:

Semantic caching = for "similar"  
CloudFront caching = for "identical"

---

# ❌ Why prompt caching is wrong

Still calls the model every time ❌

👉 Only reduces token cost, NOT invocation count

---

# ❌ Why provisioned throughput is wrong

Solves scale, NOT cost ❌

Actually increases cost

---

# 🧠 Mental Model (VERY IMPORTANT)

Caching hierarchy (EXAM GOLD):  
  
1. Exact match → CloudFront / API cache ✅  
2. Similar match → Semantic cache  
3. No match → FM call

---

# 🔥 Exam Pattern (VERY predictable)

|Scenario|Answer|
|---|---|
|identical requests|CloudFront caching|
|deterministic outputs|caching|
|global users|CloudFront|
|reduce FM calls|edge cache|
|similar queries|semantic cache|
|reduce tokens only|prompt caching|

---

# 🧠 Subtle insight (your level)

This is NOT GenAI.

This is:

CDN caching strategy

---

👉 AWS is testing:

Do you avoid calling the model?

---

# 🚀 Your architecture takeaway

Best optimization = eliminate FM calls entirely

---

# ⚡ Final intuition

If:  
- same input  
- same output  
  
→ NEVER call the model twice

---

# ⚡ Quick challenge

You see:

- similar (not identical) queries
- slight wording differences
- still want to reduce FM calls

👉 What’s BEST?

A. CloudFront caching  
B. Semantic caching  
C. Prompt caching  
D. Provisioned throughput

---

Answer when ready 👇

Question 65 Incorrect A media analytics company is building a RAG assistant on AWS by using Amazon Bedrock for text generation. For the retrieval layer, some workloads use Amazon OpenSearch Service for vector search, while other workloads use Amazon Aurora PostgreSQL with the pgvector extension for advanced metadata filtering. The GenAI team wants a single, consistent retrieval interface that Bedrock-based applications can use without being rewritten when the underlying vector store changes. Which solution will provide the MOST seamless integration mechanism for retrieval augmentation across these vector stores? Correct answer Create a stateless Model Context Protocol (MCP) server (for example, on AWS Lambda) that exposes a single tool such as "vector_search" with a stable JSON input/output contract. Use an MCP client library in the application/agent runtime to call this tool, and route the request internally to OpenSearch or Aurora as needed. Explanation Correct. An MCP server plus an MCP client provides a standardized tool interface for vector queries. The stable contract abstracts away vendor- or engine-specific query details and lets the backend implementation change (OpenSearch vs Aurora pgvector) without changing how the FM-integrated application invokes retrieval. Your answer is incorrect Store embeddings and document chunks directly in Amazon S3 objects and retrieve relevant chunks by using S3 prefix filters and object metadata filters. Pass the retrieved objects as context to the model. Explanation Incorrect. S3 prefix and metadata filtering is not a semantic (vector) retrieval mechanism and does not provide k-nearest-neighbor style similarity search. This does not meet the requirement for a consistent vector retrieval interface across vector stores. Create two Amazon API Gateway endpoints: one backed by an AWS Lambda function that queries OpenSearch and another backed by a different Lambda function that queries Aurora. Instruct the foundation model in the prompt to call the appropriate endpoint based on the user’s request. Explanation Incorrect. Exposing multiple endpoints still results in inconsistent access patterns for the model and application. Relying on prompt instructions for endpoint selection is brittle and increases the chance of incorrect routing or malformed requests. Implement separate retrieval modules in the application code: one that queries OpenSearch using its vector search APIs and another that queries Aurora using SQL with pgvector. Add conditional logic in each application to select the correct module. Explanation Incorrect. This approach duplicates integration logic across applications and creates multiple access patterns. Switching vector store choices requires code changes and redeployments, which conflicts with the goal of a single, consistent retrieval interface. Overall explanation A consistent access mechanism for retrieval augmentation is best achieved by placing a stable, tool-like contract in front of the retrieval layer and letting applications or agents invoke that contract in the same way regardless of which vector store is used. Using an MCP server to expose a single vector-query tool, combined with an MCP client in the runtime, standardizes how the FM-integrated system performs retrieval and returns normalized results (for example, chunks plus metadata). This approach prevents tight coupling to OpenSearch-specific or Aurora/SQL-specific query logic and avoids rewriting application integrations when the organization changes vector stores. Further reading (AWS): - Deploy MCP servers in AgentCore Runtime - Amazon Bedrock AgentCore (AWS Documentation) - Vector search - Amazon OpenSearch Service (AWS Documentation) - Using Aurora PostgreSQL as a Knowledge Base for Amazon Bedrock - Amazon Aurora (AWS Documentation) Domain Content Domain 1: Foundation Model Integration, Data Managem

---

This is a **very high-signal exam question** — it’s testing whether you understand **MCP as an abstraction layer**, not just “another API”.

Let’s break it properly 👇

---

# 🧠 1. What is the real requirement?

### Core requirement (hidden in wording):

Multiple vector stores → single retrieval interface → no rewrite

---

### Translate to architecture thinking:

|Requirement|Meaning|
|---|---|
|OpenSearch + Aurora pgvector|heterogeneous backends|
|consistent interface|abstraction layer|
|no rewrite|decoupling|
|Bedrock apps|agent/tool-based interaction|

---

# 🔥 2. The key concept: MCP

From your study guide:

MCP = standardized interface for agent-tool interactions :contentReference[oaicite:0]{index=0}

Think of it like:

"USB-C for AI systems"

---

# 🧩 3. What MCP is solving here

Without MCP:

App → OpenSearch API (vector)  
App → Aurora SQL (pgvector)  
  
❌ different logic  
❌ tightly coupled  
❌ rewrite when switching

---

With MCP:

App → MCP client → MCP server → (OpenSearch OR Aurora)  
  
✅ same interface  
✅ backend hidden  
✅ plug-and-play

---

# 🧠 4. The winning pattern (VERY IMPORTANT)

MCP server = abstraction layer for tools

---

## Architecture

User / Agent  
    ↓  
Bedrock / App  
    ↓  
MCP client  
    ↓  
MCP server (Lambda)  
    ↓  
[Routing logic]  
    ├── OpenSearch  
    └── Aurora pgvector

---

# 🔑 5. Why MCP is the BEST answer

### 1. Standard interface

{  
  "tool": "vector_search",  
  "query": "policy on leave",  
  "top_k": 5  
}

👉 same contract regardless of backend

---

### 2. Decoupling

Change backend → no app change

---

### 3. Agent-native design

Agents call tools (not APIs)

👉 MCP fits perfectly into agent architecture

---

### 4. Centralized logic

Fix once → applies to all agents

---

# ❌ Why other options fail

---

## ❌ Multiple API endpoints

Model decides endpoint via prompt ❌

👉 brittle + non-deterministic

---

## ❌ App-level routing

if store == opensearch:  
   do X  
else:  
   do Y

👉 tight coupling → rewrite required

---

## ❌ S3 filtering

Not vector search ❌

👉 no semantic retrieval

---

# 🧠 6. Exam mental model (VERY IMPORTANT)

This question is testing:

Skill 1.5.6: consistent access mechanisms for retrieval :contentReference[oaicite:1]{index=1}

---

### Translation:

|Phrase in question|Expected answer|
|---|---|
|consistent interface|MCP|
|multiple vector stores|abstraction|
|no rewrite|decoupling|
|Bedrock agents|MCP tools|

---

# 🔥 7. When to use MCP (exam cheat sheet)

Use MCP when:

✔ multiple tools / systems  
✔ want standard interface  
✔ agent-based architecture  
✔ backend may change  
✔ reduce integration complexity

---

# ⚡ 8. When NOT to use MCP

❌ single system only  
❌ simple API call  
❌ no need for abstraction

---

# 🧠 9. Your level insight (important)

This is NOT about vector DB.

This is about:

INTERFACE DESIGN

---

👉 MCP is essentially:

"API Gateway for AI tools"

(but smarter + standardized for LLMs)

---

# 🚀 Final intuition

If question says:  
- multiple backends  
- standard interface  
- no code change  
  
→ ALWAYS think MCP

---

# ⚡ Quick test (very exam-like)

You have:

- 5 tools (CRM, DB, Search, Analytics, API)
- multiple agents need to use them
- want consistent interface
- want to swap tools later

What do you use?

A. API Gateway  
B. Lambda wrappers  
C. MCP server  
D. Step Functions

---

Answer when ready 👇

Question 66 Incorrect A logistics software provider runs an order-tracking platform on AWS that integrates with multiple internal microservices. A shipping partner sends signed HTTPS webhooks whenever a delivery exception occurs. The provider wants to add GenAI functionality that uses an Amazon Bedrock FM to generate a short, customer-ready message and then deliver the generated message to both a case-management service and a notification service. The webhook endpoint must acknowledge requests within 2 seconds, and the provider must be able to add additional downstream consumers later without changing the webhook handler code. Which solution will meet these requirements with the LEAST operational overhead? Use Amazon API Gateway to start an AWS Step Functions workflow that validates the webhook signature, invokes Amazon Bedrock, and calls both microservice APIs. Configure the workflow to return the result to API Gateway after all steps complete. Explanation Incorrect. Returning only after the workflow completes couples the webhook acknowledgement to FM invocation and downstream API calls, making it difficult to reliably meet the 2-second acknowledgement requirement. Step Functions is useful for orchestrating multi-step workflows, but it adds unnecessary orchestration complexity for a simple event-driven fan-out integration. Use Amazon API Gateway to receive the webhook and invoke an AWS Lambda function that validates the webhook signature and sends the payload to an Amazon SQS queue. Use a Lambda consumer to read messages from the queue, call Amazon Bedrock, and then call the case-management and notification microservice APIs. Explanation Incorrect. SQS provides durable buffering, but it is not optimized for content-based routing and multi-consumer fan-out without additional design (for example, multiple queues or custom fan-out logic). Adding new downstream consumers typically requires additional queues and changes to producers/consumers, increasing integration overhead compared to EventBridge rules. Your answer is incorrect Use Amazon API Gateway to receive the webhook and invoke a single AWS Lambda function that validates the webhook signature, calls Amazon Bedrock, calls the case-management and notification microservice APIs, and then returns a response to the webhook sender. Explanation Incorrect. This tightly couples webhook acknowledgement to FM inference and downstream service latency, which can exceed the 2-second acknowledgement requirement. It also makes future fan-out harder because new consumers require modifying the same Lambda function. Correct answer Use Amazon API Gateway to receive the webhook and invoke an AWS Lambda function that validates the webhook signature and publishes a custom event to Amazon EventBridge. Use EventBridge rules to invoke a second Lambda function that calls Amazon Bedrock and publishes a new event containing the generated message. Use additional EventBridge rules to invoke Lambda functions that call the case-management and notification microservice APIs. Explanation Correct. API Gateway provides a managed HTTPS endpoint, Lambda performs custom signature validation and normalization, and EventBridge decouples producers from consumers with managed, event-driven fan-out. The webhook handler can respond immediately after publishing the event, meeting the 2-second acknowledgement requirement. Adding new downstream consumers later is done by creating new EventBridge rules/targets without modifying the webhook handler. Overall explanation The key design requirement is to enhance an existing application by integrating GenAI while keeping the inbound webhook path fast and keeping downstream integrations loosely coupled. A managed webhook endpoint can be implemented with Amazon API Gateway, while AWS Lambda is appropriate for webhook handling tasks like HMAC signature validation and request normalization. Publishing the validated event to Amazon EventBridge decouples the webhook handler from downstream processing. EventBridge rules can then trigger GenAI inference (invoking an Amazon Bedrock model from Lambda) and fan out the resulting message to multiple existing microservices. This pattern minimizes operational overhead because routing, fan-out, and future consumer additions are handled by EventBridge configuration rather than custom integration code changes. Further reading (AWS): - Event buses in Amazon EventBridge - Amazon EventBridge (AWS Documentation) - Event bus targets in Amazon EventBridge - Amazon EventBridge (AWS Documentation) - Submit prompts and generate responses using the API - Amazon Bedrock (AWS Documentation) Domain Content Domain 2: Implementation and Integration

---

This is a **classic event-driven architecture trap question** — and it shows up _a lot_ in the exam.

Let’s break it down in a way you’ll remember 👇

---

# 🧠 1. What are they REALLY testing?

### Hidden requirements (translate like an architect):

Webhook (<2 sec response)  
+ GenAI processing (slow)  
+ fan-out to multiple systems  
+ future extensibility  
+ minimal ops

---

# 🔥 2. The core conflict (VERY IMPORTANT)

FAST ACK vs SLOW PROCESSING

- Webhook must respond in **<2 seconds**
- Bedrock call = **seconds**
- Downstream calls = **seconds**

👉 So:

You MUST decouple

---

# 🧩 3. The correct mental model

Webhook = ingestion layer (fast)  
Processing = async layer (slow)  
Fan-out = event routing

---

# ✅ 4. Why EventBridge is the correct answer

## Step-by-step flow:

1. API Gateway receives webhook  
2. Lambda validates signature  
3. Lambda publishes EventBridge event  ← (FAST)  
4. Return 200 OK immediately           ← (<2 sec requirement)  
  
--- ASYNC ---  
  
5. EventBridge rule → Lambda (Bedrock)  
6. Generate message  
7. Publish new event  
  
8. EventBridge rules:  
   → case-management service  
   → notification service

---

# 🧠 5. Why this works

### ✅ Requirement 1 — fast response

ACK happens BEFORE Bedrock call

---

### ✅ Requirement 2 — fan-out

EventBridge = built-in fan-out

No custom code needed.

---

### ✅ Requirement 3 — future extensibility

Add new consumer = new rule

👉 no code change

---

### ✅ Requirement 4 — least ops

No queue orchestration  
No workflow engine  
No custom routing logic

---

# ❌ 6. Why your answer (Lambda doing everything) is wrong

API → Lambda → Bedrock → Services → return

Problems:

- ❌ webhook waits for Bedrock → timeout risk
- ❌ tightly coupled
- ❌ adding consumers = code change
- ❌ not scalable

---

# ❌ 7. Why SQS option is WRONG (important nuance)

This is subtle — exam loves this.

### SQS gives:

✔ buffering  
✔ async processing

BUT:

❌ NOT fan-out friendly  
❌ NOT dynamic routing

To support multiple consumers:

You need:  
- multiple queues OR  
- custom fan-out logic

👉 more ops overhead

---

# 🔥 8. Why Step Functions is WRONG

API → Step Functions → wait → return

Problem:

❌ synchronous coupling  
❌ violates <2 sec requirement  
❌ over-engineering

---

# 🧠 9. The pattern you MUST remember

## ⭐ EventBridge pattern

Ingestion → EventBridge → Processing → EventBridge → Consumers

---

## Compare quickly:

|Pattern|When to use|
|---|---|
|API Gateway + Lambda only|simple sync|
|SQS|buffering|
|Step Functions|orchestration|
|EventBridge|fan-out + decoupling ⭐|

---

# 🚀 10. Exam shortcut (VERY HIGH VALUE)

If you see:

✔ webhook  
✔ must respond fast  
✔ async processing  
✔ multiple consumers  
✔ future extensibility

👉 **Answer = EventBridge**

---

# 🧠 11. Tie back to study guide

This is exactly:

Event-driven architecture → loose coupling :contentReference[oaicite:0]{index=0}

And:

Skill: enterprise integration + event-driven patterns :contentReference[oaicite:1]{index=1}

---

# ⚡ 12. One-line intuition

SQS = queue  
EventBridge = router

---

# 🧪 Quick check (exam style)

You have:

- webhook
- multiple downstream services
- need to add new consumers later
- no code change allowed

What do you use?

A. SQS  
B. Step Functions  
C. EventBridge  
D. Lambda

---

Answer? 👇

Question 73 Incorrect A platform engineering team is building an internal IT support assistant by using an Amazon Bedrock agent. The agent uses an Amazon Bedrock Knowledge Base for policy documents and multiple action groups backed by AWS Lambda functions to open and update tickets in a ticketing system. After a recent change to the agent instructions and tool descriptions, the team sees occasional multi-step loops (repeated tool calls) and wants a repeatable way to verify that the agent still completes tasks successfully while using tools efficiently. Which combination of actions will create an agent performance framework with the LEAST operational overhead? (Select TWO.) Correct selection Run Amazon Bedrock Agent evaluations against a representative prompt dataset and use the results to track task completion rates and tool usage effectiveness over time. Explanation Correct. Agent evaluations provide a managed way to assess whether an agent completes the target tasks and how effectively it uses tools, which directly addresses correctness and efficiency with minimal custom infrastructure. Your selection is correct Log the agent trace output for production and test invocations to Amazon CloudWatch Logs and use CloudWatch Logs Insights to measure repeated action group invocations per request and to review reasoning steps in multi-step workflows. Explanation Correct. Agent traces show which knowledge bases and action groups were used and in what order, enabling objective measures such as tool invocation counts/loops and qualitative inspection of multi-step reasoning. Using CloudWatch Logs and Logs Insights keeps the operational burden low while still providing actionable metrics. Your selection is incorrect Build a custom evaluation pipeline with AWS Step Functions that replays prompts, calls a separate foundation model as a judge, and stores scoring results in Amazon S3 for reporting. Explanation Incorrect. This can work, but it introduces significant custom orchestration and maintenance overhead compared with using managed Bedrock agent evaluation capabilities and built-in tracing/observability. Enable Amazon SageMaker Model Monitor on the Bedrock agent to detect drift and set alarms when response quality falls below a baseline. Explanation Incorrect. SageMaker Model Monitor is used to monitor models deployed in SageMaker, and it is not the primary mechanism for evaluating Amazon Bedrock agent task completion and tool usage efficiency. Create Amazon CloudWatch Synthetics canaries that invoke the agent on a schedule and fail if the HTTP status code is not 200. Track only end-to-end latency as the primary success metric. Explanation Incorrect. Synthetic canaries can detect availability and latency regressions, but they do not measure whether the agent actually completed the intended task or whether tool usage was effective (for example, repeated or unnecessary action group invocations). Overall explanation A low-overhead agent performance framework should directly measure whether the agent completes tasks and how efficiently it uses tools. Using managed Amazon Bedrock Agent evaluations provides standardized scoring for agent task outcomes and tool effectiveness without building custom pipelines. Capturing agent traces and analyzing them in CloudWatch Logs provides concrete observability into multi-step behavior (such as repeated tool loops) and supports reasoning-quality assessment by showing the sequence of orchestration steps, knowledge base retrievals, and action group invocations. Approaches that only test endpoint availability/latency miss correctness and tool efficiency, while building a bespoke judge-and-orchestrate system increases operational complexity. Further reading (AWS): - Evaluate agent performance with Amazon Bedrock AgentCore Evaluations - Amazon Bedrock AgentCore (AWS Documentation) - Track agent's step-by-step reasoning process using trace - Amazon Bedrock (AWS Documentation) - Analyzing log data with CloudWatch Logs Insights - Amazon CloudWatch Logs (AWS Documentation) Domain Content Domain 5: Testing, Validation, and Troubleshooting

---

Nice — this is a **perfect “observability + evaluation” pattern question**. You actually got the _right learning_, just missed the pattern once.

Let’s lock this in so you never miss it again 👇

---

# 🧠 1. What is the question REALLY asking?

Agent loops / repeated tool calls  
Need:  
✔ task completion validation  
✔ tool efficiency tracking  
✔ minimal overhead  
✔ repeatable framework

👉 This is NOT monitoring  
👉 This is NOT debugging

👉 This is **Agent performance evaluation**

---

# 🔥 2. The two signals you must measure

## (1) Did it complete the task?

→ correctness

## (2) Did it use tools efficiently?

→ no loops, no redundant calls

---

# ✅ 3. Correct combo = two layers

### 🟢 Layer 1 — Evaluation (managed)

👉 **Bedrock Agent Evaluations**

Measures:  
- task success rate  
- tool usage effectiveness

This directly maps to:

Skill 5.1.7: agent performance frameworks :contentReference[oaicite:0]{index=0}

---

### 🟢 Layer 2 — Observability (trace)

👉 **Agent tracing + CloudWatch Logs**

Measures:  
- how many tool calls  
- loops / repeated actions  
- reasoning path

And this is straight from your guide:

Agent tracing shows reasoning + tool usage + steps :contentReference[oaicite:1]{index=1}

---

# 🧩 4. How they work together (this is the key insight)

Agent Evaluations → "Did it work?"  
Agent Tracing     → "How did it behave?"

---

# 🧠 5. Visual mental model

Prompt dataset  
      ↓  
Agent  
      ↓  
───────────────  
| Evaluation  | → success rate, quality  
───────────────  
| Tracing     | → steps, loops, tool calls  
───────────────

---

# ❌ 6. Why your wrong option (Step Functions pipeline) fails

You picked:

Custom pipeline (Step Functions + judge model)

Problem:

❌ reinventing Bedrock Evaluations  
❌ high operational overhead  
❌ violates "LEAST overhead"

Exam rule:

If AWS gives managed eval → ALWAYS pick it

---

# ❌ 7. Why others are wrong (quick elimination)

### SageMaker Model Monitor

❌ for ML drift  
❌ NOT for LLM / agent reasoning

---

### CloudWatch Synthetics

❌ only checks availability / latency  
❌ DOES NOT check correctness

---

# 🧠 8. The exam pattern (VERY HIGH VALUE)

If you see:

✔ agent loops / bad tool usage  
✔ need reasoning visibility  
✔ need evaluation  
✔ minimal overhead

👉 Answer ALWAYS includes:

✔ Agent Evaluations  
✔ Agent Tracing

---

# 🔥 9. Tie back to study plan (important)

This sits exactly in your:

Week 6 → Evaluation & Troubleshooting :contentReference[oaicite:2]{index=2}

And:

Monitoring + evaluation + tracing combo

---

# ⚡ 10. One-line memory trick

Agents:  
Evaluate → correctness  
Trace → reasoning

---

# 🧪 Quick exam check

You see:

- agent sometimes loops tools
- you need to measure efficiency
- you want minimal ops

What do you pick?

A. CloudWatch metrics  
B. Step Functions pipeline  
C. Agent evaluations + tracing  
D. SageMaker Monitor

---

👉 Your answer?

Question 74 Incorrect A financial services company is building a customer-support assistant that uses an Amazon Bedrock FM to summarize chat conversations and propose next-step actions for agents. Customers frequently paste sensitive data (for example, names, email addresses, phone numbers, and account identifiers) into the chat. The company must prevent sensitive information from being sent to the FM or appearing in the model’s responses, while keeping the responses useful and contextually accurate. Which combination of actions will meet these requirements with the LEAST loss of utility? (Select TWO.) Correct selection Add an AWS Lambda pre-processing step that calls Amazon Comprehend PII detection on the user message and replaces detected PII with consistent placeholders (for example, <NAME_1>, <PHONE_1>) before invoking the Amazon Bedrock model. Explanation Correct. Pre-processing with Amazon Comprehend can detect common PII types and mask them before the request reaches the FM. Using consistent placeholders preserves conversational structure and relationships (for example, the same person referenced multiple times), which helps maintain response quality while protecting privacy. Build an Amazon Comprehend custom entity recognizer to detect customer identifiers and then discard any message that contains detected entities before invoking the FM. Explanation Incorrect. Discarding entire messages whenever entities are detected removes critical context, which reduces FM utility and can degrade response accuracy. Additionally, training and maintaining a custom entity recognizer adds operational overhead when built-in PII detection and masking approaches can meet the requirement more effectively. Enable SSE-KMS encryption on the Amazon S3 buckets that store conversation transcripts and model outputs, and use AWS KMS key policies to restrict access to the encrypted data. Explanation Incorrect. Encrypting stored transcripts and outputs protects data at rest, but it does not prevent PII from being transmitted to the FM during inference or from being returned in the FM response. This does not satisfy the requirement to prevent sensitive information from being sent to the FM or appearing in responses. Use Amazon Macie to discover and classify PII in the Amazon S3 bucket that stores chat transcripts, and automatically delete objects that contain PII before invoking the Amazon Bedrock model. Explanation Incorrect. Macie is designed to discover sensitive data in S3, not to provide real-time masking for interactive FM prompts and responses. Deleting objects after discovery does not reliably prevent PII from being included in the live prompt flow, and it can also remove important context needed to keep responses useful.

---

This is a **classic “privacy vs utility trade-off” trap question** — and you were actually _very close_. Let’s lock the pattern properly.

---

# 🧠 1. What the question is REALLY testing

✔ Prevent PII from reaching FM  
✔ Prevent PII in output  
✔ KEEP usefulness (critical!)  
✔ Minimal overhead

👉 That last one is the killer:  
**“least loss of utility” = don’t destroy context**

---

# 🔥 2. The core idea (high-level)

You need:

Before FM → clean input  
After FM  → clean output

NOT:

❌ delete data  
❌ block requests  
❌ encrypt only

---

# ✅ 3. Correct answers = TWO layers

## 🟢 (1) Pre-processing → mask PII

👉 Amazon Comprehend + Lambda

Input:  
"John called, his number is 0400..."  
  
↓ transform  
  
" <NAME_1> called, his number is <PHONE_1>"

### Why this is PERFECT:

- Removes PII ✅
- Keeps structure ✅
- Preserves meaning ✅

👉 This is explicitly aligned with:

Token-level redaction / pre-processing patterns :contentReference[oaicite:0]{index=0}

---

## 🟢 (2) Post-processing → redact output

👉 (This is the one missing in your view)

You need:

Lambda post-processing OR Guardrails

To ensure:

FM does NOT reintroduce PII

---

# 🎯 Final correct combo

✔ Pre-processing (Comprehend masking)  
✔ Post-processing (redaction / guardrails)

---

# ❌ 4. Why the wrong answers fail

## 🚫 “Discard message if PII detected”

❌ kills context  
❌ reduces accuracy  
❌ violates "least loss of utility"

👉 This is the BIG exam trap

---

## 🚫 S3 encryption (KMS)

❌ protects storage only  
❌ does NOT protect inference

---

## 🚫 Macie

❌ batch / after-the-fact  
❌ not real-time

---

# 🧠 5. The exam pattern (VERY IMPORTANT)

If you see:

✔ PII protection  
✔ real-time chat / inference  
✔ must preserve usefulness

👉 ALWAYS think:

Pre-process → mask  
Post-process → validate/redact

NOT:

❌ delete  
❌ block  
❌ encrypt-only

---

# 🔄 6. Mental model (use this in exam)

User input  
   ↓  
[PII masking]  ← Comprehend  
   ↓  
Bedrock FM  
   ↓  
[PII redaction] ← Guardrails / Lambda  
   ↓  
Response

---

# ⚡ 7. One-line memory hack

Mask, don’t drop.

---

# 🔥 8. Subtle but important insight

Why placeholders matter:

"John emailed Mary"  
→ "<NAME_1> emailed <NAME_2>"

👉 The model still understands:

- relationships
- actions
- sequence

That’s why it says:

"LEAST loss of utility"

---

# 🧪 Quick exam check

Which is BEST?

A. Drop messages with PII  
B. Encrypt logs  
C. Mask before + redact after  
D. Scan with Macie

👉 Your answer?

Question 75 Incorrect A retail platform team runs a customer-support chatbot that uses an Amazon Bedrock FM. The team frequently updates prompts and inference parameters to improve tone and accuracy. After several releases, business stakeholders report that answers are becoming inconsistent and occasionally violate the required response style. The team needs a systematic quality assurance approach that performs regression testing before each deployment and continuously detects output regressions after deployment. The solution must integrate with an automated deployment workflow and require the LEAST operational overhead. Which combination of actions will meet these requirements? (Select TWO.) Your selection is incorrect For each release, use Amazon SageMaker Ground Truth Plus to have human reviewers compare responses from the current and candidate prompts, then promote the change only after a manual approval step. Explanation Incorrect. Human review can be valuable, but it adds significant operational overhead and latency and is not a lightweight, systematic regression-testing approach for frequent prompt iterations. Correct selection Create an Amazon CloudWatch Synthetics canary that invokes the chatbot’s production API on a schedule with a small set of synthetic user workflows. Publish pass/fail as CloudWatch metrics and use CloudWatch alarms to detect regressions and alert the team. Explanation Correct. CloudWatch Synthetics provides continuous, automated checks that simulate end-to-end usage. Alarms on the resulting metrics create an ongoing regression detection mechanism with minimal custom infrastructure. Your selection is correct Create a prompt dataset in Amazon S3 with representative user questions and reference responses. Add a stage in AWS CodePipeline that runs Amazon Bedrock Model Evaluations against the candidate prompt changes and fails the pipeline if quality metrics fall below defined thresholds. Explanation Correct. A fixed prompt dataset provides repeatable regression tests, and Bedrock Model Evaluations can score outputs (for example, with LLM-as-a-judge or other supported evaluation approaches). Using the results as a pipeline gate implements an automated quality gate that prevents regressions from being promoted. Export Amazon Bedrock request/response logs to Amazon S3 once per day and use Amazon Athena queries to manually review a sample of responses for tone and accuracy before approving each deployment. Explanation Incorrect. This relies on manual review and periodic exports, which does not provide an automated quality gate in the deployment workflow or continuous regression detection with low operational overhead. Increase the model temperature and top-p values during testing runs to explore more response variations, and deploy if the responses appear reasonable across multiple invocations. Explanation Incorrect. Increasing randomness makes outputs less consistent and does not create a repeatable regression test or an automated quality gate. It also does not provide continuous monitoring after deployment. Overall explanation A systematic FM quality assurance process typically combines pre-deployment regression testing with post-deployment continuous monitoring. Running structured, repeatable model evaluations on a fixed prompt dataset provides a reliable regression test that can act as an automated quality gate in a CI/CD pipeline. After deployment, synthetic user workflows run by a canary provide continuous validation of end-to-end behavior and can trigger CloudWatch alarms when regressions occur. Manual sampling and ad hoc parameter tweaking do not provide consistent, automated controls, and human-only review adds substantial operational overhead for frequent releases. Further reading (AWS): - Use prompt datasets for model evaluation in Amazon Bedrock - Amazon Bedrock (AWS Documentation) - Invoke an AWS Lambda function in a pipeline in CodePipeline - AWS CodePipeline (AWS Documentation) - Synthetic monitoring (canaries) - Amazon CloudWatch (AWS Documentation) Domain Content Domain 5: Testing, Validation, and Troubleshooting

---

Nice — this is actually the **perfect final question** because it ties everything together:  
**evaluation + CI/CD + monitoring (before + after deployment)**

---

# 🧠 1. What the question is testing

✔ Pre-deployment regression testing  
✔ Post-deployment continuous monitoring  
✔ Automated (not manual)  
✔ Integrated with pipeline  
✔ Low operational overhead

👉 This maps EXACTLY to:

Testing lifecycle (Domain 5) :contentReference[oaicite:0]{index=0}

---

# 🧩 2. The correct pattern (VERY predictable)

Think in **two phases**:

---

## 🔵 Phase 1 — BEFORE deployment

👉 “Do we allow this change?”

Prompt dataset + Model Evaluation

✔ Stored in S3  
✔ Run Bedrock Model Evaluations  
✔ Gate in CodePipeline

👉 This gives:

✔ repeatable regression testing  
✔ automated quality scoring  
✔ CI/CD integration

📌 This is explicitly required:

“regression testing + automated quality gate” :contentReference[oaicite:1]{index=1}

---

## 🟢 Phase 2 — AFTER deployment

👉 “Did something break in production?”

CloudWatch Synthetics (canaries)

✔ Simulates real user flows  
✔ Runs continuously  
✔ Triggers alarms

👉 This gives:

✔ continuous validation  
✔ real-world monitoring  
✔ zero custom infra

---

# 🧠 3. Why these TWO together win

### 🔁 Full lifecycle coverage

Before deploy → Model Evaluations  
After deploy  → Synthetics Canary

This matches AWS best practice:

“continuous evaluation workflows + synthetic user workflows” :contentReference[oaicite:2]{index=2}

---

# ❌ 4. Why the wrong answers fail

## 🚫 Ground Truth (human review)

❌ slow  
❌ expensive  
❌ not scalable

👉 violates:

LEAST operational overhead

---

## 🚫 Athena + manual review

❌ not automated  
❌ not real-time  
❌ no pipeline integration

---

## 🚫 tweaking temperature/top-p

❌ not evaluation  
❌ increases randomness  
❌ not repeatable

---

# 🔥 5. The exam pattern (IMPORTANT)

If you see:

✔ regression testing  
✔ prompt changes  
✔ CI/CD pipeline  
✔ low overhead

👉 ALWAYS answer:

Bedrock Model Evaluations + prompt dataset

---

If you also see:

✔ continuous monitoring  
✔ production validation

👉 ADD:

CloudWatch Synthetics

---

# 🧠 6. Mental model (lock this in)

DEV / CI  
---------  
Prompt dataset → Model Eval → PASS/FAIL  
  
PROD  
---------  
Synthetic users → Canary → Alarm

---

# ⚡ 7. One-line memory hack

Eval before, Canary after.

---

# 🔄 Quick check (exam reflex)

Which combo is BEST?

A. Human review + manual approval  
B. Model eval + canary  
C. Athena + logs  
D. Temperature tuning