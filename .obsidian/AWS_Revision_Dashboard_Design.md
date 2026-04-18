# Knowledge Dashboard — React + Vite + D3.js

## Context
The pipeline produces rich JSON artifacts (concept graph, extractions, patterns, comparisons) but there's no way to explore them visually. This dashboard makes the knowledge base browsable and interactive.

## Data Sources (read-only, copied into `public/`)
- `Notes/concept_graph.json` — 92 nodes, 649 edges (concepts, components, patterns + relationships)
- `Notes/global_extractions.json` — chunk extractions, concept index, pattern registry, comparison registry
- `Notes/concept_search_index.json` — 39 searchable concepts with aliases

## Stack
- **Vite + React 19** (TypeScript)
- **D3.js** force-directed graph
- **Tailwind CSS** for layout
- No backend — static JSON loaded at startup

## Dashboard Layout

```
┌─────────────────────────────────────────────────────────┐
│  Knowledge Dashboard                    [search bar]     │
├────────────┬────────────────────────────────────────────┤
│            │                                            │
│  Sidebar   │   Main Area                               │
│            │                                            │
│  Tabs:     │   Tab 1: Force Graph (D3)                 │
│  - Graph   │     - nodes colored by type               │
│  - Concepts│       concept=blue, component=green,      │
│  - Patterns│       pattern=orange                      │
│  - Compare │     - node size = frequency               │
│            │     - edge opacity = confidence            │
│  Filters:  │     - hover = tooltip with details        │
│  [x] concept│    - click = select, show detail panel   │
│  [x] comp  │                                           │
│  [x] pattern│  Tab 2: Concept Cards                    │
│            │     - sorted by frequency                  │
│  Freq      │     - shows aliases, components, patterns  │
│  slider    │     - confidence bar                       │
│            │                                            │
│            │   Tab 3: Pattern Registry                  │
│            │     - pattern cards with used_in, components│
│            │     - confidence + frequency stats          │
│            │                                            │
│            │   Tab 4: Comparisons                       │
│            │     - side-by-side tradeoff cards           │
│            │     - dimension breakdown                   │
│            │     - recommended usage                     │
└────────────┴────────────────────────────────────────────┘
```

## File Structure (new, under project root)

```
dashboard/
  package.json
  vite.config.ts
  tsconfig.json
  tailwind.config.js
  index.html
  public/
    concept_graph.json       ← copied from Notes/
    global_extractions.json  ← copied from Notes/
  src/
    main.tsx
    App.tsx
    types.ts                 ← TypeScript interfaces for all JSON shapes
    hooks/
      useGraphData.ts        ← loads + parses both JSON files
    components/
      Layout.tsx             ← sidebar + main area shell
      SearchBar.tsx
      Sidebar.tsx            ← tab selector + filters
      ForceGraph.tsx         ← D3 force graph (SVG)
      ConceptCards.tsx        ← concept index view
      PatternRegistry.tsx    ← pattern cards
      Comparisons.tsx        ← tradeoff side-by-side
      DetailPanel.tsx        ← right drawer on node click
      Tooltip.tsx
```

## Key Implementation Details

1. **ForceGraph.tsx**: D3 force simulation rendered into an SVG ref. React owns the container, D3 owns the simulation. Node colors: concept=#3b82f6, component=#22c55e, pattern=#f97316. Node radius = `Math.sqrt(frequency) * 2 + 4`. Edge stroke-opacity = confidence.

2. **Filtering**: Sidebar checkboxes filter node types. Frequency slider sets min threshold. Both re-filter the D3 simulation without remounting.

3. **Search**: Fuzzy match against concept names + aliases from `concept_search_index.json`. Highlights matching nodes in graph, scrolls to card in list views.

4. **Comparisons tab**: Reads `comparison_registry` from extractions. Renders side-by-side cards showing dimensions (which pattern wins each), shared components, recommended usage.

## Steps

1. Scaffold Vite + React + TS project in `dashboard/`
2. Copy JSON data files into `public/`
3. Create type definitions (`types.ts`)
4. Build data loading hook (`useGraphData.ts`)
5. Build layout shell + sidebar + tabs
6. Build ForceGraph with D3
7. Build ConceptCards view
8. Build PatternRegistry view
9. Build Comparisons view
10. Build search + filtering
11. Add `.claude/launch.json` config for preview

## Verification
- `cd dashboard && npm run dev` → opens on localhost
- Force graph renders 92 nodes, edges visible
- Click a concept node → detail panel shows components + patterns
- Switch to Concepts tab → 39 cards sorted by frequency
- Switch to Patterns tab → pattern cards with confidence bars
- Switch to Comparisons → WebSocket vs REST, sync vs async, streaming vs batch
- Search "RAG" → highlights node in graph, filters cards
