// src/LineChart.js
import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';

const LineChart = ({ data }) => {
  const svgRef = useRef();

  useEffect(() => {
    const svg = d3.select(svgRef.current);
    svg.selectAll("*").remove(); // Clear previous content
    
    const width = 800;
    const height = 400;
    const margin = { top: 20, right: 30, bottom: 50, left: 60 };

    svg.attr('viewBox', `0 0 ${width} ${height}`)
       .style('background', 'transparent');

    const x = d3.scaleTime()
      .domain(d3.extent(data, d => d.date))
      .range([margin.left, width - margin.right]);

    const y = d3.scaleLinear()
      .domain([0, d3.max(data, d => d.value)])
      .nice()
      .range([height - margin.bottom, margin.top]);

    // Create axes with white text
    const xAxis = g => g
      .attr('transform', `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(x).ticks(width / 80).tickSizeOuter(0))
      .selectAll('text')
      .style('fill', '#FFFFFF')
      .style('font-family', 'Inter, sans-serif');

    const yAxis = g => g
      .attr('transform', `translate(${margin.left},0)`)
      .call(d3.axisLeft(y))
      .selectAll('text')
      .style('fill', '#FFFFFF')
      .style('font-family', 'Inter, sans-serif');

    const line = d3.line()
      .defined(d => !isNaN(d.value))
      .x(d => x(d.date))
      .y(d => y(d.value))
      .curve(d3.curveMonotoneX);

    // Add grid lines
    svg.append('g')
      .attr('class', 'grid')
      .attr('transform', `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(x)
        .tickSize(-height + margin.top + margin.bottom)
        .tickFormat('')
      )
      .selectAll('line')
      .style('stroke', '#374151')
      .style('stroke-width', 0.5);

    svg.append('g')
      .attr('class', 'grid')
      .attr('transform', `translate(${margin.left},0)`)
      .call(d3.axisLeft(y)
        .tickSize(-width + margin.left + margin.right)
        .tickFormat('')
      )
      .selectAll('line')
      .style('stroke', '#374151')
      .style('stroke-width', 0.5);

    // Add axes
    svg.append('g').call(xAxis);
    svg.append('g').call(yAxis);

    // Style axis lines
    svg.selectAll('.domain')
      .style('stroke', '#374151')
      .style('stroke-width', 1);

    svg.selectAll('.tick line')
      .style('stroke', '#374151');

    // Add the line
    svg.append('path')
      .datum(data)
      .attr('fill', 'none')
      .attr('stroke', '#3B82F6')
      .attr('stroke-width', 3)
      .attr('d', line);

    // Add points
    svg.selectAll('.dot')
      .data(data)
      .enter().append('circle')
      .attr('class', 'dot')
      .attr('cx', d => x(d.date))
      .attr('cy', d => y(d.value))
      .attr('r', 4)
      .style('fill', '#3B82F6')
      .style('stroke', '#FFFFFF')
      .style('stroke-width', 2);
      
  }, [data]);

  return (
    <div className="bg-white/5 backdrop-blur-sm rounded-xl border border-white/10 p-6 mt-4">
      <h3 className="text-white font-semibold text-lg mb-4">Time Series Visualization</h3>
      <div className="bg-slate-900/50 rounded-lg p-4">
        <svg ref={svgRef}></svg>
      </div>
    </div>
  );
};

export default LineChart;
