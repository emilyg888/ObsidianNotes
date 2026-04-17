import { useState, useRef, useEffect } from "react";
import type {
  AgentRunResponse,
  AgentName,
  TutorOutput,
  QuizOutput,
  ReviewOutput,
} from "../types";
import { useAgents } from "../hooks/useAgents";
import { TutorResponse } from "./TutorResponse";
import { QuizResponse } from "./QuizResponse";
import { ReviewerResponse } from "./ReviewerResponse";

interface Message {
  id: number;
  role: "user" | "agent" | "error";
  content: string;
  response?: AgentRunResponse;
}

const AGENT_META: Record<AgentName, { label: string; color: string; icon: string }> = {
  tutor: { label: "Tutor", color: "text-blue-400", icon: "🎓" },
  quiz: { label: "Quiz", color: "text-orange-400", icon: "📝" },
  review: { label: "Reviewer", color: "text-purple-400", icon: "🔍" },
};

const SAMPLE_QUERIES = [
  "What is RAG and when should I use it?",
  "Quiz me on guardrails — 5 questions",
  "Review an architecture: API Gateway → Lambda → Bedrock → OpenSearch for a Q&A chatbot",
];

interface Props {
  concepts: string[];
}

export function AgentsPanel({ concepts }: Props) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [concept, setConcept] = useState<string>("");
  const { run, loading, error } = useAgents();
  const endRef = useRef<HTMLDivElement>(null);
  const counter = useRef(0);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const submit = async (queryText?: string) => {
    const query = (queryText ?? input).trim();
    if (!query || loading) return;

    const userMsg: Message = {
      id: ++counter.current,
      role: "user",
      content: query,
    };
    setMessages((m) => [...m, userMsg]);
    setInput("");

    const res = await run({ query, concept: concept || undefined });
    if (!res) {
      setMessages((m) => [
        ...m,
        {
          id: ++counter.current,
          role: "error",
          content:
            error ||
            "Failed to reach agent backend. Is the FastAPI server running on :8765 and LM Studio on :1234?",
        },
      ]);
      return;
    }
    setMessages((m) => [
      ...m,
      {
        id: ++counter.current,
        role: "agent",
        content: "",
        response: res,
      },
    ]);
  };

  const onKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      submit();
    }
  };

  return (
    <div className="flex flex-col h-full">
      {/* Header */}
      <div className="px-6 py-4 border-b border-slate-700 bg-slate-900/50">
        <h2 className="text-xl font-bold text-white">Agents</h2>
        <p className="text-xs text-slate-500 mt-0.5">
          Qwen 2.5-14B · dynamic routing across 3 specialist agents
        </p>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-auto px-6 py-4">
        {messages.length === 0 && (
          <div className="text-center mt-10">
            <p className="text-sm text-slate-400 mb-3">
              Ask a question, request a quiz, or submit an architecture for
              review — the router picks the right agent automatically.
            </p>
            <div className="inline-flex flex-col gap-2 text-left">
              {SAMPLE_QUERIES.map((q) => (
                <button
                  key={q}
                  onClick={() => submit(q)}
                  className="text-xs text-slate-400 hover:text-slate-200 bg-slate-800/60 hover:bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 transition-colors"
                >
                  → {q}
                </button>
              ))}
            </div>
          </div>
        )}

        {messages.map((msg) => (
          <div key={msg.id} className="mb-4">
            {msg.role === "user" && (
              <div className="flex justify-end">
                <div className="bg-blue-600/20 border border-blue-500/30 rounded-lg px-3 py-2 max-w-[85%]">
                  <p className="text-sm text-slate-100">{msg.content}</p>
                  {concept && msg === messages.at(-1) && (
                    <p className="text-[10px] text-blue-400/70 mt-1">
                      concept: {concept}
                    </p>
                  )}
                </div>
              </div>
            )}
            {msg.role === "error" && (
              <div className="bg-red-500/15 border border-red-500/30 rounded-lg px-3 py-2 text-sm text-red-300">
                {msg.content}
              </div>
            )}
            {msg.role === "agent" && msg.response && (
              <AgentMessage response={msg.response} />
            )}
          </div>
        ))}

        {loading && (
          <div className="text-xs text-slate-500 italic">
            thinking<span className="animate-pulse">...</span>
          </div>
        )}
        <div ref={endRef} />
      </div>

      {/* Input */}
      <div className="border-t border-slate-700 bg-slate-900/50 px-6 py-3">
        <div className="flex items-center gap-2 mb-2">
          <label className="text-xs text-slate-500">Concept context:</label>
          <select
            value={concept}
            onChange={(e) => setConcept(e.target.value)}
            className="flex-1 px-2 py-1 bg-slate-800 border border-slate-600 rounded text-xs text-slate-300 focus:outline-none focus:border-blue-500"
          >
            <option value="">(none — let agent infer)</option>
            {concepts.map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </select>
        </div>
        <div className="flex gap-2">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={onKeyDown}
            placeholder="Ask, quiz, or request a review..."
            rows={2}
            className="flex-1 px-3 py-2 bg-slate-800 border border-slate-600 rounded-lg text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-blue-500 resize-none"
            disabled={loading}
          />
          <button
            onClick={() => submit()}
            disabled={loading || !input.trim()}
            className="px-4 py-2 bg-blue-600 hover:bg-blue-500 disabled:bg-slate-700 disabled:text-slate-500 rounded-lg text-sm text-white font-medium transition-colors"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

function AgentMessage({ response }: { response: AgentRunResponse }) {
  const meta = AGENT_META[response.agent];
  return (
    <div className="bg-slate-800/40 border border-slate-700 rounded-lg p-3 max-w-[95%]">
      <div className="flex items-center justify-between mb-2 pb-2 border-b border-slate-700">
        <div className="flex items-center gap-2">
          <span className="text-base">{meta.icon}</span>
          <span className={`text-xs font-bold ${meta.color}`}>
            {meta.label}
          </span>
        </div>
        <span className="text-[10px] text-slate-500 italic">
          routed · {response.routing.method ?? "auto"} · {response.routing.reason}
        </span>
      </div>
      {response.agent === "tutor" && (
        <TutorResponse output={response.output as TutorOutput} />
      )}
      {response.agent === "quiz" && (
        <QuizResponse output={response.output as QuizOutput} />
      )}
      {response.agent === "review" && (
        <ReviewerResponse output={response.output as ReviewOutput} />
      )}
    </div>
  );
}
