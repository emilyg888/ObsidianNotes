import { useState, useMemo } from "react";
import { useGraphData } from "./hooks/useGraphData";
import type { TabId, Filters, SimNode } from "./types";
import { Sidebar } from "./components/Sidebar";
import { ForceGraph } from "./components/ForceGraph";
import { ConceptCards } from "./components/ConceptCards";
import { PatternRegistry } from "./components/PatternRegistry";
import { Comparisons } from "./components/Comparisons";
import { DetailPanel } from "./components/DetailPanel";
import { AgentsPanel } from "./components/AgentsPanel";

export default function App() {
  const data = useGraphData();
  const [tab, setTab] = useState<TabId>("graph");
  const [filters, setFilters] = useState<Filters>({
    showConcepts: true,
    showComponents: true,
    showPatterns: true,
    minFrequency: 0,
    search: "",
  });
  const [selectedNode, setSelectedNode] = useState<SimNode | null>(null);

  const filteredNodes = useMemo(() => {
    const searchLower = filters.search.toLowerCase();
    return data.simNodes.filter((n) => {
      if (n.type === "concept" && !filters.showConcepts) return false;
      if (n.type === "component" && !filters.showComponents) return false;
      if (n.type === "pattern" && !filters.showPatterns) return false;
      if (n.frequency < filters.minFrequency) return false;
      if (searchLower && !n.label.toLowerCase().includes(searchLower))
        return false;
      return true;
    });
  }, [data.simNodes, filters]);

  const filteredNodeIds = useMemo(
    () => new Set(filteredNodes.map((n) => n.id)),
    [filteredNodes]
  );

  const filteredLinks = useMemo(
    () =>
      data.simLinks.filter((l) => {
        const src =
          typeof l.source === "string" ? l.source : (l.source as SimNode).id;
        const tgt =
          typeof l.target === "string" ? l.target : (l.target as SimNode).id;
        return filteredNodeIds.has(src) && filteredNodeIds.has(tgt);
      }),
    [data.simLinks, filteredNodeIds]
  );

  if (data.loading) {
    return (
      <div className="flex items-center justify-center h-screen text-slate-400 text-lg">
        Loading knowledge graph...
      </div>
    );
  }

  if (data.error) {
    return (
      <div className="flex items-center justify-center h-screen text-red-400 text-lg">
        Error: {data.error}
      </div>
    );
  }

  return (
    <div className="flex h-screen overflow-hidden">
      <Sidebar
        tab={tab}
        onTabChange={setTab}
        filters={filters}
        onFiltersChange={setFilters}
        maxFrequency={data.maxFrequency}
        stats={{
          nodes: data.graph.nodes.length,
          edges: data.graph.edges.length,
          concepts: data.extractions.global_concept_index?.length ?? 0,
          patterns: data.extractions.pattern_registry?.length ?? 0,
          comparisons:
            data.extractions.comparison_registry?.filter(
              (c) => c.type === "tradeoff"
            ).length ?? 0,
        }}
      />

      <main className="flex-1 overflow-auto">
        {tab === "graph" && (
          <ForceGraph
            nodes={filteredNodes}
            links={filteredLinks}
            onNodeClick={setSelectedNode}
            selectedId={selectedNode?.id ?? null}
          />
        )}
        {tab === "concepts" && (
          <ConceptCards
            concepts={data.extractions.global_concept_index ?? []}
            search={filters.search}
          />
        )}
        {tab === "patterns" && (
          <PatternRegistry
            patterns={data.extractions.pattern_registry ?? []}
            search={filters.search}
          />
        )}
        {tab === "comparisons" && (
          <Comparisons
            comparisons={
              data.extractions.comparison_registry?.filter(
                (c) => c.type === "tradeoff"
              ) ?? []
            }
          />
        )}
        {tab === "agents" && (
          <AgentsPanel
            concepts={
              data.extractions.global_concept_index?.map((c) => c.concept) ?? []
            }
          />
        )}
      </main>

      {selectedNode && tab === "graph" && (
        <DetailPanel
          node={selectedNode}
          graph={data.graph}
          extractions={data.extractions}
          onClose={() => setSelectedNode(null)}
        />
      )}
    </div>
  );
}
