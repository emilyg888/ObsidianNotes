import { useState } from "react";
import type { QuizOutput, QuizQuestion } from "../types";

interface Props {
  output: QuizOutput;
}

function extractLetter(option: string): string {
  const match = option.match(/^([A-D])\b/i);
  return match ? match[1].toUpperCase() : option.trim().charAt(0).toUpperCase();
}

function QuestionCard({ q }: { q: QuizQuestion }) {
  const [selected, setSelected] = useState<string | null>(null);
  const revealed = selected !== null;
  const correct = q.answer?.trim().toUpperCase();

  return (
    <div className="bg-slate-800/60 border border-slate-700 rounded-lg p-3 mb-3">
      <p className="text-sm text-slate-200 mb-2">
        <span className="text-slate-500 mr-2">Q{q.id}.</span>
        {q.question}
      </p>
      <div className="space-y-1.5">
        {q.options.map((opt) => {
          const letter = extractLetter(opt);
          const isSelected = selected === letter;
          const isCorrect = letter === correct;
          let cls = "border-slate-600 text-slate-300 hover:bg-slate-700/40";
          if (revealed && isCorrect) cls = "border-green-500 bg-green-500/20 text-green-300";
          else if (revealed && isSelected && !isCorrect)
            cls = "border-red-500 bg-red-500/15 text-red-300";
          return (
            <button
              key={letter}
              onClick={() => !revealed && setSelected(letter)}
              disabled={revealed}
              className={`w-full text-left px-3 py-1.5 text-sm rounded border transition-colors ${cls}`}
            >
              {opt}
            </button>
          );
        })}
      </div>
      {revealed && (
        <div className="mt-3 text-xs text-slate-400 border-t border-slate-700 pt-2">
          <span className="text-slate-500">Correct: </span>
          <span className="text-green-400 font-medium">{correct}</span>
          {q.explanation && (
            <p className="mt-1 text-slate-400">{q.explanation}</p>
          )}
        </div>
      )}
    </div>
  );
}

export function QuizResponse({ output }: Props) {
  if (output.parse_error) {
    return (
      <div className="text-sm text-red-400">
        Quiz generation error: {output.parse_error}
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
      {output.topics.length > 0 && (
        <div className="mb-3 text-xs text-slate-500">
          topics:{" "}
          {output.topics.map((t) => (
            <span
              key={t}
              className="inline-block mr-1 px-1.5 py-0.5 rounded bg-blue-500/15 text-blue-400 border border-blue-500/30"
            >
              {t}
            </span>
          ))}
        </div>
      )}
      {output.questions.map((q) => (
        <QuestionCard key={q.id} q={q} />
      ))}
    </div>
  );
}
