import { useState, useCallback } from "react";
import type { AgentRunResponse } from "../types";

interface RunArgs {
  query: string;
  concept?: string | null;
  count?: number;
  difficulty?: "associate" | "professional";
}

export function useAgents() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const run = useCallback(async (args: RunArgs): Promise<AgentRunResponse | null> => {
    setLoading(true);
    setError(null);
    try {
      const body = {
        query: args.query,
        concept: args.concept ?? undefined,
        count: args.count,
        difficulty: args.difficulty,
      };
      const res = await fetch("/agents/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
      if (!res.ok) {
        const text = await res.text();
        throw new Error(`HTTP ${res.status}: ${text}`);
      }
      return (await res.json()) as AgentRunResponse;
    } catch (err) {
      setError(String(err));
      return null;
    } finally {
      setLoading(false);
    }
  }, []);

  return { run, loading, error };
}
