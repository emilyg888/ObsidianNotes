import type { ComparisonEntry } from "../types";

interface Props {
  comparisons: ComparisonEntry[];
}

function humanize(id: string): string {
  return id
    .replace(/_/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

export function Comparisons({ comparisons }: Props) {
  if (comparisons.length === 0) {
    return (
      <div className="p-6 text-slate-400">No comparison data available.</div>
    );
  }

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold text-white mb-1">
        Architectural Tradeoffs
      </h2>
      <p className="text-sm text-slate-400 mb-6">
        {comparisons.length} pattern comparisons with tradeoff analysis
      </p>

      <div className="space-y-6">
        {comparisons.map((c, i) => (
          <div
            key={i}
            className="bg-slate-800/60 border border-slate-700 rounded-xl overflow-hidden"
          >
            {/* Header: A vs B */}
            <div className="flex items-center justify-between p-4 border-b border-slate-700 bg-slate-800/80">
              <div className="flex items-center gap-3">
                <span className="px-3 py-1 bg-blue-500/20 text-blue-400 rounded-lg text-sm font-medium">
                  {humanize(c.from)}
                </span>
                <span className="text-slate-500 text-sm font-bold">vs</span>
                <span className="px-3 py-1 bg-purple-500/20 text-purple-400 rounded-lg text-sm font-medium">
                  {humanize(c.to)}
                </span>
              </div>
              <span className="text-xs text-slate-500">
                confidence: {Math.round(c.confidence * 100)}%
              </span>
            </div>

            <div className="p-4">
              {/* Dimensions */}
              {c.dimensions && (
                <div className="mb-4">
                  <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-2">
                    Dimension Breakdown
                  </p>
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
                    {Object.entries(c.dimensions).map(([dim, winner]) => (
                      <div
                        key={dim}
                        className="bg-slate-900/60 rounded-lg p-2 text-center"
                      >
                        <p className="text-[10px] text-slate-500 mb-1">
                          {dim.replace(/_/g, " ")}
                        </p>
                        <p
                          className={`text-xs font-medium ${
                            winner === c.from
                              ? "text-blue-400"
                              : "text-purple-400"
                          }`}
                        >
                          {humanize(winner)}
                        </p>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Recommended Usage */}
              {c.recommended_usage && (
                <div className="mb-4">
                  <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-2">
                    When to Use
                  </p>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                    {Object.entries(c.recommended_usage).map(
                      ([patternId, guidance]) => (
                        <div
                          key={patternId}
                          className="bg-slate-900/60 rounded-lg p-3"
                        >
                          <p
                            className={`text-xs font-medium mb-1 ${
                              patternId === c.from
                                ? "text-blue-400"
                                : "text-purple-400"
                            }`}
                          >
                            {humanize(patternId)}
                          </p>
                          <ul className="text-xs text-slate-400 space-y-1">
                            {(Array.isArray(guidance)
                              ? guidance
                              : [guidance]
                            ).map((g, j) => (
                              <li key={j} className="leading-relaxed">
                                {g}
                              </li>
                            ))}
                          </ul>
                        </div>
                      )
                    )}
                  </div>
                </div>
              )}

              {/* Shared components */}
              {c.shared_components.length > 0 && (
                <div>
                  <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
                    Shared Components
                  </p>
                  <div className="flex flex-wrap gap-1">
                    {c.shared_components.map((comp) => (
                      <span
                        key={comp}
                        className="inline-block px-2 py-0.5 text-xs rounded border bg-green-500/15 text-green-400 border-green-500/30"
                      >
                        {comp}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
