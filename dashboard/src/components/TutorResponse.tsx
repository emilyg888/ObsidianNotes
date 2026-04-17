import type { TutorOutput } from "../types";

interface Props {
  output: TutorOutput;
}

export function TutorResponse({ output }: Props) {
  return (
    <div>
      {output.concept && (
        <div className="mb-3 text-xs text-slate-500">
          grounded in concept:{" "}
          <span className="text-blue-400">{output.concept}</span>
        </div>
      )}
      <div className="text-sm text-slate-200 whitespace-pre-wrap leading-relaxed">
        {output.answer}
      </div>

      {output.related_components.length > 0 && (
        <div className="mt-4">
          <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
            Related components
          </p>
          <div className="flex flex-wrap gap-1">
            {output.related_components.map((c) => (
              <span
                key={c}
                className="inline-block px-2 py-0.5 text-xs rounded border bg-green-500/15 text-green-400 border-green-500/30"
              >
                {c}
              </span>
            ))}
          </div>
        </div>
      )}

      {output.related_patterns.length > 0 && (
        <div className="mt-3">
          <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-1">
            Related patterns
          </p>
          <div className="flex flex-wrap gap-1">
            {output.related_patterns.map((p) => (
              <span
                key={p}
                className="inline-block px-2 py-0.5 text-xs rounded border bg-orange-500/15 text-orange-400 border-orange-500/30"
              >
                {p}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
