import { useEffect, useState } from "react";
import type {
  ConceptGraph,
  Extractions,
  SimNode,
  SimLink,
  GraphNode,
} from "../types";

// Build frequency lookup from extractions
function buildFrequencyMap(ext: Extractions): Map<string, number> {
  const map = new Map<string, number>();
  for (const c of ext.global_concepts) map.set(c.name, c.count);
  for (const c of ext.global_components) map.set(c.name, c.count);
  for (const p of ext.global_patterns) map.set(p.name, p.count);
  return map;
}

function nodeToSim(node: GraphNode, freq: number): SimNode {
  return {
    id: node.id,
    type: node.type,
    label: node.label,
    confidence: node.confidence ?? 0.5,
    frequency: freq,
    radius: Math.sqrt(Math.max(freq, 1)) * 2 + 4,
  };
}

export interface GraphData {
  graph: ConceptGraph;
  extractions: Extractions;
  simNodes: SimNode[];
  simLinks: SimLink[];
  maxFrequency: number;
  loading: boolean;
  error: string | null;
}

export function useGraphData(): GraphData {
  const [graph, setGraph] = useState<ConceptGraph>({ nodes: [], edges: [] });
  const [extractions, setExtractions] = useState<Extractions | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    Promise.all([
      fetch("/concept_graph.json").then((r) => r.json()),
      fetch("/global_extractions.json").then((r) => r.json()),
    ])
      .then(([g, e]) => {
        setGraph(g);
        setExtractions(e);
      })
      .catch((err) => setError(String(err)))
      .finally(() => setLoading(false));
  }, []);

  if (loading || !extractions) {
    return {
      graph,
      extractions: extractions ?? ({} as Extractions),
      simNodes: [],
      simLinks: [],
      maxFrequency: 1,
      loading,
      error,
    };
  }

  const freqMap = buildFrequencyMap(extractions);
  const nodeIds = new Set(graph.nodes.map((n) => n.id));

  const simNodes: SimNode[] = graph.nodes.map((n) =>
    nodeToSim(n, freqMap.get(n.label) ?? 1)
  );

  const simLinks: SimLink[] = graph.edges
    .filter((e) => nodeIds.has(e.from) && nodeIds.has(e.to))
    .map((e) => ({
      source: e.from,
      target: e.to,
      edgeType: e.type,
      confidence: e.confidence,
    }));

  const maxFrequency = Math.max(...simNodes.map((n) => n.frequency), 1);

  return { graph, extractions, simNodes, simLinks, maxFrequency, loading, error };
}
