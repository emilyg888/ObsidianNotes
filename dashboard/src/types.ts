// ── Graph JSON ──
export interface GraphNode {
  id: string;
  type: "concept" | "component" | "pattern";
  label: string;
  confidence?: number;
}

export interface GraphEdge {
  from: string;
  to: string;
  type: string;
  evidence_count: number;
  source_diversity: number;
  confidence: number;
  // tradeoff edges
  dimensions?: Record<string, string>;
  recommended_usage?: Record<string, string[]>;
}

export interface ConceptGraph {
  nodes: GraphNode[];
  edges: GraphEdge[];
}

// ── Extractions JSON ──
export interface ChunkExtraction {
  chunk_id: number;
  title: string;
  sources: string[];
  prev_chunk_summary: string | null;
  next_chunk_summary: string | null;
  concepts: string[];
  components: string[];
  component_families: string[];
  patterns: string[];
}

export interface RollupEntry {
  name: string;
  count: number;
  chunks: number[];
  sources: string[];
}

export interface ConceptIndexEntry {
  concept: string;
  aliases: string[];
  frequency: number;
  related_components: string[];
  related_component_families: string[];
  related_patterns: string[];
  source_count: number;
  pattern_link_count: number;
  component_link_count: number;
  chunks: number[];
  sources: string[];
  confidence: number;
}

export interface PatternRegistryEntry {
  pattern_id: string;
  name: string;
  structure: string;
  aliases: string[];
  used_in: string[];
  related_components: string[];
  confidence: number;
  frequency: number;
  chunks: number[];
  sources: string[];
}

export interface ComparisonEntry {
  from: string;
  to: string;
  confidence: number;
  evidence_count: number;
  source_diversity: number;
  shared_components: string[];
  shared_sources: string[];
  shared_contexts: string[];
  type: "tradeoff" | "contrasts_with";
  dimensions?: Record<string, string>;
  recommended_usage?: Record<string, string[]>;
}

export interface Extractions {
  metadata: { input_file: string; chunk_count: number };
  chunk_extractions: ChunkExtraction[];
  global_concepts: RollupEntry[];
  global_components: RollupEntry[];
  global_component_families: RollupEntry[];
  global_patterns: RollupEntry[];
  global_concept_index: ConceptIndexEntry[];
  pattern_registry: PatternRegistryEntry[];
  concept_component_map: {
    concept: string;
    components: string[];
    component_families: string[];
    patterns: string[];
    frequency: number;
    confidence: number;
  }[];
  concept_aliases: {
    canonical: string;
    label: string;
    aliases: string[];
    frequency: number;
    confidence: number;
  }[];
  comparison_registry: ComparisonEntry[];
}

// ── D3 simulation types ──
export interface SimNode extends d3.SimulationNodeDatum {
  id: string;
  type: "concept" | "component" | "pattern";
  label: string;
  confidence: number;
  frequency: number;
  radius: number;
}

export interface SimLink extends d3.SimulationLinkDatum<SimNode> {
  edgeType: string;
  confidence: number;
}

// ── App state ──
export type TabId =
  | "graph"
  | "concepts"
  | "patterns"
  | "comparisons"
  | "agents";

// ── Agent API ──
export type AgentName = "tutor" | "quiz" | "review";

export interface AgentRouting {
  reason: string;
  method?: string;
}

export interface TutorOutput {
  answer: string;
  concept: string | null;
  related_components: string[];
  related_patterns: string[];
}

export interface QuizQuestion {
  id: number;
  question: string;
  options: string[];
  answer: string;
  explanation: string;
}

export interface QuizOutput {
  questions: QuizQuestion[];
  topics: string[];
  parse_error?: string;
  raw?: string;
}

export interface ReviewOutput {
  scores: {
    security: number;
    scalability: number;
    cost_efficiency: number;
    reliability: number;
    operational_excellence: number;
  };
  overall: number;
  strengths: string[];
  risks: string[];
  recommendations: string[];
  concept: string | null;
  parse_error?: string;
  raw?: string;
}

export interface AgentRunResponse {
  agent: AgentName;
  routing: AgentRouting;
  output: TutorOutput | QuizOutput | ReviewOutput;
  metadata: Record<string, unknown>;
}

export interface Filters {
  showConcepts: boolean;
  showComponents: boolean;
  showPatterns: boolean;
  minFrequency: number;
  search: string;
}

// d3 module augmentation
import type * as d3 from "d3";
