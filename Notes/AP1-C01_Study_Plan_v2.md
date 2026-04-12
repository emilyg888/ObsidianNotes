# AP1-C01 / AIP-C01

## AWS Certified Generative AI Developer -- Professional

### Updated Study Plan (Aligned to Official Exam Guide)

Target exam date: **31 March**

This plan aligns with the official exam domains:

  Domain                                  Weight
  --------------------------------------- --------
  FM Integration, Data Management         31%
  Implementation & Integration            26%
  AI Safety, Security, Governance         20%
  Operational Efficiency & Optimization   12%
  Testing, Validation, Troubleshooting    11%

------------------------------------------------------------------------

# Week 1 -- Foundations of Generative AI on AWS

## Day 1 -- Foundation Models and Amazon Bedrock

Concepts: - Foundation models - Transformer architecture - Bedrock model
providers (Claude, Titan, Llama) - Serverless model access

Example: Customer support chatbot summarizing support tickets.

Architecture: User → API Gateway → Lambda → Bedrock → FM → Response

------------------------------------------------------------------------

## Day 2 -- Prompt Engineering

Concepts: - Prompt structure (Instruction / Context / Input / Output) -
Zero‑shot vs few‑shot prompting - Chain‑of‑thought reasoning -
Structured JSON output

------------------------------------------------------------------------

## Day 3 -- Retrieval Augmented Generation (RAG)

Concepts: - Prevent hallucinations - Retrieval pipelines - Context
injection

Architecture: User → Retriever → Context → LLM → Answer

------------------------------------------------------------------------

## Day 4 -- Embeddings and Vector Databases

Concepts: - Embedding vectors - Cosine similarity - ANN search - Vector
stores

Services: OpenSearch, Aurora pgvector, Pinecone

------------------------------------------------------------------------

## Day 5 -- Bedrock Knowledge Bases

Concepts: - Managed RAG - Data ingestion - Chunking strategies

Architecture: S3 → Bedrock KB → Embedding → Vector Store → LLM

------------------------------------------------------------------------

## Day 6 -- Guardrails and Responsible AI

Concepts: - Bedrock Guardrails - Content filtering - PII redaction -
Contextual grounding

------------------------------------------------------------------------

# Week 2 -- Data Pipelines and Retrieval

## Day 7 -- Data Preparation for GenAI

Concepts: - Structuring unstructured data - Textract - Comprehend - Glue
pipelines

------------------------------------------------------------------------

## Day 8 -- Audio and Text Processing

Concepts: - Amazon Transcribe - Amazon Comprehend - Entity extraction -
Speech‑to‑text pipelines

------------------------------------------------------------------------

## Day 9 -- Vector Database Architecture

Concepts: - ANN search - Index tuning - Hybrid search

------------------------------------------------------------------------

## Day 10 -- Vector Optimization

Concepts: - FP16 embeddings - Binary vectors - Dimensionality tradeoffs

------------------------------------------------------------------------

## Day 11 -- Retrieval Engineering

Concepts: - Hierarchical chunking - Semantic chunking - Metadata
filtering - Reranking

Pipeline: Documents → Chunking → Embedding → Vector DB → Retriever →
Reranker → LLM

------------------------------------------------------------------------

# Week 3 -- Agentic AI Systems

## Day 12 -- Bedrock Agents

Concepts: - Planning module - Tool invocation - Action groups

Architecture: User → Agent → Tools → Knowledge Base → Response

------------------------------------------------------------------------

## Day 13 -- Multi‑Agent Architectures

Concepts: - Orchestrator pattern - Worker agents - Result synthesizer

------------------------------------------------------------------------

## Day 14 -- Agent Memory

Concepts: - Short‑term memory - Long‑term memory - DynamoDB storage

------------------------------------------------------------------------

## Day 15 -- Tool Calling and MCP

Concepts: - OpenAPI tool schemas - Model Context Protocol - Agent‑tool
communication

Architecture: User → Agent → Tool APIs → Lambda → External Systems

------------------------------------------------------------------------

# Week 4 -- Operations and Optimization

## Day 16 -- Token Optimization

Concepts: - Context pruning - maxTokens - token estimation

------------------------------------------------------------------------

## Day 17 -- Model Routing

Concepts: - Cost vs capability tradeoff - Dynamic routing

------------------------------------------------------------------------

## Day 18 -- Observability

Concepts: - CloudWatch metrics - Token usage tracking - Latency
monitoring

------------------------------------------------------------------------

## Day 19 -- GenAI Monitoring

Concepts: - Bedrock invocation logs - Agent tracing - Hallucination
detection - Response drift

------------------------------------------------------------------------

# Week 5 -- Security and Governance

## Day 20 -- Security Fundamentals

Concepts: - IAM - KMS encryption - Secrets Manager - Cognito
authentication

------------------------------------------------------------------------

## Day 21 -- Network Architecture

Concepts: - VPC endpoints - PrivateLink - Secure model inference

------------------------------------------------------------------------

## Day 22 -- Prompt Governance

Concepts: - Prompt versioning - Template management - Prompt testing
frameworks

------------------------------------------------------------------------

# Week 6 -- Evaluation and Troubleshooting

## Day 23 -- Model Evaluation

Concepts: - Bedrock evaluation jobs - RAG evaluation - ROUGE metrics -
LLM‑as‑judge

------------------------------------------------------------------------

## Day 24 -- Troubleshooting GenAI Systems

Common Problems:

  Issue                 Possible Cause
  --------------------- ------------------
  Hallucinations        Weak retrieval
  Irrelevant answers    Poor prompt
  Truncated responses   Context overflow

------------------------------------------------------------------------

## Day 25 -- Enterprise GenAI Architecture Review

Reference Architecture:

User\
→ CloudFront\
→ API Gateway\
→ Lambda\
→ Bedrock\
→ Knowledge Base (OpenSearch)\
→ Enterprise Data (S3 / RDS)

------------------------------------------------------------------------

## Day 26 -- Full Practice Exam

Simulate exam conditions:

-   65 questions
-   Multiple choice
-   Multiple response
-   Ordering
-   Matching

Focus on: - Architecture decisions - Service selection - Trade‑offs
