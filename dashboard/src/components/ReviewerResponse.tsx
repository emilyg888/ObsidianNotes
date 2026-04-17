import type { ReviewOutput } from "../types";

interface Props {
  output: ReviewOutput;
}

const CATEGORY_LABELS: Record<keyof ReviewOutput["scores"], string> = {
  security: "Security",
  scalability: "Scalability",
  cost_efficiency: "Cost Efficiency",
  reliability: "Reliability",
  operational_excellence: "Operational Excellence",
};

function ScoreBar({ label, value }: { label: string; value: number }) {
  const pct = Math.max(0, Math.min(100, (value / 10) * 100));
  const color =
    value >= 8
      ? "bg-green-500"
      : value >= 5
      ? "bg-blue-500"
      : value >= 3
      ? "bg-orange-500"
      : "bg-red-500";
  return (
    <div className="mb-2">
      <div className="flex justify-between text-xs mb-0.5">
        <span className="text-slate-300">{label}</span>
        <span className="text-slate-400 font-mono">{value}/10</span>
      </div>
      <div className="w-full h-1.5 bg-slate-700 rounded-full overflow-hidden">
        <div
          className={`${color} h-full rounded-full transition-all`}
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}

function BulletList({
  title,
  items,
  color,
}: {
  title: string;
  items: string[];
  color: "green" | "red" | "blue";
}) {
  if (items.length === 0) return null;
  const classes = {
    green: "text-green-400",
    red: "text-red-400",
    blue: "text-blue-400",
  };
  return (
    <div className="mb-3">
      <p className={`text-[10px] uppercase tracking-wider mb-1 ${classes[color]}`}>
        {title}
      </p>
      <ul className="text-xs text-slate-300 space-y-1 list-disc list-inside">
        {items.map((item, i) => (
          <li key={i} className="leading-relaxed">
            {item}
          </li>
        ))}
      </ul>
    </div>
  );
}

export function ReviewerResponse({ output }: Props) {
  if (output.parse_error) {
    return (
      <div className="text-sm text-red-400">
        Review error: {output.parse_error}
        {output.raw && (
          <pre className="mt-2 text-xs text-slate-500 bg-slate-900/50 p-2 rounded overflow-auto max-h-40">
            {output.raw}
          </pre>
        )}
      </div>
    );
  }

  return (
    <div>
      {/* Overall */}
      <div className="mb-3 flex items-center gap-3">
        {output.concept && (
          <div className="text-xs text-slate-500">
            against: <span className="text-blue-400">{output.concept}</span>
          </div>
        )}
        <div className="ml-auto">
          <span className="text-xs text-slate-500 mr-2">Overall</span>
          <span className="text-lg font-bold text-white">
            {output.overall.toFixed(1)}
          </span>
          <span className="text-xs text-slate-500">/10</span>
        </div>
      </div>

      {/* Scores */}
      <div className="mb-4">
        {(Object.keys(CATEGORY_LABELS) as (keyof typeof CATEGORY_LABELS)[]).map(
          (key) => (
            <ScoreBar
              key={key}
              label={CATEGORY_LABELS[key]}
              value={output.scores[key] ?? 0}
            />
          )
        )}
      </div>

      <BulletList title="Strengths" items={output.strengths} color="green" />
      <BulletList title="Risks" items={output.risks} color="red" />
      <BulletList
        title="Recommendations"
        items={output.recommendations}
        color="blue"
      />
    </div>
  );
}
