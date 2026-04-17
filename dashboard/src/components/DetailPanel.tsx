import type { SimNode, ConceptGraph, Extractions } from "../types";

interface Props {
  node: SimNode;
  graph: ConceptGraph;
  extractions: Extractions;
  onClose: () => void;
}

export function DetailPanel({ node, graph, extractions, onClose }: Props) {
  // Find connected edges
  const connected = graph.edges.filter(
    (e) => e.from === node.id || e.to === node.id
  );

  // Find concept index entry if concept
  const conceptEntry = extractions.global_concept_index?.find(
    (c) => c.concept === node.label
  );

  // Find pattern entry if pattern
  const patternEntry = extractions.pattern_registry?.find(
    (p) => p.pattern_id === node.id
  );

  // Group edges by type
  const edgesByType = new Map<string, typeof connected>();
  for (const edge of connected.slice(0, 20)) {
    const existing = edgesByType.get(edge.type) ?? [];
    existing.push(edge);
    edgesByType.set(edge.type, existing);
  }

  const nodeLabel = (id: string) =>
    graph.nodes.find((n) => n.id === id)?.label ?? id;

  return (
    <aside className="w-80 bg-slate-900 border-l border-slate-700 overflow-auto shrink-0">
      {/* Header */}
      <div className="p-4 border-b border-slate-700 flex items-start justify-between">
        <div>
          <span
            className="inline-block px-2 py-0.5 text-[10px] uppercase rounded mb-1"
            style={{
              color:
                node.type === "concept"
                  ? "#3b82f6"
                  : node.type === "component"
                  ? "#22c55e"
                  : "#f97316",
              background:
                node.type === "concept"
                  ? "rgba(59,130,246,0.15)"
                  : node.type === "component"
                  ? "rgba(34,197,94,0.15)"
                  : "rgba(249,115,22,0.15)",
            }}
          >
            {node.type}
          </span>
          <h3 className="text-sm font-bold text-white">{node.label}</h3>
        </div>
        <button
          onClick={onClose}
          className="text-slate-500 hover:text-slate-300 text-lg leading-none"
        >
          x
        </button>
      </div>

      {/* Stats */}
      <div className="p-4 border-b border-slate-700 grid grid-cols-3 gap-2 text-center">
        <div>
          <p className="text-lg font-bold text-white">{node.frequency}</p>
          <p className="text-[10px] text-slate-500">Frequency</p>
        </div>
        <div>
          <p className="text-lg font-bold text-white">
            {Math.round(node.confidence * 100)}%
          </p>
          <p className="text-[10px] text-slate-500">Confidence</p>
        </div>
        <div>
          <p className="text-lg font-bold text-white">{connected.length}</p>
          <p className="text-[10px] text-slate-500">Edges</p>
        </div>
      </div>

      {/* Concept-specific info */}
      {conceptEntry && (
        <div className="p-4 border-b border-slate-700">
          {conceptEntry.aliases.length > 0 && (
            <div className="mb-3">
              <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
                Aliases
              </p>
              <p className="text-xs text-slate-400">
                {conceptEntry.aliases.join(", ")}
              </p>
            </div>
          )}
          <div className="mb-3">
            <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
              Components
            </p>
            <div className="flex flex-wrap gap-1">
              {conceptEntry.related_components.map((c) => (
                <span
                  key={c}
                  className="inline-block px-1.5 py-0.5 text-[11px] rounded bg-green-500/15 text-green-400 border border-green-500/30"
                >
                  {c}
                </span>
              ))}
            </div>
          </div>
          <div>
            <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
              Patterns
            </p>
            <div className="flex flex-wrap gap-1">
              {conceptEntry.related_patterns.map((p) => (
                <span
                  key={p}
                  className="inline-block px-1.5 py-0.5 text-[11px] rounded bg-orange-500/15 text-orange-400 border border-orange-500/30"
                >
                  {p}
                </span>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Pattern-specific info */}
      {patternEntry && (
        <div className="p-4 border-b border-slate-700">
          {patternEntry.used_in.length > 0 && (
            <div className="mb-3">
              <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
                Used in concepts
              </p>
              <div className="flex flex-wrap gap-1">
                {patternEntry.used_in.map((c) => (
                  <span
                    key={c}
                    className="inline-block px-1.5 py-0.5 text-[11px] rounded bg-blue-500/15 text-blue-400 border border-blue-500/30"
                  >
                    {c}
                  </span>
                ))}
              </div>
            </div>
          )}
          {patternEntry.aliases.length > 0 && (
            <div>
              <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
                Aliases
              </p>
              <p className="text-xs text-slate-400">
                {patternEntry.aliases.join(", ")}
              </p>
            </div>
          )}
        </div>
      )}

      {/* Graph edges */}
      <div className="p-4">
        <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-2">
          Graph Relations
        </p>
        {[...edgesByType.entries()].map(([type, edgesOfType]) => (
          <div key={type} className="mb-3">
            <p className="text-xs text-slate-400 font-medium mb-1">
              {type.replace(/_/g, " ")}
            </p>
            <ul className="space-y-0.5">
              {edgesOfType.slice(0, 8).map((edge, j) => {
                const other =
                  edge.from === node.id ? edge.to : edge.from;
                const direction = edge.from === node.id ? "→" : "←";
                return (
                  <li
                    key={j}
                    className="text-xs text-slate-500 flex items-center gap-1"
                  >
                    <span className="text-slate-600">{direction}</span>
                    <span className="text-slate-300">
                      {nodeLabel(other)}
                    </span>
                    <span className="text-slate-600 ml-auto">
                      {Math.round(edge.confidence * 100)}%
                    </span>
                  </li>
                );
              })}
              {edgesOfType.length > 8 && (
                <li className="text-xs text-slate-600">
                  +{edgesOfType.length - 8} more
                </li>
              )}
            </ul>
          </div>
        ))}
      </div>
    </aside>
  );
}
