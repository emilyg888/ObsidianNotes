import type { TabId, Filters } from "../types";

const TABS: { id: TabId; label: string; icon: string }[] = [
  { id: "graph", label: "Graph", icon: "🔗" },
  { id: "concepts", label: "Concepts", icon: "💡" },
  { id: "patterns", label: "Patterns", icon: "🧩" },
  { id: "comparisons", label: "Compare", icon: "⚖️" },
  { id: "agents", label: "Agents", icon: "🤖" },
];

interface Props {
  tab: TabId;
  onTabChange: (t: TabId) => void;
  filters: Filters;
  onFiltersChange: (f: Filters) => void;
  maxFrequency: number;
  stats: {
    nodes: number;
    edges: number;
    concepts: number;
    patterns: number;
    comparisons: number;
  };
}

export function Sidebar({
  tab,
  onTabChange,
  filters,
  onFiltersChange,
  maxFrequency,
  stats,
}: Props) {
  const set = (partial: Partial<Filters>) =>
    onFiltersChange({ ...filters, ...partial });

  return (
    <aside className="w-64 bg-slate-900 border-r border-slate-700 flex flex-col shrink-0">
      {/* Header */}
      <div className="p-4 border-b border-slate-700">
        <h1 className="text-lg font-bold text-white">Knowledge Dashboard</h1>
        <p className="text-xs text-slate-400 mt-1">
          {stats.nodes} nodes &middot; {stats.edges} edges
        </p>
      </div>

      {/* Search */}
      <div className="p-3 border-b border-slate-700">
        <input
          type="text"
          placeholder="Search..."
          value={filters.search}
          onChange={(e) => set({ search: e.target.value })}
          className="w-full px-3 py-2 bg-slate-800 border border-slate-600 rounded-lg text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-blue-500"
        />
      </div>

      {/* Tabs */}
      <nav className="p-2 border-b border-slate-700">
        {TABS.map((t) => (
          <button
            key={t.id}
            onClick={() => onTabChange(t.id)}
            className={`w-full text-left px-3 py-2 rounded-lg text-sm mb-0.5 transition-colors ${
              tab === t.id
                ? "bg-blue-600/20 text-blue-400 font-medium"
                : "text-slate-400 hover:bg-slate-800 hover:text-slate-200"
            }`}
          >
            <span className="mr-2">{t.icon}</span>
            {t.label}
            {t.id === "concepts" && (
              <span className="float-right text-xs text-slate-500">
                {stats.concepts}
              </span>
            )}
            {t.id === "patterns" && (
              <span className="float-right text-xs text-slate-500">
                {stats.patterns}
              </span>
            )}
            {t.id === "comparisons" && (
              <span className="float-right text-xs text-slate-500">
                {stats.comparisons}
              </span>
            )}
          </button>
        ))}
      </nav>

      {/* Filters (graph tab only) */}
      {tab === "graph" && (
        <div className="p-3 flex-1">
          <p className="text-xs text-slate-500 uppercase tracking-wider mb-3">
            Filters
          </p>

          <label className="flex items-center gap-2 text-sm text-slate-300 mb-2 cursor-pointer">
            <input
              type="checkbox"
              checked={filters.showConcepts}
              onChange={(e) => set({ showConcepts: e.target.checked })}
              className="accent-blue-500"
            />
            <span
              className="w-2.5 h-2.5 rounded-full"
              style={{ background: "#3b82f6" }}
            />
            Concepts
          </label>

          <label className="flex items-center gap-2 text-sm text-slate-300 mb-2 cursor-pointer">
            <input
              type="checkbox"
              checked={filters.showComponents}
              onChange={(e) => set({ showComponents: e.target.checked })}
              className="accent-green-500"
            />
            <span
              className="w-2.5 h-2.5 rounded-full"
              style={{ background: "#22c55e" }}
            />
            Components
          </label>

          <label className="flex items-center gap-2 text-sm text-slate-300 mb-4 cursor-pointer">
            <input
              type="checkbox"
              checked={filters.showPatterns}
              onChange={(e) => set({ showPatterns: e.target.checked })}
              className="accent-orange-500"
            />
            <span
              className="w-2.5 h-2.5 rounded-full"
              style={{ background: "#f97316" }}
            />
            Patterns
          </label>

          <div>
            <p className="text-xs text-slate-500 mb-1">
              Min frequency: {filters.minFrequency}
            </p>
            <input
              type="range"
              min={0}
              max={maxFrequency}
              value={filters.minFrequency}
              onChange={(e) =>
                set({ minFrequency: parseInt(e.target.value, 10) })
              }
              className="w-full accent-blue-500"
            />
          </div>
        </div>
      )}

      {/* Legend */}
      <div className="p-3 border-t border-slate-700 text-xs text-slate-500">
        <p>Node size = frequency</p>
        <p>Edge opacity = confidence</p>
      </div>
    </aside>
  );
}
