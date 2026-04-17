import { useEffect, useRef, useCallback } from "react";
import * as d3 from "d3";
import type { SimNode, SimLink } from "../types";

const NODE_COLORS: Record<string, string> = {
  concept: "#3b82f6",
  component: "#22c55e",
  pattern: "#f97316",
};

interface Props {
  nodes: SimNode[];
  links: SimLink[];
  onNodeClick: (node: SimNode) => void;
  selectedId: string | null;
}

export function ForceGraph({ nodes, links, onNodeClick, selectedId }: Props) {
  const svgRef = useRef<SVGSVGElement>(null);
  const tooltipRef = useRef<HTMLDivElement>(null);
  const simRef = useRef<d3.Simulation<SimNode, SimLink> | null>(null);

  const nodeClick = useCallback(
    (_event: MouseEvent, d: SimNode) => onNodeClick(d),
    [onNodeClick]
  );

  useEffect(() => {
    if (!svgRef.current) return;

    const svg = d3.select(svgRef.current);
    const width = svgRef.current.clientWidth;
    const height = svgRef.current.clientHeight;

    svg.selectAll("*").remove();

    const g = svg.append("g");

    // Zoom
    const zoom = d3
      .zoom<SVGSVGElement, unknown>()
      .scaleExtent([0.1, 4])
      .on("zoom", (event) => g.attr("transform", event.transform));
    svg.call(zoom);

    // Deep clone nodes so D3 can mutate x/y
    const simNodes: SimNode[] = nodes.map((n) => ({ ...n }));
    const nodeMap = new Map(simNodes.map((n) => [n.id, n]));

    const simLinks: SimLink[] = links
      .filter(
        (l) =>
          nodeMap.has(l.source as string) && nodeMap.has(l.target as string)
      )
      .map((l) => ({
        source: l.source as string,
        target: l.target as string,
        edgeType: l.edgeType,
        confidence: l.confidence,
      }));

    // Simulation
    const simulation = d3
      .forceSimulation<SimNode>(simNodes)
      .force(
        "link",
        d3
          .forceLink<SimNode, SimLink>(simLinks)
          .id((d) => d.id)
          .distance(80)
          .strength(0.3)
      )
      .force("charge", d3.forceManyBody().strength(-120))
      .force("center", d3.forceCenter(width / 2, height / 2))
      .force(
        "collision",
        d3.forceCollide<SimNode>().radius((d) => d.radius + 2)
      );

    simRef.current = simulation;

    // Edges
    const link = g
      .append("g")
      .selectAll("line")
      .data(simLinks)
      .join("line")
      .attr("stroke", "#475569")
      .attr("stroke-opacity", (d) => Math.max(0.08, d.confidence * 0.5))
      .attr("stroke-width", 1);

    // Nodes
    const node = g
      .append("g")
      .selectAll<SVGCircleElement, SimNode>("circle")
      .data(simNodes)
      .join("circle")
      .attr("r", (d) => d.radius)
      .attr("fill", (d) => NODE_COLORS[d.type] ?? "#94a3b8")
      .attr("stroke", (d) =>
        d.id === selectedId ? "#ffffff" : "transparent"
      )
      .attr("stroke-width", 2)
      .attr("cursor", "pointer")
      .on("click", nodeClick as unknown as (event: Event, d: SimNode) => void);

    // Hover tooltip
    const tooltip = d3.select(tooltipRef.current);

    node
      .on("mouseenter", (_event, d) => {
        tooltip
          .style("display", "block")
          .html(
            `<strong>${d.label}</strong><br/>` +
              `<span style="color:${NODE_COLORS[d.type]}">${d.type}</span> ` +
              `&middot; freq: ${d.frequency} &middot; conf: ${d.confidence.toFixed(2)}`
          );
      })
      .on("mousemove", (event) => {
        tooltip
          .style("left", event.pageX + 12 + "px")
          .style("top", event.pageY - 10 + "px");
      })
      .on("mouseleave", () => tooltip.style("display", "none"));

    // Labels for high-frequency nodes
    const labels = g
      .append("g")
      .selectAll("text")
      .data(simNodes.filter((n) => n.frequency >= 10 || n.type === "concept"))
      .join("text")
      .text((d) =>
        d.label.length > 22 ? d.label.slice(0, 20) + "..." : d.label
      )
      .attr("font-size", 10)
      .attr("fill", "#94a3b8")
      .attr("text-anchor", "middle")
      .attr("pointer-events", "none")
      .attr("dy", (d) => d.radius + 12);

    // Drag
    const drag = d3
      .drag<SVGCircleElement, SimNode>()
      .on("start", (event, d) => {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
      })
      .on("drag", (event, d) => {
        d.fx = event.x;
        d.fy = event.y;
      })
      .on("end", (event, d) => {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      });

    node.call(drag);

    // Tick
    simulation.on("tick", () => {
      link
        .attr("x1", (d) => (d.source as SimNode).x!)
        .attr("y1", (d) => (d.source as SimNode).y!)
        .attr("x2", (d) => (d.target as SimNode).x!)
        .attr("y2", (d) => (d.target as SimNode).y!);

      node.attr("cx", (d) => d.x!).attr("cy", (d) => d.y!);

      labels.attr("x", (d) => d.x!).attr("y", (d) => d.y!);
    });

    return () => {
      simulation.stop();
    };
  }, [nodes, links, selectedId, nodeClick]);

  return (
    <div className="relative w-full h-full">
      <svg
        ref={svgRef}
        className="w-full h-full"
        style={{ background: "#0f172a" }}
      />
      <div ref={tooltipRef} className="graph-tooltip" style={{ display: "none" }} />
    </div>
  );
}
