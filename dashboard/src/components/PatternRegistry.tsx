import type { PatternRegistryEntry } from "../types";

interface Props {
  patterns: PatternRegistryEntry[];
  search: string;
}

export function PatternRegistry({ patterns, search }: Props) {
  const searchLower = search.toLowerCase();
  const filtered = patterns.filter(
    (p) =>
      !searchLower ||
      p.name.toLowerCase().includes(searchLower) ||
      p.aliases.some((a) => a.toLowerCase().includes(searchLower))
  );

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold text-white mb-1">Pattern Registry</h2>
      <p className="text-sm text-slate-400 mb-6">
        {filtered.length} architectural patterns identified
      </p>

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
        {filtered.map((p) => (
          <div
            key={p.pattern_id}
            className="bg-slate-800/60 border border-slate-700 rounded-xl p-4 hover:border-orange-500/50 transition-colors"
          >
            {/* Header */}
            <div className="flex items-start justify-between mb-2">
              <h3 className="text-sm font-semibold text-orange-400 leading-snug pr-2">
                {p.name}
              </h3>
              <span className="text-xs text-slate-500 whitespace-nowrap">
                freq: {p.frequency}
              </span>
            </div>

            {/* Confidence bar */}
            <div className="flex items-center gap-2 mb-3">
              <div className="w-full bg-slate-700 rounded-full h-1.5">
                <div
                  className="bg-orange-500 h-1.5 rounded-full transition-all"
                  style={{ width: `${Math.round(p.confidence * 100)}%` }}
                />
              </div>
              <span className="text-xs text-slate-500 whitespace-nowrap">
                {Math.round(p.confidence * 100)}%
              </span>
            </div>

            {/* Used in (concepts) */}
            {p.used_in.length > 0 && (
              <div className="mb-3">
                <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
                  Used in concepts
                </p>
                <div className="flex flex-wrap gap-1">
                  {p.used_in.map((concept) => (
                    <span
                      key={concept}
                      className="inline-block px-2 py-0.5 text-xs rounded border bg-blue-500/15 text-blue-400 border-blue-500/30"
                    >
                      {concept}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {/* Related components */}
            {p.related_components.length > 0 && (
              <div className="mb-3">
                <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
                  Components
                </p>
                <div className="flex flex-wrap gap-1">
                  {p.related_components.slice(0, 5).map((comp) => (
                    <span
                      key={comp}
                      className="inline-block px-2 py-0.5 text-xs rounded border bg-green-500/15 text-green-400 border-green-500/30"
                    >
                      {comp}
                    </span>
                  ))}
                  {p.related_components.length > 5 && (
                    <span className="inline-block px-2 py-0.5 text-xs rounded border bg-slate-700 text-slate-400 border-slate-600">
                      +{p.related_components.length - 5}
                    </span>
                  )}
                </div>
              </div>
            )}

            {/* Aliases */}
            {p.aliases.length > 0 && (
              <div className="mb-3">
                <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
                  Also known as
                </p>
                <p className="text-xs text-slate-400">
                  {p.aliases.join(", ")}
                </p>
              </div>
            )}

            {/* Footer */}
            <div className="mt-2 pt-2 border-t border-slate-700 flex gap-4 text-xs text-slate-500">
              <span>{p.sources.length} sources</span>
              <span>{p.chunks.length} chunks</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
