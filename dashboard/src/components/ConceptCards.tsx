import type { ConceptIndexEntry } from "../types";

interface Props {
  concepts: ConceptIndexEntry[];
  search: string;
}

function ConfidenceBar({ value }: { value: number }) {
  return (
    <div className="w-full bg-slate-700 rounded-full h-1.5">
      <div
        className="bg-blue-500 h-1.5 rounded-full transition-all"
        style={{ width: `${Math.round(value * 100)}%` }}
      />
    </div>
  );
}

function Tag({
  label,
  color = "slate",
}: {
  label: string;
  color?: "blue" | "green" | "orange" | "slate";
}) {
  const colors = {
    blue: "bg-blue-500/15 text-blue-400 border-blue-500/30",
    green: "bg-green-500/15 text-green-400 border-green-500/30",
    orange: "bg-orange-500/15 text-orange-400 border-orange-500/30",
    slate: "bg-slate-700 text-slate-400 border-slate-600",
  };
  return (
    <span
      className={`inline-block px-2 py-0.5 text-xs rounded border ${colors[color]}`}
    >
      {label}
    </span>
  );
}

export function ConceptCards({ concepts, search }: Props) {
  const searchLower = search.toLowerCase();
  const filtered = concepts.filter(
    (c) =>
      !searchLower ||
      c.concept.toLowerCase().includes(searchLower) ||
      c.aliases.some((a) => a.toLowerCase().includes(searchLower))
  );

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold text-white mb-1">Concepts</h2>
      <p className="text-sm text-slate-400 mb-6">
        {filtered.length} concepts extracted from study materials
      </p>

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
        {filtered.map((c) => (
          <div
            key={c.concept}
            className="bg-slate-800/60 border border-slate-700 rounded-xl p-4 hover:border-blue-500/50 transition-colors"
          >
            {/* Header */}
            <div className="flex items-start justify-between mb-2">
              <h3 className="text-sm font-semibold text-white leading-snug pr-2">
                {c.concept}
              </h3>
              <span className="text-xs text-slate-500 whitespace-nowrap">
                freq: {c.frequency}
              </span>
            </div>

            {/* Confidence */}
            <div className="flex items-center gap-2 mb-3">
              <ConfidenceBar value={c.confidence} />
              <span className="text-xs text-slate-500 whitespace-nowrap">
                {Math.round(c.confidence * 100)}%
              </span>
            </div>

            {/* Aliases */}
            {c.aliases.length > 0 && (
              <div className="mb-3">
                <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
                  Aliases
                </p>
                <div className="flex flex-wrap gap-1">
                  {c.aliases.map((a) => (
                    <Tag key={a} label={a} color="slate" />
                  ))}
                </div>
              </div>
            )}

            {/* Components */}
            {c.related_components.length > 0 && (
              <div className="mb-3">
                <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
                  Components
                </p>
                <div className="flex flex-wrap gap-1">
                  {c.related_components.slice(0, 5).map((comp) => (
                    <Tag key={comp} label={comp} color="green" />
                  ))}
                  {c.related_components.length > 5 && (
                    <Tag
                      label={`+${c.related_components.length - 5}`}
                      color="slate"
                    />
                  )}
                </div>
              </div>
            )}

            {/* Patterns */}
            {c.related_patterns.length > 0 && (
              <div>
                <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
                  Patterns
                </p>
                <div className="flex flex-wrap gap-1">
                  {c.related_patterns.slice(0, 4).map((p) => (
                    <Tag key={p} label={p} color="orange" />
                  ))}
                </div>
              </div>
            )}

            {/* Footer stats */}
            <div className="mt-3 pt-2 border-t border-slate-700 flex gap-4 text-xs text-slate-500">
              <span>{c.source_count} sources</span>
              <span>{c.chunks.length} chunks</span>
              <span>{c.component_link_count} comp links</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
